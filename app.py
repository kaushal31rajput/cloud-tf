from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "👋 Hello from Docker and Kubernetes, you are rockstar!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)