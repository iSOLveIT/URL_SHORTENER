from .views import IndexEndpoint, iShortEndpoint
from pkg import app
from flask import render_template
from datetime import datetime as dt

# Route for index
app.add_url_rule("/ishort", view_func=IndexEndpoint.as_view("index"))

# Route for Redirect
app.add_url_rule("/<gen_id>", view_func=iShortEndpoint.as_view("url_redirect"))

# Route for ErrorHandling
@app.errorhandler(404)
def url_not_found(e):
    year = dt.now().strftime('%Y')
    return render_template('error_page.html', year=year,error="Page")




