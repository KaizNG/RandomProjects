"""
Implement the Person Class to your own file. 
 Extend it to be able to create a Person with a last name 
 Create a method that helps to set your birth year**
 Create a method that helps you to print your age
"""

class Person:
  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName
    self.birthYear = None
    self.age = None

  def setBirthYear(self, year):
    self.birthYear = year

  def findAge(self):
    self.age = 2021 - self.birthYear
    print(self.age)

person = Person('first','last')
person.setBirthYear(1993)
person.findAge()
