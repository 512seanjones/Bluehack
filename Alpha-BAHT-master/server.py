from flask import Flask, render_template, redirect, url_for
from form import LoginForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    user = {'username': 'Sean'}
    return render_template('index.html', title='Home', user=user)

@app.route('/index')
def index():
    user = {'username': 'Sean'}
    return render_template('index.html', title='Home', user=user)

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

if __name__ == "__main__":
    app.run(debug=True)
