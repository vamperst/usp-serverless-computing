import boto3
import json
import datetime

eventBridge = boto3.client('events')

def put_events_orders(eventBus, source, detailType, detail):
    response = eventBridge.put_events(
        Entries=[
            {
                'Time': datetime.datetime.now(),
                'Source': source,
                'DetailType': detailType,
                'Detail': json.dumps(detail),
                'EventBusName': eventBus,
            }
        ]
    )
    print("EventBridge Response: {}".format(json.dumps(response)))
    

eventBus="<Adicione o nome do barramento>"
source = "<Adicione a fonte do evento>"
detailType = "<Adicione o detalhe do Evento>"
detail = <Adiocione o conteudo do evento>

for i in range(10):
    print(i)
    put_events_orders(eventBus, source, detailType, detail)


