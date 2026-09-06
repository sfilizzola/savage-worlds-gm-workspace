#!/usr/bin/env python3
from __future__ import annotations

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

    def test_plain_paragraph_survives(self) -> None:
        self.assertIn("unclassified text still prints", self.body)


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
