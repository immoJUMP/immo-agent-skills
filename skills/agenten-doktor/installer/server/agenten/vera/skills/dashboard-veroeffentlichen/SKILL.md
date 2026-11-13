---
name: dashboard-veroeffentlichen
description: "Baut aus einem Ergebnis eine einfache, gut lesbare HTML-Seite (eine Aussage und eine Zahl je Kachel, darunter Details) und veröffentlicht sie mit veroeffentlichen. Verwenden, wenn ein Ergebnis länger als fünf Chatzeilen wäre oder eine Routine ein Dashboard verlangt (mieteingang.html, belege-<jahr>.html). Nicht für Nachrichten an Mieter oder Dritte und nie für Geheimnisse."
---

# Dashboard veröffentlichen

## Schritte

1. Kernaussagen festlegen: höchstens sechs Kacheln, jede mit genau einer Zahl und einem Satz („1.340,00 €, echter Rückstand bei 2 Einheiten“). Wichtigstes zuerst.
2. HTML nach `/opt/data/arbeit/dashboards/<name>.html` schreiben, nach der Vorlage unten. Kopf: Titel, Stand (Datum, Uhrzeit), Quelle. Dann Kacheln, dann Tabellen.
3. Prüfen, bevor es rausgeht:
   - keine externen Quellen: `grep -c "http" <datei>` ergibt 0 (keine CDN-Skripte, keine Webfonts, keine Bilder aus dem Netz),
   - keine IBAN (höchstens die letzten vier Stellen), keine Tokens,
   - Mieter als Einheit oder Vertrags-ID.
4. `veroeffentlichen /opt/data/arbeit/dashboards/<name>.html <name>.html`. Feste Zielnamen, damit der Link gleich bleibt.
5. Den ausgegebenen Link im Chat nennen, mit einer Zeile Kernaussage.

## Vorlage

```html
<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mieteingang</title>
<style>
:root{--navy:#072645;--petrol:#077b7c;--mint:#7fd3c9;--mint-hell:#eaf7f5;--linie:#d5dce0;--grau:#4a5a6a;--rot:#b42323;--gruen:#047857;--gelb:#b45309}
body{margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:var(--navy);background:linear-gradient(180deg,var(--mint-hell),#fff 320px)}
main{max-width:960px;margin:0 auto;padding:24px 16px}
h1,h2{font-weight:800;margin:0 0 12px}
h1::before,h2::before{content:"";display:block;width:48px;height:6px;border-radius:3px;background:var(--mint);margin-bottom:8px}
.stand{color:var(--grau);margin:0 0 24px}
.kacheln{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px;margin-bottom:32px}
.kachel{background:#fff;border:1px solid var(--linie);border-radius:16px;padding:20px}
.zahl{font-size:2rem;font-weight:800;color:var(--petrol)}
.rot .zahl{color:var(--rot)}.gruen .zahl{color:var(--gruen)}.gelb .zahl{color:var(--gelb)}
.tabelle{overflow-x:auto}
table{width:100%;border-collapse:collapse;background:#fff}
th,td{text-align:left;padding:8px;border-bottom:1px solid var(--linie)}
td.betrag{text-align:right;font-variant-numeric:tabular-nums}
</style></head><body><main>
<h1>Mieteingang</h1>
<p class="stand">Stand 13.11.2026, 09:04 · Quelle: MietJUMP</p>
<div class="kacheln">
  <div class="kachel rot"><div class="zahl">1.340,00 €</div>echter Rückstand bei 2 Einheiten</div>
  <div class="kachel gelb"><div class="zahl">1</div>Klärfall wartet auf dich</div>
  <div class="kachel gruen"><div class="zahl">9 von 13</div>Einheiten bezahlt</div>
</div>
<h2>Echter Rückstand</h2>
<div class="tabelle"><table>
<tr><th>Einheit</th><th>offen</th><th>seit</th></tr>
<tr><td>E-04</td><td class="betrag">690,00 €</td><td>03.11.2026</td></tr>
</table></div>
</main></body></html>
```
