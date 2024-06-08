from sqlalchemy import Column, JSON, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Notes(Base):
    __tablename__ = 'Notes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String())
    content = Column(JSON, nullable=False)
    linked_entities = Column(JSON, nullable=True)

    def __repr__(self):
        return f"id: {self.id}, name {self.name}"