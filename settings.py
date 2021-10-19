import os
import environ


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()

env.read_env(os.path.join(BASE_DIR, '.env'))

DATABASE = dict(
    DB_USER = env('DB_USER'),
    DB_PASSWORD = env('DB_PASSWORD'),
    DB_NAME = env('DB_NAME'),
    DB_HOST = env('DB_HOST'),
    DB_PORT = env('DB_PORT'),
)
