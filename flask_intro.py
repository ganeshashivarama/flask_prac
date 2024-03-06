#print("Python with Visual Studio Code")

from flask import Flask

app = Flask(__name__)
@app.route('/')

def index():
    return "Introduction to Falsk!"

if __name__ == "__main__":
    app.run(debug=True, port=5001)