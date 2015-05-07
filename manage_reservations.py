import sqlite3


class ManageDatabase:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY
                name TEXT
                rating FLOAT
                    )
            """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS projections (
                id INTEGER PRIMARY KEY,
                movie_id INTEGER,
                type TEXT,
                date DATE,
                time TIME
                FOREIGN KEY(movie_id) REFERENCES movies(movie_id)
                    )
            """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGET PRIMARY KEY,
                username TEXT,
                projection_id INTEGER,
                row INTEGER,
                col INTEGER
                FOREIGN KEY(projection_id) REFERENCES projections(id)
                )
            """)

    def fill_tables(self):
        self.cursor.execute("""INSERT INTO movies(name, rating)
            VALUES('', )""")

