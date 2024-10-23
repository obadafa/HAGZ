import os

def get_user_info():
    if os.path.exists('user_info.txt'):
        file = open("user_info.txt", "r")
        user_info = file.readline()
        file.close()
        user = user_info.split('$$$')
    else:
        file = open("user_info.txt", "x")
        file.close()
    return user

def set_user_info(user_id, user_status):
    file = open("user_info.txt", "w")
    file.write(user_id + "$$$" + user_status)
    file.close()

def is_login():
    return os.path.exists("user_info.txt")

def logedout():
    os.remove("user_info.txt")