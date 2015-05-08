from console_interface import ConsoleInterface


def main():
    db = ConsoleInterface()
    while True:
        db.read_command()

if __name__ == '__main__':
    main()
