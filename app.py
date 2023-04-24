from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return  '<h1>helloooooo </h1>'
app.run()
@app.route('/new')
def new():
    return '<h1> it is new page'
app.run()