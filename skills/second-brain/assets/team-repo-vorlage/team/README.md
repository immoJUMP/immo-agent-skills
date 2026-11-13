# Team-Wissen

Was mehrere Agenten brauchen. Fachwissen eines einzelnen Agenten liegt in `agenten/<slug>/wissen/`.

Freigabe: Fachverantwortliche/r des vorschlagenden Agenten oder Eigentümer. Welche Agenten hier vorschlagen dürfen, steht in ihrer `rechte.yaml`.

## Index

| Frage | Seite | thema |
|---|---|---|
| Wer sind wir, welche Gesellschaften, wie sprechen wir Mieter an, wer ist erreichbar? | [firma.md](firma.md) | `firma` |
| Welche Objekte und Einheiten gibt es, welche Kennung gilt? | [objekte/README.md](objekte/README.md) | Index; je Objekt `objekt-<kennung>` |

Neue Seite: eine Zeile hier, im selben Vorschlag.

## Regeln

- Hier steht nur, was für mehrere Agenten gilt. Gilt etwas nur für einen, gehört es in dessen `wissen/`.
- Jede Seite hat Frontmatter mit eindeutigem `thema`, `sources`, `status`, `verantwortlich` und bei zeitkritischen Angaben `stale_after`.
- Operative Daten bleiben im führenden System: Mieter, Mieten, Zahlungen und offene Posten in MietJUMP, Mails in Gmail. Hier stehen höchstens Verweise.
- Keine Mieternamen, keine Kontonummern, keine Zugangsdaten.
