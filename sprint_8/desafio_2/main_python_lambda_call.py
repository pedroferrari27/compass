import boto3
import pandas as pd
from datetime import datetime
import json

def create_id_batches(list_of_ids, batch_size):
    id_batches = []

    for batch_number, i in enumerate(range(0, len(list_of_ids), batch_size), start=1):
        batch = list_of_ids[i:i + batch_size]
        id_batches.append((batch_number, batch))

    return id_batches

def create_payload(existing_payload, batch_number, id_batch):
   existing_payload["batch_number"] = batch_number
   existing_payload["IDs"] = id_batch
   return existing_payload


#donwloada and open file
aws_access_key_id = 'AKIAZIW2UFDNMJIPBJ74'
aws_secret_access_key = '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'
bucket_name = 'raw-zone-compasso'
s3_file_key = 'raw-zone-compasso/Raw/Local/CSV/Movies/26|10|23/movies.csv'
local_file_path = '/home/pedro/Desktop/rep-compasso/compas novo/compass/sprint_8/desafio 2/testes_de_produção/movies.csv'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Download the original movies csv
try:
    s3.download_file(bucket_name, s3_file_key, local_file_path)
    print(f"Downloaded {s3_file_key} from S3 bucket to {local_file_path}")
except Exception as e:
    print(f"Error: {e}")


with open(local_file_path,"r") as arquivo:
    df = pd.read_csv(arquivo,delimiter= '|',low_memory=False)



#get id of the movies for search

generos = ['Drama', 'War']

df = df[df['genero'].str.contains('|'.join(generos))]

unique_values = df['id'].unique().tolist()




# Get the current date and time
current_datetime = datetime.now()
formatted_date = current_datetime.strftime('%y/%m/%d')

function_name = 'desafio-2'
target_file =f"raw-zone-compasso/Raw/tmdb/json/{formatted_date}/responses/"

# Create a Lambda client
lambda_client = boto3.client('lambda',region_name='us-east-1',aws_access_key_id= aws_access_key_id,aws_secret_access_key= aws_secret_access_key)

Payload_data ={
  "aws_access_key_id": "AKIAZIW2UFDNKW3PZDP6",
  "aws_secret_access_key": "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",
  "bucket_name": "raw-zone-compasso",
  "target_file": target_file,
}





# Invoke Lambda function
print("enviando")
#test with 100 movie ids
unique_test = create_id_batches(unique_values,1000)



for batch_number, id_batch in unique_test:
   print("+batch") 
   json_payload = json.dumps(create_payload(Payload_data, batch_number, id_batch)) 
   response = lambda_client.invoke_async(
    FunctionName=function_name,
    #InvocationType='RequestResponse',
    InvokeArgs=json_payload.encode('utf-8')  
    )
 
   

# Get the response from the Lambda function
    



#with open("responses.json", "w") as json_file:
#    for line in json_responses :
#        json.dump(json_responses, json_file)
#        json_file.write('\n\n\n')

#df = pd.DataFrame(json_responses)
#print(df)








        
        
        


