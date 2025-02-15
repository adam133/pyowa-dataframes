from generate_data import generate_csv_data
import os
from processors.pandas_processing import calculate_result as pandas_calculate_result
from processors.dask_processing import calculate_result as dask_calculate_result
from processors.polars_processing import calculate_result as polars_calculate_result
from processors.pyspark_processing import calculate_result as pyspark_calculate_result
from profiling import benchmark
import json
# number of rows in each dataset, decrease this for faster runtime
SMALL_DATASET_ROWS: int = 200
MEDIUM_DATASET_ROWS: int = 10000
LARGE_DATASET_ROWS: int = 1000000

SMALL_DATASET_FILENAME: str = "small_dataset.csv"
MEDIUM_DATASET_FILENAME: str = "medium_dataset.csv"
LARGE_DATASET_FILENAME: str = "large_dataset.csv"

RESOURCE_PATH: str = "./resources/"

BENCH_SIZES = ["large", "medium", "small"]

BENCH_SIZE = os.environ.get("BENCH_SIZE", BENCH_SIZES[0])
assert BENCH_SIZE in BENCH_SIZES, f"BENCH_SIZE environment variable must be one of: {BENCH_SIZES}"


def check_output_files():
    expected_output: dict[str, int] = {}
    for filename in os.listdir("outputs"):
        if filename.endswith(".json"):
            with open(os.path.join("outputs", filename), "r") as f:
                data = json.load(f)
                if expected_output == {}:
                    expected_output = data
                elif data != expected_output:
                    raise ValueError(f"Output file {filename} does not match expected output")
    print(f"All output files are the same result: {expected_output}")


def main():
    # note, this will generate the csv files in the resources folder, and can take some time, about 10 minutes for the large dataset
    if not os.path.exists(RESOURCE_PATH):
        os.makedirs(RESOURCE_PATH)
        generate_csv_data(num_rows=SMALL_DATASET_ROWS, filename=SMALL_DATASET_FILENAME)
        print("Small dataset generated")
        generate_csv_data(num_rows=MEDIUM_DATASET_ROWS, filename=MEDIUM_DATASET_FILENAME)
        print("Medium dataset generated")
        generate_csv_data(num_rows=LARGE_DATASET_ROWS, filename=LARGE_DATASET_FILENAME)
        print("Large dataset generated")



    small_benchmarks = {
        "pandas_small": lambda: pandas_calculate_result(RESOURCE_PATH + SMALL_DATASET_FILENAME),
        "dask_small": lambda: dask_calculate_result(RESOURCE_PATH + SMALL_DATASET_FILENAME),
        "polars_small": lambda: polars_calculate_result(RESOURCE_PATH + SMALL_DATASET_FILENAME),
        "pyspark_small": lambda: pyspark_calculate_result(RESOURCE_PATH + SMALL_DATASET_FILENAME),
    }

    medium_benchmarks = {
        "pandas_medium": lambda: pandas_calculate_result(RESOURCE_PATH + MEDIUM_DATASET_FILENAME),
        "dask_medium": lambda: dask_calculate_result(RESOURCE_PATH + MEDIUM_DATASET_FILENAME),
        "polars_medium": lambda: polars_calculate_result(RESOURCE_PATH + MEDIUM_DATASET_FILENAME),
        "pyspark_medium": lambda: pyspark_calculate_result(RESOURCE_PATH + MEDIUM_DATASET_FILENAME),
    }

    large_benchmarks = {
        "pandas_large": lambda: pandas_calculate_result(RESOURCE_PATH + LARGE_DATASET_FILENAME),
        "dask_large": lambda: dask_calculate_result(RESOURCE_PATH + LARGE_DATASET_FILENAME),
        "polars_large": lambda: polars_calculate_result(RESOURCE_PATH + LARGE_DATASET_FILENAME),
        "pyspark_large": lambda: pyspark_calculate_result(RESOURCE_PATH + LARGE_DATASET_FILENAME),
    }

    if BENCH_SIZE == "small":
        benchmarks = small_benchmarks
    elif BENCH_SIZE == "medium":
        benchmarks = medium_benchmarks
    elif BENCH_SIZE == "large":
        benchmarks = large_benchmarks

    benchmark(benchmarks)

    # assert that the output files are all the same result
    check_output_files()

if __name__ == "__main__":
    main()
