from app import db
from flask_admin.contrib.sqla import ModelView
import datetime


class Channel(db.Model):
    __tablename__ = "youtube_channel"

    id = db.Column(db.Integer, primary_key=True)
    youtube_id = db.Column(db.String(30), unique=True)
    desc = db.Column(db.String(100))

    def __repr__(self):
        return f"{self.id} [{self.desc}]"


class Video(db.Model):
    __tablename__ = "youtube_video"

    id = db.Column(db.Integer(), primary_key=True)
    youtube_link = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(200))
    youtube_publish_date = db.Column(db.DateTime())
    is_published_in_tg = db.Column(db.Boolean(), default=False)
    channel_id = db.Column(db.String(), db.ForeignKey("youtube_channel.id"))

    def __repr__(self):
        return self.title


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(200))
    link = db.Column(db.String(100), unique=True)
    date_added = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
    is_published_in_tg = db.Column(db.Boolean(), default=False)


# Customized admin interface
class ChannelView(ModelView):
    list_template = 'list.html'
    create_template = 'create.html'
    edit_template = 'edit.html'


class VideoView(ModelView):
    list_template = 'list.html'
    create_template = 'create.html'
    edit_template = 'edit.html'


class PostView(ModelView):
    list_template = 'list.html'
    create_template = 'create.html'
    edit_template = 'edit.html'
