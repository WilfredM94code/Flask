# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# -----------------------------------------------------------------

# File: /resources/1-simple_app.py

# Flask is a Python framework tht allows to create web applications. It has 
# no database abstraction layer.

# The versatility of this framework allows to create apps employing 
# multiple other Python libraries to provide a more rich environment
# to develop web apps. It has two ´rimary componentes:

# 1 - Jinja: Is used to create HTML templates
# 2 - Werkzeug: is a utility  for Web Server Gateway Interface 
# (WSGI) applications. Werkzeug can instantiate objects for request, 
# response, and utility functions. 

# Flask is installed under the command line on terminal:
# 'pipenv install flask' or 'pip install flask'

from flask import Flask

app = Flask(__name__)
print ('app = ', app)
print ('type(app) = ',type(app))
# This process returns a <class 'flask.app.Flask'> object

@app.route('/')
def welcome():
    return 'This is my very first Flask app'
# This process allows to create a landing site once sent na http request 
# to the server. In this case, since the attribute of the decorator
# recieves an '/' as a string that completes the rute URL.

# Every argument icluded within the '.route('/')' decorator attribute 
# will be considered an URL.

# The 'welcome' function will be a type of function # (given the Flask 
# context) called view function which is a function meant to respond to
# an http request. This function have their functionallity enhanced by
# the usage of the decorators of the <class 'flask.app.Flask'> object.
# In this case the '.route()' one.


app.run(debug=True)
# This process allows to run the web app. 

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# ---------------------- Development server -----------------------
# -----------------------------------------------------------------

# File: /resources/2-development_server.py

# A Development server must not be running as the production server since 
# it's not secure. Is a bad practice to deply an app using the developer 
# server. Such server is used whenever is intended to test the app in an
# 'isolated' environment

# Once started the app it will return in the console the next message:

#  * Serving Flask app '2-development_server' (lazy loading)
#  * Environment: production
#    WARNING: This is a development server. Do not use it in a production deployment.
#    Use a production WSGI server instead.
#  * Debug mode: on
#  * Debugger is active!
#  * Debugger PIN: 126-949-115

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# ----------------------- App flow control ------------------------
# -----------------------------------------------------------------

# File: /resources/3-app_flow_control.py

# The execution of an application doesn't  follo the common Python script
# execution which goes from top to bottom. It executes every function in
# repose to the HTTP requests  associated to the web page, and this sever
# is created given by Flask. Every time is sent a request to the Flask
# server it will display the request in the terminal where the app is 
# being executed. This is called the server log

# For instance:

# 127.0.0.1 - - [05/Jun/2022 21:52:31] "GET / HTTP/1.1" 200 -

# 127.0.0.1 - - [05/Jun/2022 21:52:31] "GET /favicon.ico HTTP/1.1" 404 -
# 127.0.0.1 - - [05/Jun/2022 21:52:42] "GET / HTTP/1.1" 200 -

# Note that every view function will be called or executed every time an
# user sends a request to the URL associated with such function

# If an app is modified when executed the server will restart to apply the
# changes and keep running. It will display this log:

# * Restarting with stat

# There's a common practice whenever creating a view function and an
# URL and it is that both commonly shrare the same name

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# --------------------------- Debugging ---------------------------
# -----------------------------------------------------------------

# File: /resources/4-debugging.py

# There are several mistakes while making view functions. One of which is 
# overwriting the view. For instance. If the 'cool' view function is 
# overrwrited it will raise the next error:

# AssertionError: View function mapping is overwriting an existing endpoint function: cool

# Whenever is referenced the endpoint it is refering to the URL, the route
# that can be accessed by an user

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# ------------------ URL/View functions mapping -------------------
# -----------------------------------------------------------------

# File: /resources/5-url_view_mapping.py

# To check the way every url from an app is linked to every view function
# there can be used several attributes of the app.

app = __import__ ('5-url_view_mapping')
# NOTE: The '__import__ ('5-url_view_masking.py')' method is used to 
# import modules with problematic names lithe those starting with a sign,
# number, etc. It is no different to use the 'import hey_im_a_module'
# syntax commonly used

# Once imported our app there can be used the next set of attributes
print ('app.app.url_map = ',app.app.url_map)
print ('type(app.app.url_map) = ',type(app.app.url_map))
# This attribute return a <class 'werkzeug.routing.Map'> object that
# that prints the URL/View functions

