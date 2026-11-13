# Betriebslogbuch

Eine Datei je Monat: `JJJJ-MM.md`. Der Doktor schreibt auf dem Server nach `/opt/agenten/logbuch/` und spiegelt hierher, ohne PR. Nur anhängen, nie ändern, auch nicht von Hand.

## Format eines Eintrags

```markdown
## JJJJ-MM-TT HH:MM <befehl>
- Ergebnis: grün | gelb | rot, in einem Satz
- Maßnahmen: was der Doktor getan hat, oder „keine“
- Offen: was ein Mensch klären muss, oder „nichts“
```

Beispiel:

```markdown
## 2026-11-13 03:10 doktor reparieren
- Ergebnis: grün nach Reparatur, vorher rot (Container agent-<slug> lief nicht)
- Maßnahmen: Container neu gestartet, Modelltest bestanden
- Offen: nichts
```

## Was nie hinein gehört

Geheimnisse und Tokens, Mailtexte, Mieternamen, Kontonummern. Fehlermeldungen werden gekürzt, wenn sie solche Werte enthalten.

## Lesen

- Was ist heute Nacht passiert? Die letzten Einträge der aktuellen Monatsdatei.
- Wiederkehrende Fehler: nach „rot“ suchen.
- Jeder Eintrag, bei dem „Offen“ nicht „nichts“ ist, braucht dich.
