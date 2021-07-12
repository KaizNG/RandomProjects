import random
import sys
import string

def get_user_input():  # A general function to gather user input
    """
    This function is a general input method that we use for convenience.
    """
    #Allows the user to input their credentials
    firstName = str(input('Enter first name: '))
    lastName = str(input('Enter last name: '))
    birthDate = str(input('Enter Date of Birth: '))
    grade = str(input('Enter Grade: '))
    ethnicity = str(input('Enter Ethnicity (optional): '))
    homeroomTeacher = str(input('Enter Homeroom Teacher: '))

    #If any part of the user inputs are empty (except ethnicity), retry
    while firstName == '' or lastName == '' or birthDate == '' or grade == '' or homeroomTeacher == '':
        print("RETRY")
        firstName = str(input('Enter first name: '))
        lastName = str(input('Enter last name: '))
        birthDate = str(input('Enter Date of Birth: '))
        grade = str(input('Enter Grade: '))
        homeroomTeacher = str(input('Enter Homeroom Teacher: '))

    print()
    return firstName, lastName, birthDate, grade, ethnicity, homeroomTeacher

#Stores student information
class Student:
    def __init__(self, firstName, lastName, birthDate, grade, ethnicity, homeroomTeacher):
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.grade = grade
        self.ethnicity = ethnicity
        self.homeroomTeacher = homeroomTeacher

        self.electives = []
        self.lockerNumber = -1
        self.student_id = ""

    #The function will display the student's "profile"
    def show_student_profile(self):
        print(f"NAME: {self.firstName + ' ' + self.lastName}")
        print(f"DATE OF BIRTH: {self.birthDate}")
        print(f"GRADE: {self.grade}")
        print(f"ETHNICITY: {self.ethnicity}")
        print(f"HOMEROOM TEACHER: {self.homeroomTeacher}")
        print(f"COURSES: {self.electives}")
        print(f"LOCKER #: {self.lockerNumber}")
        print(f"STUDENT ID: {self.student_id}\n")

"""
Manages all the students
"""
class SchoolSystem:
    def __init__(self, studentList):
        self.studentList = studentList

        self.MANDATORY_COURSES = ("MATH", "SCIENCE", "ENGLISH")  #Sets the mandatory courses

        #Sets boundaries of what numbers can be assigned to locker number
        self.LOCKER_NUMBER_LOWER_BOUND = 1
        self.LOCKER_NUMBER_UPPER_BOUND = 999

        #Sets student # to allow ASCII letters and Number Digits, sets length of ID to 10 characters
        self.STUDENT_ID_CHARS = string.ascii_letters + string.digits
        self.STUDENT_ID_LENGTH = 10

        #If the number of students exceeds number of lockers, display message, exits program
        if len(self.studentList) > self.LOCKER_NUMBER_UPPER_BOUND:
            print("[Too many for the system]")
            sys.exit()

    def assign_student_number_to_all(self):  #Assigns student ID numbers to all the students
        generated = []
        for student in self.studentList:  #Gives random IDs to all the students

            #Generates the ID
            randId = ""
            for _ in range(self.STUDENT_ID_LENGTH):
                randId += random.choice(self.STUDENT_ID_CHARS)

            #Sets the ID to the student
            student.student_id = randId

            #Checks if random ID has already been generated, if so, redo randomization
            while randId in generated:
                randId = ""
                for _ in range(self.STUDENT_ID_LENGTH):
                    randId += random.choice(self.STUDENT_ID_CHARS)

                student.student_id = randId

        generated.append(randId)  #Adds ID to generated IDs list

    #Assigns mandatory courses to all students
    def assign_mandatory_courses_to_all(self):
        for student in self.studentList:
            for course in self.MANDATORY_COURSES:
                student.electives.append(course)

    #Assigns random locker # to all students
    def assign_locker_number_to_all(self):
        generated = []
        #Generates a random locker number between previously set boundaries
        for student in self.studentList:
            randNum = random.randint(self.LOCKER_NUMBER_LOWER_BOUND, self.LOCKER_NUMBER_UPPER_BOUND)

            student.lockerNumber = randNum

            #If number has already been generated, do it again
            while randNum in generated:
                randNum = random.randint(self.LOCKER_NUMBER_LOWER_BOUND, self.LOCKER_NUMBER_UPPER_BOUND)
                student.lockerNumber = randNum

            generated.append(randNum)

    #Lists all students
    def list_students(self):
        for student in self.studentList:
            #Displays student profile
            student.show_student_profile()

# Implementation

student = Student(*get_user_input())

mySchoolSystem = SchoolSystem([student])

mySchoolSystem.assign_mandatory_courses_to_all()
mySchoolSystem.assign_locker_number_to_all()
mySchoolSystem.assign_student_number_to_all()
mySchoolSystem.list_students()
