from dask import dataframe as dd

from processors.write_output import write_json


def read_csv(filename: str):
    return dd.read_csv(filename)


def calculate_result(filename: str = "./resources/small_dataset.csv") -> dict[str, int]:
    df = read_csv(filename)
    dict_output = df.groupby("state").count().compute().to_dict()["id"]
    write_json(dict_output, filename, "dask")
    return dict_output
