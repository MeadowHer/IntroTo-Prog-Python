# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Veronica hernandez,10/12/2023, Script for Assignment 05
# ------------------------------------------------------------------------------------------ #
# Define the Data Constants

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = []  # one row of student data
students: list = [dict]  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
file = open(FILE_NAME, "r")
students = json.load(file)
file.close()


# Present and Process the data
while (True):
    # Present the menu of choices
    try:
        print(MENU)
        menu_choice = input("What would you like to do: ")
    # Input user data
        if menu_choice == "1":  # This will not work if it is an integer!
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
        student_data = {"FirstName":student_first_name,"LastName": student_last_name, "CourseName":course_name}
        for row in students:
            print(f'{row["FirstName"]},{row["LastName"]},{row["CourseName"]}')
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
    except ValueError as e:
            print(e, type(e))
            print("make adjustment- ")
    try:

        # Present the current data
        if menu_choice == "2":
            print("-"*40) # Process the data to create and display a custom message
            for student in students:
                print(f'{student_first_name} ,'f'{student_last_name},' f' is enrolled in {course_name}\n')
            print("-"*40)


    # Save the data to a file
        if menu_choice == "3": #define your data
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
    except FileNotFoundError as e:
        if file.closed == False: # Make sure the file is open before trying to close it.
            file.close()


       # Stop the loop
    if menu_choice == "4":# out of the loop
        print("Program Ended")
        break
