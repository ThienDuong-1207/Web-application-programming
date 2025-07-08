from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Danh sách lưu tạm trong bộ nhớ
books = [
    {"title": "Harry Potter", "author": "J.K. Rowling"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien"}
]

@app.route('/')
def home():
    return redirect(url_for('book_list'))

@app.route('/poll', methods=['GET', 'POST'])
def book_list():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        books.append({"title": title, "author": author})
        return redirect(url_for('book_list'))
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
