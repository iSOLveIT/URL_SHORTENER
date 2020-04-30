from flask.views import MethodView
from flask import render_template, request, redirect, url_for
from .short import randomStringDigits, dbm
from pkg import mongo
from datetime import datetime as dt
from bson import ObjectId



# View for Index Route
class IndexEndpoint(MethodView):
    # This function executes when request method for this route = get
    def get(self):
        year = dt.now().strftime('%Y')
        return render_template('index.html', year=year), 200
    # This function executes when request method for this route = post
    def post(self):
        url_received = request.form['url_upload']

        add_on = randomStringDigits()
        req = dbm(url_received, add_on)
        generated_string = req

        url_shortened = 'https://iscissor.herokuapp.com/' + generated_string
        year = dt.now().strftime('%Y')
        return render_template('index.html', url_address=url_shortened, year=year)


# View for Redirect Route
class iShortEndpoint(MethodView):
    # This function executes when request method for this route = get
    def get(self, gen_id):
        query = mongo.db.url_address
        req = query.find_one({'url_generated':gen_id})
        if req is not None:
            url_address = req['url_address']
            visit = req['visits'] + 1
            oid = req['_id']
            query.update_one(
                {'_id': ObjectId(oid)},
                { '$set': { "visits": visit } }
            )
            return redirect(url_address, 302)
        
        year = dt.now().strftime('%Y')
        return render_template('error_page.html', year=year, error="URL")
    