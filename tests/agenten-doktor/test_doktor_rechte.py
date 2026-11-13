"""Unit-Tests der sicherheitskritischen Logik im Server-Befehl doktor:
Rechte-Matrix, Vorschlagspruefung, Freigabeberechtigung, symlink-sichere Dateizugriffe.

Braucht PyYAML (auf dem Server vorhanden). Lauf:
  python3 -m unittest tests/agenten-doktor/test_doktor_rechte.py
  oder auf dem Server: DOKTOR_PFAD=/usr/local/bin/doktor python3 -m unittest test_doktor_rechte
"""
import importlib.machinery
import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path

try:
    import yaml  # noqa: F401
    HAT_YAML = True
except ImportError:
    HAT_YAML = False

_HIER = Path(__file__).resolve()
REPO = _HIER.parents[2] if len(_HIER.parents) > 2 else _HIER.parent
PFAD = os.environ.get("DOKTOR_PFAD") or str(REPO / "skills/agenten-doktor/installer/server/bin/doktor")


def doktor_laden(basis: Path):
    os.environ["AGENTEN_BASIS"] = str(basis)
    loader = importlib.machinery.SourceFileLoader("doktor_modul", PFAD)
    spec = importlib.util.spec_from_loader("doktor_modul", loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


@unittest.skipUnless(HAT_YAML, "PyYAML fehlt (Test laeuft auf dem Server)")
class RechteTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.d = doktor_laden(self.tmp)
        self.d.logbuch = lambda *a, **k: None  # kein Logbuch im Test
        self.d.geheim = lambda: {"GITHUB_TOKEN": "geheimer-wert-1234567890abcdef"}
        (self.d.WISSEN / "agenten" / "vera").mkdir(parents=True)
        self.vera = {"rechte": {"lesen": ["team/**", "agenten/vera/**"],
                                "vorschlagen": ["agenten/vera/wissen/**", "agenten/vera/testfragen.yaml"]},
                     "fachverantwortlich": {"github": "fachfrau", "telegram_id": "222"}}
        self.kurt = {"rechte": {"lesen": ["**"], "vorschlagen": ["agenten/**", "team/**"]}, "telegram": True}
        self.k = {"EIGENTUEMER_GITHUB": "chefin", "EIGENTUEMER_TELEGRAM_ID": "111"}

    def vorschlag(self, agent, dateien, art="wissen", extra=""):
        o = self.d.AGENT_BASIS / agent / "vorschlaege" / f"v{len(list((self.d.AGENT_BASIS / agent / 'vorschlaege').glob('*'))) if (self.d.AGENT_BASIS / agent / 'vorschlaege').exists() else 0}"
        (o / "dateien").mkdir(parents=True)
        (o / "vorschlag.yaml").write_text(
            f'titel: "t"\nart: {art}\nausloeser: "a"\nbegruendung: "b"\ntestfragen:\n  - frage: "f"\n    erwartet: "e"\n{extra}')
        for p, inhalt in dateien.items():
            z = o / "dateien" / p
            z.parent.mkdir(parents=True, exist_ok=True)
            z.write_text(inhalt)
        return o

    # --- Rechte-Matrix
    def test_glob(self):
        self.assertTrue(self.d.passt("agenten/vera/wissen/a/b.md", ["agenten/vera/wissen/**"]))
        self.assertFalse(self.d.passt("agenten/vera/regeln.md", ["agenten/vera/wissen/**"]))
        self.assertTrue(self.d.passt("agenten/kurt/agent.yaml", ["agenten/*/agent.yaml"]))
        self.assertFalse(self.d.passt("agenten/kurt/x/agent.yaml", ["agenten/*/agent.yaml"]))

    def test_freigabestufe(self):
        self.assertEqual(self.d.freigabe_noetig(["agenten/vera/wissen/x.md"]), "fach")
        self.assertEqual(self.d.freigabe_noetig(["agenten/vera/regeln.md"]), "eigentuemer")
        self.assertEqual(self.d.freigabe_noetig(["agenten/vera/wissen/x.md", "agenten/vera/skills/a/SKILL.md"]), "eigentuemer")
        self.assertEqual(self.d.freigabe_noetig(["irgendwas/neu.md"]), "eigentuemer")

    def test_berechtigung(self):
        defs = {"vera": self.vera}
        self.assertTrue(self.d.berechtigt("github:chefin", ["agenten/vera/regeln.md"], defs, self.k)[0])
        self.assertTrue(self.d.berechtigt("github:fachfrau", ["agenten/vera/wissen/a.md"], defs, self.k)[0])
        self.assertFalse(self.d.berechtigt("github:fachfrau", ["agenten/vera/regeln.md"], defs, self.k)[0])
        self.assertFalse(self.d.berechtigt("github:fremd", ["agenten/vera/wissen/a.md"], defs, self.k)[0])
        self.assertFalse(self.d.berechtigt("telegram:222", ["team/firma.md"], defs, self.k)[0])

    # --- Vorschlagspruefung
    def test_erlaubter_vorschlag(self):
        o = self.vorschlag("vera", {"agenten/vera/wissen/a.md": "neu"})
        meta, grund = self.d.vorschlag_pruefen("vera", self.vera, o)
        self.assertIsNone(grund)
        self.assertEqual(meta["_pfade"], ["agenten/vera/wissen/a.md"])

    def test_ausserhalb_der_rechte(self):
        for pfad in ("agenten/vera/regeln.md", "geschaeftsfuehrung/x.md", "agenten/kurt/wissen/a.md", "AGENTS.md"):
            o = self.vorschlag("vera", {pfad: "x"})
            self.assertIsNotNone(self.d.vorschlag_pruefen("vera", self.vera, o)[1], pfad)

    def test_unzulaessige_pfade(self):
        o = self.vorschlag("vera", {"agenten/vera/wissen/a.md": "x"}, extra='loeschen: ["agenten/vera/wissen/../regeln.md"]\n')
        self.assertIn("unzulaessiger Pfad", self.d.vorschlag_pruefen("vera", self.vera, o)[1])
        o = self.vorschlag("vera", {"agenten/vera/wissen/.git/config": "x"})
        self.assertIsNotNone(self.d.vorschlag_pruefen("vera", self.vera, o)[1])

    def test_geheimnis_im_vorschlag(self):
        o = self.vorschlag("vera", {"agenten/vera/wissen/a.md": "token ghp_abcdefghijklmnopqrstuvwxyz0123"})
        self.assertIn("Geheimnis", self.d.vorschlag_pruefen("vera", self.vera, o)[1])
        o = self.vorschlag("vera", {"agenten/vera/wissen/b.md": "Wert geheimer-wert-1234567890abcdef aus der Datei"})
        self.assertIn("Geheimnis", self.d.vorschlag_pruefen("vera", self.vera, o)[1])

    def test_symlink_im_vorschlag(self):
        o = self.vorschlag("vera", {"agenten/vera/wissen/a.md": "x"})
        ziel = self.tmp / "geheim.env"
        ziel.write_text("RC_ADMIN_PASS=abc")
        os.symlink(ziel, o / "dateien" / "agenten" / "vera" / "wissen" / "b.md")
        self.assertIn("Symlink", self.d.vorschlag_pruefen("vera", self.vera, o)[1])

    def test_agent_einstellen(self):
        basis = {"agenten/neu/agent.yaml": "slug: neu\n", "agenten/neu/rolle.md": "r", "agenten/neu/regeln.md": "r",
                 "agenten/neu/testfragen.yaml": "testfragen: []\n", "agenten/neu/aenderungen.md": "# Protokoll\n"}
        ok = dict(basis, **{"agenten/neu/rechte.yaml": 'lesen: ["team/**"]\nvorschlagen: []\n'})
        o = self.vorschlag("kurt", ok, art="agent-einstellen")
        self.assertIsNone(self.d.vorschlag_pruefen("kurt", self.kurt, o)[1])
        gf = dict(basis, **{"agenten/neu/rechte.yaml": 'lesen: ["geschaeftsfuehrung/**"]\n'})
        o = self.vorschlag("kurt", gf, art="agent-einstellen")
        self.assertIn("Geschaeftsfuehrung", self.d.vorschlag_pruefen("kurt", self.kurt, o)[1])
        fehlt = {k: v for k, v in ok.items() if not k.endswith("regeln.md")}
        o = self.vorschlag("kurt", fehlt, art="agent-einstellen")
        self.assertIn("regeln.md fehlt", self.d.vorschlag_pruefen("kurt", self.kurt, o)[1])
        falsch = dict(ok, **{"agenten/neu/agent.yaml": "slug: anders\n"})
        o = self.vorschlag("kurt", falsch, art="agent-einstellen")
        self.assertIn("slug", self.d.vorschlag_pruefen("kurt", self.kurt, o)[1])

    # --- Dateizugriffe
    def test_sicher_schreiben_folgt_keinem_symlink(self):
        opfer = self.tmp / "opfer.txt"
        opfer.write_text("ORIGINAL")
        h = self.d.AGENT_BASIS / "vera" / "hermes"
        h.mkdir(parents=True)
        os.symlink(opfer, h / "config.yaml")
        self.d.sicher_schreiben(h / "config.yaml", "neu")
        self.assertEqual(opfer.read_text(), "ORIGINAL")
        self.assertFalse((h / "config.yaml").is_symlink())
        self.assertEqual((h / "config.yaml").read_text(), "neu")

    def test_sicher_schreiben_symlink_im_elternpfad(self):
        fremd = self.tmp / "fremd"
        fremd.mkdir()
        (self.d.AGENT_BASIS / "vera").mkdir(parents=True, exist_ok=True)
        os.symlink(fremd, self.d.AGENT_BASIS / "vera" / "plugins")
        with self.assertRaises(self.d.Fehler):
            self.d.sicher_schreiben(self.d.AGENT_BASIS / "vera" / "plugins" / "x.txt", "boese")
        self.assertFalse((fremd / "x.txt").exists())

    def test_sicher_lesen_verweigert_symlink_und_fifo(self):
        geheim = self.tmp / "geheim.env"
        geheim.write_text("X=1")
        fb = self.d.AGENT_BASIS / "vera" / "fallbuch"
        fb.mkdir(parents=True)
        os.symlink(geheim, fb / "leck.md")
        with self.assertRaises(self.d.Fehler):
            self.d.sicher_lesen(fb / "leck.md")
        os.mkfifo(fb / "fifo.md")
        with self.assertRaises(self.d.Fehler):
            self.d.sicher_lesen(fb / "fifo.md")

    def test_lies_env_folgt_keinem_symlink(self):
        geheim = self.tmp / "geheim.env"
        geheim.write_text("RC_ADMIN_PASS=streng-geheim")
        h = self.d.AGENT_BASIS / "vera" / "hermes"
        h.mkdir(parents=True)
        os.symlink(geheim, h / ".env")
        self.assertEqual(self.d.lies_env(h / ".env"), {})


if __name__ == "__main__":
    unittest.main()
