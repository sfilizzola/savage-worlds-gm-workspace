#!/usr/bin/env python3
"""GFM subset to HTML for RUN.md print. Stdlib only."""

from __future__ import annotations

import html
import re

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
LIST_RE = re.compile(r"^\s*[-*]\s+(.*)$")
SEP_RE = re.compile(r"^\s*\|?(\s*:?-{3,}:?\s*\|)+\s*:?-{3,}:?\s*\|?\s*$")
ALERT_RE = re.compile(r"^\[!(IMPORTANT|TIP)\]\s*$", re.IGNORECASE)
FENCE_RE = re.compile(r"^```([A-Za-z0-9_-]*)\s*$")
SPEECH_RE = re.compile(r"[“\"][^“”\"]{2,}[”\"]")
CODE_SLOT = "\x00%d\x00"
CODE_SLOT_RE = re.compile(r"\x00(\d+)\x00")
STAT_CONT = (
    "attributes:",
    "skills:",
    "pace:",
    "hindrances:",
    "edges:",
    "gear:",
    "special abilities:",
    "personality:",
    "authority:",
)


def inline(text: str, speech: bool = False) -> str:
    s = html.escape(text, quote=False)
    spans: list[str] = []

    def stash(m: re.Match) -> str:
        spans.append(m.group(1))
        return CODE_SLOT % (len(spans) - 1)

    s = re.sub(r"`([^`]+)`", stash, s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    if speech:
        s = SPEECH_RE.sub(r'<span class="line">\g<0></span>', s)
    return CODE_SLOT_RE.sub(lambda m: f"<code>{spans[int(m.group(1))]}</code>", s)


def visible_start(text: str) -> str:
    t = text.strip()
    t = re.sub(r"^[*_`]+", "", t)
    t = re.sub(r"^[-*]\s+", "", t)
    return t.strip()


def is_sep(line: str) -> bool:
    return bool(SEP_RE.match(line))


def split_row(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def parse_blocks(text: str) -> list[tuple]:
    lines = text.replace("\r\n", "\n").split("\n")
    blocks: list[tuple] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        fence = FENCE_RE.match(line)
        if fence:
            chunk: list[str] = []
            i += 1
            while i < n and not FENCE_RE.match(lines[i]):
                chunk.append(lines[i])
                i += 1
            if i < n:
                i += 1
            blocks.append(("code", fence.group(1), chunk))
            continue
        m = HEADING_RE.match(line)
        if m:
            blocks.append(("heading", len(m.group(1)), m.group(2).strip()))
            i += 1
            continue
        if line.lstrip().startswith(">"):
            chunk: list[str] = []
            while i < n and lines[i].lstrip().startswith(">"):
                chunk.append(re.sub(r"^>\s?", "", lines[i]))
                i += 1
            blocks.append(("quote", chunk))
            continue
        if "|" in line and i + 1 < n and is_sep(lines[i + 1]):
            rows = [split_row(line)]
            i += 2
            while i < n and "|" in lines[i] and lines[i].strip():
                if is_sep(lines[i]):
                    i += 1
                    continue
                rows.append(split_row(lines[i]))
                i += 1
            blocks.append(("table", rows))
            continue
        if LIST_RE.match(line):
            items: list[str] = []
            while i < n:
                im = LIST_RE.match(lines[i])
                if not im:
                    break
                items.append(im.group(1))
                i += 1
            blocks.append(("list", items))
            continue
        para: list[str] = []
        while i < n and lines[i].strip():
            if HEADING_RE.match(lines[i]):
                break
            if LIST_RE.match(lines[i]):
                break
            if lines[i].lstrip().startswith(">"):
                break
            if FENCE_RE.match(lines[i]):
                break
            if "|" in lines[i] and i + 1 < n and is_sep(lines[i + 1]):
                break
            para.append(lines[i])
            i += 1
        if para:
            blocks.append(("para", para))
    return blocks


def looks_mood(block: tuple) -> bool:
    if block[0] == "heading":
        return "mood (table)" in block[2].lower()
    if block[0] == "para":
        return "mood (table)" in " ".join(block[1]).lower()
    return False


def list_is_mood_body(items: list[str]) -> bool:
    keys = [visible_start(x).lower() for x in items]
    return any(k.startswith("climate:") for k in keys) and any(
        k.startswith("see:") for k in keys
    )


def is_gm_item(text: str) -> bool:
    return visible_start(text).lower().startswith("gm note")


def is_speech_item(text: str) -> bool:
    return visible_start(text).lower().startswith("spoken lines")


def opens_with_quote(lines: list[str]) -> bool:
    return visible_start(" ".join(lines)).startswith(("“", '"'))


def is_stat_header(text: str) -> bool:
    low = text.lower()
    return "wild card" in low or re.search(r"\bextra\b", low) is not None


def is_stat_cont(text: str) -> bool:
    v = visible_start(text).lower()
    return any(v.startswith(p) for p in STAT_CONT)


def has_attributes(lines: list[str]) -> bool:
    return any(visible_start(ln).lower().startswith("attributes:") for ln in lines)


def alert_scope(blocks: list[tuple]) -> str:
    for block in blocks:
        if block[0] != "heading":
            continue
        heading = block[2].lower()
        if heading.startswith("at-hand statistics"):
            return "at-hand-statistics"
        if heading.startswith("at-hand rules"):
            return "at-hand-rules"
    return ""


def classify(blocks: list[tuple]) -> list[tuple]:
    out: list[tuple] = []
    i = 0
    while i < len(blocks):
        b = blocks[i]
        if b[0] == "quote" and b[1]:
            marker = ALERT_RE.match(b[1][0].strip())
            if marker:
                inner = classify(parse_blocks("\n".join(b[1][1:])))
                out.append(("alert", marker.group(1).lower(), alert_scope(inner), inner))
                i += 1
                continue
        if b[0] == "quote" and opens_with_quote(b[1]):
            out.append(("speech-quote", b[1]))
            i += 1
            continue
        if b[0] == "code" and is_stat_header(" ".join(b[2])) and has_attributes(b[2]):
            out.append(("stat-block", b[2]))
            i += 1
            continue
        if looks_mood(b):
            chunk = [b]
            j = i + 1
            if j < len(blocks) and blocks[j][0] == "list" and list_is_mood_body(blocks[j][1]):
                chunk.append(blocks[j])
                j += 1
            out.append(("mood", chunk))
            i = j
            continue
        if b[0] == "list" and any(is_gm_item(x) for x in b[1]):
            notes = [x for x in b[1] if is_gm_item(x)]
            rest = [x for x in b[1] if not is_gm_item(x)]
            if rest:
                out.append(("list", rest))
            for note in notes:
                out.append(("gm-note", note))
            i += 1
            continue
        if b[0] == "para":
            lines = list(b[1])
            if is_gm_item(" ".join(lines)):
                out.append(("gm-note", " ".join(lines)))
                i += 1
                continue
            if is_speech_item(lines[0]):
                out.append(("speech", " ".join(lines)))
                i += 1
                continue
            if lines and is_stat_header(lines[0]) and has_attributes(lines):
                out.append(("stat-block", lines))
                i += 1
                continue
            if lines and is_stat_header(" ".join(lines)):
                j = i + 1
                while j < len(blocks) and blocks[j][0] == "para":
                    nxt_lines = blocks[j][1]
                    if nxt_lines and is_stat_cont(nxt_lines[0]):
                        lines.extend(nxt_lines)
                        j += 1
                        continue
                    break
                if has_attributes(lines):
                    out.append(("stat-block", lines))
                    i = j
                    continue
        out.append(b)
        i += 1
    return out


def render_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    head, body = rows[0], rows[1:]
    th = "".join(f"<th>{inline(c)}</th>" for c in head)
    trs = [f"<tr>{th}</tr>"]
    for row in body:
        tds = "".join(f"<td>{inline(c)}</td>" for c in row)
        trs.append(f"<tr>{tds}</tr>")
    return '<table class="run-table">' + "".join(trs) + "</table>"


def render_blocks(blocks: list[tuple]) -> str:
    parts: list[str] = []
    for b in blocks:
        kind = b[0]
        if kind == "heading":
            level, text = b[1], b[2]
            cls = ' class="section-banner"' if level == 2 else ""
            parts.append(f"<h{level}{cls}>{inline(text)}</h{level}>")
        elif kind == "para":
            parts.append(f"<p>{inline(' '.join(b[1]))}</p>")
        elif kind == "list":
            items = "".join(
                f'<li class="speech">{inline(x, speech=True)}</li>'
                if is_speech_item(x)
                else f"<li>{inline(x)}</li>"
                for x in b[1]
            )
            parts.append(f"<ul>{items}</ul>")
        elif kind == "table":
            parts.append(render_table(b[1]))
        elif kind == "quote":
            parts.append(f"<blockquote><p>{inline(' '.join(b[1]))}</p></blockquote>")
        elif kind == "speech-quote":
            body = inline(" ".join(b[1]), speech=True)
            parts.append(f'<blockquote class="speech-quote"><p>{body}</p></blockquote>')
        elif kind == "speech":
            parts.append(f'<p class="speech">{inline(b[1], speech=True)}</p>')
        elif kind == "code":
            parts.append(f"<pre><code>{html.escape(chr(10).join(b[2]))}</code></pre>")
        elif kind == "alert":
            alert_type, scope, blocks = b[1], b[2], b[3]
            classes = f"callout callout-{alert_type}"
            if scope:
                classes += f" {scope}"
            parts.append(f'<aside class="{classes}">{render_blocks(blocks)}</aside>')
        elif kind == "mood":
            parts.append(f'<div class="mood">{render_blocks(b[1])}</div>')
        elif kind == "gm-note":
            parts.append(f'<p class="gm-note">{inline(b[1])}</p>')
        elif kind == "stat-block":
            inner = "".join(f"<p>{inline(line)}</p>" for line in b[1])
            parts.append(f'<div class="stat-block">{inner}</div>')
    return "\n".join(parts)


def convert(markdown: str) -> str:
    return render_blocks(classify(parse_blocks(markdown)))
