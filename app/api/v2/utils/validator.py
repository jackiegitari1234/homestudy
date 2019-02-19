# global builtin modules
import re

# downloaded modules
from werkzeug.security import generate_password_hash, check_password_hash


class inputs_validate():
    def email_validation(self, email):
        return re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email)

    def password_validation(self, password):

        if len(password) < 6:
            return False

        total = {}

        for letter in password:
            if letter.islower():
                total['has_lower'] = 1

            if letter.isupper():
                total['has_upper'] = 1

            if letter.isdigit():
                total['has_digit'] = 1

        return sum(total.values()) == 3

    def compare_password(self, password, cpassword):
        if password == cpassword:
            return True

    # compare password stored and user input
    def check_password(self, hash_pwrd, password):
        return check_password_hash(hash_pwrd, password)

# hash the password


def hash_password(password):
    password_hash = generate_password_hash(password)
    return password_hash
