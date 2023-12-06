import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)


json_files = glueContext.create_dynamic_frame.from_catalog(
    database="movies-database",
    table_name="tmdb-jsonparquet-movies_json_to_parquet",
    transformation_ctx="datajson",
)


csv_files = glueContext.create_dynamic_frame.from_catalog(
    database="movies-database",
    table_name="movies-tmdb-csvtoparquet-movies_grouped_parquet",
    transformation_ctx="datacsv",
)

# Script generated for node Join
Join_node1701297420190 = Join.apply(
    frame1=json_files,
    frame2=csv_files,
    keys1=["imdb_id"],
    keys2=["id"],
    transformation_ctx="Join",
)

# Script generated for node Amazon S3
glue-tos3 = glueContext.write_dynamic_frame.from_options(
    frame=Join_node1701297420190,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://trusted-zone-compasso/Parquet/Movies/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="glue-s3",
)

job.commit()
