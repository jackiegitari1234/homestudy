from datetime import datetime
import psycopg2
from app.api.v2.utils.database import init_db


class User(object):

    def __init__(self, *args):
        self.firstname = args[0]
        self.lastname = args[1]
        self.othername = args[2]
        self.username = args[3]
        self.email = args[4]
        self.phone_number = args[5]
        self.password = args[6]
        self.db = init_db()

    def register_user(self):
        new_user = {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'isAdmin': False,
            "username": self.username,
            "phone_number": self.phone_number,
            "othername": self.othername,
            'registered': datetime.now(),
            "email": self.email,
            "password": self.password
        }
        try:
            query = """
                    INSERT INTO member(public_id, firstname, lastname,
                    othername, PhoneNumber, isAdmin, registered, username,
                    email, password) 
                    VALUES (1, %(firstname)s, %(lastname)s, %(othername)s,
                    %(phone_number)s, %(isAdmin)s,%(registered)s, %(username)s,
                    %(email)s,%(password)s) ;
                    """
            cur = self.db.cursor()
            cur.execute(query, new_user)
            self.db.commit()
            return new_user
        except (Exception, psycopg2.Error) as error:
            print(error)
 
