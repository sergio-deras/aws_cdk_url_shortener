from aws_cdk import core, aws_dynamodb


class UrlShortenerStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        table = aws_dynamodb.Table(self, "MyTable",
                                   partition_key=aws_dynamodb.Attribute(name="id", type=aws_dynamodb.AttributeType.STRING))