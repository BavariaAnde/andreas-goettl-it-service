# Andreas Göttl IT Service

Produktionsreife One-Page-Website für GitHub Pages.

## Inhalt

- `index.html`: Semantische One-Page-Website mit SEO, JSON-LD, Impressum und Datenschutz.
- `styles.css`: Responsive Layout, Light/Dark Theme, Cards, Animationen und Barrierearmut.
- `script.js`: Theme-Toggle mit `localStorage`, Scroll-Reveal und Header-Zustand.
- `404.html`: Fehlerseite im gleichen Design für nicht gefundene URLs.
- `assets/`: WebP-/SVG-Bildassets für Hero, Leistungen, Logo/Icons und OpenGraph.
- `robots.txt`, `sitemap.xml`, `site.webmanifest`: Basisdateien für Deployment und SEO.

## Lokal testen

Kein Build-Schritt nötig – reines HTML/CSS/JS. Zum Testen reicht ein einfacher lokaler Server
(direktes Öffnen der `index.html` per Doppelklick funktioniert grundsätzlich auch, aber manche
Browser blockieren dann `fetch`/Pfade – ein lokaler Server ist zuverlässiger):

```bash
cd andreas-goettl-it-service
python3 -m http.server 8000
```

Danach im Browser `http://localhost:8000/` öffnen. Alle Pfade in `index.html` sind relativ,
die Seite funktioniert damit sowohl unter der eigenen Domain als auch in einem
GitHub-Pages-Unterordner (`username.github.io/repo-name/`).

## Deployment auf GitHub Pages

1. Repository auf GitHub pushen.
2. In den Repository-Einstellungen unter **Pages** die Quelle festlegen: Branch `main`,
   Verzeichnis `/ (root)`.
3. Bei eigener Domain die vorhandene `CNAME`-Datei verwenden (aktuell `www.andreas-goettl.de`);
   ansonsten die Datei löschen, dann läuft die Seite unter `username.github.io/repo-name/`.
4. Nach ein paar Minuten ist die Seite unter der konfigurierten Adresse erreichbar.

## Technische Hinweise

- Keine Frameworks, keine Build-Tools. Einzige externe Abhängigkeit: Google Fonts (Poppins,
  Inter) per `<link>`-Tag in `index.html`.
- Läuft statisch direkt auf GitHub Pages.
- Theme-Auswahl (hell/dunkel) wird lokal im Browser gespeichert.
- Die Website nutzt kein Tracking und keine Cookies.
