from sqsHandler import SqsHandler

mensagens = []
numMsgsToCreate = 3000
for num in range(numMsgsToCreate):
    mensagens.append({'Id':str(num), 'MessageBody': str(num)})

splitMsg = [mensagens[x:x+10] for x in range(0, len(mensagens), 10)]
sqs = SqsHandler('<url da sua fila>')
for lista in splitMsg:    
    print(type(lista))
    print(str(lista))
    sqs.sendBatch(lista)