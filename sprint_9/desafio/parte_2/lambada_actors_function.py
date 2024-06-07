#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 16:48:52 2023

@author: pedro
"""

import json
import requests
import boto3
from concurrent.futures import ThreadPoolExecutor

def fetch_movie_data(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "[key]"
    }
    result = url.format(movie_id)
    response = requests.get(result, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def lambda_handler(event, context):
    unique_test = event['IDs']
    aws_access_key_id = event['aws_access_key_id']
    aws_secret_access_key = event['aws_secret_access_key']
    bucket_name = event['bucket_name']
    target_file = event['target_file']
    batch_number = event['batch_number']

    json_responses = []

    # Use ThreadPoolExecutor for parallelizing requests
    with ThreadPoolExecutor() as executor:
        # Map the fetch_movie_data function to each movie ID in parallel
        futures = [executor.submit(fetch_movie_data, movie_id) for movie_id in unique_test]

        # Collect the results as they become available
        for future in futures:
            result = future.result()
            if result is not None:
                json_responses.append(result)
                

    json_data = "\n".join(json.dumps(response) for response in json_responses)

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    
    target_file = f"{target_file}batch_{batch_number}.json"

    s3.put_object(Body=json_data, Bucket=bucket_name, Key=target_file)

    return "Code: Success"