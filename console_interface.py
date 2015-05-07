class ConsoleInterface:
    def __init__(self):
        self.database = DataManager('cinema.db')
        self.commands = {
            "show_movies": self.show_movies,
            "show_movies_projections": self.show_movies_projections,
            "make_reservation": self.make_reservation,
            "finalize": self.finalize,
            "give_up": self.give_up,
            "cancel_reservation": self.cancel_reservation,
            "exit": self.exit,
            "help": self.help
        }
