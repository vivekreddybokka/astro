# my_dag.py
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from my_module.dagfactory import dagfactory

dag_factory = dagfactory(config_file="conf/config.yml")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': dag_factory.start_date,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': dag_factory.default_retry_delay
}

dag = DAG(dag_id='my_dag_id', default_args=default_args, schedule_interval=dag_factory.schedule_interval)

# Define tasks using the config file
for task in dag_factory.tasks:
    task = PythonOperator(
        task_id=task['task_id'],
        python_callable=task['python_callable'],
        op_args=task.get('op_args', []),
        dag=dag,
    )
