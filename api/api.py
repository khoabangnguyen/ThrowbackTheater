import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from extractFromCsv import getGeneralList


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/recommender?charset=utf8'

app.config['SQLALCHEMY_BINDS'] = {'users': 'mysql://root:root@localhost/users?charset=utf8'}
db = SQLAlchemy(app)
CORS(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    poster = db.Column(db.String(80), nullable=False)
    overview = db.Column(db.Text(), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    duration = db.Column(db.Integer)
    genres = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float(precision=1))

    def __repr__(self):
        return f'{self.title}'

class User(db.Model):
    __bind_key__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.title}'

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/classics', methods=['GET'])
def classics():
    return jsonify(getGeneralList(40))

@app.route('/classicsTest', methods=['GET'])
def classicsTest():
    a = getGeneralList(5)
    a['movies'] = a['movies'][::-1]
    return jsonify(a)

@app.route('/createuser', methods=['GET', 'POST'])
def uploadUser():
    if request.method == 'POST':
        try:
            username = request.json['username']
            password = request.json['password']

            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()

            return jsonify({"info": "SUCCESS"})

        except Exception:
            return jsonify({"info": "FAILED"})

    return ""

@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    user = User.query.filter_by(username=username).first()
    if user: 
        if password == user.password: 
            res = "VALID"
        else:
            res = "INVALID_PASSWORD"
    else:
        res = "INVALID_USERNAME"

    return jsonify({"login": res})


@app.route('/usernames', methods=['GET'])
def getUsernames():
    users = User.query.all()
    usernames = [user.username for user in users]
    return jsonify({"usernames": usernames})

@app.route('/getMovies', methods=['GET'])
def getMovies():
    username = request.args.get('username')

    if username == "test":
        return jsonify(getGeneralList(5))
        
    return jsonify(getGeneralList(20))


if __name__ == '__main__':
    app.run()
