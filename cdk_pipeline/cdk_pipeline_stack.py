import aws_cdk as cdk

from aws_cdk import (
    # Duration,
    Stack,
)
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from constructs import Construct
from cdk_pipeline.my_pipeline_app_stage import MyPipelineAppStage

class CdkPipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        pipeline =  CodePipeline(self, "Pipeline", 
                        pipeline_name="MyCdkPipeline",
                        synth=ShellStep("Synth", 
                            input=CodePipelineSource.git_hub("akarshgowda17/cdk_pipeline", "main"),
                            commands=["npm install -g aws-cdk", 
                                "python -m pip install -r requirements.txt", 
                                "cdk synth"]
                        )
                    )

        pipeline.add_stage(MyPipelineAppStage(self, "test",
            env=cdk.Environment(account="626228733568", region="ap-south-1")))#want to check whether its necessary to add env for each stage
