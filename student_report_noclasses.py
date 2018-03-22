#!/usr/bin/env python

'''
Day 3 Exercise 1: Read Student Data File

There is a data file called "student_data.txt".Write a program to read this
file and print out a report that includes:

• A list of all students from Attleboro.
• A list of students supervised by Baker.
• A list of all clubs, and a list of students in each.

It is up to you how you read/store the data from the file, but for this script,
do not define any custom classes.
'''

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

print("Students from Attleboro:")
print("------------------------")
for name, city in zip(names,cities):
    if city == 'Attleboro':
        print(name)
print()

print("Students supervised by Baker")
print("----------------------------")
for name, supervisor in zip(names, supervisors):
    if "Baker" in supervisor:
        print(name)
print()

# create a list of unique clubs
clublist = []
for studentclubs in clubs:
    studentlist = studentclubs.split()
    for club in studentlist:
        if club.strip(',') not in clublist:
            clublist.append(club.strip(','))

# find roster for each club
studentsinclub = []
for club in clublist:
    clubroster = []
    for name, studentclub in zip(names, clubs):
        if club in studentclub:
            clubroster.append(name)
    studentsinclub.append(clubroster)

# print the names associated with each club
for club, roster in zip(clublist, studentsinclub):
    print(club + ": " + str(len(roster)) + " students")
    print("-"*15)
    for name in roster:
        print(name)
    print()
