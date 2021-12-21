import os 

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-newer-guess'
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') or \
        'sqllite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False