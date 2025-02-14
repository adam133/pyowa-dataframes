import pandas as pd


def read_csv(filename: str):
    return pd.read_csv(filename)


def calculate_result(filename: str = "./resources/small_dataset.csv") -> dict[str, int]:
    # calculate the result
    df = read_csv(filename)
    return df.groupby("state").count().to_dict()
