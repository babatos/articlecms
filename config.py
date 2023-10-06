import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'ducpm34storage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '0QNx27/ba/aGGVP/lVgPxSQPVr9Nu/iDrwwsWnco+rNW0KS5Zy1L6GlBKKq2WcbJSX/3ADnauUAH+AStXnZopQ=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'ducpm34server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'ducpm34_database'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'ducpm34'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Jamepotterbg997@'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CLIENT_SECRET = "fvx8Q~dDXbE_eVmxn6SNp31X3yDOGd.gtdAc2dcB"
    AUTHORITY = "https://login.microsoftonline.com/common"
    CLIENT_ID = "f3d139fe-b145-42ae-a07b-135da2e80956"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"