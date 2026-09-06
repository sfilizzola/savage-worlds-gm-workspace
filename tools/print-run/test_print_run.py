#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import unittest
from io import StringIO
from pathlib import Path
from unittest.mock import patch

TOOL_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOL_DIR))

import mdhtml  # noqa: E402

FIXTURE = TOOL_DIR / "testdata" / "mini-run.md"


class ConvertFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.body = mdhtml.convert(FIXTURE.read_text(encoding="utf-8"))

    def test_h2_is_section_banner(self) -> None:
        self.assertIn('class="section-banner"', self.body)
        self.assertIn("Story Point 1 - The Shed", self.body)

    def test_mood_card(self) -> None:
        self.assertIn('class="mood"', self.body)
        self.assertIn("Climate", self.body)
        self.assertIn("Thin", self.body)

    def test_gm_note(self) -> None:
        self.assertIn('class="gm-note"', self.body)
        self.assertIn("The shed is empty", self.body)

    def test_table(self) -> None:
        self.assertIn("<table", self.body)
        self.assertIn("Notice", self.body)

    def test_stat_block(self) -> None:
        self.assertIn('class="stat-block"', self.body)
        self.assertIn("WATCHER", self.body)
        self.assertIn("Attributes:", self.body)

    def test_at_hand_statistics_alert(self) -> None:
        self.assertIn('class="callout callout-important at-hand-statistics"', self.body)
        self.assertIn("<h4>At-hand statistics</h4>", self.body)

    def test_at_hand_rules_alert(self) -> None:
        self.assertIn('class="callout callout-tip at-hand-rules"', self.body)
        self.assertIn("<h4>At-hand rules</h4>", self.body)
        self.assertIn("Use the fake procedure here", self.body)
        self.assertIn("<pre><code>", self.body)

    def test_alert_marker_is_not_printed(self) -> None:
        self.assertNotIn("[!IMPORTANT]", self.body)
        self.assertNotIn("[!TIP]", self.body)
        self.assertNotIn("```", self.body)

    def test_plain_paragraph_survives(self) -> None:
        self.assertIn("unclassified text still prints", self.body)

    def test_spoken_lines_field_is_marked(self) -> None:
        self.assertIn('<li class="speech">', self.body)
        self.assertIn("The watcher, if pressed", self.body)

    def test_spoken_lines_paragraph_is_marked(self) -> None:
        self.assertIn('<p class="speech">', self.body)
        self.assertIn("speak this beat while they climb", self.body)

    def test_quote_leading_blockquote_is_speech(self) -> None:
        self.assertIn('<blockquote class="speech-quote">', self.body)
        self.assertIn("not supposed to be on this ladder", self.body)

    def test_spoken_words_are_wrapped_for_color(self) -> None:
        self.assertIn('<span class="line">“Nobody comes up here.”</span>', self.body)

    def test_prose_blockquote_stays_neutral(self) -> None:
        self.assertIn("<blockquote><p>Compiled table document", self.body)

    def test_prose_quotes_are_not_wrapped_as_speech(self) -> None:
        neutral = mdhtml.convert('A rushed glance may still read “military enough.”\n')
        self.assertNotIn('class="line"', neutral)

    def test_foreign_line_keeps_code_inside_speech(self) -> None:
        self.assertIn('<code>"Halt. Papiere." (Halt. Papers.)</code>', self.body)


