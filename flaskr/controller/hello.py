from flask import Flask, request, jsonify, Blueprint
# from model import User
from flask_cors import CORS
import psycopg2

hello_page = Blueprint('hello_page', __name__, template_folder='templates')

userName_Password = {}  # temporary storage for user and password


@hello_page.route('/', methods=['GET'])
def index():
    return "Hello, World!"


@hello_page.route("/register", methods=['POST'])
def creat_register():
    def creat_register():
    # generate register info
        data = request.get_json()
        user_info = data['body']
        user_phone = user_info['phoneNumber']
        user_password = user_info['password']
        user_age = user_info['age']
        user_gender = user_info['gender']
        user_weight = user_info['weight']
        user_heightFt = user_info['heightFt']
        user_heightIn = user_info['heightIn']
        user_name = user_info['name']
        user_email = user_info['eMail']

        # add info to DB
        try:
            conn = psycopg2.connect(
                database='teamfit',
                user='root',
                port='26257',
                host='localhost',
                sslmode='disable'
            )
            print(conn.get_dsn_parameters(), "\n")
            with conn.cursor() as cur:
                cur.execute("CREATE TABLE IF NOT EXISTS teamfit.user(PhoneNumber INTEGER PRIMARY KEY, PassWord VARCHAR, Email VARCHAR, UserName VARCHAR, Age INT, HeightFt INT , HeightIn INT ,Weight INT , Gender VARCHAR, Image VARCHAR);")
                cur.execute("SELECT PhoneNumber from teamfit.user")
                rows = cur.fetchall()

                for i in rows:
                    print(type(user_phone))

                    if i[0] == int(user_phone):
                        print("hahaha")
                        cur.close()
                        conn.close()
                        return jsonify({'state': "Account already exist"})
                cur.execute("INSERT INTO teamfit.user(PhoneNumber, PassWord, Email, UserName, Age, HeightFt , HeightIn, Weight, Gender) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (user_phone, user_password, user_email, user_name, user_age, user_heightFt, user_heightIn, user_weight, user_gender))
                conn.commit()
                return jsonify({'state': "Register successful"}), 200  #or use render to shows the login page  # shows register page
            cur.close()
            conn.close()
        except (Exception, psycopg2.Error) as error:
            print(" ", error)
            return jsonify("Error while connecting to PostgreSQL"), 200  #or use render to shows the login page  # shows register page
    # or use render to shows the login page  # shows register page

def _getUsername():
    return _userEmail


@hello_page.route("/login", methods=['POST'])
def login():
    global _userEmail
    data = request.get_json()
    user_info = data['body']
    user_email = user_info['uEmail']
    use_password = user_info['uPassword']





    if user_email in userName_Password:
        if use_password == userName_Password[user_email]:
            _userEmail = user_email
            return jsonify({'state': "Successful login"}), 200  # success login and go to home page
        else:
            return jsonify({'state': "Password wrong"}), 200
    else:
        return jsonify({'state': "Account not exist"}), 200  # fail login and will stay this page
