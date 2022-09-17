from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Channel, Video

engine = create_engine("sqlite+pysqlite:///youtube_videos.db")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def get_channels() -> list:
    with Session() as session:
        channels = session.query(Channel).all()
        channels_id = [channel.id for channel in channels]
        return channels_id


def get_videos() -> list:
    with Session() as session:
        return session.query(Video).all()


def save_new_videos(all_channels_videos):
    with Session() as session:
        for channel_videos in all_channels_videos:
            session.add_all(channel_videos)
        session.commit()