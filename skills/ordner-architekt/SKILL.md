---
name: ordner-architekt
description: "Baut eine saubere, dauerhaft tragfaehige Ordnerstruktur fuer ein Immobilien-Portfolio auf -- oder restrukturiert eine gewachsene, chaotische Ablage. Interview-gefuehrt: Der Skill testet zuerst den Zugriff auf deine Ablage (Google Drive, Dropbox, lokaler Ordner), erforscht den Ist-Zustand, bewertet ihn objektiv gegen eine bewaehrte Referenzstruktur, fragt deinen Soll-Zustand ab und legt dir einen bestaetigungspflichtigen Migrationsplan vor -- inklusive Backup-Frage -- bevor irgendetwas angelegt, umbenannt oder verschoben wird. Nutze diesen Skill wenn du deine Objektablage neu aufsetzen, vereinheitlichen oder aufraeumen willst, wenn jedes Objekt anders sortiert ist, wenn du Kuerzel-Konventionen einfuehren willst oder wenn du vor Steuererklaerung/Bankgespraech/Verkauf eine konsistente Struktur brauchst."
---

# Ordner-Architekt -- Immobilien-Ablage aufbauen & restrukturieren

Eine gewachsene Immobilien-Ablage sieht fast immer gleich aus: Das erste Objekt wurde sorgfaeltig sortiert, das zweite anders, beim dritten lagen die Belege schon lose in der Wurzel. Drei Objekte, drei Strukturen. Spaetestens bei Steuererklaerung, Bankgespraech oder Verkauf raecht sich das.

Dieser Skill baut Ordnung -- nicht, indem er raet, sondern indem er **dich interviewt**: Welcher Investor-Typ bist du, was hast du heute, wo soll es hin. Erst danach legt er Hand an, und auch das erst nach deiner ausdruecklichen Freigabe und mit Backup.

---

## Wann diesen Skill nutzen

- Du willst eine **neue Objektablage von Grund auf** aufsetzen (erstes oder naechstes Objekt).
- Deine bestehende Ablage ist **gewachsen und uneinheitlich** -- jedes Objekt anders sortiert, lose Dateien, doppelte Ordner.
- Du willst eine **Kuerzel-Konvention** fuer Strassen/Objekte einfuehren (z.B. `B8` = Beispielstrasse 8) und konsequent durchziehen.
- Du stehst vor **Steuererklaerung, Bankgespraech oder Verkauf** und brauchst eine konsistente, vorzeigbare Struktur.
- Du mischst **mehrere Halte-Entitaeten** (GbR, Bruchteilseigentum, Privat, GmbH) und willst sie sauber trennen.

**Nicht der richtige Skill, wenn:** Du nur ein einzelnes Dokument einordnen willst (→ `dokument-klassifizierer`), Belege fuers Finanzamt klassifizieren willst (→ `beleg-sortierer`) oder einen Arbeitsablauf/eine Pipeline in immoJUMP bauen willst (→ `prozess-designer`).

---

## Was du mitbringen musst: Zugriff

Du musst keine fertige Struktur vorbereiten und nichts vorab sortieren. Der Skill fragt dich ab. Das **Einzige**, was er braucht, ist **Zugriff auf deine Ablage**:

- **Google Drive / Dropbox (per Connector):** Du gibst den/die Ordner fuer den verbundenen Account frei. Der Skill testet zu Beginn, ob er sie wirklich sieht -- und ob er **schreiben** darf (siehe Schritt 0, das ist nicht selbstverstaendlich).
- **Lokaler Ordner / synchronisierter Cloud-Ordner (Drive for Desktop, Dropbox-App):** Du nennst den Pfad. Das ist der **bevorzugte Weg fuer die Umsetzung**, weil Anlegen, Umbenennen und Verschieben dort sicher und atomar funktionieren und die Aenderungen in die Cloud zuruecksynchronisieren.

Wenn du schon eine alte Struktur-Notiz, ein README oder eine Vorlage hast: rein damit. Der Skill liest sie und baut darauf auf, statt neu zu erfinden.

---

## Auftrag

**Fuehre zuerst das gefuehrte Interview (Schritte 0-6).** Teste den Zugriff, klaere mit wem du es zu tun hast, erforsche und bewerte den Ist-Zustand, frag den Soll-Zustand ab. Rate nicht, frag.

Lege dem Nutzer dann einen **vollstaendigen Migrationsplan** vor -- was neu angelegt, was umbenannt, was verschoben wird, Datei fuer Datei nachvollziehbar -- und benenne dabei ausdruecklich die kritischen Punkte (was koennte ihm in 2 Jahren auf die Fuesse fallen). Frag nach einem **Backup**.

