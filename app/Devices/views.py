from http import HTTPStatus

from flask import request
from flask_restful import Resource

from .serializers import DeviceSchema


class DevicesView(Resource):
    """
    Allows the creations of devices.
    """
    def post(self):
        """
        Post method.
        ---
        parameters:
          - name: Authorization
            in: Header
            description: Basic(rpi_status:app_key).
            required: True
          - name: body
            in: body
            schema:
              mac_address:
                type: string
                description: Device mac address.
        responses:
           201:
             description: (Json) Device password.
        """
        device_data, errors = DeviceSchema().load(request.json)
        if errors:
            return errors
        # Generate password and hash it.
        device_data.random_password()
        device_password = device_data.password
        device_data.hash_password()
        device_data.save()

        return {'password': device_password},  HTTPStatus.CREATED
