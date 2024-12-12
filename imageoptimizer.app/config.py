import os

class Config:
    SECRET_KEY = 'secret_key'
    DEBUG = True
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))