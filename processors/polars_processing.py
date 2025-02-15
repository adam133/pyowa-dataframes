from polars import read_csv

from processors.write_output import write_json


def calculate_result(filename: str = "./resources/small_dataset.csv") -> dict[str, int]:
    df = read_csv(filename)
    dict_output = (
        df.group_by("state")
        .count()
        .to_pandas(use_pyarrow_extension_array=True)
        .to_dict()
    )
    # format the output to be a dictionary of state to count
    # outputs like {"state": {"0": "Mississippi", "1": "Virginia"}, "count": {"0": 20056, "1": 20250}}
    # we want to convert it to {"Mississippi": 20056, "Virginia": 20250}
    states = dict_output["state"]
    counts = dict_output["count"]
    dict_output = {states[i]: counts[i] for i in range(len(states))}
    write_json(dict_output, filename, "polars")
    return dict_output
