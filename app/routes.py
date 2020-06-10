from app import app, db
from flask import request, jsonify

from app.models import User


# default api
@app.route('/')
def hello_world():
    return 'hello'


# api to add object in the database
@app.route('/add', methods=['POST'])
def adding_object():
    info = request.get_json()
    name = info['name']
    email = info['email']
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return "object added to database"


# api to get all objects from the database
@app.route('/get', methods=['GET'])
def getting_object():
    users = User.query.all()
    user_list = []
    for user in users:
        user_list.append({
            'name': user.name,
            'email': user.email
        })
    return jsonify(user_list)
