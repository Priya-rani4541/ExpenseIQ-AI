import pandas as pd


def read_csv(file):

    df = pd.read_csv(file)

    rows = df.to_dict(
        orient="records"
    )

    return rows