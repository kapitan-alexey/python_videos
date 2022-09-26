import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite+pysqlite:////home/python_videos/youtube_videos.db"
# SQLALCHEMY_DATABASE_URI = "sqlite+pysqlite:///E:\\python\\Python_youtube\\python_videos\\youtube_videos.db"
