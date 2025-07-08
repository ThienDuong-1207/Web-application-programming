from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def convert_temperature():
    """
    Xử lý chuyển đổi nhiệt độ giữa Celsius và Fahrenheit.
    
    Nếu là GET request: Hiển thị trang convert.html với form chuyển đổi.
    Nếu là POST request: Lấy giá trị từ form, thực hiện chuyển đổi và hiển thị kết quả.
    """
    result = None
    if request.method == 'POST':
        try:
            # Lấy giá trị từ form
            temp = float(request.form['temperature'])
            conversison = request.form['conversion']
            # Thực hiện chuyển đổi
            if conversison == 'c_to_f':
                result = f"{temp}°C = {temp * 9/5 + 32:.2f}°F"
            elif conversison == 'f_to_c':
                result = f"{temp}°F = {(temp - 32) * 5/9:.2f}°C"
        except ValueError:
            result = "Invalid input. Please enter a valid number."
    
    return render_template('temperature.html', result=result)
        
if __name__ == '__main__':
    app.run(debug=True) 
    