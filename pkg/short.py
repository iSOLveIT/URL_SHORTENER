import random
import string
from pkg import mongo
from datetime import datetime as dt

def randomStringDigits(stringLength=10):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    # Generating a Random String including letters and digits"

    short_url = ''.join(random.sample(lettersAndDigits, stringLength))
    query = mongo.db.url_address
    search = query.find_one({'url_generated':short_url})

    if search is not None:
        return randomStringDigits()
    return short_url


def dbm(url_received, generated_string):
    query = mongo.db.url_address
    datab = query.insert_one({'url_address':url_received, 'url_generated':generated_string,'visits':0, 'date_created':dt.now()})
    return generated_string
