import json
import boto3  


dynamodb = boto3.resource('dynamodb')
table_name = 'cloud-resume-challenge'
dynamodb_table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    response = dynamodb_table.get_item(Key={"ID": "visitors"})
    currentVisitCount = int(response["Item"]["visitors"]) + 1
    dynamodb_table.update_item(
        Key={"ID": "visitors"},
        UpdateExpression='ADD visitors :inc',
        ExpressionAttributeValues={':inc': 1}
                               
    )
    
    
    data = {"visitors": currentVisitCount} 
    
    response = {
        "statusCode": 200,
        "body": json.dumps(data),
        "headers": {
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
        },
    }
    
    return response
    