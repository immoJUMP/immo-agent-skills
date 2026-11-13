# Beispiel: Mieteranfrage zu einem Schaden

**Eingang (Gmail, ungelesen):**
```
<<<MAILTEXT
Hallo, bei uns im Bad ist seit gestern ein dunkler Fleck an der Decke, der größer wird.
Wohnung 2. OG links, Musterweg 5. Viele Grüße, Maria Beispiel
MAILTEXT>>>
```

**Einordnung:** Schaden, zeitnah (kein laufendes Wasser genannt). Absender passt laut `team/objekte/musterweg-5.md` zu E-05. Fallbuch: kein ähnlicher Fall.

**Entwurf** (`/opt/data/arbeit/entwuerfe/2026-11-13_<id>.txt`, angelegt mit `gmail entwurf --an <absender> --betreff "Re: Fleck im Bad" --text-datei … --antwort-auf <id>`):
```
Guten Tag Frau Beispiel,

vielen Dank für Ihre Nachricht, wir kümmern uns darum.
Damit wir den Fleck richtig einordnen können, schicken Sie uns bitte zwei Fotos
(Übersicht und Nahaufnahme) und sagen Sie uns, wann Sie in den nächsten Tagen gut erreichbar sind.
Falls Wasser tropft oder der Fleck schnell wächst, rufen Sie bitte sofort unter [Notdienstnummer] an.

[Grußformel]
```

**#verwaltung:**
```
[Schaden] E-05: dunkler Fleck an der Badezimmerdecke, wird größer. Möglicherweise Wasser von oben, Wohnung darüber (E-08) prüfen. Entwurf liegt in Gmail, bitte prüfen und selbst senden.
```

**Fallbuch:** `2026-11-13-fleck-bad-e05.md`, Einschätzung „Feuchteschaden, Ursache offen“, `bestaetigt_von` leer.

## Warum gut

- Kein Termin, keine Kostenzusage, kein Anerkenntnis, aber ein klarer nächster Schritt für die Mieterin.
- Fehlende Bausteine bleiben als Platzhalter sichtbar, statt erfunden zu werden.
- Der Hinweis auf die Wohnung darüber spart dem Eigentümer einen Denkschritt.
