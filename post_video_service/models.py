from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Video(Base):  # type: ignore
    __tablename__ = "youtube_video"

    id = Column(Integer(), primary_key=True)
    youtube_link = Column(String(50), unique=True)
    title = Column(String(200))
    youtube_publish_date = Column(DateTime())
    is_published_in_tg = Column(Boolean(), default=False)
    channel_id = Column(String(), ForeignKey("youtube_channel.id"))

    def __repr__(self):
        return self.title
