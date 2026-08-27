#!/usr/bin/env python3
"""Build the Strata reader.

Emits two artifacts from the encyclopedia corpus:
  1. docs/          — a multi-page static site (relative links; works at any base URL,
                      including GitHub Pages project sites).
  2. a single-file  — the whole encyclopedia in one HTML file with hash routing,
     reader          suitable for publishing anywhere a lone file can live.

Usage: python3 encyclopedia/tools/build_site.py [--onefile PATH]
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
OUT = REPO / "docs"

STATES = {"stub": "·", "sketch": "◔", "survey": "◑", "article": "◕", "deep": "●"}
DIVISIONS = ["logic", "metaphysics", "epistemology", "mind", "language",
             "science", "ethics", "politics", "aesthetics", "religion"]
REGISTERS = ["figures", "traditions", "meta"]
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

DIV_GLOSS = {
    "logic": "What follows from what — consequence, paradox, and the philosophy of mathematics.",
    "metaphysics": "What there is and what it is like: existence, identity, necessity, causation, time.",
    "epistemology": "Knowledge, justification, and the standing challenge of doubt.",
    "mind": "Consciousness, intentionality, and the mental's place in nature.",
    "language": "Meaning, reference, and truth.",
    "science": "Explanation, confirmation, laws, and the special sciences.",
    "ethics": "The good, the right, and how to live.",
    "politics": "Justice, authority, liberty, and the social world.",
    "aesthetics": "Beauty, art, and the strange authority of taste.",
    "religion": "God, evil, faith — and religion without theism.",
}
REG_GLOSS = {
    "figures": "Persons as subjects in themselves, each an edge into the problems.",
    "traditions": "Periods, schools, and movements treated as living wholes.",
    "meta": "Philosophy turned on itself: method, progress, disagreement.",
}

STUB_RE = re.compile(r"^- `([a-z0-9-]+)` — \*\*(.+?)\*\* — (.+?) \*\((anchor|standard|satellite)\)\*\s*$")


# ---------------------------------------------------------------- corpus ----

def parse(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
        fm[k.strip()] = v
    return fm, m.group(2).strip()


def load():
    nodes = {}
    for path in sorted(ROOT.rglob("*.md")):
        if path.name in {"METHOD.md", "INDEX.md", "NEXT.md"} or "tools" in path.parts:
            continue
        fm, body = parse(path)
        if not fm:
            continue
        nodes[fm["node"]] = {"fm": fm, "body": body, "words": len(body.split())}
    return nodes


def node_route(node, nodes):
    fm = nodes[node]["fm"]
    parent = fm.get("parent", "")
    if parent in REGISTERS:
        return f"{parent}/{node}"
    return node.replace(".", "/")


def children_of(node, nodes):
    """Ordered children: stub-lines from the body, resolved to files where they exist."""
    out = []
    fm = nodes[node]["fm"]
    for line in nodes[node]["body"].splitlines():
        m = STUB_RE.match(line.strip())
        if not m:
            continue
        slug, title, gloss, cls = m.groups()
        child = slug if node in REGISTERS else f"{node}.{slug}"
        out.append({"slug": slug, "title": title, "gloss": gloss, "cls": cls,
                    "node": child if child in nodes else None})
    return out


def backlinks(nodes):
    back = {}
    for node, v in nodes.items():
        for b in v["fm"].get("bridges", []) or []:
            tgt = resolve_token(b, nodes)
            if tgt and tgt != node:
                back.setdefault(tgt, []).append(node)
    return back


def resolve_token(tok, nodes):
    tok = tok.strip().strip("`")
    for cand in (tok, tok.replace("/", "."), tok.split("/")[-1], tok.split(".")[-1] if tok.count(".") == 0 else None):
        if cand and cand in nodes:
            return cand
    return None


# -------------------------------------------------------------- markdown ----

def inline(text, link, nodes):
    """Inline markdown on an HTML-escaped string."""
    text = html.escape(text, quote=False)
    codes = []

    def stash(m):
        tok = m.group(1)
        tgt = resolve_token(tok, nodes)
        if tgt:
            title = nodes[tgt]["fm"]["title"]
            codes.append(f'<a class="node" href="{link(tgt)}" title="{html.escape(title)}">{tok}</a>')
        else:
            codes.append(f'<span class="node unwritten" title="promised entry">{tok}</span>')
        return f"\x00{len(codes)-1}\x00"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)
    return text


def md2html(body, link, nodes, self_node=None, drop_h1=True):
    lines = body.splitlines()
    out, i, in_list, in_code = [], 0, False, False
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            if in_code:
                out.append("</code></pre>")
                in_code = False
            else:
                out.append('<pre class="fence"><code>')
                in_code = True
            i += 1
            continue
        if in_code:
            out.append(html.escape(line))
            i += 1
            continue
        if line.startswith("|") and i + 1 < len(lines) and set(lines[i + 1].replace("|", "").strip()) <= set("-: "):
            head = [c.strip() for c in line.strip("|").split("|")]
            out.append('<div class="tablewrap"><table><thead><tr>' +
                       "".join(f"<th>{inline(c, link, nodes)}</th>" for c in head) + "</tr></thead><tbody>")
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip("|").split("|")]
                out.append("<tr>" + "".join(f"<td>{inline(c, link, nodes)}</td>" for c in cells) + "</tr>")
                i += 1
            out.append("</tbody></table></div>")
            continue
        m = re.match(r"^(#{1,4}) (.*)$", line)
        if m:
            if in_list:
                out.append("</ul>")
                in_list = False
            depth = len(m.group(1))
            if depth == 1 and drop_h1:
                i += 1
                continue
            out.append(f"<h{depth}>{inline(m.group(2), link, nodes)}</h{depth}>")
            i += 1
            continue
        sm = STUB_RE.match(line.strip())
        if sm and self_node is not None:
            if not in_list:
                out.append('<ul class="children">')
                in_list = True
            slug, title, gloss, cls = sm.groups()
            child = slug if self_node in REGISTERS else f"{self_node}.{slug}"
            if child in nodes:
                st = nodes[child]["fm"]["state"]
                out.append(
                    f'<li class="child written"><span class="glyph">{STATES[st]}</span>'
                    f'<a href="{link(child)}">{html.escape(title)}</a>'
                    f'<span class="gloss"> — {inline(gloss, link, nodes)}</span>'
                    f'<span class="tag">{st} · {cls}</span></li>')
            else:
                out.append(
                    f'<li class="child promised"><span class="glyph">{STATES["stub"]}</span>'
                    f'<span class="ptitle">{html.escape(title)}</span>'
                    f'<span class="gloss"> — {inline(gloss, link, nodes)}</span>'
                    f'<span class="tag">promised · {cls}</span></li>')
            i += 1
            continue
        if line.strip().startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{inline(line.strip()[2:], link, nodes)}</li>")
            i += 1
            continue
        if in_list:
            out.append("</ul>")
            in_list = False
        if line.strip() == "":
            i += 1
            continue
        para = [line]
        while i + 1 < len(lines) and lines[i + 1].strip() != "" and not lines[i + 1].startswith(("#", "- ", "|", "```")):
            i += 1
            para.append(lines[i])
        out.append(f"<p>{inline(' '.join(para), link, nodes)}</p>")
        i += 1
    if in_list:
        out.append("</ul>")
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


# ------------------------------------------------------------------- css ----

CSS = """
:root{--parchment:#F6F0E1;--panel:#EFE7D0;--ink:#292217;--faded:#6F6350;
--line:#D9CDAF;--oxblood:#7E2B22;--gold:#8F7433;}
*{box-sizing:border-box}
body{margin:0;background:var(--parchment);color:var(--ink);
font-family:"EB Garamond",Georgia,"Times New Roman",serif;font-size:1.1rem;line-height:1.62;}
a{color:var(--oxblood);text-decoration:none}
a:hover{text-decoration:underline;text-underline-offset:3px}
.page{max-width:44rem;margin:0 auto;padding:2.2rem 1.2rem 5rem}
.rule,.masthead{border:0}
.drule{border-top:1px solid var(--ink);border-bottom:1px solid var(--ink);height:4px;margin:0 0 1.4rem}
.masthead{text-align:center;margin-bottom:2.2rem}
.masthead .eyebrow{font-variant:small-caps;letter-spacing:.32em;font-size:.86rem;color:var(--gold);margin:.4rem 0 .2rem}
.masthead .site{font-family:"Cormorant Garamond","EB Garamond",Georgia,serif;font-weight:600;
font-size:2.1rem;letter-spacing:.24em;margin:.1rem 0 .5rem;text-transform:uppercase}
.masthead .site a{color:var(--ink)}
h1{font-family:"Cormorant Garamond","EB Garamond",Georgia,serif;font-weight:600;
font-size:2.5rem;line-height:1.12;margin:.4rem 0 .8rem;text-wrap:balance}
h2{font-variant:small-caps;letter-spacing:.14em;font-weight:500;font-size:1.18rem;
border-bottom:1px solid var(--line);padding-bottom:.25rem;margin:2.4rem 0 .9rem}
h3{font-style:italic;font-weight:500;font-size:1.14rem;margin:1.8rem 0 .5rem}
p{margin:0 0 1rem}
.crumbs{font-variant:small-caps;letter-spacing:.1em;font-size:.92rem;color:var(--faded);margin-bottom:.4rem}
.crumbs a{color:var(--faded)}
.plaque{font-size:.86rem;letter-spacing:.12em;color:var(--gold);text-transform:uppercase;margin-bottom:1.6rem}
.plaque .glyph{color:var(--oxblood);letter-spacing:0}
.node{font-variant:small-caps;letter-spacing:.06em;font-size:.98em}
.node.unwritten{color:var(--faded);font-style:italic}
ul{padding-left:1.3rem;margin:0 0 1rem}
li{margin:.25rem 0}
ul.children{list-style:none;padding:0;margin:0 0 1.2rem}
.child{padding:.5rem 0;border-bottom:1px solid var(--line);margin:0}
.child .glyph{color:var(--oxblood);margin-right:.55rem}
.child a{font-weight:600}
.child .gloss{color:var(--ink)}
.child .tag{display:block;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-top:.1rem;margin-left:1.35rem}
.child.promised .ptitle{font-style:italic;color:var(--oxblood);opacity:.75;font-weight:600}
.child.promised .glyph,.child.promised .gloss{color:var(--faded)}
.epigraph{text-align:center;font-style:italic;color:var(--faded);margin:2rem auto;max-width:34rem}
.epigraph .gk{font-style:normal;font-size:1.05rem;letter-spacing:.04em}
.epigraph .attr{font-variant:small-caps;font-style:normal;letter-spacing:.14em;font-size:.85rem;margin-top:.4rem}
.dek{text-align:center;font-style:italic;font-size:1.16rem;max-width:32rem;margin:0 auto 1rem;text-wrap:balance}
.toc{list-style:none;padding:0;margin:1rem 0 2rem}
.toc li{display:grid;grid-template-columns:2.6rem 1fr;gap:.2rem .6rem;padding:.55rem 0;border-bottom:1px solid var(--line);margin:0}
.toc .num{font-family:"Cormorant Garamond",serif;font-weight:600;font-size:1.2rem;color:var(--gold);text-align:right}
.toc a{font-weight:600;font-size:1.14rem}
.toc .gloss{grid-column:2;color:var(--faded);font-size:1rem}
.toc .meta{grid-column:2;font-size:.78rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold)}
.sectionhead{text-align:center;font-variant:small-caps;letter-spacing:.3em;font-size:.95rem;color:var(--gold);margin:2.6rem 0 .4rem}
.colophon{margin-top:3rem;padding-top:1.2rem;font-size:.98rem;color:var(--faded)}
.colophon .drule{margin-bottom:1.2rem}
.backlinks{font-size:.98rem;color:var(--faded)}
.tablewrap{overflow-x:auto;margin:0 0 1rem}
table{border-collapse:collapse;font-size:.98rem;min-width:100%}
th,td{border:1px solid var(--line);padding:.4rem .6rem;text-align:left;vertical-align:top}
th{font-variant:small-caps;letter-spacing:.08em;background:var(--panel)}
pre.fence{background:var(--panel);border:1px solid var(--line);padding:.8rem 1rem;overflow-x:auto;
font-size:.85rem;line-height:1.45;font-family:ui-monospace,Menlo,Consolas,monospace}
.map ul{list-style:none;padding-left:1.1rem;border-left:1px solid var(--line);margin:0}
.map>ul{padding-left:0;border-left:0}
.map li{margin:.22rem 0}
.map .glyph{color:var(--oxblood);margin-right:.4rem}
.map .stubline{color:var(--faded);font-style:italic}
.map .cls{color:var(--gold);font-size:.8rem;letter-spacing:.08em;text-transform:uppercase;margin-left:.35rem}
.footnav{margin-top:2.6rem;padding-top:1rem;border-top:1px solid var(--line);
font-variant:small-caps;letter-spacing:.12em;font-size:.95rem;display:flex;gap:1.6rem;flex-wrap:wrap}
@media(max-width:480px){h1{font-size:2rem}.masthead .site{font-size:1.7rem;letter-spacing:.16em}}
"""

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&'
         'family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap">')


# --------------------------------------------------------------- shells -----

def masthead(home_href):
    return (f'<div class="drule"></div><header class="masthead">'
            f'<div class="eyebrow">Claude&rsquo;s Encyclop&aelig;dia of Philosophy</div>'
            f'<div class="site"><a href="{home_href}">Strata</a></div>'
            f'</header>')


def shell(title, inner, home_href, nav):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{html.escape(title)}</title>{FONTS}<style>{CSS}</style></head>'
            f'<body><div class="page">{masthead(home_href)}{inner}'
            f'<nav class="footnav">{nav}</nav></div></body></html>')


# ---------------------------------------------------------------- pages -----

def render_node(node, nodes, back, link):
    fm, body = nodes[node]["fm"], nodes[node]["body"]
    crumbs = []
    cur = fm.get("parent", "")
    chain = []
    while cur and cur not in ("root",):
        if cur in nodes:
            chain.append(cur)
            cur = nodes[cur]["fm"].get("parent", "")
        else:
            break
    for anc in reversed(chain):
        crumbs.append(f'<a href="{link(anc)}">{html.escape(nodes[anc]["fm"]["title"])}</a>')
    crumb_html = f'<div class="crumbs">{" › ".join(crumbs)}</div>' if crumbs else ""
    st, cls = fm["state"], fm["class"]
    plaque = (f'<div class="plaque"><span class="glyph">{STATES[st]}</span> '
              f'{st} &nbsp;·&nbsp; {cls} &nbsp;·&nbsp; layer {fm.get("layer", "?")} '
              f'&nbsp;·&nbsp; pass {html.escape(str(fm.get("pass", "")))}</div>')
    content = md2html(body, link, nodes, self_node=node)
    bl = ""
    if back.get(node):
        items = ", ".join(f'<a class="node" href="{link(b)}">{b}</a>' for b in sorted(back[node]))
        bl = f'<h2>Cited by</h2><p class="backlinks">{items}</p>'
    return (f'{crumb_html}<h1>{html.escape(fm["title"])}</h1>{plaque}'
            f'<article>{content}</article>{bl}')


def render_home(nodes, link, page_link, n_articles, n_stubs, n_words):
    divs = []
    for i, d in enumerate(DIVISIONS):
        n_in = sum(1 for v in nodes.values() if v["fm"]["node"].split(".")[0] == d)
        divs.append(
            f'<li><span class="num">{ROMAN[i]}</span>'
            f'<a href="{link(d)}">{html.escape(nodes[d]["fm"]["title"])}</a>'
            f'<span class="gloss">{DIV_GLOSS[d]}</span>'
            f'<span class="meta">{STATES[nodes[d]["fm"]["state"]]} {nodes[d]["fm"]["state"]} · {n_in} entries</span></li>')
    regs = []
    for r in REGISTERS:
        n_in = sum(1 for v in nodes.values() if v["fm"].get("parent") == r) + 1
        regs.append(
            f'<li><span class="num">·</span>'
            f'<a href="{link(r)}">{html.escape(nodes[r]["fm"]["title"])}</a>'
            f'<span class="gloss">{REG_GLOSS[r]}</span>'
            f'<span class="meta">{n_in} entries</span></li>')
    return f'''
<p class="dek">An encyclopedia written in layers: the depth of every entry is earned,
and every entry not yet written is declared.</p>
<div class="epigraph"><div class="gk">πάντες ἄνθρωποι τοῦ εἰδέναι ὀρέγονται φύσει</div>
<div>All human beings by nature reach out to know.</div>
<div class="attr">Aristotle · Metaphysics I.1</div></div>
<div class="sectionhead">The Divisions</div>
<ul class="toc">{"".join(divs)}</ul>
<div class="sectionhead">The Registers</div>
<ul class="toc">{"".join(regs)}</ul>
<div class="colophon"><div class="drule"></div>
<p><strong>{n_articles}</strong> entries written · <strong>{n_stubs}</strong> entries promised ·
<strong>{n_words:,}</strong> words · every invariant of the
<a href="{page_link('method')}">constitution</a> green.</p>
<p>Strata is written by Claude, an AI made by Anthropic, and by no one else. It grows in
sessions, by a fixed discipline: entries descend one layer at a time, each layer is
consolidated upward before the next is opened, and no entry is written until the field
genuinely articulates it — the <a href="{page_link('method')}">method</a> explains, and the
<a href="{page_link('queue')}">queue</a> records what is owed and wanted next. The
<a href="{page_link('map')}">full map</a> shows every entry, written and promised, at its
current depth. Its claims carry an encyclopedia&rsquo;s ambitions and a single fallible
author&rsquo;s limits; nothing here has passed human expert review.</p></div>'''


def render_map(nodes, link):
    def emit(node, depth, out):
        v = nodes[node]
        fm = v["fm"]
        out.append(f'<li><span class="glyph">{STATES[fm["state"]]}</span>'
                   f'<a href="{link(node)}">{html.escape(fm["title"])}</a>'
                   f'<span class="cls">{fm["state"]} · {fm["class"]} · {v["words"]:,}w</span>')
        kids = children_of(node, nodes)
        if kids:
            out.append("<ul>")
            for k in kids:
                if k["node"]:
                    emit(k["node"], depth + 1, out)
                else:
                    out.append(f'<li><span class="glyph">·</span>'
                               f'<span class="stubline">{html.escape(k["title"])}</span>'
                               f'<span class="cls">promised · {k["cls"]}</span></li>')
            out.append("</ul>")
        out.append("</li>")

    out = ['<h1>The Map</h1><p>Every entry at its current depth. '
           'Written entries link; <span class="map"><span class="stubline">promised entries</span></span> wait '
           'until the field earns them.</p><div class="map"><ul>']
    for d in DIVISIONS:
        emit(d, 0, out)
    out.append('</ul><div class="sectionhead">The Registers</div><ul>')
    for r in REGISTERS:
        emit(r, 0, out)
    out.append("</ul></div>")
    return "".join(out)


def render_doc(title, md_path, link, nodes):
    body = md_path.read_text(encoding="utf-8")
    return f"<h1>{html.escape(title)}</h1><article>{md2html(body, link, nodes, drop_h1=True)}</article>"


# ---------------------------------------------------------------- build -----

def build():
    nodes = load()
    back = backlinks(nodes)
    n_articles = len(nodes)
    n_words = sum(v["words"] for v in nodes.values())
    n_stubs = sum(1 for n in nodes for k in children_of(n, nodes) if not k["node"])

    routes = {}  # route -> (title, inner_html_fn taking link resolver)
    for node in nodes:
        routes[node_route(node, nodes)] = ("node", node)
    specials = {"method": ("The Constitution", ROOT / "METHOD.md"),
                "queue": ("The Queue", ROOT / "NEXT.md")}

    # ---- docs/ (multi-page, relative links) ----
    if OUT.exists():
        import shutil
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / ".nojekyll").write_text("")

    def make_link(depth):
        def link(target):
            return "../" * depth + node_route(target, nodes) + "/"
        return link

    def make_page_link(depth):
        def pl(name):
            return "../" * depth + name + "/"
        return pl

    nav_items = lambda pl: (f'<a href="{pl("")[:-1] or "."}">Home</a>'
                            f'<a href="{pl("map")}">Map</a>'
                            f'<a href="{pl("method")}">Constitution</a>'
                            f'<a href="{pl("queue")}">Queue</a>')

    for route, (_, node) in routes.items():
        depth = route.count("/") + 1
        link, pl = make_link(depth), make_page_link(depth)
        inner = render_node(node, nodes, back, link)
        d = OUT / route
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(
            shell(f'{nodes[node]["fm"]["title"]} — Strata', inner, "../" * depth, nav_items(pl)),
            encoding="utf-8")

    link0, pl0 = make_link(0), make_page_link(0)
    (OUT / "index.html").write_text(
        shell("Strata", render_home(nodes, link0, pl0, n_articles, n_stubs, n_words), ".", nav_items(pl0)),
        encoding="utf-8")
    link1, pl1 = make_link(1), make_page_link(1)
    for name, fn in (("map", lambda: render_map(nodes, link1)),
                     ("method", lambda: render_doc("The Constitution", specials["method"][1], link1, nodes)),
                     ("queue", lambda: render_doc("The Queue", specials["queue"][1], link1, nodes))):
        d = OUT / name
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(shell(f"{name.title()} — Strata", fn(), "../", nav_items(pl1)),
                                      encoding="utf-8")

    # ---- single-file reader (hash routing) ----
    onefile = None
    if "--onefile" in sys.argv:
        onefile = Path(sys.argv[sys.argv.index("--onefile") + 1])
        hlink = lambda target: "#/" + node_route(target, nodes)
        hpl = lambda name: "#/" + name
        pages = {}
        for route, (_, node) in routes.items():
            pages[route] = {"t": f'{nodes[node]["fm"]["title"]} — Strata',
                            "h": render_node(node, nodes, back, hlink)}
        pages[""] = {"t": "Strata",
                     "h": render_home(nodes, hlink, hpl, n_articles, n_stubs, n_words)}
        pages["map"] = {"t": "The Map — Strata", "h": render_map(nodes, hlink)}
        pages["method"] = {"t": "The Constitution — Strata",
                           "h": render_doc("The Constitution", specials["method"][1], hlink, nodes)}
        pages["queue"] = {"t": "The Queue — Strata",
                          "h": render_doc("The Queue", specials["queue"][1], hlink, nodes)}
        payload = json.dumps(pages, ensure_ascii=False).replace("</", "<\\/")
        nav = ('<a href="#/">Home</a><a href="#/map">Map</a>'
               '<a href="#/method">Constitution</a><a href="#/queue">Queue</a>')
        doc = f'''<title>Strata</title>{FONTS}<style>{CSS}</style>
<div class="page">{masthead("#/")}<main id="m"></main><nav class="footnav">{nav}</nav></div>
<script>
var P={payload};
function go(){{var r=location.hash.replace(/^#\\/?/,"").replace(/\\/$/,"");
var p=P[r]||P[""];document.getElementById("m").innerHTML=p.h;document.title=p.t;
window.scrollTo(0,0);}}
window.addEventListener("hashchange",go);go();
</script>'''
        onefile.write_text(doc, encoding="utf-8")

    print(f"built docs/: {len(routes)+4} pages · {n_articles} entries · {n_stubs} promised · {n_words:,} words"
          + (f" · onefile {onefile} ({onefile.stat().st_size//1024} KB)" if onefile else ""))


if __name__ == "__main__":
    build()
