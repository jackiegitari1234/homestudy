#downloaded modules
from flask import jsonify,request,abort,make_response

#local imports
from app.api.v2 import vers2 as v2
from app.api.v2.models.meetup_model import Meetup,check_admin,check_meet,delete_meetup,all_meetups,check_meetup,Rsvp
from app.api.v2.models.auth_model import User
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


@v2.route('/meetups', methods=['POST'])
@jwt_required
def add_meetup():

    current_user = get_jwt_identity()
    print (check_admin(current_user))
    member = check_admin(current_user)
    if member:
        print("is admin")
        user_data = request.get_json()

        if not user_data:
            abort(make_response(jsonify({"message":"Only Application/JSON input expected"}),400))
        
        # Check for empty inputs
        if not all(field in user_data for field in ["topic", "location", "happeningOn","tags","image"]):
            abort(make_response(jsonify({"message":"Please fill in all the required input fields"}),400))

        topic = user_data['topic']
        location = user_data['location']
        happeningOn = user_data['happeningOn']
        tags = user_data['tags']


        new_meetup = Meetup(topic,location,happeningOn,tags).register_meetup()
        abort(make_response(jsonify({"data":new_meetup}),201))
    abort(make_response(jsonify({"message":"You are not authorised to add a meetup"}),403))

@v2.route('/meetups/<int:id>', methods=['DELETE'])
@jwt_required
def delete_meetups(id):

    current_user = get_jwt_identity()
    member = check_admin(current_user)
    if member:
        print("is admin")
        if check_meet(id) == True:
            delete_meetup(id)
            abort(make_response(jsonify({"message":"Meetup sucessfully deleted"}),400))
        abort(make_response(jsonify({"message":"Meetup not found"}),400))
    abort(make_response(jsonify({"message":"You are not authorised to add a meetup"}),403))

@v2.route('/meetups', methods=['GET'])
def get_meetups():
    abort(make_response(jsonify({"meetups":all_meetups()}),200))

@v2.route('/meetups/<int:id>', methods=['GET'])
def each_meetups(id):
    if check_meetup(id) == False:
        abort(make_response(jsonify({"meetup":"meetup not found"}),200))
    abort(make_response(jsonify({"meetup":check_meetup(id)}),200))

@v2.route('/meetups/<int:id>/rsvp', methods=['POST'])
@jwt_required
def rsvp_meetups(id):

    current_user = get_jwt_identity()
    user_data = request.get_json()
    if check_meet(id) == True:
        if not user_data:
            abort(make_response(jsonify({"message":"Only Application/JSON input expected"}),400))
        
        # Check for empty inputs
        if not all(field in user_data for field in ["response"]):
            abort(make_response(jsonify({"message":"Please fill in a response"}),400))

        response = user_data['response']
        new_rsvp = Rsvp(id,current_user,response).add_rsvp()
        abort(make_response(jsonify({"data":new_rsvp}),201))

    abort(make_response(jsonify({"message":"Meetup not found"}),400))
    
