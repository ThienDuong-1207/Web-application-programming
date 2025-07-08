from flask import Flask, render_template,redirect,url_for

app = Flask(__name__)

# Dictionary chứa các FAQ
faqs = {
    1: {"question": "What is Flask?", "answer": "Flask is a lightweight web framework for Python."},
    2: {"question": "How to install Flask?", "answer": "Use pip install flask."},
    3: {"question": "Is Flask easy to learn?", "answer": "Yes, Flask is beginner-friendly."}
}

@app.route("/")
def home():
    return redirect(url_for("faq",question_id=1))

@app.route('/faq/<int:question_id>')
def faq(question_id):
    faq_item = faqs.get(question_id)
    if faq_item:
        return render_template("faq.html", faq=faq_item)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
