from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()


class Post(Base):  # type: ignore
    __tablename__ = "posts"

    id = Column(Integer(), primary_key=True)
    title = Column(String(200))
    link = Column(String(100), unique=True)
    date_added = Column(DateTime(), default=datetime.datetime.utcnow())
    is_published_in_tg = Column(Boolean(), default=False)

    def __repr__(self):
        return self.title
