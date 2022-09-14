from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship  # type: ignore

Base = declarative_base()


class Channel(Base):  # type: ignore
    __tablename__ = 'youtube_channel'

    id = Column(String(), primary_key=True)
    desc = Column(String(100))
    videos = relationship('Video', backref='channel')

    def __str__(self):
        return f'{self.id} [{self.desc}]'


class Video(Base):  # type: ignore
    __tablename__ = 'youtube_video'

    id = Column(String(), primary_key=True, index=True)
    title = Column(String(100))
    youtube_publish_date = Column(DateTime())
    is_published_in_tg = Column(Boolean(), default=False)
    channel_id = Column(String(), ForeignKey('youtube_channel.id'))

    def __str__(self):
        return self.title
