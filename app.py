#!/usr/bin/env python
import click

@click.command()
@click.option("--name")
def hello(name):
    click.echo(f'Hello {name}! I hope you enjoy this app!')

if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()
