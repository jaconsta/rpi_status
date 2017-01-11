from app import db


class Information (db.Document):
    """
    Stores the collected information of the devices.
    """
    # Device MAC.
    device_name = db.StringField(required=True)
    # Data type collected, eg. IP_ADDRESS.
    data_type = db.StringField(required=True)
    # Value of the information collected.
    information = db.StringField(requrired=True)
    # Time when the device captured the information.
    information_time = db.DateTimeField()
    # Time when the information was captured by the server.
    created_at = db.DateTimeField()
