from flask import Flask, render_template, abort

app = Flask(__name__)

# Sample menu data
menu_items = {
    "drinks": [
        {"name": "Coffee", "price": 2},
        {"name": "Tea", "price": 1.5},
        {"name": "Juice", "price": 3}
    ],
    "food": [
        {"name": "Burger", "price": 5},
        {"name": "Pizza", "price": 8},
        {"name": "Salad", "price": 4}
    ]
}

@app.route('/<category>')
def show_menu(category):
    category = category.lower()
    items = menu_items.get(category)

    if items is None:
        return "Category not found", 404

    return render_template('menu.html', category=category.capitalize(), items=items)

@app.route('/')
def home():
    return '<h3>Try <a href="/drinks">/drinks</a> ' \
    'or <a href="/food">/food</a></h3>'

if __name__ == '__main__':
    app.run(debug=True)
