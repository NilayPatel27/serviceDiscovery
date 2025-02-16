from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import threading
import time
import sys

app = Flask(__name__)
CORS(app)

registrarUrl = 'http://localhost:5000'
serviceName = sys.argv[1]
servicePort = sys.argv[2]
ollamaUrl = "http://localhost:11434/api/generate"
ollamaModelName = "llama3.2"

def register_service():
    requests.post(
        f"{registrarUrl}/register",
        json={'name': serviceName, 'address': f'http://localhost:{servicePort}'}
    )

def send_signal():
    while True:
        try:
            requests.post(
                f"{registrarUrl}/signal",
                json={'name': serviceName}
            )
        except requests.exceptions.RequestException:
            pass
        time.sleep(120)

@app.route('/process', methods=['POST'])
def process_request():
    
    data = request.get_json()
    
    ollama_response = requests.post(
        ollamaUrl,
        json={
            'model': ollamaModelName,
            'prompt': data['prompt'],
            'stream': False
        }
    )
    
    if ollama_response.status_code == 200:
        return jsonify({
            'from': serviceName,
            'to': data['from'],
            'response': ollama_response.json().get('response')
        })
    return jsonify({'error': 'Ollama processing failed'}), 500

@app.route('/ask', methods=['POST'])
def ask_service():
    data = request.get_json()
    
    response = requests.post(
        f"{registrarUrl}/forward",
        json={
            'from': serviceName,
            'to': data['service'],
            'prompt': data['prompt']
        }
    )
    return response.json()

if __name__ == '__main__':
    register_service()
    threading.Thread(target=send_signal, daemon=True).start()
    app.run(host='0.0.0.0', port=servicePort)