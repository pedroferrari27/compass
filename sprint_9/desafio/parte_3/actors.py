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
movies_grouped= glueContext.create_dynamic_frame.from_catalog(
    database="movies-database",
    table_name="moviesgrouped2movies_grouped2",
    transformation_ctx="grouped_moviex_ctx",
)

# Script generated for node Drop Fields
DropFields = DropFields.apply(
    frame=AWSGlueDataCatalog_node1701722018485,
    paths=[
        "titulopincipal",
        "titulooriginal",
        "anolancamento",
        "tempominutos",
        "genero",
        "notamedia",
        "numerovotos",
        "titulosmaisconhecidos",
    ],
    transformation_ctx="DropFieldsctx",
)

# Script generated for node Rename Field
Rename = RenameField.apply(
    frame=DropFields,
    old_name="id",
    new_name="imdb_id",
    transformation_ctx="Rename_ctx",
)

# Script generated for node Amazon S3
glue_to_s3 = glueContext.getSink(
    path="s3://refined-zone-compasso/movies_table/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="glue_to_s3_ctx",
)
glue_to_s3.setCatalogInfo(
    catalogDatabase="movies-database", catalogTableName="actors_dim"
)
glue_to_s3.setFormat("glueparquet")
glue_to_s3.writeFrame(Rename)
job.commit()

