import datetime
from http import HTTPStatus

from flask import request
from flask_restful import Resource

from .serializers import InformationSchema


class InformationsView(Resource):
    def post(self):
        information_data, errors = InformationSchema().load(request.json)
        if errors:
            return errors

        information_data.created_at = datetime.datetime.utcnow()
        information_data.save()
        return InformationSchema().dump(information_data)
