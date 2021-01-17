from aws_cdk import core, aws_dynamodb, aws_lambda, aws_apigateway

# Share existing code
# from common import CoStack

class UrlShortenerStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        table = aws_dynamodb.Table(self, "MyTable",
                                   partition_key=aws_dynamodb.Attribute(
                                       name="id", type=aws_dynamodb.AttributeType.STRING))
        # Pycharm Use Ctrl+Q to view documentation
        # cdk bootstrap aws://1234/ap-southeast-2 is needed for the lambda asset

        function = aws_lambda.Function(self, "MyLambda",
                                       runtime=aws_lambda.Runtime.PYTHON_3_7,
                                       handler="handler.main",
                                       code=aws_lambda.Code.asset("./lambda"))  # Must be a directory or zip

        # Power User cannot create roles
        table.grant_read_write_data(function)
        function.add_environment("TABLE_NAME", table.table_name)

        api = aws_apigateway.LambdaRestApi(self, "MyAPI", handler=function)
