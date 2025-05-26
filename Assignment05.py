# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Olivier Richer,5/24/2025,Created Script
#   Olivier Richer,5/24/2025,created script
#   <Your Name Here>,<Date>, <Activity>
# ------------------------------------------------------------------------------------------ #

# importing the out of the box json capabilities
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

#FILE_NAME: str = "Enrollments.csv". No longer necessary as we will be using a json file.

FILE_NAME: str =" Enrollments.json"

# Define the Data Variables which is the first name  last name, and course taken pending the user input

student_first_name: str = ''  

student_last_name: str = ''  

course_name: str = ''  


# student_data is now a dictionary, and being initialise
student_data: dict ={}

students: list = []  

 # Holds a reference to an opened file.

file = None

# Hold the choice made by the user.

menu_choice: str ='' 


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file. Open the json file for reading

# encapsulating the block in using the "try" statement pertaining to my file possibly not found if Enrollments.json is empty.

try:
   file = open("Enrollments.json",'r')
   students = json.load(file)
   file.close()
except FileNotFoundError as e:
     print("this file doesn't exist! Trying to open it again after creating...")
except Exception as e:
       print(" there was an error open up the document")
# printing out e along with doc for e
       print(e,e.__doc__)
finally:
   # print("closing file")
    file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
          student_first_name = input("Enter the student's first name: ")
        # I could also be defensive of the user. Notice the "if not" statement.
        # If the input user is not using alphabetic character then the script will raise an error and print out a custom made
        # message.
          if not student_first_name.isalpha():
            raise ValueError ('first name can only have alphabetic character')        
          student_last_name = input("Enter the student's last name: ")
          if not student_last_name.isalpha():
            raise ValueError ('last name can only have alphabetic character') 
          course_name = input("Please enter the name of the course: ")
        # now using my dictionary at which for eack "KEY" is associated to a "Value".
          student_data ={"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
          students.append(student_data)
          print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
          print(" user entered invalid information. continuing...")
          print(e,e.__doc__)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f'student {student["FirstName"]}  {student ["LastName"]} is enrolled in {student["CourseName"]}' )
            
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
           file = open(FILE_NAME, "w")
           json.dump(students,file)
           file.close()
           for student in students:
               print("The following data was saved to file!")
               print (f'student {student["FirstName"]}  {student ["LastName"]} is enrolled in {student["CourseName"]}')

        except Exception as e:
          print(" there was an error writing to the document")
# printing out e along with doc for e
          print(e,e.__doc__)

        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
