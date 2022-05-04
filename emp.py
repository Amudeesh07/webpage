from flask import Flask,render_template,request,url_for,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Solid@123"
app.config["MYSQL_DB"]="edb"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql=MySQL(app)

@app.route("/")

def home():
    return render_template("home.html")



@app.route("/login", methods=["GET", "POST"])

def login():
    if request.method =='POST':
        mail = request.form['mail']
        password = request.form['pass']
        con=mysql.connection.cursor()
        sql = "select * from user where MAIL = %s and PASSWORD=%s" 
        con.execute(sql, (mail,password))
        res = con.fetchall()
        if res:
            con=mysql.connection.cursor()
            sql1="select * from user order by rankk"
            con.execute(sql1)
            result=con.fetchall()
            return render_template("leaderboard.html",datas=result)
        else:
            msg = "Invalid mail or password"
            return render_template("login.html", msg = msg)
    return render_template("login.html", msg = "")

@app.route("/signup",methods=['GET', 'POST'])
def signup():

    if request.method =='POST':
        mail=request.form['mail']
        name=request.form['name']
        id=request.form['id']
        password=request.form['pass']
        con=mysql.connection.cursor()
        sql = "update user set mail=%s, name=%s, password=%s where regno=%s"
        con.execute(sql,[mail,name,password,id])
        mysql.connection.commit()
        con.close()
        return render_template("login.html")
    return render_template("signup.html")

@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard():
    con=mysql.connection.cursor()
    sql="select * from user order by rank;"
    con.execute(sql)
    result=con.fetchall()
    return render_template("leaderboard.html",datas=result)

@app.route("/stats<string:id>", methods=["GET", "POST"])	
def stats(id):
    con=mysql.connection.cursor()
    sql="select * from user where REGNO = %s" 
    con.execute(sql,[id,])
    res=con.fetchall()
    return render_template("stats.html",datas=res)

if(__name__=='__main__'):
    app.run(debug=True)