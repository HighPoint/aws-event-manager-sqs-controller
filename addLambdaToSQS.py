import json
import boto3

def lambda_handler(event, context):
    
    lambdaString = "LAMBDA NAME"
    sqsARN  = "SQS ARN"
    
    addLambdaToSQS(lambdaString, sqsARN)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def addLambdaToSQS(lambdaString, sqsARN):
    
    client = boto3.client('lambda') 
    
    response = client.create_event_source_mapping(EventSourceArn=sqsARN, FunctionName=lambdaString,   Enabled=True,   BatchSize=1)
    
    print(response)
    
    return True
