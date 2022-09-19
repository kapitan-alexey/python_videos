from models import Video
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite+pysqlite:////home/python_videos/youtube_videos.db")
# engine = create_engine("sqlite+pysqlite:///youtube_videos.db")
Session = sessionmaker(bind=engine)


def get_video() -> Video:
    with Session() as session:
        video = (
            session.query(Video)
            .filter(Video.is_published_in_tg == 0)
            .order_by(Video.youtube_publish_date)
            .first()
        )
        return video


def update_video_status(video: Video):
    with Session() as session:
        session.query(Video).filter(Video.id == video.id).update(
            {"is_published_in_tg": True}
        )
        session.commit()
