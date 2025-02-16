from flask import Flask, jsonify, request
import requests
import threading
import time
from datetime import datetime

app = Flask(__name__)
services = {}
lock = threading.Lock()
sessionTimeout = 300 

def cleanup_expired_services():
    while True:
        time.sleep(60)
        current_time = datetime.now().timestamp()
        with lock:
            expired = [name for name, svc in services.items() 
                      if current_time - svc['lastActive'] > sessionTimeout]
            for name in expired:
                del services[name]

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    with lock:
        services[data['name']] = {
            'address': data['address'],
            'lastActive': datetime.now().timestamp()
        }
    return jsonify({'status': 'registered'})

@app.route('/signal', methods=['POST'])
def signal():
    data = request.get_json()
    with lock:
        if data['name'] in services:
            services[data['name']]['lastActive'] = datetime.now().timestamp()
    return jsonify({'status': 'updated'})

@app.route('/services', methods=['GET'])
def list_services():
    with lock:
        return jsonify([{'name': k, 'address': v['address']} for k, v in services.items()])

@app.route('/forward', methods=['POST'])
def forward_message():
    data = request.get_json()
    with lock:
        target = services.get(data['to'])
    
    if not target:
        return jsonify({'error': 'Service not found'}), 404
    
    try:
        response = requests.post(
            f"{target['address']}/process",
            json={'from': data['from'], 'prompt': data['prompt']}
        )
        
        return response.json()
    except requests.exceptions.RequestException:
        return jsonify({'error': 'Failed to forward message'}), 500

if __name__ == '__main__':
    threading.Thread(target=cleanup_expired_services, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)