from flask import render_template,redirect,url_for,request
from flask_login import login_required
from . import main
from app.models import User,Pitch,Comment
from .forms import PitchForm,CommentForm
from .. import db

@main.route('/')
def index():
    title = 'Home'

    pitches = Pitch.get_pitches()
    comments=Comment.get_comments()

    return render_template('index.html' ,title=title, pitches=pitches,comments=comments)

@main.route('/pitch/new',methods=['GET','POST'])
@login_required
def new_pitch():
    '''
    Method to add new pitch
    '''
    form= PitchForm()
    if form.validate_on_submit():
        title=form.title.data
        description=form.description.data
        like=0
        dislike=0
        new_pitch=Pitch(title=title,description=description,like=like,dislike=dislike)
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title= 'Pitches'
    return render_template('new_pitch.html',pitch_form=form)