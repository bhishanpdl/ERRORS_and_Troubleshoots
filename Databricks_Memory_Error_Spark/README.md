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

**Fix: use ds_silver.hse as spark dataframe and create pandas from filtering this**
- notebook: a01_create_hse_enr_parsed
```python
import pyspark.sql.functions as F

#===== Data
s_hse = spark.table('ds_silver.hse')
s_hse = s_hse.filter(s_hse['ActiveFlag'] == 1)
s_hse.limit(2).toPandas()

s_hse = s_hse.withColumn('CREATED_TIMESTAMP_ymd', F.col('CREATED_TIMESTAMP').substr(1, 10))
s_hse = s_hse.withColumn('CREATED_TIMESTAMP_ymd', F.to_date(F.col('CREATED_TIMESTAMP_ymd'), 'yyyy-MM-dd'))


ext_keys_anx = ['AnnexusBMSASOPatientID', 'AnnexusPatientID']
hse_enr_anx = s_hse.filter(F.col('EXTERNAL_KEY_NAME').isin(ext_keys_anx)).toPandas()

s_hse.groupBy('EXTERNAL_KEY_NAME').count().orderBy('count', ascending=False).show()
```

# Databricks autorun error
```
can not import yaml

solution: Add module dependencies in Schedule
For yaml, python module is: pyyaml
```
