import os

from py_dotenv import read_dotenv


read_dotenv('.env')

DB_HOST = os.getenv('DB_HOST')
# DB_PORT = os.getenv('DP_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
