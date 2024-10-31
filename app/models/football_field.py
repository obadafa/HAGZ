from flask import render_template
from app.api.api import *
from app.auth.auth import *

class FootballField:
    name = ""
    user_id = ""
    location = ""
    map_link = ""
    image = ""

    # Parameterized constructor.
    def __init__(self, name, user_id, location, map_link, image):
        self.name = name
        self.admin_id = user_id
        self.location = location
        self.map_link = map_link
        self.image = image

    # Add football field to database.        
    def set_football_field(self):
        # Check if Football Field Name Unique.
        football_fields_array = get_database(f"SELECT name FROM HAGZ.football_field;")
        for football_field_name in football_fields_array:
            if self.name == football_field_name[0]:
                return render_template('add_football_field.html', message="Football Field Name MUST be Unique")
        
        #Insert the football field after checking.
        query = f"INSERT INTO HAGZ.football_field (admin_id, name, location, map_link, image) VALUES (%s, %s, %s, %s, %s);"
        values = (self.admin_id, self.name, self.location, self.map_link, self.image)
        set_database(query, values)
        football_fields_array = get_database(f"SELECT * FROM HAGZ.football_field WHERE admin_id = {self.admin_id};")
        return render_template('my_football_fields.html', football_fields_array = football_fields_array)

# Retrieve all information about the football field.    
def get_football_fields_db(admin_id):
    query = f"SELECT * FROM HAGZ.football_field WHERE admin_id = {admin_id};"
    football_fields = get_database(query)
    return football_fields
