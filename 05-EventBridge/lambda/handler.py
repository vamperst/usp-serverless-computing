import json


def detailHandler(event, context):
    print("event: {}".format(json.dumps(event)))
    
    return True
    
def sourceHandler(event, context):
    print("event: {}".format(json.dumps(event)))
    
    return True