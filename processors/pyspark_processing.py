from pyspark.sql import SparkSession

from processors.write_output import write_json


def read_csv(filename: str):
    spark_session: SparkSession = SparkSession.builder.appName(
        "pyspark_processing"
    ).getOrCreate()
    return spark_session.read.csv(filename, header=True)


def calculate_result(filename: str = "./resources/small_dataset.csv") -> dict[str, int]:
    df = read_csv(filename)
    temp_df = df.select("state").groupby("state").count()
    result = {row.asDict()["state"]: row.asDict()["count"] for row in temp_df.collect()}
    write_json(result, filename, "pyspark")
    return result
