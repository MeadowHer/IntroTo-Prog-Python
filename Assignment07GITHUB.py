# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)

# ------------------------------------------------------------------------------------------ #
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
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


class Person:
    def __int__(self, first_name: str,
                last_name: str):  # Add first_name and last_name properties to the constructor (Done)
        self.__first_name = first_name
        self.__last_name = last_name

    @property  # getter
    def first_name(self):  # Create a getter and setter for the first_name property(Done)
        return str(self.__first_name)

    @first_name.setter
    def first_name(self, value):
        if str(value).isnumeric() or value == "":
            self.__first_name = value
        else:
            raise ValueError("Names cannot be numbers")

    @property  # getter
    def last_name(self):  # Create a getter and setter for the first_name property(Done)
        return str(self.__last_name)

    @last_name.setter
    def last_name(self, value):
        if str(value).isnumeric() or value == "":
            self.__last_name = value
        else:
            raise ValueError("Names cannot be numbers")

    def __str__(self):
        return f'{self.first_name},{self.last_name}'  # TODO Override the __str__() method to return Person data (Done)


class Student(Person):
    def __int__(self,course_name: str):
        super().__int__(first_name=first_name, last_name=last_name)
        self.course_name = course_name  # TODO add a assignment to the course_name property using the course_name parameter (Done)

    @property  # getter
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, value):
        if value.isalpha() or value == "":
            self.__course_name = value
        else:
            raise ValueError("No numbers in NAME")

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.course_name}"


# Processing --------------------------------------- #
class FileProcessor:

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):

        try:
            file = open(file_name, "r")
            list_of_dictionary_data = json.load(file)

            for student in list_of_dictionary_data:
                student_object: Student = Student()
                student_data.append(student_object)
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        finally:
            if file.closed == False:
                file.close()
            return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):

        try:
            list_of_dictionary_data: list = []
            for students in student_data:
                student_file: dict \
                    = {"FirstName": students.first_name, "LastName": students.last_name,
                       "CourseName": students.course_name}
                list_of_dictionary_data.append(student_file)
            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)


        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):

        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():

        choice = ""
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        print("-" * 50)
        for students in student_data:  # student is the list and student_data is the dictionary list
            print(f'Student {students["FirstName"]} '
                  f'{students["LastName"]} is enrolled in {students["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        try:
            first_name = input("what is the first name of the student? : ")
            last_name = input("What is the last name of the student? : ")
            course_name = input("what is the COURSE name? : ")

            students = Student(first_name=first_name, last_name=last_name, course_name=course_name)

            student_data.append(students)

        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!",
                                     error=e)  # Validation code
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.",
                                     error=e)  # validation code
        return student_data


# Start of main body


# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
