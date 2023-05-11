from airflow import DAG
from datetime import datetime
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from airflow.operators.dummy_operator import DummyOperator


with DAG(dag_id = "third_dag",
        schedule_interval="@daily",
        start_date = datetime(2023,1,1),
        catchup = False
) as dag:
    
     my_task = DummyOperator(task_id  = "dummy_task",
            #    on_success_callback=lambda context: send_slack_notification.execute(context=context),
            #    on_failure_callback=lambda context: send_slack_notification.execute(context=context),
     )
     slack_notification_success = SlackWebhookOperator( task_id='slack_alert1',
        http_conn_id='slack_webhook',
        message='{{ dag.dag_id }} has completed successfully',
        username='Airflow',
        trigger_rule = "one_success"
        )
     slack_notification_failure = SlackWebhookOperator( task_id='slack_alert2',
        http_conn_id='slack_webhook',
        message='{{ dag.dag_id }} has failed ',
        username='Airflow',
        trigger_rule = "one_failed"
        )
     my_task>>[slack_notification_success,slack_notification_failure]
     