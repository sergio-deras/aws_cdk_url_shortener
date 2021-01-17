from aws_cdk.core import Construct

from aws_cdk import aws_ecs, aws_ec2


class Traffico(Construct):

    # def __init__(self, scope: Construct, id: str, vpc: aws_ec2.IVpc, url: str, tps: int):
    def __init__(self, scope: Construct, id: str, url: str, tps: int):
        super().__init__(scope, id)

        # cluster = aws_ecs.Cluster(self, "MyCluster", vpc=vpc)
        cluster = aws_ecs.Cluster(self, "MyCluster")

        taskdef = aws_ecs.FargateTaskDefinition(self, "MyTaskDef")
        taskdef.add_container("MyContainer",
                              image=aws_ecs.ContainerImage.from_asset("./pinger"),
                              environment={
                                  "URL": url
                              })

        aws_ecs.FargateService(self, "MyPingerService",
                               cluster=cluster,
                               task_definition=taskdef,
                               desired_count=tps)
