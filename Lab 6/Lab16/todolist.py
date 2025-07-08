from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task list
tasks = []

@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task_name = request.form.get('task')
        if task_name:
            tasks.append({"task": task_name, "completed": False})
        return redirect(url_for('todo'))

    return render_template('todolist.html', tasks=tasks)

@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]["completed"] = not tasks[task_id]["completed"]
    return redirect(url_for('todo'))

@app.route('/')
def home():
    return redirect(url_for('todo'))

if __name__ == '__main__':
    app.run(debug=True)
