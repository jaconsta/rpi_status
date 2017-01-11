from marshmallow_mongoengine import ModelSchema

from .models import Device


class DeviceSchema(ModelSchema):
    """
    Device schema abstraction.
    """
    class Meta:
        model = Device
        fields = ('mac_address', )
        # model_fields_kwargs = {'password': {'load_only': True}}


class AuthSchema(ModelSchema):
    """
    Authentication required fields.
    """
    class Meta:
        model = Device
        fields = ('mac_address', 'password')
