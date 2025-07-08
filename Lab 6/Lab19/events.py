from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

events = [
    {"name": "Music Concert", "date": "2023-10-01", "location": "City Park"},
    {"name": "Art Exhibition", "date": "2023-10-05", "location": "Art Gallery"},
    {"name": "Food Festival", "date": "2023-10-10", "location": "Downtown Square"}
]

@app.route('/')
def home():
    return redirect(url_for('show_events'))

@app.route('/events', methods=['GET', 'POST'])
def show_events():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        location = request.form['location']
        events.append({"name": name, "date": date, "location": location})
        return redirect(url_for('show_events'))

    return render_template('events.html', events=events)

if __name__ == '__main__':
    app.run(debug=True)
