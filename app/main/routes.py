from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm
import uuid

@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == '123':
            session['username'] = form.username.data
            return redirect(url_for('.friendlist'))
        return '''Invalid Password'''
    elif request.method == 'GET':
        form.username.data = session.get('username', '')
    return render_template('index.html', form=form)

@main.route('/friendlist')
def friendlist():
    """Choose friend to chat."""
    username = session.get('username', '')
    if username == '':
        return redirect(url_for('.index'))
    friends = ['zhangsan','lisi','wangwu']
    return render_template('friendlist.html', name=username,friends=friends)

@main.route('/choosefriend', methods=['POST'])
def choosefriend():
    if request.method == 'POST':
        friend = request.form['friend']
        session['sid'] = str(uuid.uuid4().fields[-1])[:5]
        session['friends'] = [friend]
        return redirect(url_for('.chat'))
    return redirect(url_for('.index'))

@main.route('/chat')
def chat():
    """Chat room. The user's name and room must be stored in
    the session."""
    username = session.get('username', '')
    friends = session.get('friends', '')
    if username == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=username,friends=friends)
