from sqlalchemy import Column, BIGINT, String, INTEGER, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class File(Base):
    __tablename__ = 'v_file_info'
    id = Column(BIGINT, primary_key=True)
    guid = Column(String, unique=True)
    origin = Column(String)
    name = Column(String)
    path = Column(String)
    thumb = Column(String)
    mime = Column(String)
    extension = Column(String)
    size = Column(BIGINT)
    md5 = Column(String)
    hash = Column(String)
    owner = Column(INTEGER)
    group = Column(INTEGER)
    app = Column(INTEGER)
    type = Column(INTEGER)
    property = Column(String)
    extra = Column(INTEGER)
    remark = Column(String)
    created_at = Column(String)
    updated_at = Column(BIGINT)
    deleted_at = Column(BIGINT)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
