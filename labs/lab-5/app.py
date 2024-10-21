"""app.py: render and route to webpages"""
from flask import render_template

from db.server import app

# create a webpage based off of the html in templates/index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/blackpage')
def blackpage():
    return render_template("blackpage.html")
@app.route('/whitepage')
def whitepage():
    return render_template("whitepage.html")
@app.route('/webpage')
def webpage():
    return render_template("webpage.html")

if __name__ == "__main__":
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)

