"""Tests for cli"""
from click.testing import CliRunner

from src.cli import say


def test_say_command_echos_goodbye_world():
    """Should echo Goodbye World."""
    runner = CliRunner()
    result = runner.invoke(say, ['--what', 'Goodbye', '--who', 'Everybody'])
    assert result.exit_code == 0
    assert result.output == 'Goodbye Everybody\n'
