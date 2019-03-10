from flask import Flask, render_template, redirect, url_for
from form import DataForm
from config import Config
import gmplottest

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    return render_template('index.html', title='Home')

@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/getdata',  methods=['GET', 'POST'])
def getdata():
    form = DataForm()
    if form.validate_on_submit():
        gmplottest.main(form.street.data, form.city.data, form.state.data)
        return redirect(url_for('index'))
    return render_template('getdata.html', title='Form', form=form)

@app.route('/my_map')
def my_map():
    return render_template('my_map.html', title='Heatmap')

if __name__ == "__main__":
    app.run(debug=True)
