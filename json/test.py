#!bin/python

import json
from pprint import pprint

class student(object):
	classes = []
	free1 = []
	free2 = []
	for i in range(10):
		free1 = free1 + [False]
		free2 = free2 + [False]

	def __init__(self, name, avail):
		self.name = name
		self.avail = avail

	def check(self):
		if len(classes) == 5:
			return False

class course(object):
	def __init__(self, ID, name, time1, time2):
		self.ID = ID
		self.name = name
		self.time1 = time1
		self.time2 = time2 
		self.max = 20;

	def signUp(self):
		self.max = self.max - 1

	def check(self):
		if self.max == 0:
			return False




with open('studentsByAvailability.json') as data_file:    
    availability = json.load(data_file)
pprint(availability)
list_students =[]
for i in range(1,81):
	
	var = student(availability[str(i)][0], availability[str(i)][1])
	list_students = list_students +[var]


with open('classes.json') as data_file:    
    classes = json.load(data_file)

list_classes = []

for i in range(101,111):
	list_classes = list_classes + [course(i, classes['classes'][str(i)]['name'], classes['classes'][str(i)]['times']['time1'], classes['classes'][str(i)]['times']['time2'])]

print list_classes[0].time2['start']



"""first student"""


	
if (student[0].avail['avail1']['start'] <= classes[0].time1['start']) and (student[0].avail['avail1']['end'] >= classes[0].time1['end']) : 
	"""	student[0].free1[0] = True"""

if student[0].avail['avail1']['start'] <= classes[0].time2['start'] and student[0].avail['avail1']['end'] >= classes[0].time2['end'] :
	student[0].free2[0] = True

print student[0].free1
print student[0].free2
