from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "👋 Hello from Docker and Kubernetes, hows training goining on , today is 13th April, sunday! "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)