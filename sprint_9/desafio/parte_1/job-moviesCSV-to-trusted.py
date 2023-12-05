import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from datetime import datetime
from awsglue.job import Job

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

df = glueContext.create_dynamic_frame.from_options(
"s3",
{
"paths": [
so"csv",
{"withHeader": True, "separator":","},
)

glueContext.write_dynamic_frame.from_options(
frame = df ,
connection_type = "s3",
connection_options = {"path": target_path},
format = "parquet")
job.commit()