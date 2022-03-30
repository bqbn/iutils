import click

from .main import (
    add_common_options,
    common_options,
    main,
)
from ..commands import TeamsCommand


@main.group(invoke_without_command=True)
def teams(*args, **kwargs):
    """Team related commands"""
    pass


@teams.command(name="list")
@add_common_options(common_options)
def list_command(**kwargs):
    """List all the teams

    List the team's slug by default. Use the --attrs option to change what
    attributes to show.
    """
    attrs = kwargs["attrs"] if kwargs["attrs"] else ["slug"]
    TeamsCommand(**kwargs).list_command(attrs)
