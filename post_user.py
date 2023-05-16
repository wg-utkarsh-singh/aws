import json

import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("user-table")


def handler(event, context):
    body = json.loads(event["body"])
    username = body.get("username", False)
    if not username:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing required parameters: username"}),
        }

    table.put_item(
        Item={
            "username": username,
        }
    )
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Data inserted successfully"}),
    }
