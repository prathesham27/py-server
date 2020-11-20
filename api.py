
import flask
import mysql.connector
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

app.config["DEBUG"] = True
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="shopping_cart"
)
print(mydb)

@app.route('/', methods=['GET'])
def home():
    return "<h1>MY First Page</p>"

@app.route('/signin', methods=['POST'])
def signIn():
    data = flask.request.get_json()
    userName = data.get('userName')
    password = data.get('password')
    print("Request User Name is:" + userName)
    print("Request Password is :" + password)
    mycursor = mydb.cursor()

    sql = "SELECT * FROM user WHERE user_name = '" + userName + "' and password ='" + password +"'"
    print(sql)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print(mycursor.rowcount)
    if mycursor.rowcount == 0:
        print("notfound")
        return {
            "success": False
        }
    else:
        print("found")
        return {
            "success": True
        }

@app.route('/signup', methods=['POST'])
def signup():
    data = flask.request.get_json()
    userName = data.get('user_name')
    password = data.get('password')
    first_name = data.get('intial_name')
    last_name = data.get('final_name')
    print("user_name=:" + userName)
    print("password=:" + password)
    print("initial_name=:" + first_name)
    print("final_name=:" + last_name)

    mycursor = mydb.cursor()
    sql = "INSERT INTO user (user_name,password,first_name,last_name) VALUES (%s,%s,%s,%s)"
    val = (userName, password, first_name, last_name)
    mycursor.execute(sql,val)
    mydb.commit()
    return {
        "success": True
    }

@app.route('/update', methods=['POST'])
def updateUser():
    data = flask.request.get_json()
    userName = data.get('user_name')
    first_name = data.get('intial_name')
    last_name = data.get('final_name')
    print("user_name=:" + userName)
    print("initial_name=:" + first_name)
    print("final_name=:" + last_name)
    mycursor = mydb.cursor()
    sql = "UPDATE user SET first_name =%s, last_name=%s WHERE user_name = %s";
    val = (first_name,last_name,userName)
    mycursor.execute(sql,val)
    mydb.commit()


    return {
        "success": True
    }



app.run()