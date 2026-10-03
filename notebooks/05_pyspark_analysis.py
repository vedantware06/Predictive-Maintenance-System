from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Start Spark
spark = SparkSession.builder \
    .appName("Predictive Maintenance Big Data Analysis") \
    .getOrCreate()

# Load dataset
df = spark.read.csv(
    "data/predictive_maintenance.csv",
    header=True,
    inferSchema=True
)

print("\n===== DATASET INFORMATION =====")
print("Total Records:", df.count())

print("\n===== DATASET SCHEMA =====")
df.printSchema()

print("\n===== SAMPLE DATA =====")
df.show(5)

# Failure analysis
print("\n===== FAILURE ANALYSIS =====")

failure_analysis = df.groupBy("Machine failure") \
    .agg(count("*").alias("Count")) \
    .orderBy("Machine failure")

failure_analysis.show()

# Failure by machine type
print("\n===== FAILURE BY MACHINE TYPE =====")

type_analysis = df.groupBy("Type", "Machine failure") \
    .agg(count("*").alias("Count")) \
    .orderBy("Type", "Machine failure")

type_analysis.show()

# Total failures
total_failures = df.filter(
    col("Machine failure") == 1
).count()

print("\nTotal Machine Failures:", total_failures)

print("\n===== PYSPARK ANALYSIS COMPLETED SUCCESSFULLY =====")

spark.stop()