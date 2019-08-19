import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'],
    dbname=os.environ['DBNAME']
)

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# initialize the database connection
db = SQLAlchemy(app)


@app.route('/')
def view_registered_weathers():
    from models import Weather
    weathers = Weather.query.all()
    return render_template('weather.html', weathers=weathers)

if __name__ == '__main__':
    app.run()

