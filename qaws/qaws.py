import click
import subprocess


@click.command()
@click.option(
    "--output",
    default="text",
    help='The formatting style for command output, either text, json, or table. The default is "text".',
)
@click.option("--tag-key", default="Name")
@click.option("--tag-value")
def ec2(output, tag_key, tag_value):
    cmd = [
        "aws",
        "ec2",
        "describe-instances",
        "--output",
        output,
        "--filter",
        f"Name=tag:{tag_key},Values={tag_value}",
        "--query",
        "Reservations[*].Instances[*].[InstanceId,PrivateIpAddress]",
    ]
    subprocess.run(cmd)


if __name__ == "__main__":
    ec2()
