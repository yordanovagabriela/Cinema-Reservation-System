from commands import Commands


import sys


class ConsoleInterface:
    def __init__(self):
        self.database = Commands('cinema.db')
        self.commands = {
            "show_movies": self.show_movies,
            "show_movie_projections": self.show_movie_projections,
            "grid": self.grid,
            "make_reservation": self.make_reservation,
            # "finalize": self.finalize,
            # "give_up": self.give_up,
            # "cancel_reservation": self.cancel_reservation,
            "exit": self.exit
            # "help": self.help
        }

    def read_command(self):
        user_input = input('>')
        self.commands[user_input]()

    def show_movies(self):
        movies = self.database.show_movies()
        print('Current movies:')
        for movie in movies:
            print('[{}] - {} ({})'.format(movie['movie_id'], movie['name'], movie['rating']))

    def show_movie_projections(self, reservation=False):
        movie_id = input('Choose a movie>')
        projections = self.database.show_movie_projections(movie_id)
        label = True
        for projection in projections:
            if label:
                print('Projections for {}:'.format(projection['name']))
                label = False
            if reservation is True:
                print('[{}] - {} {} ({}) - {} spots available'.format(projection['projection_id'], projection['date_projection'],projection['time'], projection['type'], 100 - projection['seats']))
            else:
                print('[{}] - {} {} ({})'.format(projection['projection_id'], projection['date_projection'],projection['time'], projection['type']))

    def make_reservation(self):

# Step 1:
        name = input('Step 1 (User): Choose name>')
        tickets = input('Step 1 (User): Choose number of tickets>')
        self.show_movies()

# Step 2:
        self.show_movie_projections(reservation=True)

# Step 3:
        projection_id = input('Step 3 (Projection): Choose a projection>')
        print('Available seats (marked with a dot):')
        self.grid(projection_id)

# Step 4:
        tuple_list = []
        for i in range(1, 1 + int(tickets)):
            seats = input('Step 4 (Seats): Choose seat {}>'.format(i))
            tuple_list.append((seats[0], seats[1]))

    def grid(self, projection_id):
        a = self.database.available_seats(projection_id)
        for i in a:
            print(' '.join(i))

    def exit(self):
        sys.exit(0)
