# global builtin modules
import unittest
import os

# local imports
from app import create_app
from app.api.v2.utils.database import init_db, create_tables, drop_all_tables
import instance
from instance.config import app_config



class BaseTest(unittest.TestCase):
    '''test configurations'''

    def setUp(self):
        os.environ['TESTING_ENV'] = 'testing'
        self.app = create_app('testing')
        self.client = self.app.test_client()
        # init_db(db_url)
        # create_tables()

        # authentication
        self.user_1 = {
            "firstname": "jackie",
            "lastname": "gitari"
        }
        self.user_2 = {
            "firstname": "jackie",
            "lastname": "muthoni",
            "othername": "gitari",
            "email": "mary@gmail.com",
            "phone_number": "+254707802693",
            "username": "jackie",
            "password": "kajd23",
            "cpassword": "kajd23"

        }
        self.user_3 = {
            "firstname": "jackie",
            "lastname": "muthoni",
            "othername": "gitari",
            "email": "lukegmail.com",
            "phone_number": "+254707802693",
            "username": "jackie",
            "password": "R#kajd23",
            "cpassword": "R#kajd23"
        }
        self.user_4 = {
            "firstname": "jackie",
            "lastname": "muthoni",
            "othername": "gitari",
            "email": "jacklinem@gmail.com",
            "phoneNumber": "+254707802693",
            "username": "jackie",
            "password": "R#kajd23",
            "cpassword": "R#kajd23"
        }
        self.new_user = {
            "firstname": "jackie",
            "lastname": "muthoni",
            "othername": "gitari",
            "email": "felix@gmail.com",
            "phone_number": "+254707802693",
            "username": "jackie",
            "password": "R#kajd23",
            "cpassword": "R#kajd23"
        }
        self.nw_user = {
            "firstname": "jackie",
            "lastname": "muthoni",
            "othername": "gitari",
            "email": "luke@gmail.com",
            "phone_number": "+254707802693",
            "username": "jackie",
            "password": "R#kajd23",
            "cpassword": "R#kajd23"
        }
        self.user_5 = {
            "email": "wronggmail.com",
            "password": "wrong"
        }
        self.user_6 = {
            "email": "wrong@gmail.com",
            "password": "wrong"
        }
        self.user_7 = {
            "email": "jacklinem@gmail.com",
            "password": "wrong"
        }
        self.user_8 = {
            "email": "jackie@gmail.com",
            "password": "R#kajd23"
        }
        self.user_9 = {
            "email": "jackie@gmail.com",
        }
        # meetups

        #meetups
        self.meetup_1 ={
            "topic" : "Programming"
        }
        self.meetup_2 ={
            "id": "1",
            "topic" : "Programming",
            "location" : "Nairobi",
            "happeningOn" : "20/05/2019",
            "tags" : "['php','java']"
        }
        self.meetup_3 ={
            "id": "1",
            "topic" : "Programming",
            "location" : "Nairobi",
            "happeningOn" : "20/05/2019",
            "tags" : "['php','java']",
        }
        self.meetup_4 ={
            "id": "1",
            "topic" : "coding",
            "location" : "Nairobi",
            "happeningOn" : "20/05/2019",
            "tags" : "['php','java']"
        }
        self.rsvp_1 = {
            "user" : "1"
        }
        self.rsvp_2 = {
            "response" : "yes",
            "user" : "1"
        }
        self.rsvp_3 = {
            "response" : "yes",
            "user" : "1",
            "name" : "jackie"
        }

        return self.client

    def tearDown(self):
        print("Dropping tables")
        drop_all_tables()
