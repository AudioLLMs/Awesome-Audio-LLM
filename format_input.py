"""Regenerate README.md, docs/data.json and docs/index.html from items/*.json.

The README is now a slim landing page that points to the live interactive site
at binwang28.github.io/audio-ai-hub/ rather than dumping every entry into
markdown. The site is the canonical view for browsing, searching and filtering.

What this script does:
  1. Load every items/*.json into a list, sorted by filename (for cross-platform
     reproducibility — see CONTRIBUTING.md for why).
  2. Write a slim README.md (hero + featured + recent + counts + contributing).
  3. Write docs/data.json (full data for the frontend).
  4. Inject server-rendered HTML into docs/index.html between the
     <!-- AUTO-...-START/END --> markers (so the site is SEO-readable
     without JS).

The timeline PNG that previous versions emitted has been retired — the live
site shows entries chronologically by sort, with much better resolution.
"""

from __future__ import annotations

import html as _html
import json
import os
import re as _re
from datetime import datetime


# ---------------------------------------------------------------------------
# 1. Load items/*.json
# ---------------------------------------------------------------------------

model_cards = []
folder_path = "items"
for filename in sorted(os.listdir(folder_path)):
    if filename.endswith(".json"):
        with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
            model_cards.append(json.load(f))

# Load star counts (built by scripts/refresh_stars.py)
stars_by_abbrev: dict[str, int] = {}
if os.path.exists("docs/stars.json"):
    with open("docs/stars.json", encoding="utf-8") as f:
        stars_by_abbrev = {k: v.get("stars", 0) for k, v in json.load(f).items()}


def _parse_time(card):
    return datetime.strptime(card["Time"], "%Y-%m")


# Sorted lists (Time desc, with Abbreviation asc as tiebreak via stable sort)
by_time_desc = sorted(model_cards, key=lambda c: c.get("Abbreviation", ""))
by_time_desc.sort(key=_parse_time, reverse=True)


# Featured = top 8 by stars (entries without a known star value are excluded)
featured = [c for c in by_time_desc if stars_by_abbrev.get(c.get("Abbreviation", ""), 0) > 0]
featured.sort(key=lambda c: -stars_by_abbrev.get(c.get("Abbreviation", ""), 0))
featured = featured[:8]

# Category counts in canonical order (matches the site's chips)
cat_order = [
    "Model and Methods", "Speech Recognition", "Speech Synthesis",
    "Audio Generation", "Benchmark", "Dataset Resource", "Multimodal",
    "Survey", "Study", "Safety", "Chatbot",
]
cat_counts = {c: 0 for c in cat_order}
for card in model_cards:
    cat_counts[card.get("Category", "")] = cat_counts.get(card.get("Category", ""), 0) + 1
# Drop any unused / unexpected categories
cat_counts = {c: n for c, n in cat_counts.items() if n}

# ---------------------------------------------------------------------------
# 2. README.md — slim landing page
# ---------------------------------------------------------------------------

total = len(model_cards)
latest = max(c["Time"] for c in model_cards) if model_cards else "—"


def _first_link(card):
    """Pick the most-canonical link to expose in markdown one-liners."""
    for key in ("Paper_Link", "GitHub_Link", "HF_Link", "Demo_Link", "Other_Link"):
        v = card.get(key)
        if v:
            return v
    return ""


def _stars_badge(card):
    n = stars_by_abbrev.get(card.get("Abbreviation", ""), 0)
    if not n:
        return "—"
    if n >= 1000:
        return f"⭐ {n // 1000}k+"
    return f"⭐ {n}"


def _one_liner(card):
    abbrev = card.get("Abbreviation", "")
    desc = (card.get("Description", "") or "").strip()
    if desc:
        # Keep the description short for the landing page (~one sentence).
        first_sentence = _re.split(r"(?<=[.!?])\s+", desc)[0]
        if len(first_sentence) > 180:
            first_sentence = first_sentence[:177].rstrip() + "…"
    else:
        first_sentence = (card.get("Title", "") or "").strip()
    link = _first_link(card)
    name_md = f"[{abbrev}]({link})" if link else abbrev
    return f"{name_md} — {first_sentence}"


readme = []

