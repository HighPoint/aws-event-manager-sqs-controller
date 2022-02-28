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
