from pkg import app
import os

app.config['SECRET_KEY'] = 'something_secret'

if __name__ == '__main__':
    app.run()
