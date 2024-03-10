from flask import Flask

app = Flask(__name__)

@app.route('/')
def first():


if __name__ == '__main__':
    app.run(debug=True)
