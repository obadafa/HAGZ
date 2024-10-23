# HAGZ: Football Field Booking System

A web-based platform to help users easily book football fields. Users can view real-time availability, confirm, or cancel bookings. The new feature allows dynamic updates of booking slots based on reservation status.

## Features

- **Dynamic Time Slot Display**: Shows available, confirmed, and unavailable booking slots based on reservation status.
- **Real-Time Updates**: Uses JavaScript and localStorage to dynamically update the booking interface.
- **Responsive Design**: Optimized for both desktop and mobile views.

## Prerequisites

Before starting, ensure you have the following installed:

- **Python 3.x**
- **Flask** (`pip install Flask`)
- Any other necessary modules (e.g., `os`, `json`).

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the dependencies.
4. Run the Flask app.

## Usage

1. Open your browser and go to `http://localhost:5000`.
2. Select a date and time to view available fields.
3. Book, confirm, or cancel your reservations as needed.

## New Feature

**Dynamic Time Slot Display**: Time slots are dynamically updated based on user reservations. Confirmed slots become unavailable, and users can manage their bookings directly on the platform.

## Project Checklist
- [x] It is available on GitHub.
- [x] It uses the Flask web framework.
- [x] It uses at least one module from the Python Standard Library other than the random module.
  Please provide the name of the module you are using in your app. 
  - Module name: json, os.
  [x] It contains at least one class written by you that has both properties and methods. It uses __init__() to let the class initialize the object's attributes (note that  __init__() doesn't count as a method). This includes instantiating the class and using the methods in your app. Please provide below the file name and the line number(s) of at least one example of a class definition in your code as well as the names of two properties and two methods.
  - File name for the class definition: User
   Line number(s) for the class definition: line 7 in user.
    Name of two properties: name, email, username, password.
  - Name of two methods: does_user_exist, add_user_to_database.
    - File name and line numbers where the methods are used: user.py , line 42,33
- [x] It makes use of JavaScript in the front end and uses the localStorage of the web browser.
- [x] It makes use of the reading and writing to the same file feature.
- [x] It contains conditional statements. Please provide below the file name and the line number(s) of at least
  one example of a conditional statement in your code.
  - File name: user.py .
  - Line number(s): 26
- [x] It contains loops. Please provide below the file name and the line number(s) of at least
  one example of a loop in your code.
  - File name: user.py.
  - Line number(s):25.
- [x] It lets the user enter a value in a text box at some point.
  This value is received and processed by your back end Python code.
- [x] It doesn't generate any error message even if the user enters a wrong input.
- [x] It is styled using CSS.
- [x] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code. 
  In particular, the code should not use print() or console.log() for any information the app user should see. Instead, all user feedback needs to be visible in the browser.  
- [x] All exercises have been completed as per the requirements and pushed to the respective GitHub repository.
