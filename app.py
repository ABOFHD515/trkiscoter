from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # صفحة البداية لاختيار السكوتر

@app.route('/race')
def race():
    return render_template('race.html')  # صفحة السباق

if __name__ == '__main__':
    app.run(debug=True)
