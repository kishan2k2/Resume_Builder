from flask import Flask, render_template
import requests

app = Flask(__name__)

# Routes

@app.route("/")
def home():
    return render_template('form.html')

@app.route("/resume", methods=["POST"])
def CreateResume():
    name = requests.form['name']
    return render_template('form.html', name = name)

# Execution of main code

if __name__ == '__main__':
    app.run(debug=True)

