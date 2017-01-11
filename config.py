import os

# Enable development environment.
DEBUG = True

# Application directory.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# Database configuration.
MONGODB_SETTINGS = {
    'host': os.environ.get('MONGO_URI', 'mongodb://localhost:32768/rpi_status')
}

# Base configurations.
THREADS_PER_PAGE = 2
SECRET_KEY = os.environ.get('SECRET_KEY', '&Lpm-6t030EWWDdGO5u>r4DZZdj6Z6')

# CRSF.
CSRF_ENABLED = False
CSRF_SESSION_KEY = os.environ.get('CSRF_SESSION_KEY', '5b8G5bgToH3B5sDfFm89z3kn59451geT')