Setze die Restrukturierung **erst nach Bestaetigung** um -- bevorzugt auf einer lokal synchronisierten Kopie (Anlegen/Umbenennen/Verschieben), niemals durch Massen-Kopieren oder Loeschen. Wo nur Lesezugriff besteht, liefere den Plan als exakte, ausfuehrbare Schritt-fuer-Schritt-Anleitung statt vorzutaeuschen, du haettest gebaut.

---

## Referenz: Bewaehrte Bestands-Ordnerstruktur

Das ist die Zielarchitektur, gegen die der Skill den Ist-Zustand bewertet. Sie ist praxiserprobt fuer Selbstverwalter mit gemischtem Portfolio (ETW + MFH + Sonderformen). **Nicht stur ausrollen** -- im Interview an Archetyp und Realitaet des Nutzers anpassen. Aber als Geruest hat sich genau das bewaehrt.

### Drei Ebenen: Entitaet → Lebenszyklus → Objekt

Die oberste Achse ist **nicht** "Bestand vs. Ankauf", sondern die **Halte-Entitaet** -- weil die Steuer pro Entitaet laeuft (eine GbR macht eine Feststellungserklaerung, Privatvermoegen laeuft ueber die Anlage V der Eigentuemer). Entitaeten zu vermischen ist ein Steuer- und Haftungsrisiko, kein Schoenheitsfehler.

```
Immobilien/
├── 00_Vorlagen/                    Muster-Blankos (Objektdatenblatt, Behoerdenvollmacht, Mieterliste ...)
├── 00_Portfolio/                   Kuerzel-Register + Portfolio-Uebersicht + Darlehensuebersicht
│
├── <Entitaet A, z.B. Musterbesitz GbR>/
│   ├── 00_Gesellschaft/            Gesellschaftsvertrag, Eintragung, Transparenzregister, Angestellte
│   ├── 0_Ankauf/                   Pipeline: gepruefte/verhandelte Objekte, noch nicht im Eigentum (leicht!)
│   ├── 1_Bestand/                  Objekte im Eigentum -- je Objekt das volle Template (s.u.)
│   └── 2_Verkauft/                 Archiv verkaufter Objekte (Unterlagen bleiben fuer Steuer/Gewaehrleistung)
│
└── <Entitaet B, z.B. Privat (Bruchteilseigentum)>/
    ├── 0_Ankauf/   1_Bestand/   2_Verkauft/      (kein 00_Gesellschaft -- keine Gesellschaft)
```

**Zwei Mal "Ankauf" -- nicht verwechseln:** `0_Ankauf/` oben ist die *Deal-Pipeline* (Objekte, die man prueft, aber noch nicht besitzt -- voller geplatzter Deals, deshalb bewusst leichtgewichtig). `02_Kaufprozess/` *innerhalb* eines Bestandsobjekts ist die *permanente Kaufakte* (Notar, Kaufvertrag, Grunderwerbsteuer -- fuer AfA und Steuer fuer immer aufzubewahren). Beim Notartermin/Uebergabe "graduiert" ein Objekt: Ordner wandert aus `0_Ankauf/` nach `1_Bestand/`, bekommt das volle Template, die Due-Diligence-Unterlagen rutschen in `01_Stammdaten` + `02_Kaufprozess`.

### Das Objekt-Template (gleich fuer ETW, MFH, Sonderformen)

Ein einziges Template fuer alle Objekttypen -- eine ETW ist einfach ein Objekt mit *einer* Einheit. Gleiche Struktur = gleiche Muskel-Erinnerung, und Folge-Skills (`beleg-sortierer`, `nebenkosten-pruefer`, `anlage-v-assistent`) finden sich auf jedem Objekt identisch zurecht. Leere Ordner kosten nichts; uneinheitliche Strukturen kosten bei jeder Automatisierung.

