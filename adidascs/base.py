from pyspark.sql import SparkSession
from .settings import APP_NAME

spark = SparkSession.builder.appName(APP_NAME).getOrCreate()