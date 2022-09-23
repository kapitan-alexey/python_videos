from models import Post
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite+pysqlite:////home/python_videos/youtube_videos.db")
# engine = create_engine("sqlite+pysqlite:///youtube_videos.db")
Session = sessionmaker(bind=engine)


def get_post() -> Post:
    with Session() as session:
        video = (
            session.query(Post)
            .filter(Post.is_published_in_tg == 0)
            .order_by(func.random()).first()
        )
        return video


def update_post_status(post: Post):
    with Session() as session:
        session.query(Post).filter(Post.id == post.id).update(
            {"is_published_in_tg": True}
        )
        session.commit()
