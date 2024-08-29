import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def process_data(engine):
    conn = engine.connect()

    data = pd.read_sql('SELECT AGE FROM test_table WHERE LENGTH(NAME) < 6',conn)

    means = data.mean()
    max1 = data.max()
    min1 = data.min()
    return means + "max " + max1 + "min " + min1

if __name__ == "__main__":
    db_user = 'postgres'
    db_password = 'password'
    db_host = 'db'
    db_port = '5432'
    db_name = 'test_db'

    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    result = process_data(engine)

    print("Среднее значение,min,max в столбике возраст")
    print(result)
