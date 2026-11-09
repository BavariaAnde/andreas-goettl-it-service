# Changelog

Änderungen an der Website von Andreas Göttl IT Service. Ton, Sie-Anrede und
Farbwelt (#f5f1e8, Light/Dark) wurden dabei nicht angetastet.

## 2026-11-09 – Drei sichtbare Leistungsbereiche

- Computer & Alltag, IT für kleine Betriebe sowie Websites & digitale Lösungen als drei gleichwertige Angebote. Bisherige Alltagshilfe bleibt enthalten; Websites, Formulare, Anmeldungen und kleine Webanwendungen werden aktiv angeboten.
- Sofort sichtbare Leistungszeilen, optional aufklappbare Kundenanliegen mit Kontaktlink. Native Details/Summary per Tastatur bedienbar, maximal ein Beispielbereich offen; Leistungen bleiben immer sichtbar.
- Echte Hofaufnahme in der Webkarte, Vereinsorganisations-Ansicht im Beispielbereich. Bildherkunft: docs/media/service-offer.md. Vorhandene Fotos in den anderen Bereichen weiterverwendet.
- Einstieg, Kontakttexte, Metadaten sowie Service-/FAQ-JSON-LD angepasst. 50 €/Stunde bleiben sichtbar; größere Projekte mit vorab abgestimmtem Aufwand und Budget.
- Geprüft bei 320/390/760/999/1024/1440px in Light/Dark: drei Angebote, kein horizontaler Überlauf, keine defekten geladenen Bilder. Beispiele per Klick und Enter, exklusives Öffnen, Anfrageanker, mobile Navigation und Preis-FAQ geprüft. JavaScript-Syntax, IDs, interne Anker und JSON-LD/FAQ-Übereinstimmung gültig. Kein Produktionsdeployment.

## 2026-11-09 – Kürzere Seite mit sichtbarem Profil

- Gesamtseite auf vier Bereiche gestrafft: Einstieg, Leistungen, persönliche Vorstellung mit Profilverweisen, Kontakt mit FAQ.
- Große Leistungskarten durch kompakte Bild-/Textzeilen ersetzt; alle fünf Leistungen bleiben enthalten. Das große Einstiegsbild entfällt auf schmalen Displays, die doppelte Kontaktbox und wiederholte Leistungs-Pills entfallen.
- „Warum ich“ und die zuvor ergänzte große Profilsektion zusammengeführt: echtes Porträt, kurze Arbeitsweise, auffälliger Profilbutton und direkte Links zu Projekten/Blog.
- Einzugsgebiet in den Kontaktbereich integriert. Kontakt und FAQ stehen am Desktop nebeneinander, mobil Kontakt zuerst. Alle fünf FAQ-Antworten, Preisangabe und Kontaktkanäle erhalten. Fragen durchgehend in Sie-Anrede.
- Hauptnavigation und früher Profilhinweis führen zum kompakten persönlichen Bereich; Profilverweis auch im Footer. Alte Anker #warum-ich und #einzugsgebiet bleiben erreichbar. Doppelte Abstände bei Sprungnavigation korrigiert.
- Vorher/Nachher am gleichen lokalen Server-Setup mit geladenen Originalbildern und geschlossenen FAQ: bei 390px ca. 7.965 → 3.535px Seitenhöhe (−56%), bei 1440px ca. 5.241 → 2.252px (−57%). Das sind Layoutmessungen, keine gemessenen Conversion-Steigerungen.
- Geprüft: 320/390/760/768/1024/1440px in beiden Themes ohne horizontalen Überlauf oder defekte geladene Bilder. Fünf Leistungen, fünf FAQ und drei Profilziele vorhanden. Mobile Navigation, FAQ per Klick/Tastatur, Impressum/Escape, eindeutige IDs und interne Anker geprüft; JavaScript-Syntax gültig. Kein Produktionsdeployment.

## 2026-07-06

### SEO & Auffindbarkeit

- JSON-LD: `priceRange` von generisch "€€" auf konkret "50 €/Std." geändert
  und `openingHoursSpecification` mit den echten Erreichbarkeitszeiten
  ergänzt (Mo–Do 18–20:30, Fr 13–20:30, Sa/So 9–13 Uhr).
- LocalBusiness- und FAQPage-Structured-Data, sitemap.xml, robots.txt sowie
  Meta-/OG-/Twitter-Tags waren bereits vorhanden und korrekt – nur das
  `lastmod`-Datum der sitemap.xml aktualisiert.
- Alt-Texte aller Bilder geprüft: waren bereits durchgängig beschreibend,
  keine Änderung nötig außer beim neuen Bild.

### Inhalt

- Neue Leistungskarte "Smartphone und Tablet" im Leistungen-Bereich
  ergänzt (Einrichtung, Fotos sichern, Apps) inkl. Eintrag in der
  JSON-LD-Leistungsliste.
- Neuer Abschnitt "Einzugsgebiet" mit kurzem, unaufdringlichem Absatz zu
  Arnstorf, Eggenfelden, Pfarrkirchen und Simbach am Inn.
- Abschnitt "Kundenstimmen" vorbereitet, aber als HTML-Kommentar
  deaktiviert (inkl. passendem CSS) – Aktivierung erst, wenn echte
  Bewertungen vorliegen.
- Footer-Zeile mit Links zu Malt-, Fiverr- und Upwork-Profil vorbereitet,
  aber ebenfalls auskommentiert. Aktivierung erst nach
  Nebentätigkeits-Zustimmung und wenn die Profile live sind.

### Technik & Qualität

- Kontrastwerte (Text/Hintergrund, hell und dunkel) rechnerisch geprüft:
  alle Kombinationen liegen über dem WCAG-AA-Grenzwert von 4.5:1.
- Fokus-Zustände für Tastaturbedienung, Lazy-Loading bei Bildern unterhalb
  des ersten Bildschirms und aria-Labels bei den Icon-Links
  (WhatsApp/Instagram/LinkedIn) waren bereits vorhanden und wurden nicht
  verändert.
- 404-Seite existierte bereits im Stil der Website.
- `assets/smartphone.webp`: die von dir hochgeladene Datei war tatsächlich
  ein 3,8 MB JPEG mit falscher `.webp`-Endung (6108×4072 px). Auf 900×600
  echtes WebP verkleinert (jetzt 22 KB), konsistent mit den anderen
  Leistungsbildern.

## Offene Punkte (manuell zu erledigen)

- **Google Business Profile** anlegen und mit den echten Öffnungszeiten
  und der Adresse befüllen.
- **Google Search Console** einrichten und die Domain verifizieren,
  sitemap.xml dort einreichen.
- **Kundenstimmen aktivieren**: sobald erste echte Bewertungen vorliegen,
  den auskommentierten Abschnitt in `index.html` (Suche nach
  "Kundenstimmen") einkommentieren und mit echten Zitaten befüllen.
- **Malt-/Fiverr-/Upwork-Zeile aktivieren**: erst nach Zustimmung zur
  Nebentätigkeit und wenn die Profile live sind – auskommentierten
  Abschnitt im Footer von `index.html` einkommentieren.
- **Aufräumen**: im `assets/`-Ordner liegt eine Datei
  `rmartinr-phone-8594571.jpg:Zone.Identifier` (Windows/WSL-Metadaten-Rest
  ohne Inhalt, vermutlich vom Download des Smartphone-Fotos). Kann
  gefahrlos gelöscht werden, wurde hier bewusst nicht automatisch entfernt.
- Optional prüfen: reales Lighthouse-Audit im Browser fahren (Performance,
  insbesondere auf einem echten Mobilgerät/Verbindung), da hier nur
  statisch geprüft wurde (Kontrast, Fokus, Lazy-Loading, HTML-Struktur).
