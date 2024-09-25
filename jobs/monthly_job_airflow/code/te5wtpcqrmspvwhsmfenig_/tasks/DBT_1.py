from te5wtpcqrmspvwhsmfenig_.utils import *

def DBT_1():
    from airflow.operators.python import PythonOperator
    from datetime import timedelta
    import os
    import zipfile
    import tempfile

    return PythonOperator(
        task_id = "DBT_1",
        python_callable = invoke_dbt_runner,
        op_kwargs = {
          "is_adhoc_run_from_same_project": False,
          "is_prophecy_managed": False,
          "run_deps": False,
          "run_seeds": False,
          "run_parents": False,
          "run_children": False,
          "run_tests": True,
          "run_mode": "project",
          "entity_kind": None,
          "entity_name": None,
          "project_id": None,
          "git_entity": "branch",
          "git_entity_value": None,
          "git_ssh_url": "",
          "git_sub_path": "",
          "select": "",
          "threads": "",
          "exclude": "",
          "run_props": "",
          "envs": {"DBT_DATABRICKS_INVOCATION_ENV" : "prophecy"}
        },
    )
