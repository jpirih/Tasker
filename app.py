from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is Main Page'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
