import flask
import typing
import json
import datetime
from flask_sqlalchemy import SQLAlchemy

HOST = '127.0.0.1'
# HOST = '0.0.0.0'
PORT = 8083


app = flask.Flask("Rifma4e4naya")
app.config.from_object('src.config.Config')
db = SQLAlchemy(app)

class Rhyme(db.Model):
    __tablename__ = 'rhyme'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(128), nullable=False)
    rhyme = db.Column(db.String(128), nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, word, rhyme):
        self.word = word
        self.rhyme = rhyme
        self.updated_at = datetime.datetime.now()

@app.route('/api/rhymes', methods=['GET'])
def process_rhymes_get():
    word = flask.request.args.get('word', type=str)
    result = {'word': word, 'rhyme': 'huy' + word}
    return flask.Response(json.dumps(result), status=200, mimetype='application/json')


@app.route('/api/rhymes', methods=['POST'])
def process_rhymes_post():
    word = flask.request.args.get('word', type=str)
    rhyme = flask.request.args.get('rhyme', type=str)
    db.session.add(Rhyme(word=word, rhyme=rhyme))
    db.session.commit()
    return flask.Response(json.dumps({}), status=204, mimetype='application/json')