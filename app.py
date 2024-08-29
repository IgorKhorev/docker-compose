import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def process_data(engine):
    conn = engine.connect()

    data = pd.read_sql('SELECT AGE FROM test_table WHERE LENGTH(NAME) < 6',conn)

     # Вычисляем среднее, максимум и минимум значений по столбцу
        means = data.mean()
        max1 = data.max()
        min1 = data.min()
        
        # Объединяем результаты в один DataFrame
        summary = pd.DataFrame({
            "Mean": means,
            "Max": max1,
            "Min": min1
        })
    
    return summary

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
