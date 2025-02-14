from flask import Flask, render_template
from utilities import cards

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', cards=cards)


if __name__ == '__main__':
    app.run()