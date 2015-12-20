from flask import Flask, render_template, request, flash, session
app = Flask(__name__)


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