class PrintCssTests(unittest.TestCase):
    def setUp(self) -> None:
        self.css = (TOOL_DIR / "run.css").read_text(encoding="utf-8")

    def declarations(self, selector: str) -> str:
        found = [
            body
            for group, body in re.findall(r"([^{}]+)\{([^}]*)\}", self.css)
            if selector in [s.strip() for s in group.split(",")]
        ]
        self.assertTrue(found, f"no rule for {selector}")
        return "\n".join(found)

    def value(self, selector: str, prop: str) -> str:
        match = re.search(rf"{prop}:\s*([^;]+);", self.declarations(selector))
        self.assertIsNotNone(match, f"{selector} has no {prop}")
        return match.group(1).strip()

    def test_callouts_are_kept_together(self) -> None:
        self.assertRegex(
            self.css,
            r"\.callout\s*\{[^}]*break-inside:\s*avoid;",
        )

    def test_statistics_and_rules_have_distinct_accents(self) -> None:
        self.assertIn(".at-hand-statistics", self.css)
        self.assertIn(".at-hand-rules", self.css)

    def test_speech_blocks_are_kept_together(self) -> None:
        self.assertIn("break-inside: avoid;", self.declarations(".speech"))
        self.assertIn("break-inside: avoid;", self.declarations(".speech-quote"))

    def test_spoken_words_are_colored(self) -> None:
        self.assertTrue(self.value(".line", "color").startswith("#"))

    def test_speech_accent_differs_from_other_cards(self) -> None:
        speech = self.value(".speech", "background")
        others = [
            self.value(".gm-note", "background"),
            self.value(".at-hand-statistics", "background"),
            self.value(".at-hand-rules", "background"),
        ]
        self.assertNotIn(speech, others)

    def test_fenced_rules_wrap_inside_the_column(self) -> None:
        self.assertRegex(
            self.css,
            r"\.callout pre\s*\{[^}]*white-space:\s*pre-wrap;",
        )


class PathTests(unittest.TestCase):
    def setUp(self) -> None:
        import render

        self.render = render

    def test_adventure_run_defaults_to_print_dir(self) -> None:
        path = Path("/repo/adventures/demo/RUN.md")
        self.assertEqual(self.render.default_out_dir(path), Path("/repo/adventures/demo/print"))

    def test_other_markdown_defaults_to_same_dir(self) -> None:
        path = Path("/tmp/notes/RUN.md")
        self.assertEqual(self.render.default_out_dir(path), Path("/tmp/notes"))


class CliTests(unittest.TestCase):
    def setUp(self) -> None:
        import render

        self.render = render

    def test_missing_file_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            missing = Path(td) / "nope.md"
            with self.assertRaises(SystemExit) as ctx:
                self.render.main([str(missing)])
            self.assertTrue(ctx.exception.code)
            self.assertEqual(list(Path(td).iterdir()), [])

    def test_no_headings_warns_but_writes(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            src = Path(td) / "RUN.md"
            src.write_text("just words\n", encoding="utf-8")
            out = Path(td) / "out"
            err = StringIO()
            with patch("sys.stderr", err):
                self.render.main([str(src), "--out-dir", str(out)])
            html = (out / "RUN.html").read_text(encoding="utf-8")
            self.assertIn("just words", html)
            self.assertIn("no headings", err.getvalue().lower())

    def test_pdf_without_chrome_keeps_html(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            src = Path(td) / "RUN.md"
            src.write_text("# Title\n\nHi.\n", encoding="utf-8")
            out = Path(td) / "out"
            with patch.object(self.render, "CHROME", str(Path(td) / "no-chrome")):
                with self.assertRaises(SystemExit) as ctx:
                    self.render.main([str(src), "--out-dir", str(out), "--pdf"])
            self.assertTrue(ctx.exception.code)
            self.assertTrue((out / "RUN.html").is_file())
            self.assertFalse((out / "RUN.pdf").exists())

    def test_pdf_chrome_failure_keeps_html(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            src = Path(td) / "RUN.md"
            src.write_text("# Title\n\nHi.\n", encoding="utf-8")
            out = Path(td) / "out"
            fake_chrome = Path(td) / "chrome"
            fake_chrome.write_text("", encoding="utf-8")
            fail = subprocess.CalledProcessError(1, ["chrome"])
            with patch.object(self.render, "CHROME", str(fake_chrome)):
                with patch.object(self.render.subprocess, "run", side_effect=fail):
                    with self.assertRaises(SystemExit) as ctx:
                        self.render.main([str(src), "--out-dir", str(out), "--pdf"])
            self.assertTrue(ctx.exception.code)
            self.assertTrue((out / "RUN.html").is_file())
            self.assertFalse((out / "RUN.pdf").exists())


if __name__ == "__main__":
    unittest.main()
