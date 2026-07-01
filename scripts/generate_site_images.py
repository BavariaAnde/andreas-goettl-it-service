#!/usr/bin/env python3
from pathlib import Path
import html
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

FONT = "DejaVu Sans"
BG = "#f7f5ef"
BG_SOFT = "#eeebe3"
SURFACE = "#ffffff"
NAVY = "#071426"
TEXT = "#17202d"
MUTED = "#647084"
GREEN = "#2f8d68"
GREEN_DARK = "#166a4c"
GREEN_SOFT = "#dceee6"
BORDER = "#d8d3c8"
YELLOW = "#f4c95d"
BLUE = "#5677b9"
RED = "#d7675f"
INK = "#101827"


def esc(value):
    return html.escape(value, quote=True)


def base(width, height, title, subtitle=None, variant="desk"):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<defs>",
        '<filter id="shadow" x="-20%" y="-20%" width="140%" height="150%">',
        '<feDropShadow dx="0" dy="22" stdDeviation="24" flood-color="#071426" flood-opacity=".16"/>',
        "</filter>",
        '<filter id="soft" x="-20%" y="-20%" width="140%" height="140%">',
        '<feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#071426" flood-opacity=".12"/>',
        "</filter>",
        "</defs>",
        f'<rect width="100%" height="100%" fill="{BG}"/>',
        f'<path d="M0 0 H{width} V{height} H0 Z" fill="{BG_SOFT}" opacity=".38"/>',
        f'<circle cx="{width * .12:.1f}" cy="{height * .18:.1f}" r="{min(width, height) * .19:.1f}" fill="{GREEN_SOFT}" opacity=".72"/>',
        f'<circle cx="{width * .88:.1f}" cy="{height * .80:.1f}" r="{min(width, height) * .24:.1f}" fill="#e7edf4" opacity=".9"/>',
        f'<path d="M0 {height * .78:.1f} C {width * .22:.1f} {height * .69:.1f}, {width * .58:.1f} {height * .92:.1f}, {width} {height * .74:.1f} L {width} {height} L 0 {height} Z" fill="#e9e4d8"/>',
    ]


