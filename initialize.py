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

photos_url=['https://drive.google.com/file/d/0Byt8kaga872MVWhYeHhMR2dwWmM/view?usp=sharing',
'https://drive.google.com/file/d/0Byt8kaga872McmxLVzJUWXJqdjQ/view?usp=sharing',
'https://drive.google.com/drive/u/0/folders/0Byt8kaga872MflROcVczWlMwTE0zT2pYYkdTd3k3THNvUVdKdGdwdWpzNnlISXdtWjd2V3c',
'https://drive.google.com/file/d/0Byt8kaga872MQnpJaWVacjBRUzA/view?usp=sharing',
'https://drive.google.com/file/d/0Byt8kaga872MRXpBRXhGd29ndTg/view?usp=sharing',
'https://drive.google.com/file/d/0Byt8kaga872MdDBUdVJ1Nkw5NTQ/view?usp=sharing']


for photo_url in photos_url:
	session_photo=Media(description="p",
		url=photo_url,
		type_of_media="photo")

	session.add(session_photo)



first_video=Media(description="v",
	url="https://www.youtube.com/watch?v=Iwv-aggzNbk&list=RDMMIwv-aggzNbk",
	type_of_media="video")

photo=Media(description="p",
	url="static/photo.jpg",
	type_of_media="photo")
session.add(first_video)
session.add(photo)



session.commit()