# The map will have this structure:
# Map([<Rule '/view_count' (OPTIONS, HEAD, GET) -> view_count>,
#  <Rule '/cool' (OPTIONS, HEAD, GET) -> cool>,
#  <Rule '/' (OPTIONS, HEAD, GET) -> welcome>,
#  <Rule '/static/<filename>' (OPTIONS, HEAD, GET) -> static>])

# Among every view function defined there's the 'static' function related
# to the '/static/<filename>' URL. This 'static' URL is a pre-dedicated 
# space to store any file meant to be served/employed by the app. This 
# space is located within the '/resources/' folder of this repository
# and it will store several files to test. This file is supposed to store
# any media, CSS and/or Javascript files

# The 'img.png' file was provided and it can be accesed using the next URL:
# http://127.0.0.1:5000/static/img.png

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# ------------------ Model-Template-View pattern ------------------
# -----------------------------------------------------------------

# File: /resources/6-mod_temp_view_pattern.py, /resources/templates/home.html


# The Model-Template-View pattern is an architecture that allows to create
# web applications employing best practices on how to organize best the 
# code. This is considered as the same model called model view-controller.

# The MTV pattern there must be created templates meant to be employed and
# a library called Jinja to implement such functionallity.

# There is a folder called 'templates' within the '/resources/' folder of
# this repository meant to store the templates of the flask application.

# Once created a template and stored within the 'templates' folder such 
# template can be associated to a view function

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

# Note that the return of the view function is a function that indicates to 
# the Flask server to return the particular HTML file related to the URL of
# the view function

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# ------------------------ Jinja variables ------------------------
# -----------------------------------------------------------------

# File: /resources/7-jinja_variables.py, /resources/templates/jinja_variables.html

# Jinja variables are a type of variable that are meant to be defined within
# Python and displayed within the HTML file/template and these are embeded
# within the HTML file by using a variable name within '{{ variablename }}'

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# ------------------------ Jinja templates ------------------------
# -----------------------------------------------------------------

# File: /resources/8-jinja_templates.py, /resources/templates/jinja_templates.html

# Jinja tempates are interpreted as a text file, processed withun the Flask
# server and then passed as an HTML file. Whenever a template file is 
# executed the web browser will take the HTM file along with every Jinja 
# variable and execute it as a string. But whenever a template is 
# interpreted by a Flask server it provides the HTML file along with every 
# Jinja variables and package it as the HTTP response to the user.

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# -------------------------- Model layer --------------------------
# -----------------------------------------------------------------

# File: /resources/9-model_layers.py, /resources/9-model_layers_module.py, /resources/templates/model_layers.html

# The model layer provides functionallity to connect to an actual database. 
# For this particular case data will be stored in a JSON file. The model layer
# allows to work also with JSON files. To connect with a database it is 
# better practice to stablish the connection and the query procces from
# another python script/module and then passing it to the Flask 
# application. This allows to have a claner code and to provide a 
# more adaptable app to recicle code if necesary. Then the data 
# can be passed as a Jinja variable to be displayed into the app.

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# ------------------------ URL parameters -------------------------
# -----------------------------------------------------------------

# File: /resources/10-url_parameter.py, /resources/9-model_layers_module.py, /resources/templates/url_parameter.html

# Within the '.route()' decorator function there can be created a 
# dynamic URL that actually provides to the app the flexibility to
# display a particular URL for sets of items within (for instance)
# a database. This particular ULR can be accessed using (for instance)
# a next button that iterates within a list, json file, etc, to 
# request different items and displacing the index that selects an
# item. This URL will act as a parameter or as an argument that 
# can be used to interact with the Flask app. This new paramenter
# has to be defined as a variable within the view function and
# interact with the index of an iterable, which, in this case, 
# will be a JSON file. 
# 
# Whenever an URL error occurs within the URL index or any other
# file there can be created an try/except block. 
# For every 'problematic' response related to the HTTP request
# sent there must be considered that Flast provides a set of
# default view funvtions returns. But if wanted to provide a 
# particular response to every particular error there can be 
# returned a 'render_template()' function.

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# ------------------ Building links in templates ------------------
# -----------------------------------------------------------------

# File: /resources/11-links.py, /resources/9-model_layers_module.py, /resources/templates/links.html

# To navigate through a website with a dynamic URL the user can type 
# manullay the index to access every item within the JSON database 
# (in this particular case), but given the impractical implication 
# related to this method, it is better to provide a dynamic way 
# of accessing the next item. For such purpuse there can be built
# a Jinja variable embeded within the 'anchor' tag, particularly
# into the 'href' attribute, as a component of the URL. To stablish
# a relation from the HTML file and the Flask app there must be
# defined the index value as a Jinja variable within the 
# 'render_template()' function.

