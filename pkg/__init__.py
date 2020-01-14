from flask import Flask
from flask_pymongo import PyMongo
import urllib


app = Flask(__name__)


# Config and Instantiate Mongo
Username = urllib.parse.quote_plus('username')
Password = urllib.parse.quote_plus('password')

app.config['MONGO_URI'] = "mongodb+srv://%s:%s@mongodb_uri" % (Username, Password)
app.config['MONGO_DB'] = "url_shortener"

# connect to MongoDB with school_DB
mongo = PyMongo(app)

from pkg import routes
