from datetime import datetime
import psycopg2
from app.api.v2.utils.database import init_db


class Meetup(object):

    def __init__(self, *args):
        self.topic = args[0]
        self.location = args[1]
        self.happeningOn = args[2]
        self.tags = args[3]
        self.db = init_db()

    def register_meetup(self):
        new_meetup = {
            'topic': self.topic,
            'location': self.location,
            "happeningOn": self.happeningOn,
            "tags": self.tags
        }
        try:
            query = """
                    INSERT INTO meetups(topic, location, happeningOn,tags) 
                    VALUES (%(topic)s, %(location)s, %(happeningOn)s,
                    %(tags)s) ;
                    """
            cur = self.db.cursor()
            cur.execute(query, new_meetup)
            self.db.commit()
            return new_meetup
        except (Exception, psycopg2.Error) as error:
            print(error)


class Rsvp(object):

    def __init__(self, *args):
        self.meetup_id = args[0]
        self.username = args[1]
        self.response = args[2]
        self.db = init_db()

    def add_rsvp (self):
        new_rsvp = {
            'meetup_id': self.meetup_id,
            'username': self.username,
            "response": self.response,
        }
        try:
            query = """
                    INSERT INTO rsvp(meetup_id, username, response) 
                    VALUES (%(meetup_id)s, %(username)s, %(response)s
                    ) ;
                    """
            cur = self.db.cursor()
            cur.execute(query, new_rsvp)
            self.db.commit()
            return new_rsvp
        except (Exception, psycopg2.Error) as error:
            print(error)


def check_admin(current_user):
    try:
        cur = init_db().cursor()
        # print(current_user)
        query = "SELECT isAdmin FROM member WHERE username= %s"
        cur.execute(query, (current_user,))
        user_exists = cur.fetchone()
        cur.close()

        details = (user_exists[0])
        print(details)

        if details == True:
            return True
        return False
    except (Exception, psycopg2.Error) as error:
        print(error)

def check_meet(id):
    try:
        cur = init_db().cursor()
        query = "SELECT * FROM meetups WHERE id= %s"
        cur.execute(query, (id,))
        all_meetups = cur.fetchone()
        cur.close()

        details = (all_meetups[0])
        if details == None:
            return False
        return True
    except (Exception, psycopg2.Error) as error:
        print(error)

def check_quiz(id):
    try:
        cur = init_db().cursor()
        query = "SELECT * FROM questions WHERE id= %s"
        cur.execute(query, (id,))
        all_meetups = cur.fetchone()
        cur.close()

        details = (all_meetups[0])
        if details == None:
            return False
        return True
    except (Exception, psycopg2.Error) as error:
        print(error)

def delete_meetup(id):
    try:
        db= init_db()
        cur = db.cursor()
        query = "DELETE FROM meetups WHERE id= %s "
        cur.execute(query, (id,))
        db.commit()
        return "deleted sucessfully"

    except (Exception, psycopg2.Error) as error:
        print(error)

    
def all_meetups():
    try:
        cur = init_db().cursor()
        query = "SELECT * FROM meetups "
        cur.execute(query, (id,))
        all_meetups = cur.fetchall()
        cur.close()

        if all_meetups == None:
            return "not found"
        return  all_meetups
    except (Exception, psycopg2.Error) as error:
        print(error)
        
def check_meetup(id):
    try:
        cur = init_db().cursor()
        query = "SELECT * FROM meetups WHERE id= %s";
        cur.execute(query, (id,))
        all_meetups = cur.fetchone()
        cur.close()

        details = (all_meetups)
        if details == None:
            return False
        return details
    except (Exception, psycopg2.Error) as error:
        print(error)
        