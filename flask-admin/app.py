from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import flask_admin as admin

app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate(app, db)

app.config.from_pyfile('config.py')

db.init_app(app)


@app.route("/")
def hello_world():
    return '<a href="/admin/">Click me to get to Admin!</a>'


# Create admin with custom base template
admin = admin.Admin(app, 'Python videos admin', base_template='layout.html', template_mode='bootstrap3')

from models import Channel, Post, Video, ChannelView, PostView, VideoView

# Add views
admin.add_view(ChannelView(Channel, db.session))
admin.add_view(VideoView(Video, db.session))
admin.add_view(PostView(Post, db.session))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
