from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.models import Variable

import jovem_nerd

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 10, 26),
}

dag = DAG(
    "jovem_nerd_dag",
    default_args=default_args,
    description="DAG que criar um dataset com todos os episódios dos podcasts do jovem nerd",
    schedule_interval=None,
)


get_jovem_nerd_operator = PythonOperator(
    task_id="get_jovem_nerd_data",
    python_callable=jovem_nerd.main,
    dag=dag,
)

send_datatase_kaggle = BashOperator(
    task_id="send_datatase_kaggle",
    bash_command="kaggle datasets version -p /home/var/data/ -m 'Automatic Update via Airflow'",
    dag=dag,
)


get_jovem_nerd_operator >> send_datatase_kaggle
