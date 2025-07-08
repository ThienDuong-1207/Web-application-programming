from flask import Flask, render_template,redirect, url_for, request

app = Flask(__name__)

votes = { "Cat":0, "Dog":0}

@app.route('/', methods=['GET', 'POST'])
def poll():
    if request.method == 'POST':
        option = request.form["animal"]
        if option in votes:
            votes[option] += 1
        return redirect(url_for('poll'))
    # Calculate  percentages
    total_votes = sum(votes.values())
    if total_votes > 0 :
        percentages = {animal: (count / total_votes) *100 for animal, count in votes.items()}
    else:
        percentages = {animal: 0 for animal in votes}

    return render_template('poll.html', votes=votes, percentages=percentages)   

if __name__ == '__main__':
    app.run(debug=True)     