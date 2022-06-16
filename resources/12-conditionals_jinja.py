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
        return render_template ('conditionals_jinja.html',quote = quote_db, index = index, max_index = len(db) - 1)
    except IndexError:
        return render_template ('url_parameters_error.html')

if __name__ == '__main__':
    app.run(debug=True)