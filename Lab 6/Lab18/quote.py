from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Don’t let yesterday take up too much of today.",
    "It’s not whether you get knocked down, it’s whether you get up.",
    "Failure will never overtake me if my determination to succeed is strong enough."
]

@app.route('/')
def random_quote():
    quote = random.choice(quotes)
    return render_template('quote.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
