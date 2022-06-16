import json

def load_db ():
    with open ('static/quotes.json') as file:
        return json.load(file)

def save_db ():
    with open ('static/quotes.json','w') as file:
        return json.dump(db, file)

db = load_db ()