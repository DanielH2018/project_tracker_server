# README
This a RESTful API for managing projects and their tasks.

## Bringing up API instructions(Linux)

1. Install `virutalenv`
    * `pip install virtualenv`
2. Clone the Repository 
    * `git clone ...` 
3. Create a virtual environment adjacent with the project repository.
    * `python3 -m venv venv`
4. Activate the virtual environment
    * `source venv/bin/activate`
5. Install the project requirements from the provided file.
    * `pip install -r requirements.txt`
6. Create Migrations
    * `python manage.py migrate`
7. Run the Server
    * `python manage.py runserver`

