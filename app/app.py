from flask import Flask, request
import redis

app = Flask(__name__)
r = redis.Redis(host='redis-service', port=6379, decode_responses=True)

@app.route('/')
def home():
    return "Usage: /set/mykey/myvalue or /get/mykey"

# Route to CHANGE/SET data 
@app.route('/set/<key>/<value>')
def set_data(key, value):
    r.set(key, value)
    return f"Successfully saved '{value}' under the key '{key}'."

# Route to READ data 
@app.route('/get/<key>')
def get_data(key):
    value = r.get(key)
    if value:
        return f"The value for '{key}' is: {value}"
    return f"Key '{key}' not found in Redis.", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)