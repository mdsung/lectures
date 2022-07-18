import os
from dotenv import load_dotenv
import pandas as pd
import pymysql

load_dotenv(verbose=True)

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))
MYSQL_DB = os.getenv("MYSQL_DB")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_CHARSET = os.getenv("MYSQL_CHARSET")


class Database:
    def __init__(
        self,
        host: str = MYSQL_HOST,
        port: int = MYSQL_PORT,
        db: str = MYSQL_DB,
        user: str = MYSQL_USER,
        passwd: str = MYSQL_PASSWORD,
        charset: str = MYSQL_CHARSET,
    ):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.conn = pymysql.connect(
            host=host,
            port=port,
            db=db,
            user=user,
            passwd=passwd,
            charset=charset,
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.cur = self.conn.cursor()

    def execute_sql_(self, sql: str) -> dict:
        self.cur.execute(sql)
        return self.cur.fetchall()

    def table_to_pandas(self, table_name: str) -> pd.DataFrame:
        self.cur.execute(f"SELECT * FROM {table_name}")
        return pd.DataFrame(self.cur.fetchall())


def save_to_pickle(df: pd.DataFrame, table_name: str):
    import pickle

    with open(f"data/raw/{table_name}.pkl", "wb") as f:
        pickle.dump(df, f)


def save_to_csv(df: pd.DataFrame, table_name: str):
    df.to_csv(f"data/raw/{table_name}.csv", index=False)


def parse_table_and_save(table_name: str):
    database = Database()
    df = database.table_to_pandas(table_name)
    save_to_pickle(df, table_name)
    save_to_csv(df, table_name)
    database.conn.close()


if __name__ == "__main__":
    database = Database()
    table_names = ["apacheApsVar", "apachePatientResult", "apachePredVar"]

    import concurrent.futures

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(parse_table_and_save, table_names)
