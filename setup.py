import subprocess


def user_input():
    """Prompt the user to flush and seed the database."""
    while True:
        response = input("Would you like to flush and seed the database? (y/n): ")
        if response.lower() == "y":
            return True
        elif response.lower() == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'")


# Install poetry dependencies
subprocess.run("poetry install", shell=True)

# Run migrations
subprocess.run("poetry run python manage.py migrate", shell=True)

# Optionally flush and seed database
if user_input():
    subprocess.run("poetry run python manage.py flush", shell=True)
    subprocess.run("poetry run python manage.py seed_employees", shell=True)
    subprocess.run("poetry run python manage.py seed_absence_requests", shell=True)

# Run server
subprocess.run("poetry run python manage.py runserver", shell=True)
