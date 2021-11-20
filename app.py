from flask import Flask
app = Flask(__name__)
@app.route('/')
#def hello_world():
#    return 'Hello world'
def welcome():
    return 'Welcome to the surfshop&icecream '
