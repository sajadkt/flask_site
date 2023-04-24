#flaskenv
from flask import Flask
new=Flask(__name__)

# @new.route('/profile/<username>')
# def home(username):
#     return  '<h1>this  page is  for %s</h1>'% username
# new.run()

@new.route('/profile/<int:id>')
def home(id):
    return  '<h1>this  page is  for %d</h1>' % id
new.run(debug=True)
