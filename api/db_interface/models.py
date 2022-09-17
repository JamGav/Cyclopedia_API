from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "USER_INFO"

    user_id = Column(Integer, primary_key=True)
    f_name = Column(String)
    l_name = Column(String)
    email = Column(String)
    # FetchedValue allows the class to instantiate without that value.  You need this for the INSERT operation
    # In the database, the creation_dt is generated automatically on INSERT
    creation_dt = Column(String, server_default=FetchedValue())


class POIType(Base):
    __tablename__ = "POINT_OF_INTEREST_TYPE"

    poi_type_id = Column(Integer, primary_key=True)
    poi_type_name = Column(String)
    pot_type_description = Column(String)


class POI(Base):
    __tablename__ = "POINT_OF_INTEREST"

    poi_id = Column(Integer, primary_key=True)
    latitude = Column(String)
    longitude = Column(String)
    altitude = Column(String)
    timestamp = Column(String, server_default=FetchedValue())
    comments = Column(String)