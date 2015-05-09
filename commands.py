import sqlite3


class Commands:

    OCCUPIED_SEAT = 'X'

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def show_movies(self):
        return self.cursor.execute("""SELECT movie_id, name, rating FROM movies
            ORDER BY rating""")

    def show_movie_name(self, movie_id):
        movie_name = self.cursor.execute("""SELECT name, rating FROM movies
            WHERE movie_id = ?""", (movie_id,))
        result = movie_name.fetchone()
        return result

    def show_movie_projection_info(self, projection_id):
        projection_info = self.cursor.execute("""SELECT date_projection, time, type
            FROM projections WHERE projection_id = ?""", (projection_id,))
        result = projection_info.fetchone()
        return result


    def show_movie_projections(self, movie_id):
        return self.cursor.execute("""SELECT
            reserved_seats.seats,movies.name, projections.projection_id, projections.date_projection,
            projections.type,
            projections.time FROM reserved_seats, projections
            JOIN movies ON projections.movie_id = ?  and projections.movie_id = movies.movie_id
        and projections.projection_id = reserved_seats.projection_id
            ORDER BY projections.date_projection""", (movie_id,))

    def available_seats(self, projection_id):
        rc = self.cursor.execute("""SELECT
            reservations.row, reservations.col FROM reservations
            WHERE reservations.projection_id = ?""", (projection_id,))
        grid = [
            [' ', ' 1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
            ['1 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['2 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['3 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['4 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['5 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['6 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['7 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['8 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['9 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['10', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ]

        for el in rc:
            grid[el['row']][el['col']] = self.OCCUPIED_SEAT

        return grid

    def finalize(self, name, projection_id, tuples):
        for n in range(len(tuples)):
            seat = tuples[n]
            self.cursor.execute('''INSERT INTO reservations (username, projection_id, row, col)
                VALUES (?, ?, ?, ?) ''',(name, projection_id, seat[0], seat[1]))
            self.cursor.execute('''UPDATE reserved_seats SET seats = seats + 1
                WHERE projection_id = ?''', (projection_id))
        self.connection.commit()