def label(svg, width, height, title, subtitle=None):
    x = width * 0.075
    y = height * 0.13
    svg.append(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{max(27, width * .045):.1f}" font-weight="800" fill="{TEXT}">{esc(title)}</text>')
    if subtitle:
        svg.append(f'<text x="{x:.1f}" y="{y + height * .07:.1f}" font-family="{FONT}" font-size="{max(16, width * .022):.1f}" font-weight="600" fill="{MUTED}">{esc(subtitle)}</text>')


def monitor(svg, x, y, w, h, lines=True):
    svg.append(f'<g filter="url(#shadow)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{SURFACE}" stroke="{BORDER}" stroke-width="2"/>')
    svg.append(f'<rect x="{x + w * .06}" y="{y + h * .08}" width="{w * .88}" height="{h * .68}" rx="10" fill="{NAVY}"/>')
    if lines:
        for i, color in enumerate([GREEN, YELLOW, "#ffffff", BLUE]):
            yy = y + h * (.18 + i * .12)
            svg.append(f'<rect x="{x + w * .13}" y="{yy}" width="{w * (.48 + .08 * (i % 2))}" height="{h * .028}" rx="5" fill="{color}" opacity="{.95 if color != "#ffffff" else .72}"/>')
    svg.append(f'<rect x="{x + w * .42}" y="{y + h * .79}" width="{w * .16}" height="{h * .13}" rx="4" fill="{BORDER}"/>')
    svg.append(f'<rect x="{x + w * .30}" y="{y + h * .91}" width="{w * .40}" height="{h * .045}" rx="6" fill="{SURFACE}" stroke="{BORDER}" stroke-width="2"/></g>')


def laptop(svg, x, y, w, h):
    svg.append(f'<g filter="url(#shadow)"><rect x="{x + w * .08}" y="{y}" width="{w * .84}" height="{h * .68}" rx="16" fill="{SURFACE}" stroke="{BORDER}" stroke-width="2"/>')
    svg.append(f'<rect x="{x + w * .14}" y="{y + h * .08}" width="{w * .72}" height="{h * .48}" rx="8" fill="{NAVY}"/>')
    svg.append(f'<path d="M{x} {y + h * .69} H{x + w} L{x + w * .91} {y + h * .86} H{x + w * .09} Z" fill="{SURFACE}" stroke="{BORDER}" stroke-width="2"/>')
    svg.append(f'<rect x="{x + w * .41}" y="{y + h * .73}" width="{w * .18}" height="{h * .035}" rx="5" fill="{BORDER}"/></g>')


def router(svg, x, y, w, h, waves=True):
    svg.append(f'<g filter="url(#soft)"><rect x="{x}" y="{y + h * .46}" width="{w}" height="{h * .34}" rx="16" fill="{SURFACE}" stroke="{BORDER}" stroke-width="2"/>')
    for i, color in enumerate([GREEN, GREEN, YELLOW, BLUE]):
        svg.append(f'<circle cx="{x + w * (.16 + i * .13):.1f}" cy="{y + h * .63:.1f}" r="{h * .025:.1f}" fill="{color}"/>')
    svg.append(f'<path d="M{x + w * .77} {y + h * .46} L{x + w * .9} {y + h * .08}" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>')
    svg.append(f'<path d="M{x + w * .23} {y + h * .46} L{x + w * .1} {y + h * .08}" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>')
    if waves:
        for r, op in [(0.58, .33), (.78, .22), (.98, .14)]:
            svg.append(f'<path d="M{x + w * (0.5 - r / 3):.1f} {y + h * (.27 - r / 9):.1f} Q{x + w * .5:.1f} {y - h * r * .25:.1f} {x + w * (0.5 + r / 3):.1f} {y + h * (.27 - r / 9):.1f}" fill="none" stroke="{GREEN}" stroke-width="7" stroke-linecap="round" opacity="{op}"/>')
    svg.append("</g>")


def printer(svg, x, y, w, h, scan=False):
    svg.append(f'<g filter="url(#shadow)"><rect x="{x + w * .12}" y="{y + h * .05}" width="{w * .76}" height="{h * .32}" rx="12" fill="{SURFACE}" stroke="{BORDER}" stroke-width="2"/>')
    svg.append(f'<rect x="{x}" y="{y + h * .31}" width="{w}" height="{h * .40}" rx="18" fill="{SURFACE}" stroke="{BORDER}" stroke-width="2"/>')
    svg.append(f'<rect x="{x + w * .12}" y="{y + h * .50}" width="{w * .76}" height="{h * .36}" rx="8" fill="#f9fafb" stroke="{BORDER}" stroke-width="2"/>')
    svg.append(f'<circle cx="{x + w * .82}" cy="{y + h * .45}" r="{h * .035}" fill="{GREEN}"/>')
    if scan:
        svg.append(f'<rect x="{x + w * .22}" y="{y + h * .59}" width="{w * .56}" height="{h * .045}" rx="4" fill="{BLUE}" opacity=".75"/>')
        svg.append(f'<rect x="{x + w * .22}" y="{y + h * .67}" width="{w * .42}" height="{h * .035}" rx="4" fill="{GREEN}" opacity=".75"/>')
    else:
        for i in range(3):
            svg.append(f'<rect x="{x + w * .24}" y="{y + h * (.60 + i * .08)}" width="{w * (.52 - i * .07)}" height="{h * .025}" rx="3" fill="{MUTED}" opacity=".42"/>')
    svg.append("</g>")


def cloud(svg, x, y, w, h, shield=False):
    svg.append(f'<g filter="url(#soft)"><path d="M{x + w * .22} {y + h * .62} C{x + w * .07} {y + h * .61}, {x} {y + h * .48}, {x + w * .08} {y + h * .36} C{x + w * .14} {y + h * .24}, {x + w * .29} {y + h * .25}, {x + w * .35} {y + h * .31} C{x + w * .43} {y + h * .14}, {x + w * .69} {y + h * .16}, {x + w * .75} {y + h * .36} C{x + w * .91} {y + h * .36}, {x + w} {y + h * .48}, {x + w * .93} {y + h * .61} Z" fill="{SURFACE}" stroke="{BORDER}" stroke-width="2"/>')
    if shield:
        svg.append(f'<path d="M{x + w * .50} {y + h * .33} L{x + w * .66} {y + h * .40} V{y + h * .53} C{x + w * .64} {y + h * .64}, {x + w * .56} {y + h * .72}, {x + w * .50} {y + h * .76} C{x + w * .44} {y + h * .72}, {x + w * .36} {y + h * .64}, {x + w * .34} {y + h * .53} V{y + h * .40} Z" fill="{GREEN}"/>')
    else:
        svg.append(f'<path d="M{x + w * .34} {y + h * .49} H{x + w * .66} M{x + w * .50} {y + h * .34} V{y + h * .65}" stroke="{GREEN}" stroke-width="10" stroke-linecap="round"/>')
    svg.append("</g>")


def nodes(svg, x, y, w, h, cable=False):
    points = [(0.16, .30), (.50, .18), (.83, .34), (.28, .68), (.68, .70)]
    for a, b in [(0, 1), (1, 2), (0, 3), (3, 4), (4, 2), (1, 4)]:
        x1, y1 = x + w * points[a][0], y + h * points[a][1]
        x2, y2 = x + w * points[b][0], y + h * points[b][1]
        svg.append(f'<path d="M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f}" stroke="{GREEN if not cable else NAVY}" stroke-width="{7 if cable else 5}" stroke-linecap="round" opacity=".55"/>')
    for i, (px, py) in enumerate(points):
        color = [GREEN, NAVY, BLUE, YELLOW, RED][i]
        svg.append(f'<circle cx="{x + w * px:.1f}" cy="{y + h * py:.1f}" r="{h * .065:.1f}" fill="{SURFACE}" stroke="{color}" stroke-width="7" filter="url(#soft)"/>')


def mail(svg, x, y, w, h):
    svg.append(f'<g filter="url(#shadow)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="{SURFACE}" stroke="{BORDER}" stroke-width="2"/>')
    svg.append(f'<path d="M{x + w * .08} {y + h * .20} L{x + w * .50} {y + h * .56} L{x + w * .92} {y + h * .20}" fill="none" stroke="{GREEN}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>')
    svg.append(f'<path d="M{x + w * .10} {y + h * .82} L{x + w * .38} {y + h * .50} M{x + w * .90} {y + h * .82} L{x + w * .62} {y + h * .50}" stroke="{BORDER}" stroke-width="6" stroke-linecap="round"/>')
    svg.append("</g>")


def phone_remote(svg, x, y, w, h):
    svg.append(f'<g filter="url(#shadow)"><rect x="{x}" y="{y}" width="{w * .42}" height="{h}" rx="26" fill="{SURFACE}" stroke="{BORDER}" stroke-width="2"/>')
    svg.append(f'<rect x="{x + w * .055}" y="{y + h * .10}" width="{w * .31}" height="{h * .75}" rx="14" fill="{NAVY}"/>')
    svg.append(f'<circle cx="{x + w * .21}" cy="{y + h * .92}" r="{h * .025}" fill="{BORDER}"/>')
    svg.append(f'<rect x="{x + w * .55}" y="{y + h * .18}" width="{w * .45}" height="{h * .52}" rx="18" fill="{SURFACE}" stroke="{BORDER}" stroke-width="2"/>')
    svg.append(f'<path d="M{x + w * .62} {y + h * .43} H{x + w * .83}" stroke="{GREEN}" stroke-width="10" stroke-linecap="round"/>')
    svg.append(f'<path d="M{x + w * .75} {y + h * .32} L{x + w * .88} {y + h * .43} L{x + w * .75} {y + h * .54}" fill="none" stroke="{GREEN}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>')
    svg.append("</g>")


def setup_new(svg, x, y, w, h):
    monitor(svg, x, y, w * .72, h * .82, lines=False)
    svg.append(f'<g filter="url(#soft)"><circle cx="{x + w * .78}" cy="{y + h * .24}" r="{h * .13}" fill="{GREEN}"/>')
    svg.append(f'<path d="M{x + w * .73} {y + h * .24} L{x + w * .77} {y + h * .29} L{x + w * .85} {y + h * .18}" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/></g>')


def draw_asset(name, title, subtitle, topic, width=900, height=590):
    svg = base(width, height, title, subtitle)
    label(svg, width, height, title, subtitle)
    if topic == "wlan":
        router(svg, width * .30, height * .31, width * .42, height * .43)
    elif topic == "router":
        router(svg, width * .28, height * .34, width * .46, height * .42, waves=False)
        nodes(svg, width * .63, height * .36, width * .20, height * .28)
    elif topic == "mesh":
        nodes(svg, width * .24, height * .31, width * .54, height * .46)
        router(svg, width * .40, height * .45, width * .24, height * .28, waves=False)
    elif topic == "network":
        nodes(svg, width * .22, height * .28, width * .58, height * .52)
    elif topic == "lan":
        nodes(svg, width * .23, height * .30, width * .58, height * .50, cable=True)
    elif topic == "internet":
        router(svg, width * .16, height * .38, width * .34, height * .35)
        cloud(svg, width * .55, height * .34, width * .28, height * .27)
    elif topic == "pc":
        monitor(svg, width * .25, height * .28, width * .52, height * .48)
    elif topic == "laptop":
        laptop(svg, width * .23, height * .31, width * .56, height * .42)
    elif topic == "windows":
        monitor(svg, width * .24, height * .29, width * .52, height * .48, lines=False)
        for dx, dy, c in [(0, 0, GREEN), (1, 0, BLUE), (0, 1, YELLOW), (1, 1, RED)]:
            svg.append(f'<rect x="{width * (.40 + dx * .07):.1f}" y="{height * (.44 + dy * .095):.1f}" width="{width * .055:.1f}" height="{height * .07:.1f}" rx="6" fill="{c}"/>')
    elif topic == "slow":
        monitor(svg, width * .22, height * .29, width * .50, height * .48, lines=False)
        svg.append(f'<path d="M{width*.65:.1f} {height*.39:.1f} A{width*.11:.1f} {width*.11:.1f} 0 1 1 {width*.56:.1f} {height*.58:.1f}" fill="none" stroke="{YELLOW}" stroke-width="12" stroke-linecap="round"/>')
        svg.append(f'<path d="M{width*.61:.1f} {height*.50:.1f} L{width*.69:.1f} {height*.42:.1f}" stroke="{GREEN_DARK}" stroke-width="10" stroke-linecap="round"/>')
    elif topic == "printer":
        printer(svg, width * .25, height * .28, width * .50, height * .48)
    elif topic == "scanner":
        printer(svg, width * .25, height * .28, width * .50, height * .48, scan=True)
    elif topic == "backup":
        cloud(svg, width * .30, height * .29, width * .42, height * .36, shield=True)
    elif topic == "data":
        cloud(svg, width * .18, height * .34, width * .28, height * .25, shield=True)
        laptop(svg, width * .52, height * .34, width * .32, height * .27)
        svg.append(f'<path d="M{width*.46:.1f} {height*.47:.1f} C{width*.50:.1f} {height*.40:.1f}, {width*.55:.1f} {height*.40:.1f}, {width*.59:.1f} {height*.47:.1f}" fill="none" stroke="{GREEN}" stroke-width="9" stroke-linecap="round"/>')
    elif topic == "newpc":
        setup_new(svg, width * .24, height * .29, width * .58, height * .50)
    elif topic == "office":
        monitor(svg, width * .18, height * .29, width * .42, height * .45, lines=False)
        cloud(svg, width * .60, height * .35, width * .25, height * .24)
    elif topic == "mail":
        mail(svg, width * .28, height * .31, width * .44, height * .34)
    elif topic == "remote":
        phone_remote(svg, width * .24, height * .26, width * .54, height * .48)
    elif topic == "service":
        laptop(svg, width * .20, height * .34, width * .34, height * .30)
        router(svg, width * .56, height * .33, width * .26, height * .32)
        cloud(svg, width * .42, height * .25, width * .22, height * .20, shield=True)
    svg.append("</svg>")
    write_webp(name, "\n".join(svg), width, height)


def draw_hero():
    width, height = 1200, 900
    svg = base(width, height, "Andreas Göttl IT Service", "Computerhilfe für Roßbach, Rottal-Inn und Niederbayern")
    label(svg, width, height, "Andreas Göttl IT Service", "Computerhilfe für Roßbach, Rottal-Inn und Niederbayern")
    monitor(svg, 150, 310, 520, 390)
    router(svg, 735, 360, 300, 280)
    printer(svg, 690, 600, 300, 210)
    svg.append(f'<rect x="132" y="735" width="936" height="36" rx="18" fill="{SURFACE}" opacity=".85"/>')
    for i, text in enumerate(["WLAN", "PC", "Drucker", "Backup", "Fernwartung"]):
        x = 177 + i * 170
        svg.append(f'<circle cx="{x}" cy="753" r="8" fill="{GREEN}"/>')
        svg.append(f'<text x="{x + 18}" y="760" font-family="{FONT}" font-size="22" font-weight="800" fill="{TEXT}">{text}</text>')
    svg.append("</svg>")
    write_webp("hero.webp", "\n".join(svg), width, height)


def draw_og():
    width, height = 1200, 630
    svg = base(width, height, "Andreas Göttl IT Service", "IT Service Roßbach")
    svg.append(f'<text x="82" y="148" font-family="{FONT}" font-size="56" font-weight="850" fill="{TEXT}">Andreas Göttl</text>')
    svg.append(f'<text x="82" y="216" font-family="{FONT}" font-size="56" font-weight="850" fill="{TEXT}">IT Service</text>')
    svg.append(f'<text x="84" y="282" font-family="{FONT}" font-size="26" font-weight="700" fill="{MUTED}">Computerhilfe, WLAN, Drucker, Backup und Fernwartung</text>')
    svg.append(f'<rect x="84" y="330" width="360" height="54" rx="27" fill="{GREEN}"/>')
    svg.append('<text x="114" y="365" font-family="DejaVu Sans" font-size="24" font-weight="800" fill="#fff">Roßbach · Rottal-Inn</text>')
    monitor(svg, 610, 170, 390, 290)
    router(svg, 870, 330, 220, 190)
    svg.append("</svg>")
    write_webp("og-image.webp", "\n".join(svg), width, height)


def write_webp(name, svg_text, width, height):
    ASSETS.mkdir(exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".svg", delete=False) as tmp:
        tmp.write(svg_text)
        svg_path = Path(tmp.name)
    out = ASSETS / name
    try:
        subprocess.run(
            ["convert", "-background", "none", "-density", "144", str(svg_path), "-resize", f"{width}x{height}", "-quality", "84", str(out)],
            check=True,
        )
    finally:
        svg_path.unlink(missing_ok=True)


def main():
    draw_hero()
    draw_og()
    assets = [
        ("wlan.webp", "WLAN verbessern", "Stabile Verbindung im ganzen Haus", "wlan"),
        ("router.webp", "Router", "Sauber eingerichtet und abgesichert", "router"),
        ("mesh.webp", "Mesh", "Mehr Reichweite ohne Technikstress", "mesh"),
        ("network.webp", "Netzwerk", "Geräte zuverlässig verbinden", "network"),
        ("lan.webp", "LAN", "Stabile Kabelverbindungen", "lan"),
        ("internet.webp", "Internetprobleme", "Ursache klar eingrenzen", "internet"),
        ("pc.webp", "PC Hilfe", "Fehler ruhig analysieren", "pc"),
        ("laptop.webp", "Laptop Hilfe", "Mobil arbeiten ohne Störungen", "laptop"),
        ("windows.webp", "Windows Probleme", "Updates, Treiber und Einstellungen", "windows"),
        ("slow-computer.webp", "Computer langsam", "Leistung sinnvoll prüfen", "slow"),
        ("printer.webp", "Drucker", "Verbinden, testen, drucken", "printer"),
        ("scanner.webp", "Scanner", "Dokumente sauber digitalisieren", "scanner"),
        ("backup.webp", "Backup", "Daten gegen Verlust schützen", "backup"),
        ("datensicherung.webp", "Datensicherung", "Wichtige Dateien wiederfinden", "backup"),
        ("new-pc.webp", "Neue PCs einrichten", "Startklar für den Alltag", "newpc"),
        ("data-transfer.webp", "Datenübernahme", "Geordnet auf neue Geräte", "data"),
        ("microsoft-365.webp", "Microsoft 365", "Office, OneDrive und Outlook", "office"),
        ("email.webp", "E-Mail", "Postfächer sauber verbinden", "mail"),
        ("remote.webp", "Fernwartung", "Schnelle Hilfe aus der Ferne", "remote"),
        ("it-service.webp", "IT-Service", "Problem sortieren, Lösung finden", "service"),
    ]
    for asset in assets:
        draw_asset(*asset)


if __name__ == "__main__":
    main()
