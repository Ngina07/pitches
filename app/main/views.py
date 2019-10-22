from flask import render_template,redirect,url_for,request.abort
from flask_login import login_required,login_user,logout_user
from . import main
from app.models import User,Pitch,Comment
from .forms import PitchForm,CommentForm,UpdateProfile
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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)