from flask import Flask, render_template, redirect, url_for
from form import DataForm
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

@app.route('/getdata')
def getdata():
    form = DataForm()
    if form.validate_on_submit():
        print("City is: " + form.city)
        print("State is: " + form.state)
        print("Street is: " + form.street)
        return redirect(url_for('index'))
    return render_template('getdata.html', title='Form', form=form)

if __name__ == "__main__":
    app.run(debug=True)
