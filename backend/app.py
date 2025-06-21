from flask import Flask, request, jsonify
from flask_cors import CORS
from jarvis_tasks import handle_jarvis_command

app = Flask(__name__)
CORS(app)

@app.route('/command', methods=['POST'])
def command():
    data = request.get_json()
    command = data.get('command')
    if command:
        response = handle_jarvis_command(command)
        return jsonify({ 'response': response })
    return jsonify({ 'response': 'No command received.' }), 400

if __name__ == '__main__':
    app.run(debug=True)
