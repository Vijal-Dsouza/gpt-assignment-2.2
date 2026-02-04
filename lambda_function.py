import json
from datetime import datetime 

def lambda_handler(event, context):
    return{
        "message": "Lambda deployed using Docker",
        "service": "devops",
        "env": "test",
        "timestamp": datetime.utcnow().isoformat()
    }
