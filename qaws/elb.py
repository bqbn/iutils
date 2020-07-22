import boto3
import click

from .resource import Resource


class ELB(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show_limits = kwargs["show_limits"]

    def run(self):
        if self.show_limits:
            limits = []

            client = boto3.client("elb")
            paginator = client.get_paginator("describe_account_limits")
            pagination_config = {
                "MaxItems": 100,
                "PageSize": 100,  # PageSize should never be greater than MaxItems.
                "StartingToken": "",
            }

            while True:
                for res in paginator.paginate(PaginationConfig=pagination_config):
                    limits += res["Limits"]
                if res.get("NextMarker"):
                    pagination_config["StartingToken"] = res["NextMarker"]
                else:
                    break

            for item in limits:
                click.echo(f"{item['Name']}: {item['Max']} max")
