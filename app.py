from flask import Flask, render_template, request
app = Flask(__name__)

# Routes

@app.route("/")
def home():
    return render_template('form.html')

@app.route("/resume", methods=["GET", "POST"])
def CreateResume():
    name = request.form
    return render_template('resume.html', name = name)

# Execution of main code

if __name__ == '__main__':
    app.run(debug=True)

