import os


SECRET_KEY = os.getenv('SECRET_KEY', 'not-set')

connection_string = "postgresql://postgres:5869@localhost:5432/accident_report_platform"

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', connection_string)