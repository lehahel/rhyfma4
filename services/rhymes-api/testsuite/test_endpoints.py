import os
import tempfile

import pytest

import importlib

import src as rhymes_api


@pytest.fixture
def client():
    db_fd, rhymes_api.app.config['DATABASE'] = tempfile.mkstemp()
    rhymes_api.app.config['TESTING'] = True

    with rhymes_api.app.test_client() as client:
        with rhymes_api.app.app_context():
            rhymes_api.db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(rhymes_api.app.config['DATABASE'])


def test_endpoints(client):
    client.post('/api/rhymes?word=some_word&rhyme=some_board')
    response = client.get('/api/rhymes?word=some_word')
    assert response.json == {'word': 'some_word', 'rhyme': 'some_board'}
