from sqsHandler import SqsHandler
sqs = SqsHandler('<url da sua fila>')

while(True):
    response = sqs.getMessage(10)
    if(len(response['Messages']) == 0):
        break

    mensagens = []
    for msg in response['Messages']:
        mensagens.append({'Id':msg['MessageId'], 'ReceiptHandle':msg['ReceiptHandle']})    
        sqs.deleteMessage(mensagens)

