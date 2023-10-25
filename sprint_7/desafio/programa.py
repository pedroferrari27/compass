import boto3

REGION = 'us-east-1'
ACCESS_KEY_ID = 'SUA_ACCESS_KEY'
SECRET_ACCESS_KEY = 'SUA_SECRET_KEY'

BUCKET_NAME = 'raw-zone-compasso'

PATH_MOVIES = '/dados/movies.csv'
PATH_SERIES = '/dados/series.csv'
KEY_MOVIES = 'Raw/Local/CSV/Movies/26|10|23/movies.csv'
KEY_SERIES = 'Raw/Local/CSV/Movies/26|10|23/series.csv'

s3 = boto3.client(
    's3',
    region_name=REGION,
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY
)