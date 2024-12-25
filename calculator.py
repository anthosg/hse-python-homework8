from flask import Flask

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

@app.route("/")
def index():
    return f"Index page {add(2, 5)}"

if __name__== "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
