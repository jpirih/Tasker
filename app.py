from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """Main page view controller"""
    title:str = 'Home'
    return render_template('main/index.html', title=title)
