from flask import Flask, render_template

name = Flask(__name__)

@name.route('/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    name.run(debug=True)