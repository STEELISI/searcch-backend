TESTING = True
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
#SESSION_TIMEOUT_IN_MINUTES = 60
SESSION_TIMEOUT_IN_MINUTES = 24*60
SQLALCHEMY_DATABASE_URI = "postgresql://psql_user:psql_password@searcch-backend-dev-postgres:5432/searcchhub_devel"
SHARED_SECRET_KEY = 'shared_secret_key'
