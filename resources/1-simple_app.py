from flask import Flask

app = Flask(__name__)
print ('app = ', app)
print ('type(app) = ',type(app))

@app.route('/')
def welcome():
    return 'This is my very first Flask app'

if __name__ == '__main__':
    app.run(debug=True)