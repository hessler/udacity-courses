"""Module to kick off database setup for Restaurant project."""


def main():
    """Main function to run when module is called."""
    import database_setup
    database_setup.create_data()


if __name__ == '__main__':
    main()
