import psycopg2

class PostgresConnection:
    _conn = None

    @classmethod
    def connect(cls):
        if cls._conn:
            return cls._conn
        cls._conn = psycopg2.connect(
            dbname='Commodity',
            user='postgres',
            password='****',
            host='localhost',
            port='5432')
        cls._conn.autocommit = True
        return cls._conn

    @classmethod
    def get_cursor(cls):
        cursor = cls.connect().cursor()
        return cursor

    @classmethod
    def create_table(cls, table_name:str, *columns):
        try:
            columns_str = ",".join(columns)
            with cls.get_cursor() as cursor:
                cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str});")
                print(f"table {table_name} created successfully.")
        except Exception as e:
            print(f"Error create table{table_name}: {e}")

    @classmethod
    def insert(cls, table_name: str, columns: list, data: list):
        try:
            columns_str = ",".join(columns)
            values_str = ",".join(["%s"] * len(columns))
            with cls.get_cursor() as cursor:
                cursor.executemany(f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})", data)
                print(f"inserting into {table_name} completed successfully.")
        except Exception as e:
            print(f"Error inserting into {table_name}: {e}")

    @classmethod
    def update(cls, table_name:str, id_colum:str, id_value:int, **columns):
        try:
            columns_str = ",".join([f"{key} = %s" for key in columns.keys()])
            values_str = list(columns.values()) + [id_value]
            with cls.get_cursor() as cursor:
                cursor.execute(f"UPDATE {table_name} SET {columns_str} WHERE {id_colum} = %s;", values_str)
                print(f"Update {table_name} completed successfully.")
        except Exception as e:
            print(f"Error Update {table_name}: {e}")


    @classmethod
    def delete(cls, table_name:str, id_colum:str, id_value:int,):
        try:
            values_str = [id_value]
            with cls.get_cursor() as cursor:
                cursor.execute(f"DELETE FROM {table_name} WHERE {id_colum} = %s;", values_str)
                print(f"Delete {table_name} completed successfully.")
        except Exception as e:
            print(f"Error Delete {table_name}: {e}")

    @classmethod
    def select_all(cls, table_name: str) -> object:
        try:
            with cls.get_cursor() as cursor:
                cursor.execute(f"SELECT * FROM {table_name};")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
        except Exception as e:
            print(f"Error fetch all {table_name}: {e}")


    @classmethod
    def select(cls, query:str) -> object:
        try:
            with cls.get_cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("No rows found!")
        except Exception as e:
            print(f"Error fetch : {e}")
