from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    x = -2
    y = 5 * x + 7
    equation = f"y = 5x + 7 with x = {x}"
    return render_template("index.html", equation=equation, x=x, y=y)

if __name__ == "__main__":
    app.run(debug=True)