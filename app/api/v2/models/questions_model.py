from datetime import datetime
import psycopg2
from app.api.v2.utils.database import init_db


class Question(object):

    def __init__(self, *args):
        self.meetup_id = args[0]
        self.username = args[1]
        self.title = args[2]
        self.body = args[3]
        self.db = init_db()

    def add_quiz (self):
        new_quiz = {
            'meetup_id': self.meetup_id,
            'username': self.username,
            "title": self.title,
            "body": self.body
        }
        try:
            query = """
                    INSERT INTO questions(meetup_id, created_by, title,body,votes) 
                    VALUES (%(meetup_id)s, %(username)s, %(title)s,%(body)s,0
                    ) ;
                    """
            cur = self.db.cursor()
            cur.execute(query, new_quiz)
            self.db.commit()
            return new_quiz
        except (Exception, psycopg2.Error) as error:
            print(error)

class Comment(object):

    def __init__(self, *args):
        self.quiz_id = args[0]
        self.username = args[1]
        self.comment = args[2]
        self.db = init_db()

    def add_comment (self):
        new_comment = {
            'quiz_id': self.quiz_id,
            'username': self.username,
            "comment": self.comment
        }
        try:
            query = """
                    INSERT INTO comments(question_id, created_by, body) 
                    VALUES (%(quiz_id)s, %(username)s, %(comment)s
                    ) ;
                    """
            cur = self.db.cursor()
            cur.execute(query, new_comment)
            self.db.commit()
            return new_comment
        except (Exception, psycopg2.Error) as error:
            print(error)

class Votes(object):

    def __init__(self, *args):
        self.username = args[0]
        self.quiz_id = args[1]
        self.upvote = args[2]
        self.value = args[3]
        self.db = init_db()

    def add_vote(self):
        quiz_id = self.quiz_id
        # username= self.username
        # upvote = self.upvote
        
        new_vote = {
            'quiz_id': self.quiz_id,
            'username': self.username,
            "comment": self.upvote
        }
        try:
            query = """ 
                    INSERT INTO votes(question_id, created_by, status) 
                    VALUES ( %(quiz_id)s, %(username)s, %(comment)s
                    ); 
                    """
            cur = self.db.cursor()
            cur.execute(query, new_vote)
            self.db.commit()

            query = "SELECT votes FROM questions WHERE id= %s"
            cur = self.db.cursor()
            cur.execute(query, (quiz_id,))
            user_exists = cur.fetchone()
            cur.close()

            details = (user_exists[0])
            total = (int(details) + int(self.value))

            query1 = """
                    UPDATE questions SET votes = %s WHERE id = %s
                    ;
                    """

            cur = self.db.cursor()
            cur.execute(query1, (total,quiz_id,))
            self.db.commit()
            return new_vote
        except (Exception, psycopg2.Error) as error:
            print(error)

def check_voter(id,username,vote):
    try:
        cur = init_db().cursor()
        query = "SELECT id FROM votes WHERE question_id = %s AND created_by= %s AND status= %s"
        cur.execute(query, (id,username,vote))
        user_exists = cur.fetchone()
        cur.close()

        details = (user_exists[0])
        print (details)
        if details:
            return True
        return False
    except (Exception, psycopg2.Error) as error:
        print(error)