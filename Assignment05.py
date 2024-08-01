# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   JBoardman, 7/30/2024, updated script with error handling
# ------------------------------------------------------------------------------------------ #
# (jb 7.30.24) import code from pythons json module into my script
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
student_data: dict = {}  # one row of student data (jb 7.30.24) made dict
students: list = []  # a table of student data
json_data: str = ''  # (jb 7.30.24) string for json data
# csv_data: str = ''  # Holds combined string data separated by a comma. (jb 7.30.24) removed
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
Show: bool = True  # (jb 7.30.24) added to hide the menu if the file doesn't load correctly

# When the program starts, read the file data into a list of dictionaries
# Extract the data from the file
try:  # (jb 7.30.2024) added try for exception error handling
    file = open(FILE_NAME, "r")
    # (jb 7.30.2024) loading the students from the json
    students = json.load(file)  # (jb 7.30.2024) fixed starter file json with Email as key for last name
    file.close()
#  (jb 7.30.24) removed the parsing format from csv & multi row comment errors inside try
except Exception as e:  # (jb 7.30.2024) adding exceptions
    print("-" * 80)
    print("Error loading file: Please verify the file exists and includes valid JSON data.")
    print("-" * 80)
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
    Show = False  # (jb 7.30.24) set to false hide the menu prompt for the user
finally:
    if file.closed == False:
        file.close()

#  Present and Process the data
if Show == True:  # (jb 7.30.24) do not display the menu if there was an error loading the file
    while True:

        # Present the menu of choices
        print(MENU)
        menu_choice = input("What would you like to do: ")
        if menu_choice == "1":  # This will not work if it is an integer!
            try:  # (jb 7.30.24) added for exception and error handling
                # Input user data
                student_first_name = input("Enter the student's first name: ")
                # (jb 7.30.24) specific error handling for non alpha
                if not student_first_name.isalpha():
                    raise ValueError("The first name only accepts letters.")
                student_last_name = input("Enter the student's last name: ")
                # (jb 7.30.24) specific error handling for non alpha
                if not student_last_name.isalpha():
                    raise ValueError("The last name only accepts letters.")
                course_name = input("Please enter the name of the course: ")
                #  (jb 7.30.24) Keys are defined as "FirstName", "LastName", "CourseName"
                student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
                students.append(student_data)
                print()  # (jb 7.30.24) blank line
                print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            # (jb 7.30.24) specific error handling
            except ValueError as e:
                # (jb 7.30.24) for value error the message for each field would be displayed
                print()  # blank line
                print(e)  # specific error message
                print("-- Technical Error Message -- ")
                print(type(e))
                print(e.__doc__)
                #  (jb 7.30.24) not including e.__str() as this double prints the exception text
            except Exception as e:
                # (jb 7.30.24) error for exceptions
                print()  # (jb 7.30.24) blank line
                print("Error: An unexpected error occurred.  Please check the data entered.")
                print("-- Technical Error Message -- ")
                print(type(e))
                print(e.__doc__)
                print(e.__str__())
            continue
        # Present the current data
        elif menu_choice == "2":

            # Process the data to create and display a custom message
            print("-"*50)
            for student in students:
                #  (jb 7.30.24) adjusted to print from dict using keys
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            print("-"*50)
            continue

        # Save the data to a file
        elif menu_choice == "3":
            try:  # (jb 7.30.2024) added try for exception error handling
                file = open(FILE_NAME, "w")
                #  (jb 7.30.24) removed write for csv
                #  (jb 7.30.24) added write for json with dump function from json module
                json.dump(students, file)
                file.close()
                print("-" * 50)  # (jb 7.30.24) added to be consistent with other print functions
                print("The following data was saved to file!")
                for student in students:
                    #  (jb 7.30.24) adjusted to print from dict using keys
                    print(f'Student {student["FirstName"]} '
                          f'{student["LastName"]} is enrolled in {student["CourseName"]}')
                print("-" * 50)  # (jb 7.30.24) added to be consistent with other print functions
            except Exception as e:  # (jb 7.30.2024) added exception error handling
                print("Error: An error occurred while writing to the file.")
                print("-- Technical Error Message -- ")
                print(e.__doc__)
                print(e.__str__())
            finally:
                if file.closed == False:
                    file.close()
            continue

        # Stop the loop
        elif menu_choice == "4":
            break  # out of the loop
        else:
            print("Please only choose option 1, 2, or 3")

    print("Program Ended")
else:
    print()
    print("-" * 80)
    print("Please resolve the file loading error and then re-run the program.")
    print("-" * 80)
