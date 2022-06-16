from flask import Flask,render_template
db = __import__ ('9-model_layers_module')
db = db.db

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('jinja_templates.html', 
                            web_title = 'Web title', 
                            web_main_header = 'This is another Jinja variable that stores web main header',
                            web_text = 'Flask is definitely awesome. And this is also a Jinja variable')

@app.route('/quotes')
def quotes_view():
    quote_db = db [0]
    return render_template ('model_layers.html',quote = quote_db)

if __name__ == '__main__':
    app.run(debug=True)