```
B8 — MFH Beispielstrasse 8, Musterstadt/
├── 00_Objektdatenblatt.md  EINE Datei (living doc): Eckdaten, Kuerzel, Flaeche, Baujahr, WE-Liste, Kaufdatum, AfA-Basis, Zaehlernummern
│                           + optional: jaehrlicher Objekt-Review/Investmentcheck ("performt das Objekt noch?")
├── 01_Stammdaten           evergreen: Grundbuch, Plaene/Grundrisse, Lageplan/Flurkarte, Wohnflaechenberechnung,
│                           Energieausweis, Baubeschreibung, Behoerdenvollmacht, Teilungserklaerung (WEG)
├── 02_Kaufprozess          einmalig, fuer immer: Expose, Notar/Kaufvertrag, Kaufpreisaufteilung (Boden/Gebaeude → AfA!),
│                           Kaufnebenkosten-Belege (Grunderwerbsteuer, Notar, Makler → AfA), Datenraum, Gutachter, Angebote
├── 03_Finanzierung         Darlehensvertraege, Grundschuldbestellung/Grundpfandrechte, Tilgungsplaene,
│                           Zinsbescheinigungen (jaehrlich → Anlage V), Restnutzungsdauer-Gutachten
├── 04_Einheiten            je WE ein Ordner: Mietvertrag, Kaution (Konto + Ein-/Rueckzahlung), Uebergabeprotokolle, Mieterkommunikation
├── 05_Verwaltung
│   ├── Versicherung/ (+ Schaeden/)    Grundsteuer/    Reparaturen/ (laufender Erhaltungsaufwand)
│   ├── Modernisierung-CapEx/          Zaehlerstaende/    Fotos/ (Aussen · Umfeld · Innen)
│   ├── Hausverwaltung-extern/         WEG/ (Wirtschaftsplan · Beschlusssammlung · Hausgeldabrechnung · Teilungserklaerung)
├── 06_Belege/              2024/  2025/  2026/   (das EINE Zuhause der Steuerbelege)
├── 07_Nebenkosten/         2024/  2025/  2026/
├── 08_Steuer/              2024/  2025/  2026/   (Anlage V / Feststellung je Jahr)
└── 09_Konto                Objektkonto (Auszuege, Kontoinfos)
```

**Steuerliche Kernregel, die nie in einen Topf darf:** `05_Verwaltung/Reparaturen/` (laufender Erhaltungsaufwand, sofort absetzbar) **getrennt von** `05_Verwaltung/Modernisierung-CapEx/`. Grund: anschaffungsnahe Herstellungskosten nach §6 Abs. 1 Nr. 1a EStG -- die **15-%-Grenze in den ersten 3 Jahren** nach Kauf. Wirft man beides zusammen, verliert man den Sofortabzug oder reisst die Grenze unbemerkt.

### Die Nummern-Regel (verhindert die Renummerier-Hoelle)

- **Geschlossene Mengen → durchnummerieren.** Die Objekt-Ebene `00-09` und der `01_Stammdaten`-Inhalt sind feste, nicht wachsende Listen → Nummern sind hier ideal und sortieren stabil.
- **Wachsende Mengen → NIE nummerieren, sondern datieren/benennen.** Belege, Nebenkosten, Steuer laufen nach **Jahr** (`2024/`, `2025/`). Einheiten/Mieter nach **Name + Einzug** (`WE1 · Mustermann seit 2021-03`). So muss nie umnummeriert werden, wenn etwas dazukommt.

### Kuerzel-Konvention (kurz, aber kollisionssicher)

Kurze Objekt-Kuerzel (Strassen-Anfangsbuchstabe + Hausnummer, z.B. `B8`, `A19`, `S42`) sind Gold: schnelles Tippen, Cross-Referenz in Buchhaltung/Anlage V, eindeutige Benennung von Dateien und im Gespraech. Aber nur mit **drei eisernen Regeln**, sonst entsteht genau das Chaos, das man aufraeumen wollte:

1. **Einmal vergeben = fuer immer eingefroren.** Der Erstbelegte zieht NIE um. Kommt spaeter eine Schlossallee 42 zur bestehenden Schildgesstrasse `S42` dazu, bleibt Schildgesstrasse `S42` und der **Neuankoemmling** wird `SC42`. Niemals andersrum -- sonst muessen alle Unterordner, Dateinamen, Kontobezuege nachgezogen werden.
2. **Kollision = gleicher Buchstabe UND gleiche Hausnummer.** `B8` (Beispielstr. 8) und `B43` (Bahnweg 43) koexistieren problemlos. Erst Beispielstr. 8 + Bachgasse 8 kollidiert → der Neue wird `BA8`.
3. **Das Kuerzel-Register ist die einzige Wahrheit.** Eine Tabelle in `00_Portfolio/`, die `A19 → "Am Beispielweg 19, Musterstadt"` aufloest. Ohne Register ist jedes Kurzschema nach 10 Objekten Raterei -- und kein Folge-Skill kann das Kuerzel zuordnen.

Wer breit ueber mehrere Staedte investiert und Kollisionen ganz vermeiden will, kann ein Stadt-Praefix voranstellen (`BN-TW43`). Laenger, dafuer nie kollidierend. Im Interview abfragen, welche Variante der Nutzer will -- und dann **konsequent** durchziehen.

### Datei-Namens-Konvention (der eigentliche Hebel)

**Identisch zu den Folge-Skills `dokument-klassifizierer` und `beleg-sortierer`** -- sonst zerbricht genau die Kette, die diesen Skill wertvoll macht. Diese nutzen `YYYY-MM-DD_Dokumenttyp_Details` (Unterstrich, Datum vorn). Diese Konvention uebernimmt der Skill 1:1:

```
YYYY-MM-DD_<Typ>_<Beschreibung>
2025-07-14_Rechnung_Heizungswartung.pdf
2024-06-01_Mietvertrag_Mustermann.pdf
2025-12-31_Zaehlerstand_Strom_WE2.pdf
```

