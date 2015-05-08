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
