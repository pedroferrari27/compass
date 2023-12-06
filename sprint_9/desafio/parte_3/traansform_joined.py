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

# Script generated for node AWS Glue Data Catalog
joined = glueContext.create_dynamic_frame.from_catalog(
    database="movies-database",
    table_name="joined_tablemovies_joined_parquet",
    transformation_ctx="joined_ctx",
)

# Script generated for node Drop Fields
DropFields = DropFields.apply(
    frame=joined,
    paths=[
        "titulosmaisconhecidos",
        "`.id`",
        "homepage",
        "video",
        "partition_0",
        "poster_path",
        "anonascimento",
        "anofalecimento",
        "profissao",
        "generoartista",
        "nomeartista",
        "backdrop_path",
    ],
    transformation_ctx="DropFields_ctx",
)

# Script generated for node Amazon S3
glue_to_s3 = glueContext.write_dynamic_frame.from_options(
    frame=DropFields_node1701722238843,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://refined-zone-compasso/movies_all/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="glue_to_s3_ctx",
)

job.commit()

