from flask import render_template
from werkzeug.security import check_password_hash, generate_password_hash
from talk_to_database import *
from talk_to_text_file import *


class User:
    id = ""
    username = ""
    password = ""
    email = ""
    status = ""

    # Parameterized constructor
    def __init__(self, name, email, password, status):
        self.name = name
        self.email = email
        self.password = password
        self.status = status

    # read usernames and passwords
    def does_user_exist(self):
        query =f"SELECT * FROM HAGZ.user"
        users = get_database(query)
        for user in users:
            if (self.email == user[2]):
                if(check_password_hash(user[3], self.password)):
                    return user
                return 0
        return -1

    # add user to database function 
    def add_user_to_database(self):
        hashed_password = generate_password_hash(self.password)
        query = f"INSERT INTO HAGZ.user (name, email, password, status) VALUES (%s, %s, %s, %s);"
        values = (self.name, self.email, hashed_password, self.status)
        set_database(query, values)
    

    # sign in function
    def sign_in(self):
        user = self.does_user_exist()
        if user != 0 and user != -1:
            set_user_info(str(user[0]), user[4])
            return user
        else:
            return False

    # sign up function
    def sign_up(self, confirm_password):
        index_html = ""
        if(self.password == confirm_password):
            case = self.does_user_exist()
            if  case == -1:
                self.add_user_to_database()
                user = self.does_user_exist()
                set_user_info(str(user[0]), user[4])
                index_html = render_template(f'{self.status}_dashboard.html', user = user, message="You have been Sign Up successfully")
            else:
                index_html = render_template('register.html', message="This Email already exists")
        else:
            index_html = render_template('register.html', message="Passwords do NOT match") 
        return index_html
    
def user_search(football_field_location):
    query =f"SELECT * FROM HAGZ.football_field WHERE location = '{football_field_location}';"
    football_fields = get_database(query)
    return football_fields
