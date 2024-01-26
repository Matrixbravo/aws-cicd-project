import os

def handler(event, context):
    version = os.environ.get("VERSION", "0.0")
    response_body = {
        "message": "Test Beta",
        "version": version
    }
    return {"statusCode": 200, "body": response_body}