# In case the parent URL of a file within the '.route()' argument of the
# decorator of the view function there can be conflicts when accessing
# certain URL. To automatically provide a solution for any change related
# to the mapping of a website, there can be passed, as a Jinja variable, a
# function called url_for() wich recieves the view function associated with
# a page and the variable that is supposed to change using the keyword/value
# syntax as shown below:

# <a href="{{url_for ('quotes_view',index = index + 1)}}">Next Quote Button using the 'url_for()' function</a>

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# --------------------- Conditionals in Jinja ---------------------
# -----------------------------------------------------------------

# File: /resources/12-conditionals_jinja.py, /resources/9-model_layers_module.py, /resources/templates/conditionals_jinja.html

# To add more functionallity and to avoid the 'IndexError' displayed 
# everytime the user goes further the index/page 1623 there can be placed 
# a conditional embeded within the HTML code. This conditional works
# under the Jinja syntax, which is considered a Jinja conditional.

# The conditionals in Jinja are composed as the content of an HTML element
# and it has the next syntax/notation:

# <button>
#     {% if index < max_index %}
#     <a href="{{url_for ('quotes_view',index = index + 1)}}">Next Quote Button </a>
#     {% else %}
#     <a href="{{url_for ('quotes_view',index = 0)}}">Go back to the fisrst quote</a>
#     {% endif %}
# </button>

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# ------------------------ Loops in Jinja -------------------------
# -----------------------------------------------------------------

# File: /resources/13-loops_jinja.py, /resources/9-model_layers_module.py, 
# /resources/templates/jinja_templates_2.html

# As well as with conditionals there can be also used the Jinja syntax
# to provide loops within the HTML code. This can be used to control
# the flow of a web app.


# The for loops in Jinja are composed as the content of an HTML element
# and it has the next syntax/notation:

# <ul>
#     {% for quote in random_quotes %}
#     <li>
#         <a href="{{ url_for('quotes_view', index = quote[1]) }}">{{ quote[0].text }}</a>
#     </li>
#     {% endfor %}
# </ul>

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# --------------------------- Rest API ----------------------------
# -----------------------------------------------------------------

# File: /resources/14-rest_api.py, /resources/9-model_layers_module.py, 

# A REST API stands for Representation State Transfer Application 
# Programming Interface

# For this exercise there will be created two particular new view functions.
# One is to provide one quote and the other to provide a list of quotes.
# This data will be provided in a JSON file. This can be achieved by using
# a Flask function called 'jsonify()' and apssing as an argument the JSON
# element meant to be recieved when requesting a response from a 
# particular URL.

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# ---------------------- Jinja form templates ---------------------
# -----------------------------------------------------------------

# File: /resources/15-jinja_form_templates.py, /resources/9-model_layers_module.py, 
# /resources/templates/jinja_form_templates.html, /resources/templates/jinja_form_templates_remove.html

# HTML allows to send information to the server, and such information can
# be processed by a Flask app

# To allow this to happen, there must be privded within the '.route()' 
# decorator method an additional argument besides the URL, and such 
# argument is the HTTP methods that this page will allow. By default this 
# value will be setted to only accept the GET method within the request,
# but since it is required to recieve data from a form it has to also
# accept the POST method which will be added using the next syntax

# @app.route('/add_new_quote', method = ['GET', 'POST'])

# Every request made by an user employs a method (being GET to request
# the content of an URL to the server or POST to pass information to the 
# server) that is recieved by the server, and depending on the method
# within the request, a website can act in a different war. For instance:

# @app.route('/add_new_quote', methods = ['GET', 'POST'])
# def new_quote():
#     if request.method == 'POST':
#         return redirect (url_for('quotes_view', index = len(db) - 1))
#     else:
#         return render_template('jinja_form_templates.html')

# Each of any method on the made request can lead to a different behaviour 
# of the URL

# In this particular case, the '/add_new_quote' URL is meant to recieve
# the data provided within a form and then add a new quote to a JSON 
# database.

# There's also a way to dlete data from a database, and even ask for a 
# confirmation. Such methodology can be seen within these files:

# /resources/templates/jinja_form_templates_remove.html
# /resources/15-jinja_form_templates.py

# -----------------------------------------------------------------
# ----------------------------- Flask -----------------------------
# --------------------- Styling HTML with CSS ---------------------
# -----------------------------------------------------------------



# A stylized and clean version for this web app will be stored in 
# an extern repository within the 'WilfredM94code' github account 
# as 'quotes web app' 