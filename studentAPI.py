
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
  database="students_db"
)
print(mydb)

# RegNumber, Student Name, DOB, AGE, Standard, Parent Name, Blood Group
@app.route('/', methods=['GET'])
def home():
    return "<h1>MY First Page</p>"

@app.route('/student/create', methods=['POST'])
def studentCreate():
    data = flask.request.get_json()
    regNo = data.get('regNumber')
    studentName = data.get('studentName')
    DOB = data.get('dob')
    parentName = data.get('parentName')
    bloodGroup = data.get('bloodGroup')
    print("Register Number is=" + regNo)
    print("Student Name is=" + studentName)
    print("DOB is=" + DOB)
    print("Parent Name is=" + parentName)
    print("Blood Group is=" + bloodGroup)
    mycursor = mydb.cursor()
    sql = "INSERT INTO studenttable (RegNo,StudentName,DOB,ParentName,BloodGroup) VALUES (%s,%s,%s,%s,%s)"
    val = (regNo, studentName, DOB, parentName, bloodGroup)
    mycursor.execute(sql, val)
    mydb.commit()
    return {
        "success": True
    }

@app.route('/student/update', methods=['POST'])
def studentUpdate():
    data = flask.request.get_json()
    regNo = data.get('regNumber')
    studentName = data.get('studentName')
    DOB = data.get('dob')
    parentName = data.get('parentName')
    bloodGroup = data.get('bloodGroup')
    print("Register Number is=" + regNo)
    print("Student Name is=" + studentName)
    print("DOB is=" + DOB)
    print("Parent Name is=" + parentName)
    print("Blood Group is=" + bloodGroup)
    # update Query Goes Here
    mycursor = mydb.cursor()
    sql = "UPDATE studenttable SET StudentName =%s, DOB =%s, ParentName =%s, BloodGroup =%s WHERE regNo=%s"
    val = (studentName, DOB, parentName, bloodGroup,regNo)
    mycursor.execute(sql, val)
    mydb.commit()
    return {
        "success": True
    }

@app.route('/student/delete', methods=['POST'])
def studentdelete():
    data = flask.request.get_json()
    regNo = data.get('regNumber')
    mycursor = mydb.cursor()
    sql = "DELETE FROM studenttable WHERE RegNo = %s"
    val = (regNo)
    mycursor.execute(sql, val)
    mydb.commit()

@app.route('/student/select', methods=['POST'])
def studentSelect():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM studenttable"
    mycursor.execute(sql )
    myresult= mycursor.fetchall()
    return{
        "success": True,
        "data": myresult
    }

app.run()