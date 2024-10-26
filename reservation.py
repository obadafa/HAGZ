from talk_to_database import *
from talk_to_text_file import *

class Reservation:
    id = ""
    football_field_id = ""
    player_id = ""
    time = ""
    date = ""
    status = ""

    # Parameterized constructor
    def __init__(self, football_field_name, player_id, time, date, status):
        self.football_field_name = football_field_name
        self.player_id = player_id
        self.time = time
        self.date = date
        self.status = status

    def set_reservation_data(self):
        query = f"INSERT INTO HAGZ.reservations (football_field_name, player_id, time, date, status) VALUES (%s, %s, %s, %s, %s);"
        values = (self.football_field_name, self.player_id, self.time, self.date, self.status)
        set_database(query, values)

def get_reservations_data(field_name):
    query = (f"SELECT * FROM HAGZ.reservations WHERE football_field_name = '{field_name}';")
    football_field_reservations = get_database(query) 
    return football_field_reservations

def get_reservations_table(id):
    query = (f"SELECT name FROM HAGZ.football_field WHERE admin_id = {id};")
    football_field_names = [name[0] for name in get_database(query)]
    reservations_table = []

    for football_field_name in football_field_names:
        query = (f"SELECT * FROM hagz.reservations WHERE football_field_name = '{football_field_name}' AND status <> 'cancelled' ORDER BY date ASC, time ASC;")
        reservations_table.append(get_database(query))
    return reservations_table

def update_reservation(id):
    query = f"UPDATE hagz.reservations SET status = 'cancelled' WHERE id = {id};"
    edit_database(query)
    return True

def get_my_reservations_table(id):
    query = (f"SELECT * FROM hagz.reservations WHERE player_id = {id} ORDER BY date ASC, time ASC;")
    reservations_table = get_database(query)
    return reservations_table

def delete_reservation(id):
    query = f"DELETE FROM hagz.reservations WHERE id = {id};"
    edit_database(query)
    return True