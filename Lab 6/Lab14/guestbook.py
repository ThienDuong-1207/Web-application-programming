from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Danh sách lưu trữ các entry (dữ liệu chỉ tồn tại trong thời gian chạy server)
guestbook_entries = []

@app.route('/', methods=['GET', 'POST'])
def guestbook():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        if name and message:
            guestbook_entries.append({'name': name, 'message': message})
        return redirect('/')  # Tránh bị gửi lại form khi refresh

    return render_template('guestbook.html', entries=guestbook_entries)

if __name__ == '__main__':
    app.run(debug=True)
