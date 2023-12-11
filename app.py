from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return render_template('resume.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
