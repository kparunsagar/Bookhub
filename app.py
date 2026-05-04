from flask import Flask, render_template, request, redirect
from db import get_connection

app = Flask(__name__)

# ✅ HOME (UPDATED - WITH BOOKS)
@app.route('/')
def home():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM books LIMIT 6")
    books = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('home.html', books=books)


# ✅ CATEGORIES PAGE
@app.route('/categories')
def categories():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM categories")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('categories.html', categories=data)


# ✅ BOOKS PAGE
@app.route('/books')
def books():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM books")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('books.html', books=data)


# ✅ LOGIN PAGE
@app.route('/login')
def login():
    return render_template('login.html')


# ✅ ADMIN PANEL
@app.route('/admin')
def admin():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('admin.html', categories=categories)


# ✅ ADD CATEGORY
@app.route('/add-category', methods=['POST'])
def add_category():
    name = request.form['name']

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO categories (name) VALUES (%s)", (name,))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect('/admin')


# ✅ ADD BOOK
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

    cursor.close()
    conn.close()

    return redirect('/admin')

@app.route('/book/<int:id>')
def book_detail(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
    book = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template('book_detail.html', book=book)

@app.route('/buy/<int:id>')
def buy_book(id):
    return render_template('payment.html', book_id=id)

# ✅ RUN APP
if __name__ == '__main__':
    app.run(debug=True)