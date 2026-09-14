#!/usr/bin/env python3
"""Generate Local SEO pages for Elite Craft Honor LLC without inventing business facts."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SITE = "https://elitecrafthonor.com"
PHONE = "+1-401-616-0779"
PHONE_DISPLAY = "(401) 616-0779"
EMAIL = "gmonsalve@elitecrafthonor.com"
OG_IMAGE = f"{SITE}/images/logotipo_principal.png"
PAGES: list[dict] = []

CITIES_RI = [
    ("central-falls-ri.html", "Central Falls", "RI", "02863"),
    ("pawtucket-ri.html", "Pawtucket", "RI", "02860"),
    ("providence-ri.html", "Providence", "RI", "02903"),
    ("cranston-ri.html", "Cranston", "RI", "02910"),
    ("lincoln-ri.html", "Lincoln", "RI", "02865"),
    ("cumberland-ri.html", "Cumberland", "RI", "02864"),
    ("johnston-ri.html", "Johnston", "RI", "02919"),
    ("north-providence-ri.html", "North Providence", "RI", "02911"),
    ("smithfield-ri.html", "Smithfield", "RI", "02917"),
    ("woonsocket-ri.html", "Woonsocket", "RI", "02895"),
    ("warwick-ri.html", "Warwick", "RI", "02886"),
    ("east-providence-ri.html", "East Providence", "RI", "02914"),
    ("bristol-ri.html", "Bristol", "RI", "02809"),
    ("coventry-ri.html", "Coventry", "RI", "02816"),
]
CITIES_MA = [
    ("attleboro-ma.html", "Attleboro", "MA", "02703"),
    ("north-attleborough-ma.html", "North Attleborough", "MA", "02760"),
    ("seekonk-ma.html", "Seekonk", "MA", "02771"),
    ("foxborough-ma.html", "Foxborough", "MA", "02035"),
]


def rel(depth: int) -> str:
    return "../" * depth


def track(path: str, title: str, changefreq: str = "monthly", priority: str = "0.7") -> None:
    PAGES.append({"path": path, "title": title, "changefreq": changefreq, "priority": priority})


def json_ld(data) -> str:
    return json.dumps(data, indent=2, ensure_ascii=False)


def head(
    *,
    title: str,
    description: str,
    canonical: str,
    depth: int,
    og_type: str = "website",
    extra: str = "",
    robots: str = "index, follow",
) -> str:
    r = rel(depth)
    canon = f"{SITE}/" if canonical in ("", "index.html") else f"{SITE}/{canonical}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="robots" content="{robots}" />
  <link rel="canonical" href="{canon}" />
  <link rel="icon" href="{r}images/isotipe.png" type="image/png" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:type" content="{og_type}" />
  <meta property="og:site_name" content="Elite Craft Honor LLC" />
  <meta property="og:image" content="{OG_IMAGE}" />
  <meta property="og:image:alt" content="Elite Craft Honor LLC logo" />
  <meta property="og:locale" content="en_US" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{description}" />
  <meta name="twitter:image" content="{OG_IMAGE}" />
  <meta name="theme-color" content="#0d0b09" />
  <!-- Add Google Search Console verification here -->
  <!-- Add Google Analytics 4 measurement ID here -->
  <!-- Add Google Tag Manager container ID here -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{r}style.css" />
  {extra}
</head>"""


def header(depth: int, active: str) -> str:
    r = rel(depth)

    def cls(name: str) -> str:
        return ' class="active"' if name == active else ""

    return f"""  <a class="skip-link" href="#main-content">Skip to content</a>
  <header class="site-header">
    <div class="topline">
      <div class="container topline-inner">
        <span>Registered and insured contractor serving Rhode Island and nearby Massachusetts</span>
        <div class="topline-links">
          <a href="mailto:{EMAIL}">{EMAIL}</a>
          <a href="tel:{PHONE}">{PHONE_DISPLAY}</a>
        </div>
      </div>
    </div>
    <div class="container nav">
      <a class="brand" href="{r}index.html">
        <span class="brand-mark">E</span>
        <span class="brand-name">
          <img src="{r}images/logotipo_horizontal.png" alt="Elite Craft Honor LLC logo" width="1796" height="876" />
        </span>
      </a>
      <ul class="nav-links">
        <li><a{cls("home")} href="{r}index.html">Home</a></li>
        <li><a{cls("services")} href="{r}services.html">Services</a></li>
        <li><a{cls("areas")} href="{r}locations/index.html">Service Areas</a></li>
        <li><a{cls("about")} href="{r}about.html">About</a></li>
        <li><a{cls("gallery")} href="{r}projects.html">Gallery</a></li>
        <li><a{cls("contact")} href="{r}contact.html">Contact</a></li>
      </ul>
      <a class="btn btn-contact" href="{r}contact.html#estimate-form">Get a Free Estimate</a>
    </div>
  </header>"""


def footer(depth: int) -> str:
    r = rel(depth)
    return f"""  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <p class="footer-brand">Elite Craft Honor LLC</p>
        <p>Painting | Carpentry | Handyman | Remodeling</p>
        <p>Serving Rhode Island and nearby Massachusetts</p>
        <p><a href="tel:{PHONE}">{PHONE_DISPLAY}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <p class="placeholder-note">Street address for Google Business Profile: [PLACEHOLDER: business street address]</p>
      </div>
      <nav aria-label="Footer">
        <a href="{r}index.html">Home</a>
        <a href="{r}about.html">About</a>
        <a href="{r}services.html">Services</a>
        <a href="{r}services/painting.html">Painting</a>
        <a href="{r}services/carpentry.html">Carpentry</a>
        <a href="{r}services/handyman.html">Handyman</a>
        <a href="{r}services/remodeling.html">Remodeling</a>
        <a href="{r}locations/index.html">Service Areas</a>
        <a href="{r}contact.html">Contact</a>
      </nav>
      <div>
        <p>Request an estimate for painting, finish carpentry, drywall, cabinets, or general home repairs.</p>
        <a class="btn btn-primary" href="{r}contact.html#estimate-form">Get a Free Estimate</a>
      </div>
    </div>
    <div class="container">
      <p class="footer-copy">&copy; <span data-year></span> Elite Craft Honor LLC. Crafted with excellence and integrity.</p>
    </div>
  </footer>
  <script src="{r}script.js"></script>
</body>
</html>"""


def crumbs(items: list[tuple[str, str]]) -> str:
    parts = []
    for label, href in items[:-1]:
        parts.append(f'<a href="{href}">{label}</a> <span aria-hidden="true">/</span>')
    parts.append(f"<span>{items[-1][0]}</span>")
    return f'<nav class="breadcrumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'


def breadcrumb_ld(items: list[tuple[str, str]]) -> dict:
    elements = []
    for i, (name, url) in enumerate(items, 1):
        elements.append({"@type": "ListItem", "position": i, "name": name, "item": url})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": elements}


def faq_html(faqs: list[tuple[str, str]]) -> str:
    blocks = []
    for q, a in faqs:
        blocks.append(f"<details><summary>{q}</summary><p>{a}</p></details>")
    return '<section class="section"><div class="container seo-prose"><h2>Frequently asked questions</h2><div class="faq-list">' + "".join(blocks) + "</div></div></section>"


def faq_ld(faqs: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }


def org_ld() -> dict:
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["LocalBusiness", "HomeAndConstructionBusiness"],
                "@id": f"{SITE}/#business",
                "name": "Elite Craft Honor LLC",
                "url": f"{SITE}/",
                "telephone": PHONE,
                "email": EMAIL,
                "description": "Registered and insured painting, carpentry, handyman, and remodeling contractor serving Rhode Island and nearby Massachusetts.",
                "areaServed": [{"@type": "State", "name": "Rhode Island"}, {"@type": "State", "name": "Massachusetts"}]
                + [{"@type": "City", "name": name, "addressRegion": st} for _, name, st, _ in CITIES_RI + CITIES_MA],
                "address": {"@type": "PostalAddress", "addressRegion": "RI", "addressCountry": "US"},
                "priceRange": "[PLACEHOLDER: price range, e.g. $$]",
                "image": OG_IMAGE,
            },
            {
                "@type": "WebSite",
                "@id": f"{SITE}/#website",
                "url": f"{SITE}/",
                "name": "Elite Craft Honor LLC",
                "publisher": {"@id": f"{SITE}/#business"},
            },
        ],
    }


def cta(depth: int, heading: str, copy: str) -> str:
    r = rel(depth)
    return f"""    <section class="container cta">
      <div>
        <h2>{heading}</h2>
        <p>{copy}</p>
      </div>
      <div class="hero-actions" style="margin-bottom:0;">
        <a class="btn btn-primary" data-track="estimate-click" href="{r}contact.html#estimate-form">Request an Estimate</a>
        <a class="btn btn-ghost" href="tel:{PHONE}">Call {PHONE_DISPLAY}</a>
      </div>
    </section>"""