# Hero
readme.append("# 🎧 audio-ai-hub")
readme.append("")
readme.append(
    "**The hub for audio AI research.** Curated papers, open models, "
    "benchmarks and datasets across audio LLMs · speech recognition · "
    "speech synthesis · music & audio generation."
)
readme.append("")
readme.append(f"`{total} entries` · `{len(cat_counts)} categories` · `latest: {latest}`")
readme.append("")
readme.append(
    "👉 **[Browse the interactive hub →](https://binwang28.github.io/audio-ai-hub/)** "
    "· [Contribute](CONTRIBUTING.md) "
    "· [Suggest a paper](https://github.com/BinWang28/audio-ai-hub/issues/new?template=add-paper.yml)"
)
readme.append("")
readme.append("> The page below is a quick snapshot. For search, filtering by category and sorting by stars or date, the **[live site](https://binwang28.github.io/audio-ai-hub/)** is much faster than scrolling this README.")
readme.append("")
readme.append("---")
readme.append("")

# Featured
readme.append("## ⭐ Featured")
readme.append("")
readme.append("_Top 8 by GitHub stars — refreshed weekly by `.github/workflows/refresh-stars.yml`._")
readme.append("")
readme.append("| # | Project | Stars | What it does |")
readme.append("|---|---------|-------|--------------|")
for i, c in enumerate(featured, 1):
    abbrev = c.get("Abbreviation", "")
    link = _first_link(c)
    name_md = f"**[{abbrev}]({link})**" if link else f"**{abbrev}**"
    desc = (c.get("Description", "") or "").strip()
    if desc:
        first = _re.split(r"(?<=[.!?])\s+", desc)[0]
        if len(first) > 140:
            first = first[:137].rstrip() + "…"
    else:
        first = (c.get("Title", "") or "")[:140]
    # Markdown-table-safe: collapse newlines and escape pipes
    first = first.replace("\n", " ").replace("|", "\\|")
    readme.append(f"| {i} | {name_md} | {_stars_badge(c)} | {first} |")
readme.append("")

# Recently added
readme.append("## 🆕 Recently added")
readme.append("")
readme.append("_The 10 most recent entries by date. See the [interactive site](https://binwang28.github.io/audio-ai-hub/) for everything else._")
readme.append("")
for c in by_time_desc[:10]:
    readme.append(f"- `{c.get('Time','')}` · {_one_liner(c)}")
readme.append("")

# Category overview (counts only, no listings)
readme.append("## 📚 What's inside")
readme.append("")
readme.append("| Category | Entries |")
readme.append("|----------|--------:|")
for cat, n in cat_counts.items():
    readme.append(f"| [{cat}](https://binwang28.github.io/audio-ai-hub/#cat={_html.escape(cat).replace(' ', '%20')}) | {n} |")
readme.append(f"| **Total** | **{total}** |")
readme.append("")
readme.append("Each row links into the live site with the corresponding category filter pre-applied.")
readme.append("")

# Contributing
readme.append("## 🤝 Contributing")
readme.append("")
readme.append(
    "Add an `items/<Abbreviation>.json` (template in [`schema.json`](schema.json)), "
    "run `python3 format_input.py` to regenerate the README and site data, "
    "and open a PR. CI validates JSON, checks README sync, and the site "
    "rebuilds automatically on merge. Full guide: **[CONTRIBUTING.md](CONTRIBUTING.md)**."
)
readme.append("")
readme.append(
    "Don't want to write a PR yourself? **[Suggest a paper](https://github.com/BinWang28/audio-ai-hub/issues/new?template=add-paper.yml)** via the issue form and a maintainer will add it."
)
readme.append("")

# Citation
readme.append("## 📑 Citation")
readme.append("")
readme.append("If this hub is useful in your work, please cite it — metadata is in [`CITATION.cff`](CITATION.cff) (GitHub's \"Cite this repository\" button on the sidebar uses it).")
readme.append("")

# Contributors + star history
readme.append("## 🙏 Contributors")
readme.append("")
readme.append(
    "Thanks to "
    "[zwenyu](https://github.com/zwenyu), "
    "[Yuan-ManX](https://github.com/Yuan-ManX), "
    "[chaoweihuang](https://github.com/chaoweihuang), "
    "[Liu-Tianchi](https://github.com/Liu-Tianchi), "
    "[Sakshi113](https://github.com/Sakshi113), "
    "[hbwu-ntu](https://github.com/hbwu-ntu), "
    "[potsawee](https://github.com/potsawee), "
    "[czwxian](https://github.com/czwxian), "
    "[marianasignal](https://github.com/marianasignal), "
    "and many others who suggested entries or opened PRs."
)
readme.append("")
readme.append(
    "[![Star History Chart](https://star-history.dera.page/svg?repos=BinWang28/audio-ai-hub&type=Date)](https://star-history.dera.page/#BinWang28/audio-ai-hub&Date)"
)
readme.append("")

with open("README.md", "w", encoding="utf-8") as f:
    f.write("\n".join(readme))
print("README.md has been generated.")


