from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Video(Base):
    __tablename__ = 'youtube_video'

    id = Column(String(), primary_key=True, index=True)
    youtube_link = Column(String(40), unique=True)
    title = Column(String(100))
    youtube_publish_date = Column(DateTime())
    is_published_in_tg = Column(Boolean(), default=False)
    channel_id = Column(String(), ForeignKey('youtube_channel.id'))

    def __str__(self):
        return self.title
