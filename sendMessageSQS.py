import json
import boto3

def lambda_handler(event, context):
    

    sqsURL = "SQS URL"
    message = "SQS String Message"

    sendMessageSQS(sqsURL, message)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def sendMessageSQS(sqsURL, message):

    sqs = boto3.client('sqs')

    response = sqs.send_message(
        QueueUrl=sqsURL,
        DelaySeconds=10,
        MessageAttributes={
            'Folders': {
                'DataType': 'String',
                'StringValue': str(message)
            }
        },
        MessageBody=(
            str(message)
        )
    )
