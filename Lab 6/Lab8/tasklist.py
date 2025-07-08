from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple to-do list stored in memory
# In a real application, you would store it in a database
tasks = [
    "Buy milk",
    "Complete project report",
    "Call customer X",
    "Make plans for the weekend"
]

@app.route('/')
@app.route('/tasks', methods=['GET', 'POST'])
def task_list():
    """
    Xử lý hiển thị danh sách công việc và thêm công việc mới.

    Nếu là GET request: Hiển thị trang tasklist.html với danh sách công việc hiện có.
    Nếu là POST request: Thêm công việc mới từ form vào danh sách và chuyển hướng lại trang.
    """
    if request.method == 'POST':
        # Get new job from form
        # 'task_description' is the name of the input in the form
        new_task = request.form.get('task_description') 

        if new_task: # Make sure job is not empty
            tasks.append(new_task) # Add tasks to list
        
        # Redirect user to /tasks page to show updated list
        # This also avoids form resubmission problem when refreshing page
        return redirect(url_for('task_list'))
    
    # Đối với GET request, hiển thị template với danh sách công việc
    return render_template('tasklist.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True) 