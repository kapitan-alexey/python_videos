from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Video

engine = create_engine("sqlite+pysqlite:///youtube_videos.db")
Session = sessionmaker(bind=engine)


def get_video() -> Video:
    with Session() as session:
        video = session.query(Video).filter(Video.is_published_in_tg == False).order_by(
            Video.youtube_publish_date).first()
        return video


def update_video_status(video: Video) -> True:
    with Session() as session:
        session.query(Video).filter(Video.id == video.id).update({"is_published_in_tg": True})
        session.commit()
