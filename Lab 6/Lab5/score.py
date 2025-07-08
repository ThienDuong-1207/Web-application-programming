from flask import Flask, render_template,request


app = Flask(__name__)

@app.route('/')
def student_form():
    return render_template('student_form.html')

@app.route('/show_details', methods=['POST'])
def show_details():
    # Lấy dữ liệu từ form
    if request.method == 'POST':
        name = request.form['name']
        # 
        try:
            physics = int(request.form['physics'])
            chemistry = int(request.form['chemistry'])
            maths = int(request.form['maths'])
        except ValueError:
            return "Invalid input. Please enter valid numbers for marks."
        
        # Calculate total
        total_score = physics + chemistry + maths

        # Show details
        return render_template('student_details.html',
                            name=name,
                            physics=physics,
                            chemistry=chemistry,
                            maths=maths,
                            total_score=total_score)
    # # Non-POST request case
    return 'Method not allowed. Please use POST request.'

if __name__ == '__main__':
    app.run(debug=True) 