# ---------------------------------------------------------------------------
# 3. docs/data.json — full data for the frontend
# ---------------------------------------------------------------------------

os.makedirs("docs", exist_ok=True)
with open("docs/data.json", "w", encoding="utf-8") as out:
    json.dump(by_time_desc, out, ensure_ascii=False, indent=2)
print(f"docs/data.json written ({len(by_time_desc)} entries).")


# ---------------------------------------------------------------------------
# 4. Server-side render of docs/index.html (between AUTO-* marker comments)
# ---------------------------------------------------------------------------

def _h(s):
    return _html.escape(str(s) if s is not None else "", quote=True)


def _slug(s):
    return _re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")


def _card_html(card):
    abbrev = card.get("Abbreviation", "")
    cat = card.get("Category", "")
    cat_slug = _slug(cat)
    links = []
    if card.get("Paper_Link"):
        links.append(f'<a href="{_h(card["Paper_Link"])}" target="_blank" rel="noopener">Paper</a>')
    if card.get("GitHub_Link"):
        links.append(f'<a href="{_h(card["GitHub_Link"])}" target="_blank" rel="noopener">Code</a>')
    if card.get("HF_Link"):
        links.append(f'<a href="{_h(card["HF_Link"])}" target="_blank" rel="noopener">🤗 HF</a>')
    if card.get("Demo_Link"):
        links.append(f'<a href="{_h(card["Demo_Link"])}" target="_blank" rel="noopener">Demo</a>')
    if card.get("Other_Link"):
        links.append(f'<a href="{_h(card["Other_Link"])}" target="_blank" rel="noopener">Site</a>')
    tags = [f'<span class="tag tag-cat" data-cat="{cat_slug}">{_h(cat)}</span>']
    if card.get("Type") and card["Type"] != cat:
        tags.append(f'<span class="tag">{_h(card["Type"])}</span>')
    if card.get("Audio_Input") == "Yes":
        tags.append('<span class="tag">Audio In</span>')
    if card.get("Audio_Output") == "Yes":
        tags.append('<span class="tag">Audio Out</span>')
    if card.get("Language") and card["Language"] not in ("-", ""):
        tags.append(f'<span class="tag">{_h(card["Language"])}</span>')
    stars = stars_by_abbrev.get(abbrev, 0)
    star_badge = f'<span class="card-stars" title="GitHub stars">★ {stars:,}</span>' if stars else ""
    affil = card.get("Affiliation", "")
    desc = card.get("Description", "")
    return (
        f'<article class="card" data-abbrev="{_h(abbrev)}" data-cat="{cat_slug}" data-stars="{stars}">'
        f'<header class="card-head"><span class="card-abbrev">{_h(abbrev)}</span>'
        f'<span class="card-time">{_h(card.get("Time", ""))}</span></header>'
        f'<p class="card-title">{_h(card.get("Title", ""))}</p>'
        + (f'<p class="card-affil">{_h(affil)}</p>' if affil else "")
        + f'<div class="tags">{"".join(tags)}{star_badge}</div>'
        + (f'<p class="card-desc">{_h(desc)}</p>' if desc else "")
        + f'<footer class="card-links">{"".join(links)}</footer>'
        "</article>"
    )


featured_html = "\n".join(_card_html(c) for c in featured)
grid_html = "\n".join(_card_html(c) for c in by_time_desc)
stats_html = (
    f'<div class="stat"><strong>{total}</strong>entries</div>'
    f'<div class="stat"><strong>{len(cat_counts)}</strong>categories</div>'
    f'<div class="stat"><strong>{latest}</strong>latest</div>'
)
chips_html = "".join(
    f'<button class="chip" type="button" data-category="{_h(c)}" data-cat="{_slug(c)}" aria-pressed="false">'
    f'{_h(c)}<span class="count">{cat_counts[c]}</span></button>'
    for c in cat_counts
)


def _inject(html_text, marker, content):
    pattern = _re.compile(
        rf"(<!-- {marker}-START -->).*?(<!-- {marker}-END -->)",
        flags=_re.DOTALL,
    )
    return pattern.sub(lambda m: m.group(1) + content + m.group(2), html_text)


with open("docs/index.html", encoding="utf-8") as f:
    page = f.read()

page = _inject(page, "AUTO-STATS", stats_html)
page = _inject(page, "AUTO-CATEGORY-FILTER", chips_html)
page = _inject(page, "AUTO-FEATURED", featured_html)
page = _inject(page, "AUTO-GRID", grid_html)

with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(page)
print(f"docs/index.html SSR'd (featured: {len(featured)}, grid: {total}).")
