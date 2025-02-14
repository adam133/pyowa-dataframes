from faker import Faker
import csv
import os
from pandas_processing import calculate_result as pandas_calculate_result
from dask_processing import calculate_result as dask_calculate_result
from polars_processing import calculate_result as polars_calculate_result
from pyspark_processing import calculate_result as pyspark_calculate_result
from profiling import benchmark

# number of rows in each dataset, decrease this for faster runtime
SMALL_DATASET_ROWS: int = 200
MEDIUM_DATASET_ROWS: int = 10000
LARGE_DATASET_ROWS: int = 1000000



def generate_csv_data(num_rows: int = SMALL_DATASET_ROWS, filename: str = "small_dataset.csv"):
    fake = Faker()
    data = []
    for _ in range(num_rows):
        data.append({
            "id": _ + 1,
            "name": fake.name(),
            "email": fake.email(),
            "phone": fake.phone_number(),
            "address": fake.street_address(),
            "city": fake.city(),
            "state": fake.state(),
            "zip": fake.zipcode(),
        })
    
    with open("./resources/" + filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def main():
    # note, this will generate the csv files in the resources folder, and can take some time, about 10 minutes for the large dataset
    if not os.path.exists("./resources"):
        os.makedirs("./resources")
        generate_csv_data()
        print("Small dataset generated")
        generate_csv_data(num_rows=MEDIUM_DATASET_ROWS, filename="medium_dataset.csv")
        print("Medium dataset generated")
        generate_csv_data(num_rows=LARGE_DATASET_ROWS, filename="large_dataset.csv")
        print("Large dataset generated")



    benchmarks = {
        "pandas_small": lambda: pandas_calculate_result("./resources/small_dataset.csv"),
        "pandas_medium": lambda: pandas_calculate_result("./resources/medium_dataset.csv"),
        "pandas_large": lambda: pandas_calculate_result("./resources/large_dataset.csv"),
        "dask_small": lambda: dask_calculate_result("./resources/small_dataset.csv"),
        "dask_medium": lambda: dask_calculate_result("./resources/medium_dataset.csv"),
        "dask_large": lambda: dask_calculate_result("./resources/large_dataset.csv"),
        "polars_small": lambda: polars_calculate_result("./resources/small_dataset.csv"),
        "polars_medium": lambda: polars_calculate_result("./resources/medium_dataset.csv"),
        "polars_large": lambda: polars_calculate_result("./resources/large_dataset.csv"),
        "pyspark_small": lambda: pyspark_calculate_result("./resources/small_dataset.csv"),
        "pyspark_medium": lambda: pyspark_calculate_result("./resources/medium_dataset.csv"),
        "pyspark_large": lambda: pyspark_calculate_result("./resources/large_dataset.csv"),
    }


    benchmark(benchmarks)

if __name__ == "__main__":
    main()
