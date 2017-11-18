from flask import Flask, url_for, flash, redirect, request, render_template, session as login_session

from database_setup import *

app = Flask(__name__)
app.secret_key = "jazz"

engine = create_engine('sqlite:///Data.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()
@app.route('/music')
def music_page():
	return render_template("music.html")

@app.route('/')
def main_page():
	return render_template('index.html')

@app.route('/video')
def video_page():
	return render_template('video.html')



if __name__ == '__main__':
	app.run(debug=True)
