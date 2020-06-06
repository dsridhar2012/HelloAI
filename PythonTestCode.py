import findspark
findspark.init()

import pyspark
sc = pyspark.SparkContext(appName="my")

df = pyspark.range(500).toDF("number")
df.select(df["number"] + 10)