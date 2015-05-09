from commands import Commands


import sys


class ConsoleInterface:

    OCCUPIED_PLACE = 'X'

    def __init__(self):

        self.database = Commands('cinema.db')
        self.commands = {
            "show_movies": self.show_movies,
            "show_movie_projections": self.show_movie_projections,
            "grid": self.print_grid,
            "make_reservation": self.make_reservation,
            "finalize": self.finalize,
            "give_up": self.give_up,
            # "cancel_reservation": self.cancel_reservation,
            "exit": self.exit,
            "help": self.help
        }
        self.tuple_list = []

    def read_command(self):
        user_input = input('>')
        arguments = user_input.split(" ")[1:]
        function = ''.join(user_input.split(" ")[0:1])
        self.commands[function](*arguments)

    def show_movies(self):
        movies = self.database.show_movies()
        print('Current movies:')
        for movie in movies:
            print(
                '[{}] - {} ({})'.format(movie['movie_id'], movie['name'], movie['rating']))

    def show_movie_projections(self, movie_id, reservation=False):
        projections = self.database.show_movie_projections(movie_id)
        label = True
        for projection in projections:
            if label:
                print('Projections for {}:'.format(projection['name']))
                label = False
            if reservation is True:
                print('[{}] - {} {} ({}) - {} spots available'.format(projection['projection_id'], projection[
                      'date_projection'], projection['time'], projection['type'], 100 - projection['seats']))
            else:
                print('[{}] - {} {} ({})'.format(projection['projection_id'],
                                                 projection['date_projection'], projection['time'], projection['type']))

    def make_reservation(self):

        name = input('Step 1 (User): Choose name>')
        tickets = input('Step 1 (User): Choose number of tickets>')

        self.show_movies()

        movie_id = input('Step 2 (Movie): Choose a movie>')

        self.show_movie_projections(movie_id, reservation=True)

        projection_id = input('Step 3 (Projection): Choose a projection>')

        print('Available seats (marked with a dot):')

        self.print_grid(projection_id)
        self.manage_tickets(tickets, projection_id)
        self.print_reservation_info(movie_id, projection_id, self.tuple_list)

        command = input('Step 5 (Confirm - type "finalize") >')
        if command == 'finalize':
            self.finalize(name, projection_id, self.tuple_list)

    def manage_tickets(self, tickets, projection_id):
        grid = self.database.available_seats(projection_id)
        step = 1

        while (step - 1) != int(tickets):
            user_input = input('Step 4 (Seats): Choose seat {}>'.format(step))
            seat = eval(user_input)
            row = seat[0]
            col = seat[1]
            if row > 10 or col > 10 or row == 0 or col == 0:
                print('Lol...NO!')
            elif grid[row][col] == self.OCCUPIED_PLACE:
                print('This seat is already taken!')
            else:
                self.tuple_list.append((row, col))
                step += 1
        print(self.tuple_list)

    def print_reservation_info(self, movie_id, projection_id, tuple_list):
        movie_name = self.database.show_movie_name(movie_id)
        proj = self.database.show_movie_projection_info(projection_id)
        print('This is your reservation:')
        print('Movie: {} ({})'.format(
            movie_name['name'], movie_name['rating']))
        print('Date and Time: {} {} ({})'.format(
            proj['date_projection'], proj['time'], proj['type']))
        print('Seats: {}'.format(tuple_list))

    def finalize(self, name, projection_id, tuples):
        self.database.finalize(name, projection_id, tuples)
        print('Thanks.')

    def print_grid(self, projection_id):
        a = self.database.available_seats(projection_id)
        for i in a:
            print(' '.join(i))

    def give_up(self):
        print('GAVE UP!')

    def help(self):
        RED = '\033[91m'
        NORMAL = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        spells = ['show_movies',
                  'show_movie_projections <movie_id>',
                  'make reservation',
                  'finalize (CAUTION!You cast it only on 3d step)',
                  'give_up (CAUTION!You cast it only on 3d step)',
                  'help',
                  'exit']
        print(BOLD + UNDERLINE + RED + 'A list of spells to use:' + NORMAL)
        for spell in range(1, len(spells)):
            print('\t{}.{}'.format(spell, spells[spell-1]))

    def exit(self):
        sys.exit(0)
