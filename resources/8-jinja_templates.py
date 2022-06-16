from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('jinja_templates.html', 
                            web_title = 'Web title', 
                            web_main_header = 'This is another Jinja variable that stores web main header',
                            web_text = 'Flask is definitely awesome. And this is also a Jinja variable')

if __name__ == '__main__':
    app.run(debug=True)