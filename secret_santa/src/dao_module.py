""" data access module
"""
import sqlite3


class Dao:
    """Dao data access class"""

    _con = sqlite3.connect(":memory:")
    _table_columns = {
        "secret_santa_pairs": "match_year, gift_giver, gift_receiver",
        "secret_santa_immediate_family": "family_year, member1, member2",
    }

    def __init__(self):
        """__init__ constructor"""

    @classmethod
    def store_to_db(cls, table_name, val):
        """write to database"""
        with cls._con:
            cls._con.execute(
                f"""CREATE TABLE IF NOT EXISTS
                {table_name}({cls._table_columns.get(table_name)})"""
            )
            cls._con.executemany(
                f"INSERT INTO {table_name} VALUES(?, ?, ?)",
                list(val),
            )
        return True

    @classmethod
    def read_gifts_from_db(cls, year):
        """reads past match info from db
        :todo: create generic reader for read dbs"""
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
                result = res.fetchall()
                return result
            return ()

    @classmethod
    def read_family_from_db(
        cls,
    ):
        """Reads family details from in memory db
        :todo: create generic reader for read dbs"""
        with cls._con:
            res = cls._con.execute(
                """SELECT count(name) FROM sqlite_master
                WHERE type='table' AND name='secret_santa_immediate_family'"""
            )
            if res.fetchone()[0] == 1:
                res = cls._con.execute(
                    """SELECT member1, member2
                    FROM secret_santa_immediate_family"""
                )
                result = res.fetchall()
                return result
            return ()


if __name__ == "__main__":
    pass
