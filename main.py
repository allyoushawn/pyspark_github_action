# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, LongType, StringType

def create_dataset():
    data = [
        (1001, "[0.1,0.1]"),
        (1002, "[0.2,0.2]"),
    ]

    schema = StructType(
        [
            StructField("userNumber", LongType(), True),
            StructField("vector", StringType(), True),
        ]
    )
    dataset = spark.createDataFrame(data=data, schema=schema)
    dataset.show()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    spark = SparkSession.builder.appName("TestPySpark").enableHiveSupport().getOrCreate()
    create_dataset()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
