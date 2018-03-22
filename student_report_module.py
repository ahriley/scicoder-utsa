#!/usr/bin/env python

'''
Day 3 Exercise 3: Creating a Library

Create a custom Python module for your studentdata classes.

Your new script should import the classes like this:
    """
    from studentdata.student import Student
    from studentdata.club import Club
    from studentdata.supervisor import Supervisor
    """
'''

from studentdata.student import Student
from studentdata.club import Club
from studentdata.supervisor import Supervisor
from studentdata.city import City

filename = 'data/student_data.txt'

with open(filename) as datafile:
    lines = datafile.readlines()

names, cities, supervisors, statii, clubs = [], [], [], [], []
for line in lines:
    if line[0] == "#":
        continue
    split = line.split("|")
    if split[0] != 'first_name':
        assert len(split) == 6
        names.append(split[0]+' '+split[1])
        cities.append(split[2])
        supervisors.append(split[3])
        statii.append(split[4])
        clubs.append(split[5].strip())

# list of UNIQUE items.  note 'names' already unique
unique_cities = set(cities)
unique_clubs = []
for studentclubs in clubs:
    studentlist = studentclubs.split()
    for club in studentlist:
        if club.strip(',') not in unique_clubs:
            unique_clubs.append(club.strip(','))
unique_supers = []
for supervisor in supervisors:
    slist = supervisor.split(',')
    for s in slist:
        if s.strip() not in unique_supers:
            unique_supers.append(s.strip())

# create dictionaries mapping names to clubs, cities, supers
myClubs, myCities, mySupers = {}, {}, {}
for city in unique_cities:
    myCities[city] = City(name=city)
for club in unique_clubs:
    myClubs[club] = Club(name=club)
for superv in unique_supers:
    mySupers[superv] = Supervisor(name=superv)

myClubs[''] = Club(name='')     # create Club for students in no clubs

myStudents = {}
for name,city,superv,status,stuclubs in zip(names,cities,supervisors,statii,clubs):
    superlist = [mySupers[key.strip()] for key in superv.split(',')]
    stuClubs = [myClubs[key.strip()] for key in stuclubs.split(',')]
    iStudent = Student(name=name,status=status,city=myCities[city],supervisor=superlist,clubs=stuClubs)
    myStudents[name] = iStudent

# propagate Club, Supervisor, City rosters
for name,student in myStudents.items():
    [club.addStudent(student) for club in student.clubs]
    [superv.addStudent(student) for superv in student.supervisor]
    myCities[student.city.name].addStudent(student)

print("Students from Attleboro:")
print("------------------------")
[print(student.name) for student in myCities['Attleboro'].roster]
print()

print("Students supervised by Baker")
print("----------------------------")
for key, superv in mySupers.items():
    if "Baker" in key:
        [print(student.name) for student in mySupers[key].roster]
print()

for key, club in myClubs.items():
    if key == "":
        continue
    print(key+": "+str(len(myClubs[key].roster))+" students")
    print("-"*15)
    [print(student.name) for student in myClubs[key].roster]
    print()
