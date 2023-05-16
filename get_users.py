import json

import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("user-table")


def handler(event, context):
    items = table.scan()["Items"]
    usernames = list(map(lambda x: x["username"], items))
    response = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {},
        "multiValueHeaders": {},
        "body": json.dumps(usernames),
    }
    return response