Datum vorn → chronologische Sortierung. Typ-Tag (Rechnung / Vertrag / Abrechnung / Zaehlerstand / Mahnung) → filterbar.

**Das Kuerzel gehoert in den Ordnernamen und ins Register -- nicht zwingend in jeden Dateinamen.** Der Objektordner (`B8 — ...`) liefert den Objektbezug bereits, und ein erzwungenes Kuerzel im Dateinamen wuerde mit den Dateien kollidieren, die `dokument-klassifizierer`/`beleg-sortierer` ohne Kuerzel erzeugen. Nur fuer Dateien **ausserhalb** der Objektstruktur oder objektuebergreifend gesammelt ist ein vorangestelltes Kuerzel sinnvoll -- konventionskonform mit Unterstrich: `YYYY-MM-DD_B8_<Typ>_<Beschreibung>`. So bleibt jede Datei kompatibel, und die Suche nach `B8` findet trotzdem alles Objektuebergreifende.

### Sonderformen (gleiches Template, nur Marker)

- **ETW:** `05_Verwaltung/WEG/` aktiv (Wirtschaftsplan, Beschlusssammlung, Hausgeldabrechnung, Teilungserklaerung); Hausgeld statt voller NK gegenueber dem eigenen Mieter trotzdem in `07_Nebenkosten/`.
- **Kurzzeitvermietung:** Marker im Objektnamen; ggf. Umsatzsteuer-Thema (USt-Voranmeldungen in `08_Steuer/`), Plattform-Abrechnungen (Airbnb/Booking) in `06_Belege/`.
- **Grundstueck (unbebaut):** keine AfA aufs Land, kein `04_Einheiten`; `01_Stammdaten` + `02_Kaufprozess` + Grundsteuer reichen oft.
- **Extern verwaltetes Objekt:** `05_Verwaltung/Hausverwaltung-extern/` mit Verwaltervertrag, Abrechnungen, Korrespondenz.

---

## Strategie

### Schritt 0: Zugriff testen (IMMER zuerst)

Bevor irgendetwas anderes passiert, klaere praktisch -- nicht theoretisch -- ob du an die Ablage rankommst. Frag in Klartext und **teste sofort**:

> *"Bevor wir loslegen: Wo liegt deine Ablage -- Google Drive, Dropbox, oder ein Ordner auf diesem Rechner? Gib mir bitte den Link oder den Pfad, und sag mir, ob du den Ordner fuer mich freigegeben hast. Dann teste ich direkt, ob ich wirklich reinkomme."*

Dann **zwei Dinge testen, nacheinander, und das Ergebnis ehrlich melden:**

1. **Lesezugriff:** Oeffne den Zielordner und liste den Inhalt (Drive-Connector: `get_file_metadata` + `search_files` auf die Ordner-ID; lokal: Verzeichnis auflisten).
   - Schlaegt es fehl ("nicht gefunden"), liegt es fast immer daran, dass der Ordner mit dem *falschen Account* geteilt ist oder gar nicht. Sag das klar und nenne den konkreten Fix: *"Ich haenge am Account X. Gib den Ordner fuer X frei, oder nenn mir einen lokalen Pfad. Dann teste ich neu."* **Nicht weitermachen, solange du nichts siehst.**

2. **Schreib-Faehigkeit feststellen -- ohne dabei selbst zu schreiben (kritisch, wird gern vergessen):** Du musst *wissen*, ob der Zugang Ordner anlegen/umbenennen/verschieben/loeschen kann, bevor du einen Umsetzungsweg versprichst. Aber **ein echter Schreibversuch ist bereits eine Aenderung an Live-Dateien** -- der darf nicht vor Backup und Freigabe passieren. Stelle die Faehigkeit deshalb **passiv** fest, in dieser Reihenfolge:
   - **Permission-Metadaten lesen** (Drive: `get_file_permissions` / die Capability-Felder aus `get_file_metadata` wie `canAddChildren`, `canRename`, `canEdit`; lokal: Schreibrecht am Pfad pruefen). Das ist read-only und reicht in den allermeisten Faellen, um Lese- von Schreibzugang zu unterscheiden.
   - **Konnektor-Faehigkeiten kennen:** Viele Cloud-Connectoren sind faktisch **read-only** -- sie koennen lesen und teils Dateien anlegen/kopieren, aber **nicht umbenennen, verschieben oder loeschen**. Wenn die verfuegbaren Tools kein Move/Rename/Delete anbieten, steht das Ergebnis schon fest, ohne irgendetwas anzufassen.
   - **Nur wenn die Metadaten nicht eindeutig sind:** hol dir eine **ausdrueckliche Mini-Freigabe** fuer *eine* harmlose Schreibprobe (einen leeren Test-Ordner `_zugriffstest_` anlegen und sofort wieder entfernen) -- und nur in einem klar als Test markierten Bereich, nie an Bestandsdateien. Frag vorher: *"Darf ich kurz einen leeren Test-Ordner anlegen, um Schreibrechte zu pruefen? Loesche ich sofort wieder."*
   - Wenn Schreiben/Verschieben **nicht** geht: sag es offen und biete die zwei tragfaehigen Wege an:
     > *"Ich kann deine Ablage lesen, aber ueber diesen Connector nicht umbenennen oder verschieben. Zwei saubere Wege: (a) Du oeffnest den Ordner lokal mit Drive for Desktop / der Dropbox-App -- dann erledige ich Anlegen/Umbenennen/Verschieben direkt auf dem Rechner, und es synct in die Cloud zurueck. Oder (b) ich liefere dir den kompletten Migrationsplan als exakte Klick-Anleitung, die du selbst abarbeitest. Was ist dir lieber?"*
   - **Tu niemals so, als haettest du umgebaut, wenn der Connector es nicht kann.** Lieber ein praeziser Plan als eine Luege.

