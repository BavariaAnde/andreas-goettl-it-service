# Changelog

Änderungen an der Website von Andreas Göttl IT Service. Ton, Sie-Anrede und
Farbwelt (#f5f1e8, Light/Dark) wurden dabei nicht angetastet.

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
