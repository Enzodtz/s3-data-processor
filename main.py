import json
from re import A
import boto3
from botocore import UNSIGNED
from botocore.client import Config
import pandas as pd
from io import StringIO
from orm import CessaoFundo, engine
from sqlalchemy.orm import sessionmaker

s3 = boto3.client("s3", config=Config(signature_version=UNSIGNED))

Session = sessionmaker(bind=engine)
session = Session()

object_key = "arquivo_exemplo.csv"
bucket_name = "edesoft-test-bucket"

obj = s3.get_object(Bucket=bucket_name, Key=object_key)
body = obj["Body"]
csv_string = body.read().decode("latin-1")

df = pd.read_csv(StringIO(csv_string), delimiter=";")

df["Doc Originador"] = (
    df["Doc Originador"].str.replace(".", "").str.replace("/", "").str.replace("-", "")
)
df["Doc Cedente"] = (
    df["Doc Cedente"]
    .astype(str)
    .astype(str)
    .str.replace(".", "")
    .str.replace("/", "")
    .str.replace("-", "")
)
df["CPF/CNPJ"] = (
    df["CPF/CNPJ"].str.replace(".", "").str.replace("/", "").str.replace("-", "")
)
df["Valor do Empréstimo"] = df["Valor do Empréstimo"].str.replace(",", ".")
df["Parcela R$"] = (
    df["Parcela R$"].str.replace(",", ".").str.replace("[a-zA-Z]", "")
)  # Um elemento da coluna do exemplo continha o valor A666
df["Preço de Aquisição"] = df["Preço de Aquisição"].astype(str).str.replace(",", ".")
df["Data de Emissão"] = pd.to_datetime(df["Data de Emissão"], format="%d/%m/%Y")
df["Data de Vencimento"] = pd.to_datetime(df["Data de Emissão"], format="%d/%m/%Y")

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

session.commit()