Erst wenn der Zugriff (mindestens Lesen) steht, weiter zu Schritt 1.

### Schritt 1: Wer bist du -- und was haeltst du? (Archetyp + Entitaeten)

Der Investor-Typ praegt die ganze Struktur. Ein Fix-&-Flipper braucht eine andere Ablage als ein Bestandshalter. **Frag, rate nicht** -- eine Frage nach der anderen, in normaler Sprache:

1. *"Was fuer ein Investor bist du -- eher Bestandshalter (kaufen & halten), Fix & Flip (sanieren & verkaufen), Aufteiler (MFH kaufen, Wohnungen einzeln verkaufen), Kurzzeitvermietung, oder gemischt?"*
   - **Bestandshalter** → Schwerpunkt auf dem Betriebs-/Jahreszyklus (06-08, Verwaltung, Einheiten).
   - **Fix & Flip** → starker Ankauf/Sanierungs-Block, kurzer Lebenszyklus, Abverkaufs-Ordner wichtiger als jahrelange NK.
   - **Aufteiler** → MFH-Ankauf + pro Einheit ein Abverkaufsstrang.
   - **Kurzzeit** → USt, Plattform-Abrechnungen, hohe Beleg-Frequenz.
2. *"Machst du Nebenkosten, Steuer und Verwaltung selbst -- oder laeuft das ueber eine Hausverwaltung / einen Steuerberater?"* (Selbstverwalter brauchen die Betriebsordner tief; extern Verwaltete brauchen v.a. saubere Schnittstellen-Ordner.)
3. *"Ueber welche Eigentuemer-Konstrukte haeltst du -- privat, GbR, Bruchteilseigentum, GmbH? Eines oder mehrere?"* -- **Das bestimmt die oberste Ebene.** Spiegele zurueck: *"Dann trennen wir oben sauber: eine Ebene pro Entitaet, weil die Steuer pro Entitaet laeuft. Richtig?"*
4. *"Aendert sich daran in absehbarer Zeit etwas -- neue GbR geplant, Uebertrag, Verkauf eines Strangs?"* (Beeinflusst, ob man Ebenen schon vorsieht.)

Halte das Gespraech schlank: eine Frage, ein bis zwei Saetze Kontext, fertig. Keine Fragebogen-Wand.

### Schritt 2: Ist-Zustand erforschen

Jetzt crawlst du die echte Ablage und baust ein **vollstaendiges Inventar** -- nicht aus Annahmen, sondern aus dem, was wirklich da ist. Ein Migrationsplan, der „Datei fuer Datei" verspricht, braucht auch eine Datei-Ebene als Grundlage; eine reine Top-Ebenen-Sicht reicht dafuer nicht.

**Inventar-Regeln (verbindlich):**
- **Voll rekursiv crawlen**, nicht nur eine Ebene (Drive: `search_files` mit `parentId`, pro Ordner weiter absteigen; lokal: rekursives Listing). Tiefer liegende Altstruktur, Dubletten und falsch einsortierte Dateien faellt man sonst nicht auf.
- **Pro Datei erfassen:** Pfad, Name, Typ/Endung, Groesse, Aenderungsdatum, Eltern-Ordner. Daraus baust du eine echte Datei-Liste (kein Bauchgefuehl).
- **Dubletten-Heuristik:** gleicher/aehnlicher Name oder gleiche Groesse in verschiedenen Ordnern markieren (`Fotos` vs. `2_Fotos`, `Kalkulation (1).pdf`).
- **Skalierungsregel statt stillem Abbruch:** Bei sehr grossen Bestaenden (Richtwert > ~2.000 Dateien oder > ~25 Objekte) nicht abbrechen, sondern **objektweise** vorgehen -- ein Objekt vollstaendig inventarisieren, Muster-Migration zeigen, bestaetigen lassen, dann das Muster batchweise ueber die restlichen Objekte ziehen. **Sag offen, wenn du aus Mengengruenden gerade nur eine Stichprobe gezeigt hast** -- nie so tun, als sei alles erfasst, wenn es das nicht ist.
- Vorhandene Struktur-Hinweise lesen: `README.md`, `Info.md`, `Anleitung`, alte Vorlagen-Ordner -- der Nutzer hat oft schon mal etwas angefangen. Lies es, statt neu zu erfinden (aber pruefe, ob es noch aktuell ist oder nur Archaeologie).
- Erfasse pro Objekt: Kuerzel (falls vorhanden), Objekttyp, vorhandene Unterordner, lose Dateien in der Wurzel, Entitaet.

