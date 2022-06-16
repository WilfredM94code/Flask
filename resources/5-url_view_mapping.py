from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'This is my very first Flask app'

@app.route('/cool')
def cool():
    return 'Flask is awesome!'

counter = 0
@app.route('/view_count')
def view_count():
    global counter
    counter += 1
    return f'View count {counter}'

if __name__ == '__main__':
    app.run(debug=True)