Coaching Management System
This Python script provides a simple Coaching Management System using MySQL as a database. It allows you to store, manage, and manipulate student records efficiently.

Features
Add a new student record
Search for student records
Display all stored records
Update student fee records
Delete student records

Prerequisites
MySQL installed on your system.
Python with mysql-connector-python package installed.
Basic understanding of MySQL commands.

Setup Instructions
1. Download the Code: Clone this repository or download the coaching.py file.
2. Setup MySQL Database: Before running the script, ensure that your MySQL server is running and you have the necessary credentials.
3. Edit MySQL Credentials:
Modify the following line in coaching.py with your MySQL username and password:-
con=sqltor.connect(host='localhost',user='your_username',passwd='your_password')
4. Run the Script:
Execute the script using:-
python coaching.py

Usage Instructions
Once the script is running, you can perform the following operations:
Add Student Record - Enter the student's details to store a new record.
Search Student Record - Retrieve details of a specific student using their serial number.
Display All Records - View all stored student records.
Update Student Record - Modify the fee details of an existing student.
Delete Student Record - Remove a student's record from the database.
Exit - Quit the program.

Important Notes
Ensure that your MySQL database server is running before executing the script.
Use correct credentials to avoid authentication errors.
The program automatically creates a database named coaching and a table named stud_rec if they do not exist.

Troubleshooting
1. Database Connection Error: Verify that MySQL is running and the credentials are correct.
2. Table Not Found Error: The script automatically creates the table, but you may manually verify it using:
SHOW DATABASES;
USE coaching;
SHOW TABLES;
3. Query Not Supported: Ensure correct input format while interacting with the program.

Author
Katyayani

License
This project is open-source and available under the MIT License.
