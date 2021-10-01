import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()
dotenv_path=join(dirname(__file__),'.env')
load_dotenv(dotenv_path)

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SECRET_KEY=os.urandom(32)