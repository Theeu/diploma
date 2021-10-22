from flask import Flask, redirect, url_for, render_template 
app = Flask(__name__)
from flaskext.mysql import MySQL
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'cbr'
app.config['MYSQL_DATABASE_HOST'] = '172.23.130.20'
mysql.init_app(app)
conn = mysql.connect()



@app.route('/')
def hello_world():
    cursor =conn.cursor()
    cursor.execute("select * from ValCurs")
    data = cursor.fetchall()
    return render_template("index.html",ValCurs=data)

if __name__ == '_main_':
    app.run(host='0.0.0.0')
