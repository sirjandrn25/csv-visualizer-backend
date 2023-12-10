from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from csv_visualizer_api.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    files = relationship("CsvFile", back_populates="users")


class CsvFile(Base):
    __tablename__ = "csv_files"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,index=True)
    description = Column(String,index=True)
    file_url = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="files")
