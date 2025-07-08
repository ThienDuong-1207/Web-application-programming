from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('calculate'))

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    result = None
    error = None

    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    error = "Error: Division by zero is not allowed."
                else:
                    result = num1 / num2
            else:
                error = "Invalid operation."
        except ValueError:
            error = "Please enter valid numbers."

    return render_template('calculator.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
