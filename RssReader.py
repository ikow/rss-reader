from __future__ import print_function
from flask import *
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.session import Session
from markupsafe import Markup
from HandleRequest import HandleRequest
import sys

t = HandleRequest()
app = Flask(__name__)
SESSION_TYPE = 'redis'
manager = Manager(app)
bootstrap = Bootstrap(app)
sess = Session()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print(request.form['email']+' '+request.form['password'], file=sys.stderr)
        if request.form['email'] == "root@ev1l.com" and request.form['password'] == "dontbeev1l":
            session['user_name'] = 'admin'
            flash(Markup('Login successfully!'), 'success')
            return redirect('/user/admin')
        else:
            print('1', file=sys.stderr)
            flash(Markup('Login failed!'), 'danger')
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    if 'user_name' in session:
        return render_template('user.html', title=t.feed.feed.title, items=t.feed['items'])
    else:
        flash(Markup('Please login first!'), 'danger')
        return redirect('/')


@app.route('/logout')
def logout():
    if 'user_name' in session:
        session.pop('user_name', None)
        return redirect('/')
    else:
        flash(Markup('You haven\'t login yet!'), 'danger')
        return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.jinja_env.add_extension('jinja2.ext.do')
    sess.init_app(app)
    app.run()
