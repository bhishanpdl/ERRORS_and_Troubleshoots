# Memory Error
```python
#===== Data
# hse = spark.read.load('/mnt/databricksprod1/silver/hse/').toPandas()
hse = spark.table('ds_silver.hse').toPandas()
hse = hse.loc[lambda x: x['ActiveFlag']==1]
print(hse.shape)
```
```
org.apache.spark.SparkException: Exception thrown in awaitResult: Job aborted due to stage failure:
Total size of serialized results of 53 tasks (13.9 GiB)
is bigger than local result size limit 13.7 GiB, to address it,
set spark.driver.maxResultSize bigger than your dataset result size.
```
