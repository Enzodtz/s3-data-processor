import json
from utils import process
from orm import engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()


def lambda_handler(event, context):
    """
    Pode ser tanto um evento gerado por uma requisicao GET
    com os parâmetros, quanto por um trigger ao subir para o S3
    """

    if "Records" in event:  # S3 trigger
        for e in event["Records"]:
            object_key = e["s3"]["object"]["key"]
            bucket_name = e["s3"]["bucket"]["name"]

            try:
                process(bucket_name, object_key, session)
            except:
                return {
                    "statusCode": 404,
                }

    else:  # GET request
        object_key = event["queryStringParameters"]["object_key"]
        bucket_name = event["queryStringParameters"]["bucket_name"]

        try:
            process(bucket_name, object_key, session)
        except:
            return {
                "statusCode": 404,
            }

    try:
        session.commit()
    except Exception as e:
        return {"statusCode": 500, "message": str(e)}

    return {"statusCode": 200}
