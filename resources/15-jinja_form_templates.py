from flask import Flask,render_template, abort, jsonify, request,redirect, url_for
import random
module = __import__ ('9-model_layers_module')
db = module.db
db_len = len(db) 

app = Flask(__name__)

def quotes(index):
    try:
        quote_db = (db[index],index)
        return render_template ('conditionals_jinja.html',quote = quote_db, index = index, max_index = len(db)  - 1)
    except IndexError:
        return render_template ('url_parameters_error.html')

@app.route('/')
def welcome():
    random_index = random.sample(range(0,len(db)),10)
    random_quotes = [(db[index],index) for index in random_index]
    return render_template('jinja_templates_2.html', 
                            web_title = 'Historic quotes', 
                            web_main_header = 'Welcome to this space of wisdom',
                            web_text = 'This in an effort to provide a space from ancient to modern wisdom',
                            random_quotes = random_quotes)


@app.route('/quotes/<int:index>')
def quotes_view(index):
    return quotes(index)

@app.route('/api/quote/')
def single_quote():
    random_index = random.randint(0,len(db))
    random_quote = db[random_index]
    return jsonify(random_quote)

@app.route('/api/quotes/')
def multiple_quote():
    random_index = random.sample(range(0,len(db)),10)
    random_quotes = [db[index] for index in random_index]
    return jsonify(random_quotes)

@app.route('/add_new_quote', methods = ['GET', 'POST'])
def new_quote():
    if request.method == 'POST':
        quote_dict = {
            'text' : request.form['quote'],
            'author' : request.form['author'] 
        }
        db.append (quote_dict)
        module.save_db ()
        return redirect (url_for('quotes_view', index = len(db) - 1))
    else:
        return render_template('jinja_form_templates_add.html')

@app.route('/remove_quote/<int:index>', methods = ['GET', 'POST'])
def remove_quote(index):
    try:
        if request.method == 'POST':
            del db[index]
            module.save_db ()
            return redirect (url_for('welcome'))
        else:
            return render_template('jinja_form_templates_remove.html', quote = (db[index],index))
    except IndexError:
        return render_template ('url_parameters_error.html')

@app.route('/random_quote/')
def random_quote():
    index = random.randint(0,len(db))
    return quotes(index)

if __name__ == '__main__':
    app.run(debug=True)