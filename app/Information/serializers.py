from marshmallow_mongoengine import ModelSchema

from .models import Information


class InformationSchema(ModelSchema):
    """
    Information schema abstraction.
    """
    class Meta:
        model = Information
        fields = ('device_name', 'data_type', 'information', 'information_time')
