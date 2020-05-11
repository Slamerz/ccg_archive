# Collectible Card Game Archive

An open source project to preserve and maintain aging Collectible card games.

For testing feel free to spin up a postgresql server using the provided docker compose.


### Requirements
Python 3\
Docker

#### How to run

Edit the `template.env` file and rename it `.env`


`pipenv install`\
`pipenv shell`\
`docker-compose up`\
`python manage.py makemigrations`\
`python manage.py migrate`\
`python manage.py runserver`