import pandas as pd


def treat_df(df):
    df["Doc Originador"] = (
        df["Doc Originador"]
        .str.replace(".", "")
        .str.replace("/", "")
        .str.replace("-", "")
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
    df["Preço de Aquisição"] = (
        df["Preço de Aquisição"].astype(str).str.replace(",", ".")
    )
    df["Data de Emissão"] = pd.to_datetime(df["Data de Emissão"], format="%d/%m/%Y")
    df["Data de Vencimento"] = pd.to_datetime(df["Data de Emissão"], format="%d/%m/%Y")

    return df