Melde dem Nutzer den Ist-Stand **kompakt und faktisch** zurueck (z.B. Tabelle: Entitaet / Objekt / Kuerzel / Dateianzahl / Auffaelligkeiten), und nenne explizit, ob das Inventar **vollstaendig** oder eine **Stichprobe** ist, bevor du wertest.

### Schritt 3: Ist-Zustand objektiv bewerten

Jetzt der ehrliche Abgleich gegen die Referenzstruktur. Sei **Sparringspartner, nicht Schoenfaerber** -- aber benenne auch, was schon gut ist (das motiviert und verhindert, dass Bewaehrtes weggeworfen wird). Typische Befunde, gezielt suchen:

- **Mehrere Strukturen statt einer:** Objekt A themenbasiert, Objekt B durchnummeriert, Objekt C lose Dateien. Das ist der haeufigste Befund.
- **Entitaeten verwischt:** Gesellschaftsdokumente liegen lose zwischen Objekten; zwei Entitaeten unter einem Sammelordner.
- **Belege an zwei Orten:** zentral *und* pro Objekt → niemand weiss, wo der Beleg liegt. Eines muss sterben (Empfehlung: zentral aufloesen, pro Objekt fuehren).
- **Kuerzel-Chaos:** dasselbe Objekt hat mehrere Kuerzel (Ordnername ≠ Beschreibung ≠ Dateibenennung); manche Objekte ohne Kuerzel.
- **Doppelte/verwaiste Ordner:** `Fotos` und `2_Fotos` nebeneinander; kaputte Nummern (`20_`, `21_`, `2_`).
- **Steuerlich riskante Vermischung:** Reparatur und Modernisierung im selben Ordner (§6 Abs. 1 Nr. 1a EStG).
- **Fehlende Pflichtbloecke:** kein Stammdaten-Block, keine Kaution, kein Objektkonto, keine Zinsbescheinigungen.

Fasse die Befunde priorisiert zusammen: zuerst die mit steuerlichen/rechtlichen Zaehnen, dann die reinen Ordnungsthemen. Halte es knapp -- 3-7 Punkte, nicht dreissig.

### Schritt 4: Soll-Zustand abfragen

Jetzt klaeren, wohin es gehen soll -- einzeln, nacheinander:

1. *"Sollen wir die Referenzstruktur uebernehmen, oder gibt es Eigenheiten, die rein muessen?"* (Spiegele die Referenz kurz, frag nach Anpassungen.)
2. *"Kuerzel-Schema: ganz kurz (Buchstabe + Nummer, `B8`) oder mit Stadt-Praefix (`BN-TW43`)?"* -- und die drei Kuerzel-Regeln erklaeren, damit er die Konsequenz versteht (eingefroren, Neuankoemmling disambiguiert, Register).
3. *"Hast du bestehende Kuerzel, die nicht ins Schema passen? Sollen die mit umziehen (einmalige Konsistenz) oder lassen wir sie (gemischtes System)?"* -- bei kleinem Portfolio klar zur Vereinheitlichung raten.
4. *"Gibt es Sonderfaelle -- Kurzzeit, Grundstueck, extern verwaltet -- die einen abweichenden Zuschnitt brauchen?"*
5. *"Planst du Aenderungen am Konstrukt -- neue Entitaet, anstehender Verkauf, Uebertrag?"* (damit die Struktur das vorsieht).

### Schritt 5: Migrationsplan + kritischer Langzeit-Review

Stelle den **kompletten Plan** in Klartext zusammen, bevor irgendetwas passiert:

- **Was neu angelegt wird** (Entitaets-Ebenen, fehlende Objektordner, `00_Vorlagen`, `00_Portfolio` mit Kuerzel-Register).
- **Was umbenannt wird** (alte Kuerzel → neue; kaputte Nummern → saubere) -- als Vorher/Nachher-Tabelle.
- **Was wohin verschoben wird** -- lose Dateien in ihren `00-09`-Zielordner, Datei fuer Datei nachvollziehbar (zumindest fuer ein Muster-Objekt vollstaendig, dann das Muster auf die anderen anwenden).

