from sqsHandler import SqsHandler
import time

sqs = SqsHandler('<url da sua fila>')


while(True):
    response = sqs.getMessage(10)
    if(len(response['Messages']) == 0):
        break

    time.sleep(1)

