from flask import Flask, render_template, url_for, request, session, redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient
import bcrypt

client = MongoClient('localhost', 27017)
db = client.some_database
collection = client.db['database']
app = Flask(__name__)

the_dictionary = request.data
username = the_dictionary.keys()
password = request.data.values()

#users_and_pass = dict()
#need variable to store username, get it from database
#need variable to store password, get that from databses

app.config['MONGO_DBNAME'] = 'mongodb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017' #need URL
mongo = PyMongo(app)


@app.route('/')
def index():
  if request.data.username in session: #need username in quotes
    return ('You\'re logged in!', list_of_contacts)
  return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
  users = mongo.db.users
  for x in users.keys():
        #list_of_users.append(x)

    login_user = users.find_one({'name' : request.form[username]}) #need variable

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user[username].encode('utf-8')) == login_user[''].encode('utf-8'):
            session[username] = request.form[username]
            return redirect(url_for('index'))

    return 'Invalid username/password'
    

@app.route('/register', methods=['POST', 'GET'])
def register_user():
   if request.method == 'POST':
       users = mongo.db.users
       existing_user = users.find_one({'name' : request.form[username]})

       if existing_user is None:
           hashpass = bcrypt.hashpw(request.form[username].encode('utf-8'), bcrypt.gensalt())
           users.insert({'name' : request.form[username], '' : hashpass})
           session[username] = request.form[username]
           return redirect(url_for('index'))

       return render_template('register.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)