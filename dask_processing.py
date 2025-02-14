from dask import dataframe as dd


def read_csv(filename: str):
    return dd.read_csv(filename)

def calculate_result(filename: str = "./resources/small_dataset.csv") -> dict[str, int]:
    df = read_csv(filename)
    return df.groupby("state").count().compute().to_dict()
