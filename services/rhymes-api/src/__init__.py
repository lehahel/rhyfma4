import flask
import typing
import json
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect


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

    # def serialize(self):
    #     d = Serializer.serialize(self)
    #     return d

@app.route('/api/rhymes', methods=['GET'])
def process_rhymes_get():
    word = flask.request.args.get('word', type=str)
    rhyme = db.session.execute(db.select(Rhyme.rhyme).order_by(Rhyme.updated_at.desc()).limit(1))
    result = rhyme.all()
    if len(result) == 0:
        return flask.Response(
            json.dumps({'code': 404, 'message': 'rhyme not found'}),
            status=404,
            mimetype='application/json',
        )
    result = {'word': word, 'rhyme': str(result[0].rhyme)}
    return flask.Response(json.dumps(result), status=200, mimetype='application/json')


@app.route('/api/rhymes', methods=['POST'])
def process_rhymes_post():
    word = flask.request.args.get('word', type=str)
    rhyme = flask.request.args.get('rhyme', type=str)
    db.session.add(Rhyme(word=word, rhyme=rhyme))
    db.session.commit()
    return flask.Response(json.dumps({}), status=204, mimetype='application/json')


@app.route('/static/<path:filename>')
def process_frontend(filename):
    return flask.send_from_directory(app.config["STATIC_FOLDER"], filename)
