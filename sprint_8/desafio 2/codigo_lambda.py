import json
import boto3
import requests

def lambda_handler(event, context):
    # TODO implement
    unique_test = event['IDs']
    aws_access_key_id = event['aws_access_key_id']
    aws_secret_access_key = event['aws_secret_access_key']
    bucket_name = event['bucket_name']
    target_file = event['target_file']    
    
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMTk1ZmQ4YzlhZmVmMGRiMmJmODEzNmU1NDUyYjU3NCIsInN1YiI6IjY1NDkyODI5NmJlYWVhMDBjOWZkNzI5NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.TK_o1CliJTUqQ9x_q353CkHopwkxrxb_eGK9b-ZiaEc"
    }
    json_responses = []
    for item in unique_test:
        result = url.format(item)
        print("\n")
        response = requests.get(result, headers=headers)
        if response.status_code == 200:
            data = response.json() 
            json_responses.append(data)
            
    json_data = json.dumps(json_responses)        

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    s3.put_object(Body=json_data, Bucket=bucket_name, Key=target_file)
    
    
    return json_responses
