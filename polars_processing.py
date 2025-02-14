from polars import read_csv


def calculate_result(filename: str = "./resources/small_dataset.csv") -> dict[str, int]:
    df = read_csv(filename)
    return df.group_by("state").count().to_pandas().to_dict()
