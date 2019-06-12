import os

from flask import Flask, render_template, request, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from geek import *

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
#Log in
# "SELECT * FROM users WHERE (username = 'input_username') AND (password = 'input_password')";
#    books = db.execute("SELECT * FROM books").fetchall()
#    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html") #, books=books)

@app.route("/login", methods=["POST"])
def login():
#    floory = Geek(2, "Jack Floory", "password")
    name = request.form.get("name")
    password = request.form.get("password")
    pword = db.execute("SELECT password FROM users WHERE name = :name", {"name": name}).fetchall()

    try:
        if pword[0][0] == password:
            return render_template("logon.html", name=name, password=password, pword=pword)
        else:
            return render_template("error.html", message="It's Invalid user or password")
    except:
            return render_template("error.html", message="It's Invalid user or password")


@app.route("/register", methods=["POST"])
def register():
    return render_template("register.html")

@app.route("/newuser", methods=["POST"])
def newuser():
    name = request.form.get("name")
    user = db.execute("SELECT name FROM users WHERE name = :name", {"name": name}).fetchall()
    try:
        if user[0][0] == name:
            return render_template("error.html", message="That name is already taken")
    except IndexError:
        password = request.form.get("password")
        db.execute("INSERT INTO users (name, password) VALUES (:name, :password);", {"name": name, "password": password})
        db.commit()
        return render_template("newuser.html", name=name)

#    for table in dbtables:
#        return "{table.table_name}"
#    return "Project 1: TODO"

@app.route("/books", methods=["POST"])
def books():
    query = request.form.get('query')
    books = db.execute("SELECT * FROM books WHERE author = :query", {"query": query}).fetchall()

#    for line in books:
#        line = line.split(',')

    #books = books.split("()")
#    books = "bla bla <br> more bla"
    if books == []:
        return render_template("error.html", message="There are no books by " + query)
    else:
        return render_template("books.html", books=books , author=query)



#   return render_template("error.html", message="Invalid book or something spooky")#Log in
#"SELECT * FROM users WHERE (username = 'input_username') AND (password = 'input_password')";
#    query = request.form.get("query")
#    books = db.execute("SELECT * FROM books WHERE title = :query", {"query": query}).fetchall()
#    return render_template("books.html", books=books)
