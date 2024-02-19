import boto3
import json
import datetime

import random

regions = ['eu-west','us-east','sa-east']

peeker = random.SystemRandom()

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
    
def makeEvent():
    eventBus="Orders"
    source = "com.aws.orders"
    detailType = "Order Notification"
    detail = {
      "category": "lab-supplies",
      "value": 415,
      "location": peeker.choice(regions)
    }
    put_events_orders(eventBus, source, detailType, detail)

for i in range(10):
    print(i)
    makeEvent()


