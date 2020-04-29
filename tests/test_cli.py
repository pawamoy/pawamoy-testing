"""Tests for the `cli` module."""

import pytest

from pawamoy_testing import cli


def test_main():
    """Basic CLI test."""
    assert cli.main([]) == 0


def test_main_help(capsys):
    """Basic CLI test."""
    with pytest.raises(SystemExit):
        cli.main(["-h"])
    captured = capsys.readouterr()
    assert "pawamoy-testing" in captured.out
