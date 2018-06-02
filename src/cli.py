"""Command line interface for ???."""

import logging

import click
import click_log

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


@click.group()
@click.version_option(version='0.1.0')
def cli():
    pass


@cli.command()
@click_log.simple_verbosity_option(logger)
@click.option(
    '--what',
    prompt='What do you want to say?',
    help='Thing to say.',
    default='Hello',
)
@click.option(
    '--who',
    prompt='Who do you want to say it to?',
    help='Who to say it to.',
    default='World',
)
def say(**kwargs):
    """Example command."""
    click.echo('{} {}'.format(kwargs['what'], kwargs['who']))


if __name__ == '__main__':
    cli()
