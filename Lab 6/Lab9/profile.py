from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/admin/<username>')
def profile_form(username):
    return render_template('profile.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)