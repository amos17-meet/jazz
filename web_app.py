from flask import Flask, url_for, flash, redirect, request, render_template, session as login_session

from database_setup import *
import os
app = Flask(__name__)
app.secret_key = "jazz"

engine = create_engine('sqlite:///Data.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()




@app.route('/')
def home_page():
	return render_template('home.html')

@app.route('/video')
def video_page():
	videos=session.query(Media).filter_by(type_of_media="video").all()
	return render_template("video.html", videos=videos)

@app.route('/audio')
def audio_page():
	audios=session.query(Media).filter_by(type_of_media="audio").all()
	return render_template('audio.html')

@app.route('/gallery')
def gallery_page():
	photos=session.query(Media).filter_by(type_of_media="photo").all()
	for photo in photos:
		print(photo.url)
	url_of_photos=[]

	indir = 'static/vintjazz-photos'
	for root, dirs, filenames in os.walk(indir):
		for f in filenames:
			print(f)
			print(type(f))
			url_of_photos.append("static/vintjazz-photos/"+f)
			print(url_of_photos[-1])



	return render_template('gallery.html', url_of_photos=url_of_photos)


@app.route('/contact')
def contact_page():
	return render_template('contact.html')

if __name__ == '__main__':
	app.run(debug=True)
