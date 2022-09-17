from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Video

engine = create_engine("sqlite+pysqlite:///youtube_videos.db")
Session = sessionmaker(bind=engine)


def get_video() -> str:
    with Session() as session:
        video = session.query(Video).filter(Video.is_published_in_tg == False).order_by(
            Video.youtube_publish_date).first()
        return video.id
