from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Docker!"

@app.route("/demo")
def demo():
    return "Demo Page"

app.run(host="0.0.0.0", port=8000)
