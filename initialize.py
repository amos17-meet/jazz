from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import *


engine = create_engine('sqlite:///Data.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

photos_url=['https://docs.google.com/uc?id=121QqhyTZVrSbWwLxHmBsgga-N1uGU3Hy',
'https://docs.google.com/uc?id=0Byt8kaga872McmxLVzJUWXJqdjQ',
'https://docs.google.com/uc?id=0Byt8kaga872MQnpJaWVacjBRUzA',
'https://docs.google.com/uc?id=0Byt8kaga872MRXpBRXhGd29ndTg',
'https://docs.google.com/uc?id=0Byt8kaga872MdDBUdVJ1Nkw5NTQ']


for photo_url in photos_url:
	session_photo=Media(description="p",
		url=photo_url,
		type_of_media="photo")

	session.add(session_photo)






session.commit()
