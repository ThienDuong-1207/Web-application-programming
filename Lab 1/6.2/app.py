from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def student():
    student_info = {
        "Name": "Nguyen Van A",
        "Student ID": "SV123456",
        "Academic Year": "2nd Year",
        "Major": "Computer Science",
        "Hobbies": "Reading, Coding, Football"
    }
    return render_template("student.html", info=student_info)

if __name__ == "__main__":
    app.run(debug=True)