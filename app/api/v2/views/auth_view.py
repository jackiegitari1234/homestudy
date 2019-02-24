# global builtin modules
import datetime
import os

# downloaded modules
from flask import jsonify, request, abort, make_response, json
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

# local imports
from app.api.v2 import vers2 as v2
from app.api.v2.models.auth_model import User
from app.api.v2.utils.validator import inputs_validate, hash_password
from app.api.v2.utils.database import init_db

inputs_validate = inputs_validate()


SECRET_KEY = os.getenv("SECRET")
os.environ['TESTING_ENV'] = 'production'


# sign up endpoint
@v2.route('/signup', methods=['POST'])
def register():

    # Check for json data
    data = request.get_json()
    if not data:
        abort(make_response(
            jsonify({"message": "POST of type Application/JSON expected"}),
            400))

    # Check for empty inputs
    if not all(field in data for field in ["firstname", "lastname",
                                           "othername", "email",
                                           "phone_number",
                                           "username", "password",
                                           "cpassword"]):
        abort(make_response(
            jsonify({"message": "All fields are required"}), 400))

    firstname = data['firstname']
    lastname = data['lastname']
    othername = data['othername']
    username = data['username']
    email = data['email']
    phone_number = data['phone_number']
    password = data['password']
    cpassword = data['cpassword']

    # validate email
    if not inputs_validate.email_validation(email):
        abort(make_response(
            jsonify({"message": "Your email is not valid"}), 400))

    # validate password
    if not inputs_validate.password_validation(password):
        abort(make_response(
            jsonify({"message": "Your password is not valid"}), 400))

    if not inputs_validate.compare_password(password, cpassword):
        abort(make_response(
            jsonify({"message": "Passwords do not match"}), 400))

    pwd = hash_password(password)  # encrypt the password
    new_user = User(firstname, lastname, othername,
                    username, email, phone_number, pwd)
    mb = new_user.register_user()
    if mb is None:
        return make_response(jsonify(
            {"message": "Email had already registered",
             "status": 400}))
    else:
        return make_response(jsonify({"message": "successfully registered",
                                      "status": 201}), 201)

# sign in endpoint


@v2.route('/signin', methods=['POST'])
def login():

    data = request.get_json()
    if not data:
        abort(make_response(
            jsonify({"message": "POST of type Application/JSON expected"}),
            400))

    # Check for empty inputs
    if not all(field in data for field in ["username", "password"]):
        abort(make_response(
            jsonify({"message": "Username and Paswword are required"}), 400))

    username = data['username']
    password = data['password']

    # check if email exists
    cur = init_db().cursor()
    query = "SELECT email from member WHERE username = %s;"
    cur.execute(query, (data['username'],))
    user_data = cur.fetchone()
    cur.close()

    if not user_data:
        abort(make_response(jsonify({"message": "User not Found"}), 404))


    cur = init_db().cursor()
    query = "SELECT password from member WHERE username = %s;"
    cur.execute(query, (data['username'],))
    user_data = cur.fetchone()
    cur.close()

    details = (user_data[0])
    print (details)
    if not inputs_validate.check_password(details, data['password']):
        print (inputs_validate.check_password(user_data, data['password']))
        abort(make_response(
            jsonify({"message": "Wrong Password"}), 400))

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200
  