"""Command line interface for ???."""

import logging
from pprint import pprint

import click
import click_log

from src.common.yaml_utils import parse_yaml

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.group()
@click.version_option(version='0.1.0')
def cli():
    pass


@cli.command()
@click_log.simple_verbosity_option(logger)
@click.option(
    '--file',
    help='YAML file to parse',
)
def parse(**kwargs):
    """Parse provided YAML file."""
    result = parse_yaml(kwargs['file'])
    pprint(result)


if __name__ == '__main__':
    cli()
