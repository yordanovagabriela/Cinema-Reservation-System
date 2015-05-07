import sqlite3


class DataManager:

    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def show_movies(self):
        return self.cursor.execute('SELECT * FROM movies ORDER BY rating')

    def show_movie_projections(self, movie_id, date=''):
        if self.date != '':
            return self.cursor.execute('SELECT movie_id FROM projections ORDER BY date_projection')
        return self.cursor.execute('SELECT movie_id FROM projections ORDER BY time')

