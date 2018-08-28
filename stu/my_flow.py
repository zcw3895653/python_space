#coding=utf-8
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from datetime import datetime,timedelta

default_arg={
    'owner':'airflow',
    'depends_on_past':False,

}