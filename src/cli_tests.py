"""Tests for cli"""
from click.testing import CliRunner

from src.cli import parse


def test_parse_woks_as_expected():
    """Should parse provided YAML file as expected."""
    runner = CliRunner()
    # TODO: instead create temp file and delete afterward
    result = runner.invoke(parse, ['--file', 'data/test1.yml'])
    assert result.exit_code == 0
