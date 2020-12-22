import configparser
from dynamodb_helper import UserTable
import os

def get_user_table():
    config = configparser.ConfigParser()
    # config.read('../config.ini')
    config.read(os.environ['LAMBDA_TASK_ROOT'] + '/config.ini')  # TODO: fix this; I don't like it!

    return UserTable(
        region=config['dynamodb']['region'],
        table_name=config['dynamodb']['table']
    )