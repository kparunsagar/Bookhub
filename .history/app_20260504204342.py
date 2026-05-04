
from flask import Flask, render_template
from db import get_connection
from flask import request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/categories')
def categories():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM categories")
    data = cursor.fetchall()
    return render_template('categories.html', categories=data)

@app.route('/books')
def books():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    data = cursor.fetchall()
    return render_template('books.html', books=data)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/admin')
def admin():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    return render_template('admin.html', categories=categories)

if __name__ == '__main__':
    app.run(debug=True)
