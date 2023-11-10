import requests
import boto3
import json

function_name = 'desafio-2'
aws_access_key_id = 'AKIAZIW2UFDNKW3PZDP6'
aws_secret_access_key = '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'

# Create a Lambda client
lambda_client = boto3.client('lambda',region_name='us-east-1',aws_access_key_id= aws_access_key_id,aws_secret_access_key= aws_secret_access_key)

# Input data for your Lambda function (if required)
input_data ={
  "IDs": [
    "tt0000591",
    "tt0000615",
    "tt0000630",
    "tt0000886",
    "tt0000941",
    "tt0001049",
    "tt0001112",
    "tt0001175",
    "tt0001184",
    "tt0001240"
  ],
  "aws_access_key_id": "AKIAZIW2UFDNKW3PZDP6",
  "aws_secret_access_key": "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",
  "bucket_name": "raw-zone-compasso",
  "target_file": "raw-zone-compasso/Raw/tmdb/json/2023/11/9/responses.csv"
}
json_payload = json.dumps(input_data)

# Invoke Lambda function
response = lambda_client.invoke(
    FunctionName=function_name,
    InvocationType='RequestResponse',  # Can be 'Event' for asynchronous invocation
    Payload=json_payload.encode('utf-8')  # Pass input data as a string
)

# Get the response from the Lambda function
response_payload = response['Payload'].read()
print(response_payload)

