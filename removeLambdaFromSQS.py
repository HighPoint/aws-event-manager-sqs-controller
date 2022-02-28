import json
import boto3

def lambda_handler(event, context):
    
    lambdaString = "LAMBDA NAME"
    sqsARN  = "SQS ARN"
    
    removeLambdaFromSQS(lambdaString, sqsARN)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

    
    
def removeLambdaFromSQS(lambdaString, sqsARN):
    

    client = boto3.client('lambda') 
    
    response = client.list_event_source_mappings(EventSourceArn=sqsARN,FunctionName=lambdaString)    
    uuid = response['EventSourceMappings'][0]['UUID']   
    
    response = client.delete_event_source_mapping(UUID=str(uuid))  
    
    return True  
