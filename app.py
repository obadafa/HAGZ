from flask import Flask, request, render_template, redirect, current_app
from user import User, user_search
from football_field import FootballField, get_football_fields_db
from werkzeug.utils import secure_filename
from reservation import *
from talk_to_text_file import *


app = Flask("HAGZ")

##########          routing          ##########

# get html pages.
def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

#1 route to homepage.
@app.route("/", methods=["GET","POST"])
def home_page():
    if is_login(): 
        user_info = get_user_info()
        return render_template(f"{user_info[1]}_dashboard.html")
    return get_html("./templates/homepage")


#2 route to register.
@app.route("/register", methods=["GET","POST"])
def returnRegister():
    if is_login():
        user_info = get_user_info()
        return render_template(f"{user_info[1]}_dashboard.html")
    return render_template("register.html")

#3 route to homepage after sign up successfully.
@app.route ("/add_user", methods=['GET', 'POST'])
def singup():
    if is_login():
        user_info = get_user_info()
        return render_template(f"{user_info[1]}_dashboard.html")
    name = request.form.get('name')
    email = request.form.get('email')
    password =  request.form.get('password')
    confirm_password =  request.form.get('confirm-password')
    status = request.form.get('userType')
    _user = User(name, email, password, status)
    index_html = _user.sign_up(confirm_password)
    return index_html

#4 route to sign in.
@app.route("/signin", methods=["GET","POST"])
def singin():
    if is_login():
        user_info = get_user_info()
        return render_template(f"{user_info[1]}_dashboard.html")
    return render_template("login.html")

#5 route to dashboard after sign in successfully.
@app.route("/auth", methods=["GET","POST"])
def store():
    if is_login():
        user_info = get_user_info()
        return render_template(f"{user_info[1]}_dashboard.html")
    
    email = request.form.get('email')
    password = request.form.get('password')
    _user = User("",email, password, "")
    user = _user.sign_in()
    if(user != 0 and user != -1):
        index_html = render_template(f"{user[4]}_dashboard.html", user = user)
    else:
        index_html = render_template("login.html", message = "Email or Password is not correct.")
    return index_html


#6 route to admin dashboard.
@app.route ("/admin_dashboard",methods=['GET', 'POST'])
def admin_dashboard():
    if is_login():
        user_info = get_user_info()
        return render_template(f"{user_info[1]}_dashboard.html")
    return render_template("login.html")


#7 route to admplayerin dashboard.
@app.route ("/player_dashboard",methods=['GET', 'POST'])
def player_dashboard():
    if is_login():
        user_info = get_user_info()
        return render_template(f"{user_info[1]}_dashboard.html")

#8 route to add football field page.
@app.route("/add_football_field", methods=["GET","POST"])
def add_field_dashboard():
    if is_login():
        user_info = get_user_info()
        if user_info[1] == "admin":
            return render_template("add_football_field.html")
        else:
            return render_template(f"{user_info[1]}_dashboard.html")
    else:
        return render_template("login.html")

#9 route to store football field data in database.
@app.route("/football_field_data", methods=["GET","POST"])
def football_field_data():
    if is_login():
        user_info = get_user_info()
        if user_info[1] == "admin":
            try:
                index_html = ""
                user_info = get_user_info()
                field_name = request.form.get('field_name')
                location = request.form.get('location')
                map_link = request.form.get('map_link')
                image = request.files.get('image')
    
                if image:
                    image_file_name = f"{secure_filename(image.filename)}"
                    dir = os.path.join(current_app.root_path, './static/img')
                    image_path = os.path.join(dir, image_file_name)
                    image.save(image_path)
                # elif image == "":
                #     image = "./static/img/football_field_profile.jpg"
                print(image)
                print(image_file_name)
                print(dir)
                print(image_path)
                football_field = FootballField(field_name, user_info[0], location, map_link, str(image_file_name))
                index_html = football_field.set_football_field()
                return index_html
            except:
                return render_template("add_football_field.html")
        else:
            return render_template(f"{user_info[1]}_dashboard.html")
    else:
        return render_template("login.html")


