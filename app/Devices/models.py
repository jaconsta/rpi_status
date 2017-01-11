import random
import string

from werkzeug.security import generate_password_hash, check_password_hash

from app import db

APP_SECRET = 'TjZt1eB5Nd2Tt45ii8vG5JD11ptHIK70'


class Device(db.Document):
    """
    Manage the registered devices connected.
    """
    # Device Eth0 MAC address
    mac_address = db.StringField(required=True, unique=True)
    # Auto generated password
    password = db.StringField(required=True)

    def random_password(self):
        """
        Assigns a random string to password.
        :return: Random string
        """
        self.password = ''.join(random.SystemRandom().
                                choice(string.ascii_uppercase + string.digits)
                                for _ in range(10))

    def hash_password(self):
        """
        Hash device password.
        """
        self.password = generate_password_hash(self.password)

    def check_password(self, password):
        """
        Validate device password.

        :param password: Device password.
        :return: (Boolean) Passwords match.
        """
        return check_password_hash(self.password, password)
