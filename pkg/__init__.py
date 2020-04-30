from flask import Flask
from flask_pymongo import PyMongo
import urllib


app = Flask(__name__)


# Config and Instantiate Mongo
Username = urllib.parse.quote_plus('USERNAME')
Password = urllib.parse.quote_plus('PASSWORD')

app.config['MONGO_URI'] = "mongodb+srv://%s:%s@example.mongodb.net/DB_NAME" % (Username, Password)
# Name of Database to connect to
app.config['MONGO_DB'] = "DB_NAME"

# connect to MongoDB with school_DB
mongo = PyMongo(app)

from pkg import routes
