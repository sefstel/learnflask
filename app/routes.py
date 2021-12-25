from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, BlogForm
from app import db
from app.models import Blog

@app.route('/')
@app.route('/index')
def index():
    user = {'username': "Sefstel"}
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
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data,form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign in',form=form)


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
