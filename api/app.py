# coding: utf-8

import os
from flask import Flask, abort
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

class AlmanaxResource(Resource):
    def get(self):
        f = open('data/almanax.json')
        almanax = json.load(f)
        f.close()
        return almanax

class AlmanaxDateResource(Resource):
    def get(self, date):
        f = open('data/almanax.json')
        almanax = json.load(f)
        f.close()

        if almanax.get(date) == None:
            abort(404)
        return almanax.get(date)

api.add_resource(AlmanaxResource, '/almanax/')
api.add_resource(AlmanaxDateResource, '/almanax/<string:date>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'), debug=True)