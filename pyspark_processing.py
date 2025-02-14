from pyspark.sql import SparkSession


def read_csv(filename: str):
    spark_session: SparkSession = SparkSession.builder.appName("pyspark_processing").getOrCreate()
    # disable logging
    spark_session.sparkContext.setLogLevel("ERROR")
    return spark_session.read.csv(filename, header=True)

def calculate_result(filename: str = "./resources/small_dataset.csv") -> dict[str, int]:
    df = read_csv(filename)
    temp_df = df.select("state").groupby("state").count()
    result = {row.asDict()["state"]: row.asDict()["count"] for row in temp_df.collect()}
    return result
