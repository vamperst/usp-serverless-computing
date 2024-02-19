from sqsHandler import SqsHandler

mensagens = []
for num in range(3000):
    mensagens.append({'Id':str(num), 'MessageBody': str(num)})

splitMsg = [mensagens[x:x+10] for x in range(0, len(mensagens), 10)]
sqs = SqsHandler('https://sqs.us-east-1.amazonaws.com/867061838226/demoqueue')
for lista in splitMsg:    
    print(type(lista))
    print(str(lista))
    sqs.sendBatch(lista)