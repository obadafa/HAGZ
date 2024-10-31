import os
from flask import session

def get_user_info():
    if os.path.exists('user_info.txt'):
        file = open("user_info.txt", "r")
        user_info = file.readline()
        file.close()
        user = user_info.split('$$$')
    return user

def set_user_info(user_id, user_status):
    file = open("user_info.txt", "w")
    file.write(user_id + "$$$" + user_status)
    file.close()

def is_login():
    email = session.get('email') 
    if email:
        return True
    return False

def logedout():
    os.remove("user_info.txt")
    session.pop('email', None)