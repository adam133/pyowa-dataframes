from daft.io import read_csv

from processors.write_output import write_json


def calculate_result(filename: str = "./resources/small_dataset.csv") -> dict[str, int]:
    df = read_csv(filename)
    dict_counted = df.groupby("state").count('id').to_pydict()
    states = dict_counted["state"]
    counts = dict_counted["id"]
    dict_output = {states[i]: counts[i] for i in range(len(states))}
    write_json(dict_output, filename, "daft")
    return dict_output
