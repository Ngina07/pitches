from flask import render_template
from flask_login import login_required
from . import main
from app.models import User,Pitch,Comment

@main.route('/')
def index():
    title = 'Home'

    pitches = Pitch.get_pitches()
    comments=Comment.get_comments()

    return render_template('index.html' ,title=title, pitches=pitches,comments=comments)
