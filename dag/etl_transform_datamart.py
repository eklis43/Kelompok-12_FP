import json
from datetime import datetime
import pandas as pd
import numpy as np
import fastavro
from glob import glob
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator

# CONFIG
with open("/opt/airflow/dags/config.json", "r") as f:
    CONFIG = json.load(f)

# PYTHON FUNCTION
def _extract_to_bronze(**kwargs):
    table_name = kwargs['table_name']
    extension = kwargs['extension']

    # Initialize the PostgreSQL hook and SQLAlchemy engine
    hook = PostgresHook(postgres_conn_id="postgres_dw")
    engine = hook.get_sqlalchemy_engine()

    # Initialize an empty DataFrame
    df = pd.DataFrame()

    for filepath in glob(f"data/{table_name}*.{extension}"):
        if extension == "json":
            df_temp = pd.read_json(filepath)
        elif extension == "csv":
            df_temp = pd.read_csv(filepath)
        elif extension == "avro":
            with open(filepath, 'rb') as f:
                reader = fastavro.reader(f)
                records = [r for r in reader]
            df_temp = pd.DataFrame(records)
        elif extension == "parquet":
            df_temp = pd.read_parquet(filepath)
        elif extension == "xls":
            df_temp = pd.read_excel(filepath)

        df = pd.concat([df, df_temp])

    # Remove Unnamed: 0 columns if they exist
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    # Load to data warehouse
    df.to_sql(table_name, engine, index=False, schema="bronze", if_exists="replace")

# DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
}

# Define the DAG
dag = DAG(
    "etl_transform_datamart",
    default_args=default_args,
    schedule_interval="@once",
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

# TASK
extract_to_bronze_tasks = []
for config in CONFIG['ingestion']:
    extract_to_bronze = PythonOperator(
        task_id=f"extract_to_bronze{config['table_name']}",
        python_callable=_extract_to_bronze,
        op_kwargs={
            "table_name": config['table_name'],
            "extension": config['extension'],
        },
        dag=dag
    )

    extract_to_bronze_tasks.append(extract_to_bronze)

transform_bronze_to_silver_tasks = []
for config in CONFIG['transformation']:
    transform_bronze_to_silver = PostgresOperator(
        task_id=f"transform_bronze_to_silver{config['name']}",
        postgres_conn_id="postgres_dw",
        sql=config['filepath'],
        dag=dag,
    )

    transform_bronze_to_silver_tasks.append(transform_bronze_to_silver)


datamart_to_gold_tasks = []
for config in CONFIG['datamart']:
    datamart_to_gold = PostgresOperator(
        task_id=f"datamart_to_gold.{config['name']}",
        postgres_conn_id='postgres_dw',
        sql=config['filepath'],
        dag=dag,
    )
    
    datamart_to_gold_tasks.append(datamart_to_gold)

datamart1_to_gold_tasks = []
for config in CONFIG['datamart1']:
    datamart1_to_gold = PostgresOperator(
        task_id=f"datamart1_to_gold.{config['name']}",
        postgres_conn_id='postgres_dw',
        sql=config['filepath'],
        dag=dag,
    )
    
    datamart1_to_gold_tasks.append(datamart1_to_gold)

datamart2_to_gold_tasks = []
for config in CONFIG['datamart2']:
    datamart2_to_gold = PostgresOperator(
        task_id=f"datamart2_to_gold.{config['name']}",
        postgres_conn_id='postgres_dw',
        sql=config['filepath'],
        dag=dag,
    )
    
    datamart2_to_gold_tasks.append(datamart2_to_gold)

datamart3_to_gold_tasks = []
for config in CONFIG['datamart3']:
    datamart3_to_gold = PostgresOperator(
        task_id=f"datamart3_to_gold.{config['name']}",
        postgres_conn_id='postgres_dw',
        sql=config['filepath'],
        dag=dag,
    )
    
    datamart3_to_gold_tasks.append(datamart3_to_gold)

datamart4_to_gold_tasks = []
for config in CONFIG['datamart4']:
    datamart4_to_gold = PostgresOperator(
        task_id=f"datamart4_to_gold.{config['name']}",
        postgres_conn_id='postgres_dw',
        sql=config['filepath'],
        dag=dag,
    )
    
    datamart4_to_gold_tasks.append(datamart4_to_gold)

# CONTROL FLOW
transform_to = DummyOperator(task_id="transform_to", dag=dag)
datamart_to = DummyOperator(task_id="datamart_to", dag=dag)
datamart1_to = DummyOperator(task_id="datamart1_to", dag=dag)
datamart2_to = DummyOperator(task_id="datamart2_to", dag=dag)
datamart3_to = DummyOperator(task_id="datamart3_to", dag=dag)
datamart4_to = DummyOperator(task_id="datamart4_to", dag=dag)

extract_to_bronze_tasks >> transform_to >> transform_bronze_to_silver_tasks >> datamart_to >> datamart_to_gold_tasks >> datamart1_to >> datamart1_to_gold_tasks >> datamart2_to >> datamart2_to_gold_tasks>> datamart3_to >> datamart3_to_gold_tasks >> datamart4_to >> datamart4_to_gold_tasks
