from flask import Flask, render_template

homepage = Flask(__name__)

@homepage.route('/')
def hello():
    return render_template('homepage.html')

if __name__ == '__main__':
    homepage.run(debug=True)