""" data access module
"""
import sqlite3
from typing import Dict


class Dao:
    """Dao data access class"""

    _con = sqlite3.connect(":memory:")
    _table_columns = {"secret_santa_pairs" : "match_year, gift_giver, gift_receiver"}

    def __init__(self):
        """__init__ constructor
        """
        pass

    @classmethod
    def store_to_db(cls, table_name, val):
        """create a database connection to SQLite database"""
        with cls._con:
            cls._con.execute(
                f"""CREATE TABLE IF NOT EXISTS
                {table_name}({cls._table_columns.get(table_name)})"""
            )
            print(table_name,val)
            cls._con.executemany(
                f"INSERT INTO {table_name} VALUES(?, ?, ?)",
                    list(val),
            )


    @classmethod
    def read_gifts_from_db(cls, year):
        """create a database connection to a SQLite database"""
        with cls._con:
            res = cls._con.execute(
                """SELECT count(name) FROM sqlite_master
                WHERE type='table' AND name='secret_santa_pairs'"""
            )
            if res.fetchone()[0] == 1:
                res = cls._con.execute(
                    f"""SELECT gift_giver, gift_receiver
                    FROM secret_santa_pairs WHERE match_year > {year-3}"""
                )
                print("showing results from db")
                result = res.fetchall()
                print(result)
                return result
            return ()


if __name__ == "__main__":
    pass
