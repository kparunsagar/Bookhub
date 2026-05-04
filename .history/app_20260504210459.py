
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

@app.route('/add-category', methods=['POST'])
def add_category():
    name = request.form['name']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO categories (name) VALUES (%s)", (name,))
    conn.commit()

    return redirect('/admin')

@app.route('/add-book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    category_id = request.form['category_id']
    price = request.form['price']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO books (title, author, category_id, price)
        VALUES (%s, %s, %s, %s)
    """, (title, author, category_id, price))

    conn.commit()

    return redirect('/admin')

@app.route('/')
def home():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM books LIMIT 6")
    books = cursor.fetchall()

    return render_template('home.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
