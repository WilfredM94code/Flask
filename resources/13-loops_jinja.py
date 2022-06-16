from flask import Flask,render_template, abort
import random
db = __import__ ('9-model_layers_module')
db = db.db
db_len = len(db) 

app = Flask(__name__)

@app.route('/')
def welcome():
    random_index = random.sample(range(0,db_len),10)
    random_quotes = [(db[index],index) for index in random_index]
    return render_template('jinja_templates_2.html', 
                            web_title = 'Web title', 
                            web_main_header = 'This is another Jinja variable that stores web main header',
                            web_text = 'Flask is definitely awesome. And this is also a Jinja variable',
                            random_quotes = random_quotes)

@app.route('/quotes/<int:index>')
def quotes_view(index):
    try:
        quote_db = db [index]
        return render_template ('conditionals_jinja.html',quote = quote_db, index = index, max_index = db_len - 1)
    except IndexError:
        return render_template ('url_parameters_error.html')

if __name__ == '__main__':
    app.run(debug=True)