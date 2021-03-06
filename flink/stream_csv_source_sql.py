from pyflink.table import EnvironmentSettings, TableEnvironment, DataTypes, Schema, TableDescriptor

t_env = TableEnvironment.create(EnvironmentSettings.in_streaming_mode())
t_env.get_config().get_configuration().set_string("parallelism.default", "1")

input_path = "./sample.csv"
source_ddl = f"""
    CREATE TABLE source (
        framework STRING,
        chapter INT
    ) WITH (
        'connector' = 'filesystem',
        'format' = 'csv',
        'path' = '{input_path}'
    )
"""

t_env.execute_sql(source_ddl)
src = t_env.from_path("source")
print(src.to_pandas())
# src.print_schema()