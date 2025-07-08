from flask import Flask, render_template,request

app = Flask(__name__)
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():
    username = request.form['username']
    
    # Here you would typically check the username and password against a database
    if username == 'admin':
        return "Login successfully!"
    else:
        return render_template('login.html', error='Invalid credentials')
    
if __name__ == '__main__':
    app.run(debug=True)