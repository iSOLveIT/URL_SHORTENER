from flask import Flask
from flask_pymongo import PyMongo
import urllib


app = Flask(__name__)


# Config and Instantiate Mongo
Username = urllib.parse.quote_plus('isolveit')
Password = urllib.parse.quote_plus('laden1472')

app.config['MONGO_URI'] = "mongodb+srv://%s:%s@isolveit-jzamv.mongodb.net/url_shortener" % (Username, Password)
app.config['MONGO_DB'] = "url_shortener"

# connect to MongoDB with school_DB
mongo = PyMongo(app)

from pkg import routes