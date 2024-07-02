from flask import Flask, render_template, request, redirect
import sqlite3

DATABASE = "movielist.db"
app = Flask(__name__)

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db()
    movies = conn.execute("SELECT * FROM movies").fetchall()
    conn.close()
    return render_template("index.html", movies = movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    name = request.form["name"]
    director = request.form["director"]
    released = request.form["released"]

    conn = get_db()
    conn.execute("INSERT INTO movies (name, director, released) VALUES (?, ?, ?)", (name, director, released))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)