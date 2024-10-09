# docs/config.py
class Config:
    SECRET_KEY = 'password'
    SQLALCHEMY_DATABASE_URI = 'postgresql://usuario:senha@localhost/tigre'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
