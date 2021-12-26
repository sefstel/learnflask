from flask import render_template, flash, redirect, url_for,request
from app import app
from app.forms import LoginForm, BlogForm
from app import db
from app.models import Blog
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Какая гадость эта ваша заливная рыба'
         },
        {
            'author': {'username': 'Ипполит'},
            'body': 'The advengers movie was so cool'
         }
    ]
    return render_template('index.html',
                           title='Home',
                           posts=posts)


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/blog',methods=['GET','POST'])
def blog():
    form = BlogForm()
    if form.validate_on_submit():
        post =  Blog(author = form.author.data, body = form.body.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog'))
    posts = Blog.query.all()
    return render_template('blog.html',form=form,posts = posts)

@app.route('/blog/<int:id>')
def delete_blog(id):
    post = Blog.query.get(id)
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('blog'))