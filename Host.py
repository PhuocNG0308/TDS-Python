from flask import Flask, request, jsonify

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Định nghĩa endpoint POST
@app.route('/process', methods=['POST'])
def process_query():
    # Lấy dữ liệu từ request
    data = request.json  # Lấy JSON body
    if not data or 'query' not in data:
        return jsonify({"error": "Missing 'query' parameter"}), 400

    # Trích xuất query
    query = data['query']
    
    # Xử lý logic trả về (trong ví dụ này, chỉ đơn giản trả về query đã gửi)
    response = f"You sent: {query}"
    
    return jsonify({"response": response}), 200

# Chạy server
if __name__ == '__main__':
    app.run(debug=True)
