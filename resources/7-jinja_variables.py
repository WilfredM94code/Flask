from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('jinja_variables.html', title = 'This a Jinja variable', text = 'This is another Jinja variable')

if __name__ == '__main__':
    app.run(debug=True)