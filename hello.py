from flask import Flask, render_template, request, flash, session
from flaskext.mysql import MySQL


mysql = MySQL()

app = Flask(__name__)
app.config.from_object(__name__)

app.config['MYSQL_DATABASE_USER'] = 'b31ec76d1b8f9e'
app.config['MYSQL_DATABASE_PASSWORD'] = '2cacb672'
app.config['MYSQL_DATABASE_DB'] = 'heroku_4195a882ccb08b2'
app.config['SECRET_KEY'] = 'development key'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-iron-east-03.cleardb.net'

mysql.init_app(app)
app.config.from_envvar('VENV_SETTINGS', silent=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        session['logged_in'] = True
        flash('You were logged in')
        return render_template('admin.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return render_template('index.html')


@app.route('/')
def hello():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/news")
def news():
    # cursor = mysql.connect().cursor()
    # cursor.execute("SELECT * from news LIMIT 5")
    # info = cursor.fetchall()
    # return render_template('news.html', info=info)
    return render_template('news.html')


@app.route("/batting", methods=['POST', 'GET'])
def batting():
    if request.method == 'GET':
        return render_template('batting.html')


@app.route("/bowling", methods=['POST', 'GET'])
def bowling():
    if request.method == 'GET':
        return render_template('bowling.html')
