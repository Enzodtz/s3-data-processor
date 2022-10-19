import os
import boto3
from utils import treat_df
from orm import CessaoFundo
import pandas as pd
from io import StringIO


s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ["AWS_ACCESS"],
    aws_secret_access_key=os.environ["AWS_SECRET"],
)


def process(bucket_name, object_key, session):
    obj = s3.get_object(Bucket=bucket_name, Key=object_key)

    body = obj["Body"]
    csv_string = body.read().decode("latin-1")

    df = pd.read_csv(StringIO(csv_string), delimiter=";")

    df = treat_df(df)

    for i, row in df.iterrows():
        session.add(
            CessaoFundo(
                row["Originador"],
                row["Doc Originador"],
                row["Cedente"],
                row["Doc Cedente"],
                row["CCB"],
                row["Id"],
                row["Cliente"],
                row["CPF/CNPJ"],
                row["Endereço"],
                row["CEP"],
                row["UF"],
                row["Valor do Empréstimo"],
                row["Parcela R$"],
                row["Total Parcelas"],
                row["Parcela #"],
                row["Data de Emissão"],
                row["Data de Vencimento"],
                row["Preço de Aquisição"],
            )
        )
