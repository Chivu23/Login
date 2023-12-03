from flask import Flask, render_template, request, redirect, url_for, session
# from flask_mysqldb import MySQL

app = Flask('__name__')
app.secret_key = b'_5#y2L"F4Q8z\n\xec)'

# MySQL Config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'table_users'

# connect to db
# mysql = MySQL(app)


@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connect.cursor()
        cur.execute(f"select username, password from table_users where username = '{username}'")
        user = cur.fetchone()
        cur.close()
        if user and password == user[1]:
            session['username'] = user[0]
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error = 'Invalid username or password ')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connenct_mysql()
        cur.execute(f"insert into table_users (username, password) values ( '{username}', '{password}')")
        mysql.connenct_mysql.commit()
        cur.close()

        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/logut')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=7001)

# currentlocation = os.path.dirname(os.path.abspath(__file))
#
# myapp = Flask(__name__)
#
# @my.app.route(/)
# def homepage():
#     return render_template("homepage.html")
#
# @myapp.route("/", methods=["POST"])
# def checklogin():
#     UN = request.form["Username"]
#     PW = request.form["Password"]
#
#     sqlconnection = sqlite3.Connection(currentlocation + "\login.db")
#     cursor = sqlconnection.cursor()
#     query1 = f"SELECT Username, Password From User WHERE Username = {UN} and Password = {PW}"
