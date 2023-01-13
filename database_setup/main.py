import psycopg2
import io
from sqlalchemy import create_engine
import pandas as pd

hostname = 'postgres.clsw1arwkc7a.eu-central-1.rds.amazonaws.com'
username = 'postgres'
password = 'database'
database = 'postgres'

df = pd.read_excel(r'product catalogue.xlsx')
cols = ",".join([str(i) for i in df.columns.tolist()])

#https://morioh.com/p/80d864fb55c7
if __name__ == '__main__':
        # connection = psy.connect(host=hostname, user=username, password = password, dbname = database)
        # cursor = connection.cursor()
        #
        # for i, row in data.iterrows():
        #         sql = "INSERT INTO products (" +cols + ") VALUES (" + "%s,"*(len(row)-1) + "%s)"
        #         cursor.execute(sql, tuple(row))
        # connection.commit()
        # connection.close()
        #engine = create_engine('postgresql+psycopg2://postgres:database@postgres.clsw1arwkc7a.eu-central-1.rds.amazonaws.com:5432/postgres')
        #df.head(0).to_sql('products', engine, if_exists='replace',index=False) #drops old table and creates new empty table
        #conn = engine.raw_connection()
        # cur = conn.cursor()
        # output = io.StringIO()
        # df.to_csv(output, sep='\t', header=False, index=False)
        # output.seek(0)
        # contents = output.getvalue()
        # cur.copy_from(output, 'products', null="")  # null values become ''
        # conn.commit()
        conn_string = 'postgresql+psycopg2://postgres:database@postgres.clsw1arwkc7a.eu-central-1.rds.amazonaws.com:5432/postgres'
        db = create_engine('postgresql+psycopg2://postgres:database@postgres.clsw1arwkc7a.eu-central-1.rds.amazonaws.com:5432/postgres')
        conn = db.connect()
        df.to_sql('products', con =conn, if_exists='replace', index=False)
        # conn = psycopg2.connect(conn_string)
        # conn.autocommit = True
        # cursor = conn.cursor()