#10 route to my football field page.
@app.route("/my_football_fields", methods=["GET","POST"])
def my_field_dashboards():
    if is_login():
        user_info = get_user_info()
        if user_info[1] == "admin":
            football_fields = get_football_fields_db(user_info[0])
            return render_template('my_football_fields.html', football_fields_array = football_fields)
        else:
            return render_template(f"{user_info[1]}_dashboard.html")
    else:
        return render_template('login.html')

#11 route to search about specific field.
@app.route("/search", methods=["GET","POST"])
def search():
    if is_login():
        user_info = get_user_info()
        if user_info[1] == "player":
            location = request.form.get('search_field')
            football_fields = user_search(location)
            return render_template('player_dashboard.html', user = "", football_fields_array = football_fields)
        else:
            return render_template(f"{user_info[1]}_dashboard.html")
    else:
        return render_template("login.html")

#12 route to book specific field.
@app.route('/book/<string:field_name>', methods=['GET', 'POST'])
def book(field_name):
    if is_login():
        user_info = get_user_info()
        if user_info[1] == "player":
            reservations_data = [list(entry) for entry in get_reservations_data(field_name)]
            return render_template('book.html', reservations_data = reservations_data, football_field_name = field_name)
        else:
            return render_template(f"{user_info[1]}_dashboard.html")
    else:
        return render_template("login.html")

#13 route to sumbit booking of specific field data.
@app.route('/submit_booking', methods=['GET', 'POST'])
def submint_booking():
    if is_login():
        user_info = get_user_info()
        if user_info[1] == "player":
            football_field_name = request.form.get('football_field_name')
            selected_date = request.form.get('selected_date')
            selected_time = request.form.get('selected_time')
            football_field_reservation = Reservation(football_field_name, user_info[0], selected_time, selected_date, 'confirmed')
            football_field_reservation.set_reservation_data()
            return get_html("./templates/submit_booking")
        else:
            return render_template(f"{user_info[1]}_dashboard.html")
    else:
        return render_template("login.html")

#14 route to admin reservations.   
@app.route('/admin_reservations')
def see_reservation():
    if is_login():
        user_info = get_user_info()
        if user_info[1] == "admin":
            reservations_table = get_reservations_table(user_info[0])
            print(reservations_table)
            return render_template('admin_reservations.html', reservations_table = reservations_table)
        else:
            return render_template(f"{user_info[1]}_dashboard.html")
    else:
        return render_template("login.html")

#15 route to admin delete any reservation.  
@app.route('/delete_reservations/<int:id>', methods=['POST'])
def delete_reservations(id):
    if is_login():
        user_info = get_user_info()
        if user_info[1] == "admin":
            update_reservation(id)
            reservations_table = get_reservations_table(user_info[0])
            return render_template('admin_reservations.html', reservations_table = reservations_table, message = 'Reservation cancelled successfully')
        else:
            return render_template(f"{user_info[1]}_dashboard.html")
    else:
        return render_template("login.html")

#16 route to player reservations.  
@app.route('/player_reservations')
def see_my_reservation():
    if is_login():
        user_info = get_user_info()
        if user_info[1] == "player":
            reservations_table = get_my_reservations_table(user_info[0])
            return render_template('player_reservations.html', reservations_table = reservations_table)
        else:
            return render_template(f"{user_info[1]}_dashboard.html")
    else:
        return render_template("login.html")

#17 route to admin delete any reservation. 
@app.route('/delete_my_reservation/<int:id>', methods=['POST'])
def delete_my_reservation(id):
    if is_login():
        user_info = get_user_info()
        if user_info[1] == "player":
            delete_reservation(id)
            reservations_table = list(filter(lambda x: x != [], get_my_reservations_table(user_info[0])))
            return render_template('player_reservations.html', reservations_table = reservations_table, message = 'Reservation deleted successfully')
        else:
            return render_template(f"{user_info[1]}_dashboard.html")
    else:
        return render_template("login.html")

#18 log out route.
@app.route('/logout')
def logout():
    if is_login():
        logedout()
    return redirect("/")

#19 If the user inputs something invalid route.
@app.errorhandler(404)
def page_not_found(e):
    if is_login():
        user_info = get_user_info()
        return render_template(f"{user_info[1]}_dashboard.html")
    return render_template("login.html")