Dann der **kritische Review aus deiner Sicht** -- das ist Pflicht, nicht Kuer: Sag dem Nutzer 1-3 Punkte, die ihm langfristig auf die Fuesse fallen koennten. Beispiele: *"Wenn du in drei Staedten kaufst, kollidiert das kurze Kuerzel-Schema frueher als du denkst -- willst du nicht doch das Stadt-Praefix?"* oder *"Die zentrale Belege-Ablage stirbt jetzt -- stell sicher, dass dein Steuerberater die neue Pro-Objekt-Logik mittraegt."* Du draengst nicht, aber du sprichst es aus.

Fasse zusammen und lass bestaetigen: *"Soll ich genau das so umsetzen?"*

### Schritt 6: Backup + Bau-Freigabe

Bevor du **irgendetwas** anlegst, umbenennst oder verschiebst, hol dir zwei Dinge:

1. **Backup -- Pflicht, keine Option, sobald mehr als ein Objekt betroffen ist.** Formuliere es als feste Regel, nicht als offene Frage, sonst klickt der Nutzer sie weg: *"Bevor ich umbaue, brauchen wir ein Backup -- bei mehr als einem Objekt setze ich nur **nach** Backup um, sonst bleibe ich im Plan-Modus. Am einfachsten: den ganzen Bestand-Ordner einmal duplizieren oder als ZIP herunterladen. Sag mir Bescheid, wenn das Backup steht."* Erst wenn das Backup bestaetigt ist (oder der Nutzer ausdruecklich nur den Plan will), geht es weiter. Bei genau **einem** Objekt mit wenigen Dateien darf der Nutzer bewusst darauf verzichten -- dann aber explizit benannt.
2. **Freigabe:** *"Soll ich jetzt loslegen?"* -- niemals ungefragt ins Live-System.

### Schritt 7: Umsetzung + Bericht

Setze um -- in dieser Sicherheits-Reihenfolge:

- **Bevorzugt: lokal synchronisierter Ordner.** Anlegen (`mkdir`), Umbenennen/Verschieben (`mv`). Atomar, schnell, behaelt bei Cloud-Sync die Datei-Historie. Arbeite **objektweise** und melde nach jedem Objekt kurz, was passiert ist.
- **Cloud-Connector mit Schreibrechten:** Ordner anlegen, dann Dateien verschieben. **Bevorzuge Umbenennen/Verschieben vor Kopieren** -- Umbenennen behaelt in Google Drive die Datei-ID und alle Freigabe-Links; **Kopieren erzeugt neue IDs (zerstoert Links, verdoppelt Speicher, verliert Kommentare/Versionen).** Niemals massenhaft kopieren.
- **Nur Lesezugriff:** kein Pseudo-Bau. Gib den Migrationsplan als exakte, nummerierte Klick-Anleitung aus (oder als Shell-Skript fuer den lokalen Sync-Ordner), die der Nutzer selbst ausfuehrt.

**Sicherheitsregeln bei der Umsetzung:**
- **Niemals loeschen.** Was unklar ist, kommt in einen `_Zu_pruefen/`-Ordner, nicht in den Papierkorb. Der Nutzer entscheidet ueber Loeschungen selbst.
- **Bei Namenskonflikten** (Zielname existiert schon) anhalten und fragen, nicht ueberschreiben.
- Lege das **Kuerzel-Register** und ein leeres **`00_Vorlagen/`** an -- das ist die Versicherung gegen das naechste Chaos.

Melde am Ende **konkret**, was steht (Anzahl angelegter/umbenannter/verschobener Ordner+Dateien, was im `_Zu_pruefen/` gelandet ist) -- nicht nur "fertig".

---

## Ausgabeformat

### Ist-Zustand-Bericht (kompakt, faktisch)

Tabelle: Entitaet / Objekt / aktuelles Kuerzel / Objekttyp / Auffaelligkeiten. Darunter die priorisierten Befunde (steuerlich/rechtlich zuerst).

### Migrationsplan (bestaetigungspflichtig)

| Aktion | Von | Nach |
|--------|-----|------|
| Anlegen | -- | `Musterbesitz GbR/1_Bestand/B8 — .../00_Objektdatenblatt.md` |
| Umbenennen | `BNBU8 - ...` | `B8 — MFH Beispielstr. 8, Musterstadt` |
| Verschieben | `Kalkulation.pdf` (Wurzel) | `B8 — .../02_Kaufprozess/` |

Plus: kritischer Langzeit-Review (1-3 Punkte) + Backup-Frage + Freigabe-Frage.

### Abschlussbericht

