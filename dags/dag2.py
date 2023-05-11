from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
from airflow.operators.email_operator import EmailOperator
with DAG(dag_id = "second_dag",
         start_date = datetime(2022,1,1),
         catchup = False,
         schedule_interval = "@daily"
)   as dag:
        dummy_task = DummyOperator(task_id = "dummy_task")

        send_notification = EmailOperator(task_id = "send_notificatons",
                                           conn_id = "email_notifier",
                                           to = ["akash.s@sigmoidanalytics.com"],
                                           subject= "Airflow_notification",
                                           html_content = '<h1>The dag with id second_dag is executed successfully</h1>'
        )

        dummy_task>>send_notification
    
