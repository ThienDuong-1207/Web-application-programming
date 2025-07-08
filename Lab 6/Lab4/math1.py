from flask import Flask, render_template, request
import math

math = Flask(__name__)
@math.route('/')
def maths_form():
    return render_template('math_form.html')

@math.route('/calculate_square', methods=['POST']) # đường dẫn xử lý khi form được gửi đi
def calculate_square():
    if request.method == 'POST':
        try:
            number_str = request.form['number']  # Lấy giá trị từ form
            number = int(number_str)  # Chuyển đổi chuỗi thành số nguyên

            square = number ** 2  # Tính bình phương

            return render_template('result.html', number=number, square=square)  # Trả về kết quả
        except ValueError:
            return "Invalid input. Please enter a valid number."
    return "Method not allowed" # trả về thông báo nếu không phải là phương thức POST

########
if __name__ == '__main__':
    math.run(debug=True)  # Chạy ứng dụng Flask với chế độ debug