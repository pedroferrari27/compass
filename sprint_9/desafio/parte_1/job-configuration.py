import boto3

def update_worker_type(JobName, WorkerType, NumberOfWorkers,ScriptLocation):
    glue = boto3.client('glue', aws_access_key_id='AKIAZIW2UFDNKW3PZDP6', aws_secret_access_key='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')

    try:
        response = glue.update_job(
            JobName=JobName,
            JobUpdate={
                'WorkerType': WorkerType,
                'NumberOfWorkers': NumberOfWorkers,
                'Role': 'AWSGlueServiceRole' ,
                'Timeout': 60,
                'Command': {
                    'Name': JobName,
                    'ScriptLocation': ScriptLocation
                    # Add other required command parameters if necessary
                }
            }
        )
        print(response)

    except Exception as e:
        print(e)


JobName ="join-tables-for-refining"
ScriptLocation = 's3://glue-jobscripts/join-tables-for-refining.py'
NumberOfWorkers = 2
WorkerType = "G.1X"

update_worker_type(JobName, WorkerType, NumberOfWorkers,ScriptLocation)

