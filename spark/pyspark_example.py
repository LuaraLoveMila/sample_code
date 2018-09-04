
def read_write_parquet(sc):
    """
    :param sc: SparkSession, The entry point to programming Spark with the Dataset and DataFrame API.
    """
    df = sc.read.parquet('s3://bucket/test/part.snappy.parquet')
    # mode: append, overwrite, ignore, error (default)
    df.write.parquet('s3://bucket/test/', mode='overwrite')


def read_write_csv(sc):
    df = sc.read.csv('s3://bucket/test/part.csv')
    df.write.csv('s3://bucket/test/')


def create_dataframe_from_list(sc, lst):
    _lst = map(lambda x: (x, ), lst)
    df = sc.createDataFrame(_lst)