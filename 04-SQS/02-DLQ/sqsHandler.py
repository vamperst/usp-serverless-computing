import boto3

class SqsHandler:
    def __init__(self,queueUrl):
        self.__sqs = boto3.client('sqs')
        self.__queueUrl = queueUrl

    def getMessage(self,qtdMsgs):
        response = self.__sqs.receive_message(
            QueueUrl=self.__queueUrl,
            MaxNumberOfMessages=qtdMsgs
        )
        return response

    def deleteMessage(self,receiptHandle):
        response = self.__sqs.delete_message(
            QueueUrl=self.__queueUrl,
            ReceiptHandle=receiptHandle
        )
        return response
    
    def deleteBatch(self,lista):
        response = self.__sqs.delete_message_batch(
            QueueUrl=self.__queueUrl,
            Entries=lista
        )
        print(response)

    def sendBatch(self,lista):
        response = self.__sqs.send_message_batch(
            QueueUrl=self.__queueUrl,
            Entries=lista
        )
        print(response)
    
    def send(self,msg):
        response = self.__sqs.send_message(
            QueueUrl=self.__queueUrl,
            MessageBody=msg
        )
        print(response)
    