import click

from awscli.completer import Completer as AwsCompleter
from .ec2 import EC2
from .elb import ELB


# Need invoke_without_commands=True because need to call --all-commands
# without any command.
@click.group(invoke_without_command=True)
@click.option(
    "--all-commands", is_flag=True, help="List all known commands.",
)
def cli(*args, **kwargs):
    if kwargs["all_commands"]:
        for cmd in AwsCompleter().complete("aws", 3):
            click.echo(cmd)


@cli.command()
@click.option(
    "--attrib",
    "-a",
    default=[
        "InstanceId",
        "InstanceType",
        "KeyName",
        "ImageId",
        "PrivateIpAddress",
        "LaunchTime",
    ],
    show_default=True,
    multiple=True,
    help="One or multiple comma-seperated attributes to show",
)
@click.option(
    "--limit",
    default=0,
    show_default=True,
    help="Limit the number of results that get shown. 0 means no limit.",
)
@click.option(
    "--known-attributes",
    is_flag=True,
    help="List all known attributes by this script.",
)
@click.option(
    "--output",
    type=click.Choice(["json", "table", "text"], case_sensitive=False),
    default="text",
    show_default=True,
    help="The formatting style for command output.",
)
@click.option("--tag-key", "-k", default="Name", show_default=True)
@click.option("--tag-value", "-v")
def ec2(*args, **kwargs):
    EC2(*args, **kwargs).run()


@cli.command()
@click.option(
    "--limit",
    default=0,
    show_default=True,
    help="Limit the number of results that get shown. 0 means no limit.",
)
@click.option(
    "--show-limits", is_flag=True, help="Show ELB limits for this account.",
)
def elb(*args, **kwargs):
    ELB(*args, **kwargs).run()


if __name__ == "__main__":
    cli()
