import pandas as pd

from processors.write_output import write_json


def read_csv(filename: str):
    return pd.read_csv(filename)


def calculate_result(filename: str = "./resources/small_dataset.csv") -> dict[str, int]:
    # calculate the result
    df = read_csv(filename)
    dict_output = df.groupby("state").count().to_dict()["id"]
    write_json(dict_output, filename, "pandas")
    return dict_output
