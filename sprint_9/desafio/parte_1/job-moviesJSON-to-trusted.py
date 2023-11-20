import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from datetime import datetime
from awsglue.job import Job

#foi criado uma database,a partir de um crawler, com os arquivos json , e a partir disso ,criamos uma tabela com as informasoes do json, que usaremos para a transformação

args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH','S3_TARGET_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
source_file = args['S3_INPUT_PATH']
target_path = args['S3_TARGET_PATH']

current_date = datetime.now().strftime("%y/%m/%d")
target_path = target_path.replace('{current_date}', current_date)


database_name = 'movies-database'
table_name = 'json-tmdbresponses'

json_dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database=database_name,
    table_name=table_name,
    transformation_ctx="json_dynamic_frame"
)


parquet_output_path = target_path
glueContext.write_dynamic_frame.from_catalog(
    frame=json_dynamic_frame,
    database=database_name,
    table_name="parquet-tmdb-responses",  # Specify the Parquet table name in the Data Catalog
    transformation_ctx="parquet_output",
)

#escrevendo no s3

glueContext.write_dynamic_frame.from_options(
frame = df ,
connection_type = "s3",
connection_options = {"path": target_path},
format = "parquet")


job.commit()