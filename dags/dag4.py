from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def push_value(ti):
    ti.xcom_push(key='qwerty',value=43)

def pull_value(**context):
    xcom_value = context['task_instance'].xcom_pull(task_ids='push_value', key='my_xcom_key')
    print('The pushed value is:', xcom_value)

dag = DAG(
    'xcom_example',
    description='Example DAG demonstrating the usage of XCom',
    start_date=datetime(2023, 5, 1),
    schedule_interval=None
)

push_task = PythonOperator(
    task_id='push_value',
    python_callable=push_value,
    dag=dag
)

pull_task = PythonOperator(
    task_id='pull_value',
    python_callable=pull_value,
    provide_context=True,  # Required to access the task context
    dag=dag
)

push_task >> pull_task  # Set the task dependency
