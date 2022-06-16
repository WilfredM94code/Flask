from flask import Flask,render_template, abort
db = __import__ ('9-model_layers_module')
db = db.db

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('jinja_templates.html', 
                            web_title = 'Web title', 
                            web_main_header = 'This is another Jinja variable that stores web main header',
                            web_text = 'Flask is definitely awesome. And this is also a Jinja variable')

@app.route('/quotes/<int:index>')
def quotes_view(index):
    try:
        quote_db = db [index]
        return render_template ('url_parameters.html',quote = quote_db)
    except IndexError:
        return render_template ('url_parameters_error.html')

@app.route('/quotes_other/<int:index>')
def quotes_view_other(index):
    try:
        quote_db = db [index]
        return render_template ('url_parameters.html',quote = quote_db)
    except IndexError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)