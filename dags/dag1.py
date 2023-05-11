from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.postgres_operator import PostgresOperator
# def execution_time(**context):



with DAG(
    dag_id = "first_dag",
    schedule_interval = timedelta(minutes=1),
    start_date = datetime(2022 , 1,1)
    ) as dag:
   
   create_table = PostgresOperator(
      task_id = "create_table",
      postgres_conn_id='my_postgres_connection',
      sql = "create table if not exists records( dag_run_iteration serial primary key , execution_time timestamp)"
   )
   add_data_in_table = PostgresOperator(
      task_id = "add_current_time",
      postgres_conn_id = "my_postgres_connection",
      sql =  "insert into records values(default , '{}')".format(datetime.now())
   )
   
   select_from_table = PostgresOperator(
      task_id = "query_table",
      postgres_conn_id = "my_postgres_connection",
      sql = "select * from records"
   )


create_table>>add_data_in_table>>select_from_table
