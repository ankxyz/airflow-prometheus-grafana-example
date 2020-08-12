from airflow import DAG, settings
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.utils.trigger_rule import TriggerRule
from datetime import timedelta


def py_op_callback():
    print('Airflow::test_dag::py_op')


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    'test_dag',
    default_args=default_args,
    description='dvc_mlflow_airflow',
    schedule_interval=timedelta(days=1),
)

py_op = PythonOperator(
    task_id='py_op',
    dag=dag,
    python_callable=py_op_callback,
    provide_context=False,
    retries=0
)

py_op