Was wurde angelegt/umbenannt/verschoben (mit Zahlen), was liegt in `_Zu_pruefen/`, wo steht das Kuerzel-Register, was sind die naechsten Schritte (z.B. Dateinamen nach Konvention nachziehen -- optional als Folgelauf).

---

## Warnsignale

- **Kein Backup, aber Massen-Umbau gewuenscht** → erst Backup, dann bauen. Nicht verhandelbar bei >1 Objekt.
- **Connector ist read-only, Nutzer erwartet Umbau** → ehrlich sagen, auf lokalen Sync oder Klick-Anleitung umschwenken.
- **Entitaeten sollen "der Einfachheit halber" zusammen** → widersprechen: Steuer laeuft pro Entitaet, Vermischung ist ein echtes Risiko.
- **Nutzer will Kuerzel rueckwirkend aendern** (Erstbelegten umbenennen) → die Eingefroren-Regel erklaeren, Neuankoemmling disambiguiert stattdessen.
- **Loeschen statt Parken** → niemals loeschen, immer `_Zu_pruefen/`.
- **Massen-Kopieren in der Cloud** → stoppen: zerstoert Links, verdoppelt Speicher. Umbenennen/Verschieben nutzen.

## Bei fehlenden Daten

- **Objekttyp/Entitaet unklar** → fragen, nicht annehmen; im Zweifel das volle Template (leere Ordner kosten nichts).
- **Kein Schreibzugriff feststellbar** → Plan-Modus, exakte Anleitung liefern.
- **Alte Struktur-Notizen widerspruechlich** → dem Nutzer vorlegen und entscheiden lassen, was gilt.

## Konfidenz-Bewertung

Gib am Ende des Ist-Bewertung eine kurze Einschaetzung, wie sicher die Zuordnung loser Dateien ist (HOCH/MITTEL/NIEDRIG) -- bei NIEDRIG landet die Datei im `_Zu_pruefen/`, nicht geraten in einem Zielordner.

---

## Beispiele

**1. Selbstverwalter, zwei Entitaeten, gemischtes Portfolio (Hauptfall).** Investor haelt aeltere Objekte privat (Bruchteilseigentum), neuere in einer eGbR. Drei verschiedene Innenstrukturen, Gesellschaftsdokumente lose, Belege zentral *und* pro Objekt. → Oberste Ebene nach Entitaet (eGbR mit `00_Gesellschaft`, Privat ohne), pro Objekt das `00-09`-Template, zentrale Belege pro Objekt aufgeloest, Kuerzel vereinheitlicht, Register angelegt.

**2. Fix & Flip.** Kurzer Lebenszyklus, Sanierung im Zentrum. → `0_Ankauf` und ein starker Sanierungsstrang, `2_Verkauft` frueh relevant; der jahrelange Betriebsblock (06-08) bleibt schlank, dafuer Sanierungs-Gewerke und Abverkaufs-Unterlagen ausgebaut.

**3. Kurzzeitvermietung.** Hohe Belegfrequenz, USt. → Plattform-Abrechnungen (Airbnb/Booking) in `06_Belege/`, USt-Voranmeldungen in `08_Steuer/`, Reinigung/Wartung als wiederkehrende Posten; Einheiten-Ordner schlank, dafuer Belege-Disziplin hoch.

**4. ETW-Einsteiger, erstes Objekt.** Noch keine Struktur. → Skill baut von null das Template, `05_Verwaltung/WEG/` aktiv (Wirtschaftsplan, Beschlusssammlung, Hausgeld, Teilungserklaerung), `00_Vorlagen` + Register gleich mit -- damit das zweite Objekt sauber andocken kann.

**5. Extern verwaltetes Portfolio.** Hausverwaltung macht NK + Mieter. → Betriebsordner schlanker, dafuer `05_Verwaltung/Hausverwaltung-extern/` (Verwaltervertrag, Abrechnungen, Korrespondenz) als saubere Schnittstelle; Eigentuemer-Sicht (Finanzierung, Steuer, Stammdaten) bleibt vollstaendig beim Investor.

---

## Verwandte Skills

- **`dokument-klassifizierer`** -- ordnet *einzelne* Dokumente dem richtigen Objekt + Zielordner zu. Ideal als Folgelauf, um lose Dateien nach dem Strukturaufbau einzusortieren.
- **`beleg-sortierer`** -- klassifiziert Belege (Erhaltung vs. Herstellung) fuer `06_Belege/` und die Steuer.
- **`prozess-designer`** -- baut Arbeitsablaeufe/Pipelines in immoJUMP (z.B. "Onboarding nach Kauf"), die das angelegte Objekt-Template bespielen.
- **`anlage-v-assistent`** / **`nebenkosten-pruefer`** -- arbeiten direkt auf den Jahres-Ordnern (`07`, `08`), die diese Struktur bereitstellt.
