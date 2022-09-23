from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_migrate import Migrate
import datetime

from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate(app, db)

app.config['SECRET_KEY'] = '123456790'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite+pysqlite:////home/python_videos/youtube_videos.db"
# app.config[
#     "SQLALCHEMY_DATABASE_URI"] = "sqlite+pysqlite:///E:\\python\\Python_youtube\\python_videos\\youtube_videos.db"

db.init_app(app)


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
    # column_list = ('id', 'desc')
    list_template = 'list.html'
    create_template = 'create.html'
    edit_template = 'edit.html'


class VideoView(ModelView):
    # column_list = ('id', 'desc')
    list_template = 'list.html'
    create_template = 'create.html'
    edit_template = 'edit.html'


class PostView(ModelView):
    # column_list = ('title', 'is_published_in_tg')
    list_template = 'list.html'
    create_template = 'create.html'
    edit_template = 'edit.html'


@app.route("/")
def hello_world():
    return '<a href="/admin/">Click me to get to Admin!</a>'


# Create admin with custom base template
admin = admin.Admin(app, 'Python videos admin', base_template='layout.html', template_mode='bootstrap3')

# Add views
admin.add_view(ChannelView(Channel, db.session))
admin.add_view(VideoView(Video, db.session))
admin.add_view(PostView(Post, db.session))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