def write(path: Path, html: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def redirect_page(old: str, new: str, title: str) -> None:
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>{title}</title>
  <link rel="canonical" href="{SITE}/{new}" />
  <meta http-equiv="refresh" content="0; url={new}" />
  <meta name="robots" content="noindex, follow" />
</head>
<body>
  <p>This page has moved to <a href="{new}">{SITE}/{new}</a>.</p>
</body>
</html>
"""
    write(ROOT / old, html)


def service_page(
    filename: str,
    title: str,
    description: str,
    h1: str,
    intro: list[str],
    included: list[tuple[str, str]],
    process: list[tuple[str, str]],
    related: list[tuple[str, str]],
    faqs: list[tuple[str, str]],
    service_type: str,
    keywords_note: str,
) -> None:
    depth = 1
    r = rel(depth)
    path = f"services/{filename}"
    track(path, title, "monthly", "0.8")
    crumb_items = [
        ("Home", f"{SITE}/"),
        ("Services", f"{SITE}/services.html"),
        (h1, f"{SITE}/{path}"),
    ]
    schema = [
        breadcrumb_ld(crumb_items),
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": h1,
            "serviceType": service_type,
            "provider": {"@id": f"{SITE}/#business"},
            "areaServed": [{"@type": "State", "name": "Rhode Island"}, {"@type": "State", "name": "Massachusetts"}],
            "url": f"{SITE}/{path}",
            "description": description,
        },
        faq_ld(faqs),
    ]
    extra = "\n".join(f'<script type="application/ld+json">\n{json_ld(s)}\n</script>' for s in schema)
    cards = "".join(
        f'<article class="card is-reveal"><h3>{h}</h3><p>{p}</p></article>' for h, p in included
    )
    steps = "".join(
        f'<article class="plan-step is-reveal"><strong>Step {i:02d}</strong><h3>{h}</h3><p>{p}</p></article>'
        for i, (h, p) in enumerate(process, 1)
    )
    related_html = "".join(f'<a href="{href}">{label}</a>' for href, label in related)
    paras = "".join(f"<p>{p}</p>" for p in intro)
    html = f"""{head(title=title, description=description, canonical=path, depth=depth, extra=extra)}
<body class="page-services" data-service-name="{h1}">
{header(depth, "services")}
  <main id="main-content">
    <section class="page-banner">
      <div class="container">
        {crumbs([("Home", f"{r}index.html"), ("Services", f"{r}services.html"), (h1, "")])}
        <span class="badge">Service</span>
        <h1>{h1}</h1>
        <p>{intro[0]}</p>
      </div>
    </section>
    <section class="section">
      <div class="container seo-prose">{paras[len(f"<p>{intro[0]}</p>"):] if False else paras}</div>
    </section>
    <section class="section">
      <div class="container">
        <h2>What's included</h2>
        <div class="cards">{cards}</div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <h2>How we complete the work</h2>
        <div class="plan-grid">{steps}</div>
      </div>
    </section>
    <section class="section section-alt">
      <div class="container">
        <h2>Areas we serve</h2>
        <p class="lead">This service is available across Rhode Island and nearby Massachusetts communities listed on our <a href="{r}locations/index.html">service areas</a> page, including Providence, Pawtucket, Cranston, and Attleboro.</p>
        <p>Related work: <span class="related-links">{related_html}</span></p>
      </div>
    </section>
    {faq_html(faqs)}
    {cta(depth, "Request a free estimate", "Call or send project details and we will follow up with a clear scope.")}
  </main>
{footer(depth)}
"""
    write(ROOT / "services" / filename, html)


def support_page(
    filename: str,
    title: str,
    description: str,
    h1: str,
    intro: list[str],
    included: list[tuple[str, str]],
    process: list[tuple[str, str]] | None,
    related: list[tuple[str, str]],
    faqs: list[tuple[str, str]],
    service_name: str,
) -> None:
    depth = 0
    r = rel(depth)
    track(filename, title, "monthly", "0.65")
    crumb_items = [
        ("Home", f"{SITE}/"),
        ("Services", f"{SITE}/services.html"),
        (h1, f"{SITE}/{filename}"),
    ]
    schema = [breadcrumb_ld(crumb_items), faq_ld(faqs)]
    extra = "\n".join(f'<script type="application/ld+json">\n{json_ld(s)}\n</script>' for s in schema)
    cards = "".join(f'<article class="card is-reveal"><h3>{h}</h3><p>{p}</p></article>' for h, p in included)
    steps = ""
    if process:
        step_html = "".join(
            f'<article class="plan-step is-reveal"><strong>Step {i:02d}</strong><h3>{h}</h3><p>{p}</p></article>'
            for i, (h, p) in enumerate(process, 1)
        )
        steps = f'<section class="section"><div class="container"><h2>Our plan of work</h2><div class="plan-grid">{step_html}</div></div></section>'
    related_html = "".join(f'<a href="{href}">{label}</a>' for href, label in related)
    paras = "".join(f"<p>{p}</p>" for p in intro)
    html = f"""{head(title=title, description=description, canonical=filename, depth=depth, extra=extra)}
<body data-service-name="{service_name}">
{header(depth, "services")}
  <main id="main-content">
    <section class="page-banner">
      <div class="container">
        {crumbs([("Home", f"{r}index.html"), ("Services", f"{r}services.html"), (h1, "")])}
        <span class="badge">Dedicated service</span>
        <h1>{h1}</h1>
        <p>{intro[0]}</p>
      </div>
    </section>
    <section class="section"><div class="container seo-prose">{paras}</div></section>
    <section class="section"><div class="container"><h2>What's included</h2><div class="cards">{cards}</div></div></section>
    {steps}
    <section class="section"><div class="container"><h2>Related services</h2><div class="related-links">{related_html}</div></div></section>
    {faq_html(faqs)}
    {cta(depth, "Get a free estimate", "Tell us about the rooms, surfaces, or repairs you want completed.")}
  </main>
{footer(depth)}
"""
    write(ROOT / filename, html)


def location_page(data: dict) -> None:
    filename = data["file"]
    city = data["city"]
    st = data["st"]
    zipc = data["zip"]
    depth = 1
    r = rel(depth)
    path = f"locations/{filename}"
    title = data["title"]
    description = data["description"]
    h1 = data["h1"]
    track(path, title, "monthly", "0.7")
    crumb_items = [
        ("Home", f"{SITE}/"),
        ("Service Areas", f"{SITE}/locations/index.html"),
        (f"{city}, {st}", f"{SITE}/{path}"),
    ]
    faqs = data["faqs"]
    schema = [
        breadcrumb_ld(crumb_items),
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": f"Home improvement services in {city}, {st}",
            "provider": {"@id": f"{SITE}/#business"},
            "areaServed": {"@type": "City", "name": city, "addressRegion": st, "postalCode": zipc},
            "url": f"{SITE}/{path}",
            "description": description,
        },
        faq_ld(faqs),
    ]
    extra = "\n".join(f'<script type="application/ld+json">\n{json_ld(s)}\n</script>' for s in schema)
    nearby = "".join(f'<a href="{href}">{label}</a>' for href, label in data["nearby"])
    services = "".join(f'<a href="{href}">{label}</a>' for href, label in data["services"])
    paras = "".join(f"<p>{p}</p>" for p in data["body"])
    html = f"""{head(title=title, description=description, canonical=path, depth=depth, extra=extra)}
<body class="page-services">
{header(depth, "areas")}
  <main id="main-content">
    <section class="page-banner">
      <div class="container">
        {crumbs([("Home", f"{r}index.html"), ("Service Areas", f"{r}index.html"), (f"{city}, {st}", "")])}
        <span class="badge">{city}, {st} {zipc}</span>
        <h1>{h1}</h1>
        <p>{data["lede"]}</p>
      </div>
    </section>
    <section class="section"><div class="container seo-prose">{paras}</div></section>
    <section class="section">
      <div class="container">
        <h2>Services available in {city}</h2>
        <div class="related-links">{services}</div>
      </div>
    </section>
    <section class="section section-alt">
      <div class="container">
        <h2>Nearby communities</h2>
        <p>Homeowners in {city} often also ask about work in neighboring towns.</p>
        <div class="related-links">{nearby}</div>
      </div>
    </section>
    {faq_html(faqs)}
    {cta(depth, f"Contact Elite Craft Honor for a {city} project", "Share the address, photos if you have them, and the work you want quoted.")}
  </main>
{footer(depth)}
"""
    write(ROOT / "locations" / filename, html)


def build_core() -> None:
    extra = f'<script type="application/ld+json">\n{json_ld(org_ld())}\n</script>'
    track("index.html", "Home", "weekly", "1.0")
    r = ""
    faqs = [
        ("Do you provide free estimates?", "Yes. Contact Elite Craft Honor by phone or the estimate form and we will review the project details with you."),
        ("What areas of Rhode Island do you serve?", "We serve Rhode Island communities including Central Falls, Pawtucket, Providence, Cranston, Lincoln, Cumberland, Johnston, North Providence, Smithfield, Woonsocket, Warwick, East Providence, Bristol, and Coventry."),
        ("Do you work in Massachusetts?", "Yes. Nearby Massachusetts towns include Attleboro, North Attleborough, Seekonk, and Foxborough."),
        ("Do you provide interior and exterior painting?", "Yes. We handle residential painting including wall painting, trim painting, preparation, primer, and finish coats."),
        ("Do you offer small handyman repairs?", "Yes. Handyman work covers everyday residential repairs and punch-list items alongside larger painting or carpentry jobs."),
    ]
    extra += f'\n<script type="application/ld+json">\n{json_ld(faq_ld(faqs))}\n</script>'
    extra += f'\n<script type="application/ld+json">\n{json_ld(breadcrumb_ld([("Home", f"{SITE}/")]))}\n</script>'
    areas = "".join(
        f'<a href="locations/{f}"><strong>{n}</strong><span>{st} {z}</span></a>'
        for f, n, st, z in CITIES_RI + CITIES_MA
    )
    html = f"""{head(
        title="Painting, Carpentry & Handyman Contractor Rhode Island | Elite Craft Honor LLC",
        description="Professional painting, carpentry, handyman and remodeling services throughout Rhode Island. Interior and exterior painting, trim, drywall, cabinets and residential repairs. Request an estimate from Elite Craft Honor LLC.",
        canonical="",
        depth=0,
        extra=extra,
    )}
<body class="page-home">
{header(0, "home")}
  <main id="main-content">
    <section class="hero">
      <div class="container hero-grid">
        <div>
          <div class="hero-logo">
            <img src="images/logotipo_principal.png" alt="Elite Craft Honor LLC primary logo" width="598" height="647" />
          </div>
          <span class="badge">Elite Craft Honor LLC</span>
          <h1>Painting, Carpentry & Handyman Services in Rhode Island</h1>
          <p>Registered and insured residential contractor for interior painting, exterior painting, finish carpentry, drywall, cabinets, and everyday home repairs. Free estimates with clear communication from start to finish.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="contact.html#estimate-form">Get a Free Estimate</a>
            <a class="btn btn-ghost" href="services.html">View Services</a>
          </div>
          <div class="hero-stats">
            <div class="stat"><strong>RI + MA</strong><span>Primary service area</span></div>
            <div class="stat"><strong>Registered</strong><span>Professional contractor</span></div>
            <div class="stat"><strong>Insured</strong><span>Protected job execution</span></div>
          </div>
        </div>
        <aside class="showcase">
          <div class="showcase-grid">
            <article class="tile"><h3>Interior & Exterior Painting</h3><p>Prep, primer, and finish coats for walls, ceilings, trim, and siding.</p></article>
            <article class="tile"><h3>Carpentry</h3><p>Finish carpentry, trim, doors, and practical wood repairs.</p></article>
            <article class="tile"><h3>Handyman Repairs</h3><p>Residential repairs and small projects completed to a professional standard.</p></article>
            <article class="tile"><h3>Remodeling Support</h3><p>Drywall, cabinets, and coordinated home improvement work.</p></article>
          </div>
        </aside>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <h2>Home improvement services</h2>
        <p class="lead">Painting contractors, carpenters, and handyman crews are often booked separately. We keep prep, finish work, and repairs on one coordinated plan so Rhode Island homeowners are not managing three schedules.</p>
        <div class="cards">
          <article class="card is-reveal"><h3>Painting services in Rhode Island</h3><p>Residential painting for interiors and exteriors, including wall painting, trim painting, and house painting after proper preparation.</p><a class="service-link" href="services/painting.html">Painting services in Rhode Island</a></article>
          <article class="card is-reveal"><h3>Carpentry and trim</h3><p>Finish carpentry, baseboards, door installation, and millwork details that sit cleanly with paint-ready surfaces.</p><a class="service-link" href="services/carpentry.html">Carpentry services in Rhode Island</a></article>
          <article class="card is-reveal"><h3>Handyman services</h3><p>General residential repairs, punch lists, and small upgrades for occupied homes.</p><a class="service-link" href="services/handyman.html">Handyman services in Rhode Island</a></article>
          <article class="card is-reveal"><h3>Remodeling</h3><p>Kitchen and bathroom refresh support, drywall, cabinets, and related home improvement work.</p><a class="service-link" href="services/remodeling.html">Remodeling services in Rhode Island</a></article>
          <article class="card is-reveal"><h3>Drywall repair</h3><p>Patching, installation, and paint-ready finishing before interior painting.</p><a class="service-link" href="services/drywall.html">Drywall repair in Rhode Island</a></article>
          <article class="card is-reveal"><h3>Cabinets, doors & windows</h3><p>Cabinet installation, trim carpentry, and window or door installation when the opening and finish work need to line up.</p><a class="service-link" href="services/cabinet-installation.html">Cabinet installation in Rhode Island</a></article>
        </div>
      </div>
    </section>
    <section class="section section-alt">
      <div class="container">
        <h2>Why homeowners hire Elite Craft Honor</h2>
        <div class="trust-grid">
          <article class="trust-item is-reveal"><h3>Registered contractor</h3><p>A professional Rhode Island business operating with registration and accountability.</p></article>
          <article class="trust-item is-reveal"><h3>Fully insured</h3><p>Work completed with insurance coverage to protect your property and the project.</p></article>
          <article class="trust-item is-reveal"><h3>Craftsmanship first</h3><p>Prep, protection, and finish details receive the same attention as the visible last coat.</p></article>
          <article class="trust-item is-reveal"><h3>Clear estimates</h3><p>You know the scope before work begins. License or registration numbers: [PLACEHOLDER: RI contractor registration number].</p></article>
          <article class="trust-item is-reveal"><h3>Fast communication</h3><p>Phone and email responses for scheduling, material questions, and next steps.</p></article>
          <article class="trust-item is-reveal"><h3>Real project photos</h3><p>See completed exterior painting examples in the gallery. Additional interior photos: [PLACEHOLDER: add interior project photos].</p></article>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <h2>Areas we serve</h2>
        <p class="lead">Rhode Island is the core market. Nearby Massachusetts towns are served when the project and schedule fit.</p>
        <div class="areas-grid">{areas}</div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <h2>Project gallery</h2>
        <p class="lead">Exterior painting photos from completed residential work.</p>
        <div class="gallery-teaser is-reveal">
          <div>
            <small>Painting portfolio</small>
            <h3>Browse completed house painting</h3>
            <p>Open the gallery for exterior finishes, trim painting, and siding work.</p>
          </div>
          <a class="btn btn-primary" href="projects.html">Open gallery</a>
        </div>
      </div>
    </section>
    {faq_html(faqs)}
    {cta(0, "Ready to start your project with confidence?", "Call or email today for a free estimate and scheduling details.")}
  </main>
{footer(0)}
"""
    write(ROOT / "index.html", html)

    track("about.html", "About", "yearly", "0.6")
    about_faqs = [
        ("Is Elite Craft Honor registered and insured?", "Yes. The site and company materials describe Elite Craft Honor LLC as a registered and insured contractor. Ask for current certificates when you request an estimate."),
        ("Do you invent reviews or awards on this site?", "No. We only publish information we can stand behind. Customer reviews belong on Google Business Profile when clients choose to leave them."),
    ]
    extra_a = "\n".join(
        [
            f'<script type="application/ld+json">\n{json_ld(org_ld())}\n</script>',
            f'<script type="application/ld+json">\n{json_ld(faq_ld(about_faqs))}\n</script>',
            f'<script type="application/ld+json">\n{json_ld(breadcrumb_ld([("Home", f"{SITE}/"), ("About", f"{SITE}/about.html")]))}\n</script>',
        ]
    )
    about = f"""{head(
        title="About Elite Craft Honor LLC | Rhode Island Painting & Carpentry Contractor",
        description="Learn how Elite Craft Honor LLC approaches painting, carpentry, handyman work, and home improvement across Rhode Island: registered, insured, and focused on clean craftsmanship.",
        canonical="about.html",
        depth=0,
        extra=extra_a,
    )}
<body class="page-about">
{header(0, "about")}
  <main id="main-content">
    <section class="page-banner">
      <div class="container">
        {crumbs([("Home", "index.html"), ("About", "")])}
        <span class="badge">Who we are</span>
        <h1>About Elite Craft Honor LLC</h1>
        <p>A Rhode Island painting, carpentry, and handyman contractor built around preparation, honest scopes, and finishes that hold up in New England weather.</p>
      </div>
    </section>
    <section class="section">
      <div class="container seo-prose">
        <p>Elite Craft Honor LLC is a registered and insured contractor serving homeowners in Rhode Island and nearby Massachusetts. The company name is the standard: craft in the work, honor in how the job is quoted and completed.</p>
        <p>We do not list years in business, awards, or license numbers here unless they are confirmed. If you need documentation for a lender, landlord, or insurance file, request it with your estimate. [PLACEHOLDER: year founded] [PLACEHOLDER: owner bio]</p>
        <p>Day-to-day work is residential: interior painting, exterior painting, finish carpentry, drywall repair, cabinet installation, and general repairs that often appear on the same punch list.</p>
      </div>
    </section>
    <section class="section">
      <div class="container cards">
        <article class="card is-reveal"><h2>Mission</h2><p>Improve homes with precise finishing and carpentry that lasts longer than a cosmetic cover-up.</p></article>
        <article class="card is-reveal"><h2>Standards</h2><p>Protect floors and furnishings, repair substrates, and inspect edges before calling a room complete.</p></article>
        <article class="card is-reveal"><h2>Process</h2><p>Estimate, schedule, execute, walkthrough. You know who is coming and what will happen that day.</p></article>
      </div>
    </section>
    {faq_html(about_faqs)}
    {cta(0, "Talk with Elite Craft Honor", "Call for a project estimate or send photos of the rooms you want finished.")}
  </main>
{footer(0)}
"""
    write(ROOT / "about.html", about)

    track("services.html", "Services", "monthly", "0.9")
    svc_extra = f'<script type="application/ld+json">\n{json_ld(breadcrumb_ld([("Home", f"{SITE}/"), ("Services", f"{SITE}/services.html")]))}\n</script>'
    services = f"""{head(
        title="Painting, Carpentry, Handyman & Remodeling Services | Elite Craft Honor",
        description="Browse Elite Craft Honor services: interior and exterior painting, carpentry, trim, drywall, cabinets, handyman repairs, and remodeling support across Rhode Island.",
        canonical="services.html",
        depth=0,
        extra=svc_extra,
    )}
<body class="page-services">
{header(0, "services")}
  <main id="main-content">
    <section class="page-banner">
      <div class="container">
        {crumbs([("Home", "index.html"), ("Services", "")])}
        <span class="badge">What we do</span>
        <h1>Painting, carpentry, and home improvement services</h1>
        <p>Choose a service page for scope details, process, and related work. Every estimate is based on the actual rooms and surfaces on site.</p>
      </div>
    </section>
    <section class="section">
      <div class="container service-list">
        <article class="service-item is-reveal"><h2>Painting</h2><p>Interior painting, exterior painting, and residential house painting with prep and finish coats.</p><a class="service-link" href="services/painting.html">Painting services in Rhode Island</a></article>
        <article class="service-item is-reveal"><h2>Interior painting</h2><p>Walls, ceilings, and trim painting for occupied homes.</p><a class="service-link" href="interior-painting.html">Interior painting in Rhode Island</a></article>
        <article class="service-item is-reveal"><h2>Exterior painting</h2><p>Siding, trim, and weather-facing finishes.</p><a class="service-link" href="exterior-painting.html">Exterior painting in Rhode Island</a></article>
        <article class="service-item is-reveal"><h2>Carpentry</h2><p>Finish carpentry, repairs, and wood details.</p><a class="service-link" href="services/carpentry.html">Carpentry services in Rhode Island</a></article>
        <article class="service-item is-reveal"><h2>Trim carpentry</h2><p>Baseboards, casings, and interior trim installation.</p><a class="service-link" href="services/trim-carpentry.html">Trim carpentry in Rhode Island</a></article>
        <article class="service-item is-reveal"><h2>Cabinet installation</h2><p>Kitchen, bath, and storage cabinet setting and alignment.</p><a class="service-link" href="services/cabinet-installation.html">Cabinet installation in Rhode Island</a></article>
        <article class="service-item is-reveal"><h2>Windows & doors</h2><p>Window and door installation with trim finishing.</p><a class="service-link" href="services/window-door-installation.html">Window and door installation</a></article>
        <article class="service-item is-reveal"><h2>Drywall</h2><p>Drywall installation and drywall repair before paint.</p><a class="service-link" href="services/drywall.html">Drywall repair in Rhode Island</a></article>
        <article class="service-item is-reveal"><h2>Handyman</h2><p>General residential repairs and small projects.</p><a class="service-link" href="services/handyman.html">Handyman services in Rhode Island</a></article>
        <article class="service-item is-reveal"><h2>Remodeling</h2><p>Kitchen and bathroom remodeling support and coordinated upgrades.</p><a class="service-link" href="services/remodeling.html">Remodeling in Rhode Island</a></article>
        <article class="service-item is-reveal"><h2>Demolition & cleanup</h2><p>Selective tear-out before remodel or painting.</p><a class="service-link" href="demolition-cleanup.html">Demolition and cleanup</a></article>
        <article class="service-item is-reveal"><h2>Flooring & tile</h2><p>Floor and tile installation with clean transitions.</p><a class="service-link" href="flooring-tile.html">Flooring and tile</a></article>
        <article class="service-item is-reveal"><h2>Millwork</h2><p>Architectural millwork and interior wood details.</p><a class="service-link" href="millwork.html">Millwork</a></article>
        <article class="service-item is-reveal"><h2>Baseboards</h2><p>Baseboard installation after flooring or remodel work.</p><a class="service-link" href="baseboard.html">Baseboard installation</a></article>
      </div>
    </section>
    {cta(0, "Need one trade or a combined scope?", "Request an estimate and we will tell you what should be sequenced first.")}
  </main>
{footer(0)}
"""
    write(ROOT / "services.html", services)

    track("projects.html", "Gallery", "monthly", "0.6")
    gal_extra = f'<script type="application/ld+json">\n{json_ld(breadcrumb_ld([("Home", f"{SITE}/"), ("Gallery", f"{SITE}/projects.html")]))}\n</script>'
    gallery = f"""{head(
        title="Painting Project Gallery | Elite Craft Honor LLC",
        description="Photos of completed residential exterior painting by Elite Craft Honor LLC, including siding, trim, and entry finishes in Rhode Island.",
        canonical="projects.html",
        depth=0,
        extra=gal_extra,
    )}
<body class="page-projects">
{header(0, "gallery")}
  <main id="main-content">
    <section class="page-banner">
      <div class="container">
        {crumbs([("Home", "index.html"), ("Gallery", "")])}
        <span class="badge">Project gallery</span>
        <h1>Residential painting project photos</h1>
        <p>These photos show completed exterior painting. Interior, carpentry, and remodel photos can be added as new projects are documented.</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <article class="gallery-column is-reveal">
          <div class="gallery-column-head">
            <small>Exterior painting</small>
            <h2>House painting examples</h2>
            <p>Siding, trim painting, and entry details from residential work.</p>
          </div>
          <div class="photo-grid photo-grid-zigzag">
            <figure class="photo-card"><img src="ECH2/01-casa-pintada.jpg" alt="Blue house exterior painting with white trim in Rhode Island" width="1536" height="2048" loading="lazy" /></figure>
            <figure class="photo-card"><img src="ECH2/02-casa-pintada-lado.jpg" alt="Side elevation of freshly painted blue siding" width="2048" height="1536" loading="lazy" /></figure>
            <figure class="photo-card"><img src="ECH2/03-casa-azul-pintada.jpg" alt="Dark blue colonial house with white door trim after painting" width="235" height="292" loading="lazy" /></figure>
            <figure class="photo-card"><img src="ECH2/04-entrada-puerta-azul.jpg" alt="Front entry with blue door and white porch trim painting" width="660" height="989" loading="lazy" /></figure>
            <figure class="photo-card"><img src="ECH2/06-residencia-costera.jpg" alt="Coastal residence exterior paint and trim work" width="736" height="1097" loading="lazy" /></figure>
            <figure class="photo-card"><img src="ECH2/07-fachada-costera.jpg" alt="Coastal home facade painting with white trim" width="768" height="511" loading="lazy" /></figure>
          </div>
        </article>
      </div>
    </section>
    {cta(0, "Want similar painting results on your home?", "Request a painting estimate and share a few photos of the elevations.")}
  </main>
{footer(0)}
"""
    write(ROOT / "projects.html", gallery)

    track("contact.html", "Contact", "yearly", "0.8")
    contact_faqs = [
        ("How fast do you respond?", "Typical response time is within 24 hours on business days."),
        ("What should I include in an estimate request?", "City or town, service needed, rooms or elevations involved, and any photos of the current condition."),
    ]
    extra_c = "\n".join(
        [
            f'<script type="application/ld+json">\n{json_ld(faq_ld(contact_faqs))}\n</script>',
            f'<script type="application/ld+json">\n{json_ld(breadcrumb_ld([("Home", f"{SITE}/"), ("Contact", f"{SITE}/contact.html")]))}\n</script>',
        ]
    )
    contact = f"""{head(
        title="Contact Elite Craft Honor LLC | Free Estimate in Rhode Island",
        description="Request a free estimate from Elite Craft Honor LLC. Call (401) 616-0779 or email gmonsalve@elitecrafthonor.com for painting, carpentry, and handyman work in Rhode Island.",
        canonical="contact.html",
        depth=0,
        extra=extra_c,
    )}
<body class="page-contact">
{header(0, "contact")}
  <main id="main-content">
    <section class="page-banner">
      <div class="container">
        {crumbs([("Home", "index.html"), ("Contact", "")])}
        <span class="badge">Get in touch</span>
        <h1>Contact Elite Craft Honor</h1>
        <p>Tell us about the painting, carpentry, drywall, cabinet, or repair work you need. Typical response time: within 24 hours.</p>
      </div>
    </section>
    <section class="section">
      <div class="container contact-grid">
        <article class="contact-card is-reveal">
          <h2>Contact information</h2>
          <ul class="contact-list">
            <li><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li><strong>Phone</strong><a href="tel:{PHONE}">{PHONE_DISPLAY}</a></li>
            <li><strong>Service area</strong>Rhode Island and nearby Massachusetts</li>
            <li><strong>Street address</strong>[PLACEHOLDER: public business address for Google Business Profile]</li>
          </ul>
          <div class="hero-actions" style="margin-top:20px;margin-bottom:0;">
            <a class="btn btn-primary" data-track="estimate-click" href="#estimate-form">Request a Free Estimate</a>
            <a class="btn btn-ghost" href="tel:{PHONE}">Call for a project estimate</a>
          </div>
        </article>
        <article class="contact-card is-reveal">
          <h2>Request form</h2>
          <form id="estimate-form" class="estimate-form" data-estimate-form>
            <label for="full-name">Full name</label>
            <input id="full-name" name="fullName" type="text" autocomplete="name" required />
            <label for="phone">Phone number</label>
            <input id="phone" name="phone" type="tel" autocomplete="tel" required />
            <label for="email">Email</label>
            <input id="email" name="email" type="email" autocomplete="email" required />
            <label for="service">Service needed</label>
            <select id="service" name="service" required>
              <option value="">Select one</option>
              <option>Interior painting</option>
              <option>Exterior painting</option>
              <option>Carpentry</option>
              <option>Trim carpentry</option>
              <option>Cabinet installation</option>
              <option>Window or door installation</option>
              <option>Drywall repair</option>
              <option>Handyman repairs</option>
              <option>Remodeling</option>
              <option>Flooring & tile</option>
              <option>Demolition & cleanup</option>
            </select>
            <label for="city">Project city/town</label>
            <input id="city" name="city" type="text" required />
            <label for="details">Project details</label>
            <textarea id="details" name="details" rows="4" required></textarea>
            <button class="btn btn-primary" type="submit">Submit free estimate request</button>
            <p class="form-note">By submitting, you agree to be contacted about your project request.</p>
            <p class="form-success" data-form-success hidden>Thanks! Your estimate request is ready to send.</p>
          </form>
        </article>
      </div>
    </section>
    {faq_html(contact_faqs)}
  </main>
{footer(0)}
"""
    write(ROOT / "contact.html", contact)


def build_services() -> None:
    service_page(
        "painting.html",
        "Painting Contractor in Rhode Island | Elite Craft Honor LLC",
        "Residential painting in Rhode Island: interior painting, exterior painting, prep, primer, and finish coats. Request an estimate from Elite Craft Honor LLC.",
        "Professional painting contractor in Rhode Island",
        [
            "House painters are judged on what happens before the first coat. Elite Craft Honor treats surface preparation, protection, primer, and finish coats as one system so walls, trim, and siding look even after they dry.",
            "Interior painting covers living rooms, bedrooms, kitchens, ceilings, and trim painting. Exterior painting covers siding, fascia, and weather-facing trim. We quote residential painting based on access, substrate condition, and color changes rather than a one-size-fits-all gallon count.",
            "If drywall repairs, caulk joints, or rotted trim show up during walkthrough, we will say so before paint goes on. Related pages cover interior painting, exterior painting, and drywall repair in more detail.",
        ],
        [
            ("Prep and protection", "Masking, furniture protection, washing or sanding where needed, and patching before primer."),
            ("Coatings", "Primer where the substrate requires it, then finish coats for coverage and durability."),
            ("Trim and details", "Cut-ins, doors, window casing, and baseboards so wall color and millwork stay crisp."),
        ],
        [
            ("Walkthrough", "Review rooms or elevations, existing coatings, and color goals."),
            ("Prep", "Repairs, sanding, and primer as required."),
            ("Paint", "Even application on walls, ceilings, or siding."),
            ("Detail", "Edges, hardware, and touch-ups."),
            ("Handoff", "Walkthrough of finished surfaces."),
        ],
        [
            ("../interior-painting.html", "Interior painting"),
            ("../exterior-painting.html", "Exterior painting"),
            ("drywall.html", "Drywall repair"),
            ("trim-carpentry.html", "Trim carpentry"),
            ("../locations/index.html", "Rhode Island service areas"),
        ],
        [
            ("Do you provide interior and exterior painting?", "Yes. Both are quoted separately because weather, access, and prep differ."),
            ("Do you paint trim and walls together?", "Often yes. Trim painting can be scheduled with wall painting so colors and sheens are planned together."),
            ("Do you work throughout Rhode Island?", "Yes. See the service areas page for cities and nearby Massachusetts towns."),
        ],
        "House Painting",
        "painting contractor Rhode Island",
    )
    service_page(
        "carpentry.html",
        "Carpentry Contractor in Rhode Island | Elite Craft Honor LLC",
        "Finish carpentry and carpenter services in Rhode Island: trim, doors, repairs, and wood details from Elite Craft Honor LLC.",
        "Carpentry contractor serving Rhode Island homes",
        [
            "A carpenter on a Rhode Island home is usually solving fit, not just adding decoration. Floors settle, plaster waves, and door openings are rarely square. Elite Craft Honor focuses on finish carpentry that still looks intentional after paint.",
            "Typical work includes trim installation, door installation, window casing, built-in repairs, and small framing adjustments that make the next paint or remodel phase cleaner.",
            "When millwork, baseboards, or cabinets are the main request, those dedicated pages go deeper. This page is the hub for carpentry scope and sequencing.",
        ],
        [
            ("Finish carpentry", "Casings, baseboards, and interior wood details with tight joints."),
            ("Doors and hardware", "Hanging, adjusting, and trimming doors so they close cleanly."),
            ("Repairs", "Damaged trim, soft spots, and wood details that should be fixed before painting."),
        ],
        [
            ("Measure", "Openings, runs, and existing profiles."),
            ("Material plan", "Match or upgrade profiles to the house."),
            ("Cut and fit", "Copes, miters, and scribes for out-of-square rooms."),
            ("Install", "Fasten, shim, and align."),
            ("Paint-ready", "Fill, caulk, and coordinate with painting if requested."),
        ],
        [
            ("trim-carpentry.html", "Trim carpentry"),
            ("window-door-installation.html", "Window and door installation"),
            ("../millwork.html", "Millwork"),
            ("painting.html", "Painting services in Rhode Island"),
        ],
        [
            ("Do you install trim and baseboards?", "Yes. Trim carpentry and baseboard installation are core finish-carpentry services."),
            ("Can carpentry and painting be combined?", "Yes. Many interiors need carpentry repairs before primer and finish coats."),
        ],
        "Finish Carpentry",
        "carpentry contractor Rhode Island",
    )
    service_page(
        "handyman.html",
        "Handyman Services in Rhode Island | Elite Craft Honor LLC",
        "Handyman services in Rhode Island for residential repairs, punch lists, and small home improvement jobs. Request an estimate from Elite Craft Honor LLC.",
        "Handyman services for Rhode Island homes",
        [
            "Searches for a handyman near me usually mean a list, not a single trade. Elite Craft Honor takes residential punch lists seriously: mounting, adjustments, minor repairs, and the leftover items after a move or a paint job.",
            "We are a contractor, not a marketplace of random helpers. If a task belongs with a licensed plumber or electrician, we will say so instead of forcing it into a handyman visit.",
            "Handyman work often sits next to painting, carpentry, and drywall repair. Combining those visits can reduce disruption in occupied homes.",
        ],
        [
            ("Repairs", "Everyday residential repairs that do not require a separate specialty crew."),
            ("Adjustments", "Doors, hardware, trim that opened up, and fixtures that loosened."),
            ("Punch lists", "Items left after painting, a tenant turnover, or a small remodel."),
        ],
        [
            ("List review", "Prioritize tasks and flag specialty trades."),
            ("Quote", "Time and materials or a defined punch-list price."),
            ("Schedule", "One visit or a short series."),
            ("Complete", "Work through the list with cleanup."),
            ("Confirm", "Walk the items with you."),
        ],
        [
            ("painting.html", "Painting"),
            ("carpentry.html", "Carpentry"),
            ("drywall.html", "Drywall"),
            ("remodeling.html", "Remodeling"),
        ],
        [
            ("Do you offer small handyman repairs?", "Yes. Small repairs and punch-list work are part of our residential services."),
            ("Do you serve people searching for a handyman near me?", "If you are in our Rhode Island or nearby Massachusetts service towns, yes. Start with your city on the estimate form."),
        ],
        "Handyman",
        "handyman Rhode Island",
    )
    service_page(
        "remodeling.html",
        "Remodeling Contractor in Rhode Island | Elite Craft Honor LLC",
        "Home improvement and remodeling support in Rhode Island: kitchens, baths, drywall, paint, and finish carpentry coordinated by Elite Craft Honor LLC.",
        "Remodeling and home improvement in Rhode Island",
        [
            "Remodeling in older Rhode Island housing stock is rarely a blank box. Triple-deckers, capes, and colonials hide out-of-level floors and plaster that does not love demolition. Elite Craft Honor supports kitchen remodeling, bathroom remodeling, and general home improvement by keeping demolition, drywall, carpentry, and paint in a sensible order.",
            "We do not claim to be a design-build firm or to hold licenses we have not listed. Large structural, plumbing, or electrical scopes should include the right licensed trades. Our value is finish quality and coordination of the surfaces homeowners actually live with.",
            "If your project is mostly paint and trim, start with those service pages. If walls are coming out or cabinets are moving, this remodeling page is the better starting point.",
        ],
        [
            ("Sequence", "Demo, drywall, carpentry, then paint so coats are not wasted."),
            ("Kitchens and baths", "Cabinet setting, trim, paint, and related finish work alongside other trades."),
            ("Whole-room refreshes", "When a room needs more than a single-color repaint."),
        ],
        [
            ("Scope", "What stays, what goes, and which trades are required."),
            ("Prep / demo", "Selective demolition and cleanup when included."),
            ("Rebuild surfaces", "Drywall, carpentry, and cabinets."),
            ("Finish", "Paint, trim, and punch list."),
            ("Walkthrough", "Confirm remaining items."),
        ],
        [
            ("drywall.html", "Drywall"),
            ("cabinet-installation.html", "Cabinet installation"),
            ("painting.html", "Painting"),
            ("../demolition-cleanup.html", "Demolition and cleanup"),
        ],
        [
            ("Do you remodel kitchens and bathrooms?", "We support kitchen and bathroom remodeling with finish work, cabinets, drywall, and paint. Specialty trades may be required for plumbing or electrical."),
            ("Is this the same as a handyman visit?", "No. Remodeling is a planned sequence. Handyman visits cover smaller, contained tasks."),
        ],
        "Home Remodeling",
        "remodeling contractor Rhode Island",
    )
    service_page(
        "drywall.html",
        "Drywall Repair in Rhode Island | Elite Craft Honor LLC",
        "Drywall installation and drywall repair in Rhode Island, finished paint-ready before interior painting. Request an estimate from Elite Craft Honor LLC.",
        "Drywall installation and repair in Rhode Island",
        [
            "Paint will not hide a bad patch. Elite Craft Honor repairs and installs drywall so interior painting has a flat, consistent substrate. That includes holes from fixtures, water stains that have been diagnosed, and new board after a small remodel.",
            "Rhode Island homes mix plaster, drywall, and previous patches. Matching texture and sheen matters more than speed. We will tell you when a wall should be skimmed versus spot-patched.",
            "Drywall work is usually scheduled immediately before primer. Linking this page with interior painting keeps that sequence obvious for homeowners.",
        ],
        [
            ("Repair", "Holes, cracks, and failed tape where the rest of the wall is sound."),
            ("Installation", "New board on framed walls or ceilings when a room is opened up."),
            ("Finish", "Mud, sand, and paint-ready surfaces."),
        ],
        [
            ("Inspect", "Cause of damage and whether moisture is still active."),
            ("Cut or hang", "Remove failed material or hang new board."),
            ("Finish", "Tape, mud, and sand."),
            ("Prime", "Spot prime or full prime before color."),
            ("Paint", "Interior painting when included in the same project."),
        ],
        [
            ("painting.html", "Interior painting"),
            ("remodeling.html", "Remodeling"),
            ("handyman.html", "Handyman repairs"),
        ],
        [
            ("Do you provide drywall repair?", "Yes. Drywall repair and installation are available as standalone work or with painting."),
            ("Can you paint the same week?", "Often, once compound is dry. Timing depends on humidity and the number of coats of mud."),
        ],
        "Drywall",
        "drywall repair Rhode Island",
    )
    service_page(
        "cabinet-installation.html",
        "Cabinet Installation in Rhode Island | Elite Craft Honor LLC",
        "Cabinet installation for kitchens, baths, and storage in Rhode Island. Level, align, and finish with Elite Craft Honor LLC.",
        "Cabinet installation for Rhode Island kitchens and baths",
        [
            "Cabinet installation is layout, shimming, and fastening—not just setting boxes on a wall. Elite Craft Honor installs kitchen, bathroom, and storage cabinets so doors, drawers, and filler pieces line up on floors that are rarely level.",
            "This page replaces the thinner cabinetry overview. If you already have boxes on site, we can quote hanging, scribing, and hardware. Custom fabrication beyond installation should be discussed during the estimate so expectations stay accurate.",
            "Cabinet jobs often continue into backsplash timing, trim, and paint. We will not paint boxes that still need hardware adjustments.",
        ],
        [
            ("Set and fasten", "Level runs, secure to structure, and use fillers where walls turn."),
            ("Doors and drawers", "Adjust overlay and reveal so gaps stay even."),
            ("Trim integration", "Scribe moldings and adjacent finish carpentry."),
        ],
        [
            ("Measure", "Walls, appliances, and existing utilities."),
            ("Layout", "Find the high point of the floor and plan shims."),
            ("Install boxes", "Start from a true line."),
            ("Doors and hardware", "Adjust after the boxes are locked in."),
            ("Final check", "Operation, fasteners, and adjacent trim."),
        ],
        [
            ("carpentry.html", "Carpentry"),
            ("remodeling.html", "Kitchen remodeling"),
            ("trim-carpentry.html", "Trim carpentry"),
        ],
        [
            ("Do you install cabinets?", "Yes. Cabinet installation is a listed service for kitchens, baths, and storage walls."),
            ("Do you build custom cabinets from scratch?", "Ask during the estimate. Installation of supplied cabinets is the core offering described here."),
        ],
        "Cabinet Installation",
        "cabinet installation Rhode Island",
    )
    service_page(
        "trim-carpentry.html",
        "Trim Carpentry in Rhode Island | Elite Craft Honor LLC",
        "Trim carpentry in Rhode Island including baseboards, casings, and interior trim installation by Elite Craft Honor LLC.",
        "Trim carpentry and interior millwork details",
        [
            "Trim carpentry is how a painted room reads as finished. Elite Craft Honor installs baseboards, door casings, window trim, and related interior profiles with joints that still look tight after seasonal humidity swings.",
            "Many Rhode Island interiors mix colonial casings with later replacements. We can match existing profiles or install a consistent new package after flooring or drywall.",
            "Paint-ready trim is part of the job. If you also need wall painting, sequence the work so caulk and primer happen once.",
        ],
        [
            ("Baseboards", "Runs, corners, and returns after flooring."),
            ("Casings", "Doors and windows with even reveals."),
            ("Specialty trim", "Chair rail, transitions, and small millwork details."),
        ],
        [
            ("Profile choice", "Match existing or specify new."),
            ("Measure", "Openings and wall lengths."),
            ("Cut", "Miters and copes."),
            ("Install", "Nail, glue, and align."),
            ("Fill and caulk", "Ready for paint."),
        ],
        [
            ("../baseboard.html", "Baseboard installation"),
            ("../trim.html", "Trim work"),
            ("../millwork.html", "Millwork"),
            ("carpentry.html", "Carpentry contractor services"),
        ],
        [
            ("Do you install trim and baseboards?", "Yes. Baseboards and trim installation are central to this service."),
            ("Should trim be painted off the wall?", "Sometimes. We will recommend the method that fits the profile and site conditions."),
        ],
        "Trim Carpentry",
        "trim carpentry Rhode Island",
    )
    service_page(
        "window-door-installation.html",
        "Window & Door Installation in Rhode Island | Elite Craft Honor LLC",
        "Window installation and door installation in Rhode Island with trim finishing by Elite Craft Honor LLC.",
        "Window and door installation with finish trim",
        [
            "A new door or window is only as good as the opening, the flashing conversation, and the interior trim that follows. Elite Craft Honor installs and replaces interior doors regularly and handles window and exterior door work when the opening, product, and weather details are clear at estimate time.",
            "Rhode Island weather punishes sloppy exterior installations. If a unit needs a specialty installer or manufacturer-certified crew, we will not pretend otherwise.",
            "After units are set, trim carpentry and painting bring the room back together. Those pages explain the finish side in more depth.",
        ],
        [
            ("Doors", "Interior slab or prehung doors, hardware, and swing clearance."),
            ("Windows", "Replacement or new units when the opening and product are specified."),
            ("Trim", "Interior casing and paint-ready details."),
        ],
        [
            ("Verify opening", "Square, plumb, and existing damage."),
            ("Unit check", "Size, handing, and manufacturer instructions."),
            ("Install", "Shim, fasten, and foam or seal as specified."),
            ("Interior finish", "Casings and adjustments."),
            ("Exterior notes", "Flag flashing or siding work that must be correct for warranty."),
        ],
        [
            ("../doors-trim-small-projects.html", "Doors, trim, and small projects"),
            ("trim-carpentry.html", "Trim carpentry"),
            ("carpentry.html", "Carpentry"),
        ],
        [
            ("Do you install doors?", "Yes. Door installation and adjustments are common requests."),
            ("Do you install windows?", "Window installation is quoted when the unit and opening are defined. Some products require specific installers."),
        ],
        "Window and Door Installation",
        "door installation Rhode Island",
    )


def build_support() -> None:
    support_page(
        "interior-painting.html",
        "Interior Painting in Rhode Island | Elite Craft Honor LLC",
        "Interior painting in Rhode Island for walls, ceilings, and trim. Prep, primer, and finish coats by Elite Craft Honor LLC.",
        "Interior painting for Rhode Island homes",
        [
            "Interior painting is where occupied homes feel the disruption most. Elite Craft Honor plans room order, drying time, and protection so families can still live in the house.",
            "Wall painting, ceiling work, and trim painting each need a different sheen and prep. Kitchens and baths may need coatings that handle moisture better than a living-room eggshell.",
            "If the walls are cracked or patched poorly, see drywall repair before choosing colors.",
        ],
        [
            ("Rooms and ceilings", "Even coverage without flashing on raking light."),
            ("Trim painting", "Doors, casings, and baseboards with clean cut-ins."),
            ("Protection", "Floors, furniture, and HVAC registers masked or covered."),
        ],
        [
            ("Consultation", "Rooms, lighting, and sheen."),
            ("Prep", "Patch, sand, prime."),
            ("Paint", "Finish coats."),
            ("Detail", "Edges and hardware."),
            ("Handover", "Walkthrough."),
        ],
        [
            ("services/painting.html", "All painting services"),
            ("exterior-painting.html", "Exterior painting"),
            ("services/drywall.html", "Drywall repair"),
        ],
        [
            ("Do you provide interior painting?", "Yes. Interior painting is a core service."),
            ("Do you move furniture?", "Light shifting is common. Large pieces should be discussed before the start date."),
        ],
        "Interior Painting",
    )
    support_page(
        "exterior-painting.html",
        "Exterior Painting in Rhode Island | Elite Craft Honor LLC",
        "Exterior painting in Rhode Island for siding, trim, and house exteriors. Weather-aware prep and coatings from Elite Craft Honor LLC.",
        "Exterior painting for New England weather",
        [
            "Exterior painting in Rhode Island has to respect salt air in some neighborhoods, freeze-thaw cycles, and wood that stays wet on north elevations. Elite Craft Honor schedules house painting around weather, not just the calendar.",
            "Prep may include washing, scraping failed film, and priming bare wood. Skipping that step is how peeling starts by the following spring.",
            "Gallery photos show completed exterior work. Color changes on large elevations are quoted with coverage in mind.",
        ],
        [
            ("Siding", "Even film on wood, fiber cement, or previously coated surfaces as assessed on site."),
            ("Trim and entries", "Fascia, casings, and doors that take the most sun and rain."),
            ("Access", "Ladders or staging discussed during the estimate."),
        ],
        [
            ("Inspect", "Failed coatings and soft wood."),
            ("Prep", "Wash, scrape, prime."),
            ("Coat", "Finish coats in suitable weather."),
            ("Detail", "Edges and metal flashings nearby."),
            ("Review", "Walk elevations with you."),
        ],
        [
            ("services/painting.html", "Painting contractor services"),
            ("interior-painting.html", "Interior painting"),
            ("projects.html", "Painting gallery"),
        ],
        [
            ("Do you provide exterior painting?", "Yes. Exterior painting is quoted from the actual elevations."),
            ("When is the season?", "Mild, dry weather is best. We will not paint over damp or freezing surfaces."),
        ],
        "Exterior Painting",
    )
    support_page(
        "millwork.html",
        "Millwork in Rhode Island | Elite Craft Honor LLC",
        "Architectural millwork and interior wood details in Rhode Island from Elite Craft Honor LLC.",
        "Millwork for finished interiors",
        [
            "Millwork is the custom layer on top of standard trim: paneling, decorative assemblies, and wood components that have to fit a specific wall.",
            "Elite Craft Honor installs and fits millwork as part of finish carpentry. Highly ornamental shop-built packages should be reviewed during the estimate so lead times are honest.",
        ],
        [
            ("Fit", "Scribe to plaster and floors that move."),
            ("Alignment", "Consistent reveals across a run."),
            ("Finish", "Paint-ready or stain-ready as specified."),
        ],
        [
            ("Review", "Drawings or photos of the desired detail."),
            ("Measure", "The actual wall, not the plan."),
            ("Prep pieces", "Cut and dry-fit."),
            ("Install", "Fasten and align."),
            ("Finish prep", "Fill and caulk."),
        ],
        [
            ("services/carpentry.html", "Carpentry"),
            ("services/trim-carpentry.html", "Trim carpentry"),
        ],
        [("Is millwork the same as trim?", "Trim is the everyday casing and base. Millwork is more custom or architectural.")],
        "Millwork",
    )
    support_page(
        "baseboard.html",
        "Baseboard Installation in Rhode Island | Elite Craft Honor LLC",
        "Baseboard installation in Rhode Island after flooring or remodel work, completed by Elite Craft Honor LLC.",
        "Baseboard installation",
        [
            "Baseboards close the gap after new floors and hide the expansion space. Elite Craft Honor cuts, copes, and fastens baseboard so outside corners and door returns stay consistent.",
            "This page is the task-level view. The trim carpentry service page covers full casing packages.",
        ],
        [
            ("Layout", "Plan joints away from high-visibility stretches when possible."),
            ("Fastening", "Secure to plates, not only drywall."),
            ("Paint-ready", "Fill nail holes and caulk to the wall."),
        ],
        [
            ("Assess", "Floor height and wall condition."),
            ("Measure", "Runs and corners."),
            ("Cut", "Inside and outside corners."),
            ("Install", "Align the top line."),
            ("Finish", "Fill and caulk."),
        ],
        [("services/trim-carpentry.html", "Trim carpentry"), ("trim.html", "Trim work")],
        [("Do you install baseboards after flooring?", "Yes. That is a common sequence.")],
        "Baseboard Installation",
    )
    support_page(
        "trim.html",
        "Interior Trim Work in Rhode Island | Elite Craft Honor LLC",
        "Interior trim work in Rhode Island for doors, windows, and accent profiles by Elite Craft Honor LLC.",
        "Interior trim work",
        [
            "Trim work covers casings, accent profiles, and the small pieces that make openings look deliberate. Elite Craft Honor treats it as finish carpentry, not decoration glued over bad walls.",
        ],
        [
            ("Door and window casings", "Even margins around the jamb."),
            ("Accent trim", "Where the design calls for extra profile."),
            ("Transitions", "Where different materials meet."),
        ],
        [
            ("Design review", "Profile and paint or stain."),
            ("Measurements", "Each opening."),
            ("Cut and prep", "Dry-fit corners."),
            ("Install", "Align and fasten."),
            ("Final detail", "Fill joints."),
        ],
        [("services/trim-carpentry.html", "Trim carpentry hub"), ("baseboard.html", "Baseboards")],
        [("Can trim be installed before paint?", "Yes. Many rooms are trimmed, then primed and painted as a set.")],
        "Trim Work",
    )
    support_page(
        "flooring-tile.html",
        "Flooring & Tile in Rhode Island | Elite Craft Honor LLC",
        "Flooring and tile installation in Rhode Island for kitchens, baths, and living areas by Elite Craft Honor LLC.",
        "Flooring and tile installation",
        [
            "Flooring and tile set the height that every baseboard and appliance has to follow. Elite Craft Honor plans layout, transitions, and grout or finish details so the next carpentry phase is not fighting the floor.",
            "Subfloor condition decides the quote. We will not hide movement under tile.",
        ],
        [
            ("Layout", "Center lines and cuts at walls."),
            ("Installation", "Level, consistent joints."),
            ("Transitions", "Clean meetings with existing floors."),
        ],
        None,
        [("services/remodeling.html", "Remodeling"), ("baseboard.html", "Baseboards after flooring")],
        [("Do you remove old flooring?", "Ask in the estimate. Some jobs include demolition; others assume a ready subfloor.")],
        "Flooring & Tile",
    )
    support_page(
        "demolition-cleanup.html",
        "Demolition & Cleanup in Rhode Island | Elite Craft Honor LLC",
        "Selective demolition and cleanup in Rhode Island to prepare homes for painting or remodeling with Elite Craft Honor LLC.",
        "Demolition and cleanup",
        [
            "Selective demolition is controlled removal, not wrecking. Elite Craft Honor protects adjoining rooms, contains dust where practical, and leaves a site that can accept drywall or paint.",
            "Hazardous materials such as suspected asbestos are outside casual demo. Testing and abatement belong with qualified firms.",
        ],
        [
            ("Selective removal", "Cabinets, trim, or finishes that must come out."),
            ("Protection", "Floors and remaining assemblies."),
            ("Cleanup", "Debris handling and broom-clean handoff."),
        ],
        None,
        [("services/remodeling.html", "Remodeling"), ("services/drywall.html", "Drywall after demo")],
        [("Do you haul debris?", "Debris handling is part of many demolition quotes. Confirm dumpster or haul-off during the estimate.")],
        "Demolition & Cleanup",
    )
    support_page(
        "doors-trim-small-projects.html",
        "Doors, Trim & Small Projects | Elite Craft Honor LLC",
        "Door installs, trim upgrades, and small interior projects in Rhode Island by Elite Craft Honor LLC.",
        "Doors, trim, and small interior projects",
        [
            "This page is for homeowners who have a short list: a door that sticks, missing casing, or a handful of finish items. Larger window packages belong on the window and door installation service page.",
        ],
        [
            ("Doors", "Installs and adjustments."),
            ("Trim", "Small runs and repairs."),
            ("Small projects", "Interior upgrades that do not need a full remodel schedule."),
        ],
        None,
        [
            ("services/window-door-installation.html", "Window and door installation"),
            ("services/handyman.html", "Handyman services"),
        ],
        [("Is this different from handyman work?", "It overlaps. This page emphasizes doors and trim; handyman covers a wider punch list.")],
        "Doors, Trim & Small Projects",
    )


def build_locations() -> None:
    track("locations/index.html", "Service Areas", "monthly", "0.85")
    r = "../"
    cards = "".join(
        f'<a href="{f}"><strong>{n}, {st}</strong><span>{z}</span></a>' for f, n, st, z in CITIES_RI + CITIES_MA
    )
    extra = f'<script type="application/ld+json">\n{json_ld(breadcrumb_ld([("Home", f"{SITE}/"), ("Service Areas", f"{SITE}/locations/index.html")]))}\n</script>'
    html = f"""{head(
        title="Areas We Serve in Rhode Island & Nearby Massachusetts | Elite Craft Honor",
        description="Elite Craft Honor LLC serves Rhode Island cities including Providence, Pawtucket, Cranston, and Central Falls, plus nearby Massachusetts towns such as Attleboro and Seekonk.",
        canonical="locations/index.html",
        depth=1,
        extra=extra,
    )}
<body class="page-services">
{header(1, "areas")}
  <main id="main-content">
    <section class="page-banner">
      <div class="container">
        {crumbs([("Home", f"{r}index.html"), ("Service Areas", "")])}
        <span class="badge">Local coverage</span>
        <h1>Areas we serve</h1>
        <p>Rhode Island is the primary market. Nearby Massachusetts towns are included when the project and travel schedule fit.</p>
      </div>
    </section>
    <section class="section">
      <div class="container seo-prose">
        <p>Local search terms like painter near me or carpenter near me only help if the business actually shows up in those towns. This directory lists the communities Elite Craft Honor serves, with a dedicated page for each so the housing types and nearby cities stay specific.</p>
        <p>ZIP codes appear only where they help identify the place, such as Central Falls, RI 02863. We do not publish long ZIP lists for search engines.</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <h2>Rhode Island and nearby Massachusetts</h2>
        <div class="areas-grid">{cards}</div>
      </div>
    </section>
    {cta(1, "Not sure if we cover your street?", "Include your city on the estimate form. If the location is outside this list, we will say so.")}
  </main>
{footer(1)}
"""
    write(ROOT / "locations/index.html", html)

    svc = [
        ("../services/painting.html", "Painting services in Rhode Island"),
        ("../services/carpentry.html", "Carpentry"),
        ("../services/handyman.html", "Handyman"),
        ("../services/remodeling.html", "Remodeling"),
        ("../contact.html#estimate-form", "Request an estimate"),
    ]

    locations = [
        {
            "file": "providence-ri.html",
            "city": "Providence",
            "st": "RI",
            "zip": "02903",
            "title": "Painting & Handyman Contractor Providence RI | Elite Craft Honor",
            "description": "Painting, carpentry, and handyman services in Providence, RI. Interior and exterior painting, trim, drywall, and residential repairs from Elite Craft Honor LLC.",
            "h1": "Painting, carpentry & handyman services in Providence, RI",
            "lede": "From East Side colonials to West End triple-deckers, Providence homes need prep that respects old plaster, tight streets, and occupied apartments.",
            "body": [
                "Providence is Rhode Island’s capital and a mix of historic one-families, student rentals, condos downtown, and triple-deckers that share walls and stair halls. Painting and carpentry here is often about access: parking, porch protection, and colors that have to be approved in a condo document.",
                "East Side interiors still show plaster waves. A flat drywall patch in raking light from a tall window will telegraph. We plan interior painting and drywall repair with that in mind instead of promising a glass-smooth wall that the substrate cannot support.",
                "Exterior painting on older clapboard needs honest scraping. Federal Hill, Elmwood, and the West End see a lot of sun on street-facing elevations and moisture on shaded sides. House painting quotes should mention both.",
                "Typical Providence projects include apartment turnovers, trim carpentry after a kitchen refresh, and handyman lists in occupied two-families. Nearby work often continues into Cranston, East Providence, and Pawtucket.",
            ],
            "nearby": [("east-providence-ri.html", "East Providence"), ("cranston-ri.html", "Cranston"), ("pawtucket-ri.html", "Pawtucket"), ("north-providence-ri.html", "North Providence")],
            "services": svc,
            "faqs": [
                ("Do you work in Providence condos?", "Yes, when building rules allow. Share any contractor insurance or certificate requests with the estimate."),
                ("Can you paint a triple-decker?", "Exterior and interior work on multi-families is quoted from access, occupancy, and the number of elevations or units involved."),
            ],
        },
        {
            "file": "pawtucket-ri.html",
            "city": "Pawtucket",
            "st": "RI",
            "zip": "02860",
            "title": "Painters & Carpenters in Pawtucket RI | Elite Craft Honor",
            "description": "Residential painting, carpentry, and handyman work in Pawtucket, RI, including mill-era homes and multi-families. Free estimates from Elite Craft Honor LLC.",
            "h1": "Painting and carpentry in Pawtucket, RI",
            "lede": "Pawtucket’s mill-city housing—dense lots, older wood, and the Massachusetts line—shapes how painting and repairs get scheduled.",
            "body": [
                "Pawtucket grew around mills and still lives in that pattern: triple-deckers, modest colonials, and infill near the Blackstone. Interior painting often means working around radiators, small rooms, and floors that are not level.",
                "Quality Hill and Oak Hill have different trim profiles than a later ranch off Newport Avenue. Finish carpentry should match the house you have, not a catalog photo.",
                "Because Pawtucket sits on the MA border, many households also have family in Attleboro or Seekonk. We can quote those nearby towns on the same trip when the schedule allows.",
                "Common requests include exterior painting on weathered clapboard, drywall repair after a leak that has already been fixed, and handyman punch lists for rental turnovers.",
            ],
            "nearby": [("central-falls-ri.html", "Central Falls"), ("providence-ri.html", "Providence"), ("attleboro-ma.html", "Attleboro"), ("east-providence-ri.html", "East Providence")],
            "services": svc,
            "faqs": [
                ("Do you work near downtown Pawtucket?", "Yes. Include street parking notes if the crew will need space for ladders."),
                ("Can you help with a rental turnover?", "Painting, small repairs, and punch lists are a common combination for turnovers."),
            ],
        },
        {
            "file": "cranston-ri.html",
            "city": "Cranston",
            "st": "RI",
            "zip": "02910",
            "title": "Painting Contractor Cranston RI | Elite Craft Honor LLC",
            "description": "Interior and exterior painting, trim, and handyman services in Cranston, RI. Elite Craft Honor LLC serves Garden City, Edgewood, and west Cranston homes.",
            "h1": "Painting, trim, and home repairs in Cranston, RI",
            "lede": "Cranston stretches from Edgewood’s older streets to west Cranston ranches—two housing patterns that need different paint and carpentry approaches.",
            "body": [
                "Cranston is one of Rhode Island’s larger cities, and the housing stock shows it. Edgewood and Auburn have tighter lots and older wood. Garden City and western neighborhoods add capes, ranches, and later additions.",
                "Exterior painting on a ranch with wide eaves is a different quote than a two-story colonial with more linear feet of trim. We measure elevations instead of guessing from a neighborhood average.",
                "Interior projects often follow kitchen or bath updates: cabinet installation, drywall patches, then interior painting. Cranston homeowners also ask for baseboard replacement after new floors.",
                "Warwick, Providence, and Johnston sit on Cranston’s edges, so multi-property families sometimes book two addresses in one conversation.",
            ],
            "nearby": [("warwick-ri.html", "Warwick"), ("providence-ri.html", "Providence"), ("johnston-ri.html", "Johnston"), ("east-providence-ri.html", "East Providence")],
            "services": svc,
            "faqs": [
                ("Do you work in Garden City?", "Yes. Cranston neighborhoods including Garden City are in the service area."),
                ("Are ranches faster to paint outside?", "Sometimes, if access is easy. Roof pitch, plantings, and color changes still affect time."),
            ],
        },
        {
            "file": "central-falls-ri.html",
            "city": "Central Falls",
            "st": "RI",
            "zip": "02863",
            "title": "Handyman & Painting in Central Falls RI 02863 | Elite Craft Honor",
            "description": "Painting, carpentry, and handyman services in Central Falls, RI 02863. Dense mill housing and multi-families served by Elite Craft Honor LLC.",
            "h1": "Home improvement services in Central Falls, RI",
            "lede": "Central Falls is Rhode Island’s smallest city. ZIP 02863 covers a compact grid of mill housing where access and neighbor walls matter.",
            "body": [
                "Central Falls packs a lot of living into a small footprint. Multi-families sit close together, so exterior painting needs extra care with overspray, walkways, and shared porches.",
                "Interior painting and drywall repair here are often unit-by-unit. Stair halls and compact kitchens show every cut-in. Trim carpentry has to deal with out-of-square mill construction.",
                "Pawtucket surrounds much of the city, and Lincoln and Cumberland are a short drive. We treat Central Falls as its own page because the housing density is not the same as a suburban lot in those towns.",
                "Handyman lists—door adjustments, patching, and punch items after a tenant leaves—are common. We still quote painting separately when a full repaint is the real need.",
            ],
            "nearby": [("pawtucket-ri.html", "Pawtucket"), ("lincoln-ri.html", "Lincoln"), ("cumberland-ri.html", "Cumberland"), ("providence-ri.html", "Providence")],
            "services": svc,
            "faqs": [
                ("Why mention ZIP 02863?", "Central Falls is small enough that the ZIP helps people confirm the city. We do not list every ZIP in Rhode Island."),
                ("Do you work in occupied multi-families?", "Yes, with a clear unit-by-unit plan so residents know which rooms are in progress."),
            ],
        },
        {
            "file": "lincoln-ri.html",
            "city": "Lincoln",
            "st": "RI",
            "zip": "02865",
            "title": "Carpenter & Painter in Lincoln RI | Elite Craft Honor",
            "description": "Finish carpentry, painting, and handyman services in Lincoln, RI, including Lonsdale, Albion, and Manville. Elite Craft Honor LLC.",
            "h1": "Painting and finish carpentry in Lincoln, RI",
            "lede": "Lincoln mixes mill villages along the Blackstone with later suburban streets—two scales of house in one town.",
            "body": [
                "Lonsdale, Albion, and Manville still show mill-village proportions: closer neighbors, older wood, and trim that has been painted many times. Lime Rock and other later streets add larger lots and different siding.",
                "Finish carpentry in a mill house often means scribing to plaster. In a later colonial it may mean matching factory casings after a window replacement.",
                "Exterior painting quotes should mention tree cover. Shaded elevations stay wet longer in this part of northern Rhode Island.",
                "Cumberland, Smithfield, Central Falls, and North Providence are the usual nearby towns when a family has more than one property.",
            ],
            "nearby": [("cumberland-ri.html", "Cumberland"), ("smithfield-ri.html", "Smithfield"), ("central-falls-ri.html", "Central Falls"), ("north-providence-ri.html", "North Providence")],
            "services": svc,
            "faqs": [
                ("Do you work in Manville and Albion?", "Yes. Those Lincoln villages are part of the service area."),
                ("Can you match old mill-house trim?", "We can often match or come close. Bring a photo or a short offcut to the estimate if you have one."),
            ],
        },
        {
            "file": "cumberland-ri.html",
            "city": "Cumberland",
            "st": "RI",
            "zip": "02864",
            "title": "Home Improvement Contractor Cumberland RI | Elite Craft Honor",
            "description": "Painting, carpentry, drywall, and handyman services in Cumberland, RI. Elite Craft Honor LLC serves Valley Falls, Ashton, and Berkeley.",
            "h1": "Residential painting and repairs in Cumberland, RI",
            "lede": "Cumberland’s villages—Valley Falls, Ashton, Berkeley—sit between mill-city density and suburban lots.",
            "body": [
                "Valley Falls feels closer to Central Falls and Pawtucket. Ashton and Berkeley open into larger yards and split-level or colonial plans. Painting contractors who quote a flat “Cumberland price” miss that difference.",
                "Many homes here have additions. Interior painting across an addition joint needs primer strategy so sheen does not flash. Drywall repair is common where old and new walls meet.",
                "Cabinet installation and kitchen remodeling support show up in later houses with builder-grade boxes that are due for replacement.",
                "Lincoln, Woonsocket, and Attleboro are typical neighboring requests.",
            ],
            "nearby": [("lincoln-ri.html", "Lincoln"), ("woonsocket-ri.html", "Woonsocket"), ("attleboro-ma.html", "Attleboro"), ("central-falls-ri.html", "Central Falls")],
            "services": svc,
            "faqs": [
                ("Do you serve Valley Falls?", "Yes. Valley Falls is part of Cumberland coverage."),
                ("Are larger lots easier for exterior painting?", "Access is often easier. Height, peeling, and color change still drive the quote."),
            ],
        },
        {
            "file": "johnston-ri.html",
            "city": "Johnston",
            "st": "RI",
            "zip": "02919",
            "title": "Painting & Handyman Johnston RI | Elite Craft Honor LLC",
            "description": "Interior painting, exterior painting, and handyman repairs in Johnston, RI. Elite Craft Honor LLC.",
            "h1": "Painting and handyman services in Johnston, RI",
            "lede": "Johnston sits west of Providence with commercial corridors and residential side streets that still need careful residential painting.",
            "body": [
                "Hartford Avenue is the commercial spine, but most of our Johnston work is houses: capes, raised ranches, and colonials on side streets. Exterior painting here often includes decks or trim that took sun without enough overhang.",
                "Interior projects may follow a basement finishing conversation or a kitchen refresh. We stay in finish and repair trades unless a specialty license is required.",
                "Cranston, North Providence, and Smithfield border Johnston, so estimates sometimes cover two towns in one email.",
            ],
            "nearby": [("cranston-ri.html", "Cranston"), ("north-providence-ri.html", "North Providence"), ("smithfield-ri.html", "Smithfield"), ("providence-ri.html", "Providence")],
            "services": svc,
            "faqs": [
                ("Do you work west of I-295?", "Yes, Johnston addresses on both sides of the highway are in area when the project fits."),
            ],
        },
        {
            "file": "north-providence-ri.html",
            "city": "North Providence",
            "st": "RI",
            "zip": "02911",
            "title": "Painter Near Me North Providence RI | Elite Craft Honor",
            "description": "Residential painting, carpentry, and handyman services in North Providence, RI. Compact lots and capes served by Elite Craft Honor LLC.",
            "h1": "Painting and carpentry in North Providence, RI",
            "lede": "North Providence is compact. Capes and colonials sit on smaller lots, so protection of driveways and neighboring siding is part of every exterior quote.",
            "body": [
                "North Providence homeowners often search painter near me because the town is dense and jobs are local. We still want the city name on the estimate so routing is clear.",
                "Interior painting in smaller capes means working room-by-room. Closets, hallways, and low ceilings need cut-in discipline more than large open plans do.",
                "Finish carpentry requests include replacing short runs of baseboard after vinyl plank and adjusting doors that dropped on older pins.",
                "Providence, Johnston, Lincoln, and Pawtucket are the usual neighboring cities.",
            ],
            "nearby": [("providence-ri.html", "Providence"), ("johnston-ri.html", "Johnston"), ("lincoln-ri.html", "Lincoln"), ("pawtucket-ri.html", "Pawtucket")],
            "services": svc,
            "faqs": [
                ("Is North Providence in your core area?", "Yes. It is one of the listed Rhode Island cities."),
            ],
        },
        {
            "file": "smithfield-ri.html",
            "city": "Smithfield",
            "st": "RI",
            "zip": "02917",
            "title": "Carpentry & Painting Smithfield RI | Elite Craft Honor",
            "description": "Painting, finish carpentry, and home repairs in Smithfield, RI, including Greenville and Esmond. Elite Craft Honor LLC.",
            "h1": "Home painting and carpentry in Smithfield, RI",
            "lede": "Smithfield still reads as village centers—Greenville, Esmond, Georgiaville—plus later subdivisions in the woods.",
            "body": [
                "Greenville streets can look suburban until you notice the older mill-village core. Exterior painting on shaded lots needs extra dry time. Interior work in newer colonials is more about volume of trim than plaster repair.",
                "Homeowners here often combine exterior painting with carpentry on fascia and window sills before coatings. That sequence is cheaper than painting rotted wood twice.",
                "Lincoln, Johnston, North Providence, and Woonsocket are nearby when relatives book the same crew.",
            ],
            "nearby": [("lincoln-ri.html", "Lincoln"), ("johnston-ri.html", "Johnston"), ("woonsocket-ri.html", "Woonsocket"), ("north-providence-ri.html", "North Providence")],
            "services": svc,
            "faqs": [
                ("Do you work in Greenville?", "Yes. Greenville is part of Smithfield."),
            ],
        },
        {
            "file": "woonsocket-ri.html",
            "city": "Woonsocket",
            "st": "RI",
            "zip": "02895",
            "title": "Painting Contractor Woonsocket RI | Elite Craft Honor LLC",
            "description": "Interior and exterior painting, carpentry, and handyman services in Woonsocket, RI mill-city housing. Elite Craft Honor LLC.",
            "h1": "Painting and repairs in Woonsocket, RI",
            "lede": "Woonsocket’s triple-deckers and mill neighborhoods need painting and carpentry that can handle shared porches and older wood.",
            "body": [
                "Northern Rhode Island’s mill history is visible on almost every Woonsocket block. Multi-families, steep lots, and winters that ice north stairs all show up in exterior painting estimates.",
                "Interior painting after a long-term tenant often includes more drywall repair than a suburban repaint. We would rather patch correctly than roll over bad tape.",
                "Cumberland, Smithfield, and Blackstone Valley Massachusetts towns are typical neighboring jobs.",
            ],
            "nearby": [("cumberland-ri.html", "Cumberland"), ("smithfield-ri.html", "Smithfield"), ("lincoln-ri.html", "Lincoln"), ("attleboro-ma.html", "Attleboro")],
            "services": svc,
            "faqs": [
                ("Do you paint multi-families in Woonsocket?", "Yes, quoted by unit or by building depending on occupancy and access."),
            ],
        },
        {
            "file": "warwick-ri.html",
            "city": "Warwick",
            "st": "RI",
            "zip": "02886",
            "title": "Exterior Painting Warwick RI | Elite Craft Honor LLC",
            "description": "Exterior and interior painting, carpentry, and handyman services in Warwick, RI, from Apponaug to coastal neighborhoods. Elite Craft Honor LLC.",
            "h1": "Painting and home improvement in Warwick, RI",
            "lede": "Warwick is large: airport-adjacent inland streets, Apponaug, and coastal neighborhoods that see more wind and salt.",
            "body": [
                "A Warwick exterior painting quote should mention whether the house is inland or near the bay. Coastal trim fails faster. Inland ranches may be simpler in height but wider in elevation.",
                "Interior painting in later Warwick colonials often includes a lot of millwork. Trim painting and wall painting should be specified as one plan so sheens match the architecture.",
                "Cranston, East Greenwich is not on our priority list unless requested separately, and Coventry sit on other edges. We list Coventry and Cranston as served neighbors on this site.",
            ],
            "nearby": [("cranston-ri.html", "Cranston"), ("coventry-ri.html", "Coventry"), ("east-providence-ri.html", "East Providence"), ("bristol-ri.html", "Bristol")],
            "services": svc,
            "faqs": [
                ("Do you work near T.F. Green?", "Yes. Inland Warwick addresses are routinely in area."),
                ("Do coastal homes need different paint?", "They need honest prep and coatings rated for the exposure. We discuss that on site."),
            ],
        },
        {
            "file": "east-providence-ri.html",
            "city": "East Providence",
            "st": "RI",
            "zip": "02914",
            "title": "Painters in East Providence RI | Elite Craft Honor",
            "description": "Painting, carpentry, and handyman services in East Providence, RI, including Riverside and Rumford. Elite Craft Honor LLC also serves Seekonk, MA.",
            "h1": "Painting and carpentry in East Providence, RI",
            "lede": "East Providence sits across the river from the capital, with Riverside, Rumford, and Seekonk, Massachusetts just over the line.",
            "body": [
                "Rumford and Riverside have different house ages and lot sizes. Riverside’s closer-to-the-water streets can mean more exterior maintenance. Rumford colonials often need interior trim work after window replacements.",
                "Because Seekonk is next door, many East Providence clients also ask about a Massachusetts property. We keep those as separate location pages so the content stays specific.",
                "Providence, Pawtucket, and Barrington (not a priority-list town unless you ask) sit nearby. Our published list includes Providence, Pawtucket, and Seekonk.",
            ],
            "nearby": [("providence-ri.html", "Providence"), ("seekonk-ma.html", "Seekonk"), ("pawtucket-ri.html", "Pawtucket")],
            "services": svc,
            "faqs": [
                ("Do you cross into Seekonk?", "Yes. Seekonk, MA is a listed nearby Massachusetts town."),
            ],
        },
        {
            "file": "bristol-ri.html",
            "city": "Bristol",
            "st": "RI",
            "zip": "02809",
            "title": "Historic Home Painting Bristol RI | Elite Craft Honor",
            "description": "Painting, finish carpentry, and repairs for Bristol, RI homes, including historic downtown and waterfront streets. Elite Craft Honor LLC.",
            "h1": "Painting and finish work in Bristol, RI",
            "lede": "Bristol’s historic downtown and waterfront housing ask for painting and carpentry that respect old wood and salt air.",
            "body": [
                "Bristol is not a suburb of Providence in character even though the drive is short. Independence Park, Hope Street, and the harbor area have houses that have been painted for generations. Scraping and primer matter more than speed.",
                "Interior work in historic homes can include wavy plaster and original millwork. We would rather maintain character than flatten every wall into modern drywall unless that is the stated goal.",
                "Warwick and East Providence are the usual mainland neighbors on our list. Barrington sits between; ask if you need that town specifically.",
            ],
            "nearby": [("warwick-ri.html", "Warwick"), ("east-providence-ri.html", "East Providence"), ("coventry-ri.html", "Coventry")],
            "services": svc,
            "faqs": [
                ("Do you work on historic homes?", "Yes, with prep that matches the substrate. We do not claim historic-preservation certification unless you have been given that documentation separately. [PLACEHOLDER: historic certifications if any]"),
            ],
        },
        {
            "file": "coventry-ri.html",
            "city": "Coventry",
            "st": "RI",
            "zip": "02816",
            "title": "Painting & Remodeling Coventry RI | Elite Craft Honor",
            "description": "Residential painting, carpentry, and remodeling support in Coventry, RI. Larger lots and mixed rural-suburban housing. Elite Craft Honor LLC.",
            "h1": "Painting, carpentry, and remodeling in Coventry, RI",
            "lede": "Coventry is geographically large. Drive time, well water, and wooded lots show up in scheduling even when the work itself is a standard interior paint.",
            "body": [
                "Western Coventry feels more rural; eastern sections read as suburban. Exterior painting on a house in the trees needs algae and moisture checks. Interior painting in a newer colonial is often trim-heavy.",
                "Home improvement projects here sometimes include garage interiors, older ranch kitchens, and drywall after a wood-stove or leak repair.",
                "Warwick, Cranston, and West Greenwich (ask if needed; not on the priority list) sit nearby. We list Warwick and Cranston as served neighbors.",
            ],
            "nearby": [("warwick-ri.html", "Warwick"), ("cranston-ri.html", "Cranston")],
            "services": svc,
            "faqs": [
                ("Is Coventry far for you?", "It is in the published Rhode Island service area. Remote roads may affect start times, not eligibility."),
            ],
        },
        {
            "file": "attleboro-ma.html",
            "city": "Attleboro",
            "st": "MA",
            "zip": "02703",
            "title": "Rhode Island Contractor Serving Attleboro MA | Elite Craft Honor",
            "description": "Painting, carpentry, and handyman services in Attleboro, Massachusetts, near the Rhode Island line. Elite Craft Honor LLC.",
            "h1": "Painting and handyman services in Attleboro, MA",
            "lede": "Attleboro sits on I-95 just over the Rhode Island border. Many clients already have a Pawtucket or Cumberland project with us.",
            "body": [
                "Attleboro’s housing mixes older downtown neighborhoods with later subdivisions. Painting and carpentry needs look familiar to our Rhode Island work: clapboard, vinyl over wood, and interior trim after replacements.",
                "We are a Rhode Island company serving nearby Massachusetts. Confirm any town permit questions during the estimate. [PLACEHOLDER: MA permit notes if required]",
                "North Attleborough, Seekonk, Pawtucket, and Cumberland are the usual neighboring pages.",
            ],
            "nearby": [("north-attleborough-ma.html", "North Attleborough"), ("seekonk-ma.html", "Seekonk"), ("pawtucket-ri.html", "Pawtucket"), ("cumberland-ri.html", "Cumberland")],
            "services": svc,
            "faqs": [
                ("Do you work in Massachusetts?", "Yes. Attleboro, North Attleborough, Seekonk, and Foxborough are listed."),
            ],
        },
        {
            "file": "north-attleborough-ma.html",
            "city": "North Attleborough",
            "st": "MA",
            "zip": "02760",
            "title": "Painting Services North Attleborough MA | Elite Craft Honor",
            "description": "Residential painting, trim, and handyman work in North Attleborough, MA. Elite Craft Honor LLC serves this town from our Rhode Island base.",
            "h1": "Residential painting and repairs in North Attleborough, MA",
            "lede": "North Attleborough’s later suburban streets and older town center need the same prep standards we use in Rhode Island, with Massachusetts scheduling in mind.",
            "body": [
                "Subdivisions around the commercial corridors often have builder trim that is due for caulk and paint. The town center has older wood that needs scraping before exterior coatings.",
                "Cabinet installation and interior painting after a kitchen refresh are common combined scopes.",
                "Attleboro, Foxborough, Cumberland, and Plainville (ask if needed) sit nearby. We list Attleboro, Foxborough, and Cumberland.",
            ],
            "nearby": [("attleboro-ma.html", "Attleboro"), ("foxborough-ma.html", "Foxborough"), ("cumberland-ri.html", "Cumberland")],
            "services": svc,
            "faqs": [
                ("Is North Attleborough different from Attleboro on your site?", "Yes. Each town has its own page so the nearby communities stay accurate."),
            ],
        },
        {
            "file": "seekonk-ma.html",
            "city": "Seekonk",
            "st": "MA",
            "zip": "02771",
            "title": "Painter & Handyman Seekonk MA | Elite Craft Honor LLC",
            "description": "Painting, carpentry, and handyman services in Seekonk, MA, next to East Providence, RI. Elite Craft Honor LLC.",
            "h1": "Painting and home repairs in Seekonk, MA",
            "lede": "Seekonk is the first Massachusetts town east of East Providence. Fall River Avenue traffic is real; job timing should account for it.",
            "body": [
                "Seekonk lots are often larger than East Providence’s denser streets, which can make exterior painting access easier. Interiors still include the usual New England mix of additions and original rooms.",
                "Many Seekonk homeowners also have a Rhode Island address in the family. We keep invoices and site notes per property.",
                "East Providence, Attleboro, and Providence are the closest pages on this site.",
            ],
            "nearby": [("east-providence-ri.html", "East Providence"), ("attleboro-ma.html", "Attleboro"), ("providence-ri.html", "Providence")],
            "services": svc,
            "faqs": [
                ("Do you regularly work in Seekonk?", "Yes. It is one of the four nearby Massachusetts towns listed."),
            ],
        },
        {
            "file": "foxborough-ma.html",
            "city": "Foxborough",
            "st": "MA",
            "zip": "02035",
            "title": "Home Improvement Foxborough MA | Elite Craft Honor LLC",
            "description": "Painting, carpentry, and handyman services in Foxborough, Massachusetts, as a nearby MA town served by Elite Craft Honor LLC.",
            "h1": "Painting and handyman services in Foxborough, MA",
            "lede": "Foxborough is farther north than Attleboro. We include it because it is a listed nearby Massachusetts town, and we schedule it when travel and project size make sense.",
            "body": [
                "Foxborough housing is largely suburban: colonials, capes, and later construction. Painting and carpentry scopes look like other suburban New England work—volume of trim, garage interiors, and exterior maintenance cycles.",
                "Because the drive is longer than Seekonk or Attleboro, smaller punch-list-only visits may be combined with a larger job or quoted with travel in mind. We will be direct about that on the estimate.",
                "North Attleborough and Attleboro are the usual neighboring Massachusetts pages.",
            ],
            "nearby": [("north-attleborough-ma.html", "North Attleborough"), ("attleboro-ma.html", "Attleboro")],
            "services": svc,
            "faqs": [
                ("Do you take small Foxborough jobs?", "Ask. Travel relative to job size matters more here than in Pawtucket or Providence."),
            ],
        },
    ]

    # Fix invalid nearby links
    for loc in locations:
        loc["nearby"] = [(href, label) for href, label in loc["nearby"] if href.endswith(".html")]
        location_page(loc)


def build_404() -> None:
    html = f"""{head(
        title="Page not found | Elite Craft Honor LLC",
        description="The page you requested is not on Elite Craft Honor LLC. Return home, view services, or request an estimate.",
        canonical="404.html",
        depth=0,
        robots="noindex, follow",
    )}
<body>
{header(0, "")}
  <main id="main-content">
    <section class="page-banner">
      <div class="container">
        <span class="badge">404</span>
        <h1>We cannot find that page</h1>
        <p>The link may be old. Use the paths below to keep going.</p>
      </div>
    </section>
    <section class="section">
      <div class="container related-links">
        <a href="index.html">Home</a>
        <a href="services.html">Services</a>
        <a href="locations/index.html">Service areas</a>
        <a href="contact.html">Contact</a>
        <a href="contact.html#estimate-form">Request an estimate</a>
      </div>
    </section>
  </main>
{footer(0)}
"""
    write(ROOT / "404.html", html)


def build_redirects() -> None:
    redirect_page("painting.html", "services/painting.html", "Painting")
    redirect_page("carpentry.html", "services/carpentry.html", "Carpentry")
    redirect_page("handyman.html", "services/handyman.html", "Handyman")
    redirect_page("cabinetry.html", "services/cabinet-installation.html", "Cabinetry")


def build_robots_sitemap() -> None:
    (ROOT / "robots.txt").write_text(
        """User-agent: *
Allow: /

Sitemap: https://elitecrafthonor.com/sitemap.xml
""",
        encoding="utf-8",
    )
    urls = []
    for page in PAGES:
        loc = f"{SITE}/" if page["path"] in ("", "index.html") else f"{SITE}/{page['path']}"
        if page["path"] == "index.html":
            loc = f"{SITE}/"
        urls.append(
            f"""  <url>
    <loc>{loc}</loc>
    <changefreq>{page['changefreq']}</changefreq>
    <priority>{page['priority']}</priority>
  </url>"""
        )
    xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
""" + "\n".join(urls) + "\n</urlset>\n"
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")

    (ROOT / ".htaccess").write_text(
        """ErrorDocument 404 /404.html
Redirect 301 /painting.html /services/painting.html
Redirect 301 /carpentry.html /services/carpentry.html
Redirect 301 /handyman.html /services/handyman.html
Redirect 301 /cabinetry.html /services/cabinet-installation.html
""",
        encoding="utf-8",
    )


def main() -> None:
    build_core()
    build_services()
    build_support()
    build_locations()
    build_404()
    build_redirects()
    build_robots_sitemap()
    print(f"Wrote {len(PAGES)} indexable paths plus redirects, robots, sitemap.")


if __name__ == "__main__":
    main()
