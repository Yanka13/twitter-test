# app/apis/tweets.py
# pylint: disable=missing-docstring

from flask_restx import Namespace, Resource, fields
from app import db
from app.models import Tweet
api = Namespace('tweets')


@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
class TweetResource(Resource):
    def get(self, id):
        tweet = db.session.query(Tweet).get(id)
        if tweet is None:
            api.abort(404)
        else:
            return tweet
