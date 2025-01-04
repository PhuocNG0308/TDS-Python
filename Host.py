from flask import Flask, request, jsonify
import TDS as TDS

app = Flask(__name__)

@app.route('/postendpoint', methods=['POST'])
def handle_post():
    data = request.json
    
    tiktok_id = data.get('tiktok_id')
    tds_token = data.get('tds_token')
    
    if not tiktok_id or not tds_token:
        return jsonify({
            'error': 'Missing required fields'
        }), 400
    
    return jsonify({"response": TDS.process_recaptcha(tiktok_id, tds_token)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)