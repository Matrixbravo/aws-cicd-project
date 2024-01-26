import os
import boto3

def handler(event, context):
    
    #Raw event data.
    path = event["rawPath"]
    if path != "/":
        return {"statusCode": 404, "body": "Not found."}
    
    #Get a reference to the DDB table.
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ.get("TABLE_NAME"))   
    
    # Red the "VISIT COUNT" key (or create it if it doesn't exist)
    response = table.get_item(Key={"key": "visit_count"})
    if "Item" in response:
        visit_count = response["Item"]["value"]
    else:
        visit_count = 0
        
    # Increment the visit count and write it back to the table
    new_vist_count = visit_count + 1
    table.put_item(Item={"key": "visit_count", "value": new_vist_count})
    
    version = os.environ.get("VERSION", "0.0")
    response_body = {
        "message": "Hello world",
        "version": version,
        "visit_count": new_vist_count
    }
    return {"statusCode": 200, "body": response_body}