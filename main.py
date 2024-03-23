from flask import Flask, render_template
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home_page():
    return render_template("home.html")
@app.route('/<string:name>')
def home2(name):
    return render_template('home.html', name=name)