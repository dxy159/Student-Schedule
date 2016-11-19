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
pprint(availability['1'][1]['avail1']['start'])
list_students =[]

print len(availability[str(1)][1])
for i in range(1,81): 
	for j in range(1,len(availability[str(i)][1])+1):
		stri = availability[str(i)][1]['avail'+str(j)]['start']
		if stri.find('am') != -1:
			lis = stri.split('a')
			stri = lis[0]
		elif stri.find('pm') != -1:
			lis = stri.split('p')
			lis1 = lis[0].split(":")
			lis1[0] = int(lis1[0]) 
			if lis1[0] != 12:
				lis1[0] = lis1[0] + 12
			lis[0] = str(lis1[0]) + ":" + lis1[1]
			stri = lis[0]
		print (stri)
		availability[str(i)][1]['avail'+str(j)]["start"] = stri

for i in range(1,81): 
	for j in range(1,len(availability[str(i)][1])+1):
		stri = availability[str(i)][1]['avail'+str(j)]['end']
		if stri.find('am') != -1:
			lis = stri.split('a')
			stri = lis[0]
		elif stri.find('pm') != -1:
			lis = stri.split('p')
			lis1 = lis[0].split(":")
			lis1[0] = int(lis1[0]) 
			if lis1[0] != 12:
				lis1[0] = lis1[0] + 12
			lis[0] = str(lis1[0]) + ":" + lis1[1]
			stri = lis[0]
		print (stri)
		availability[str(i)][1]['avail'+str(j)]['end'] = stri



	var = student(availability[str(i)][0], availability[str(i)][1])
	list_students = list_students +[var]


with open('classes.json') as data_file:    
    classes = json.load(data_file)

list_classes = []

for i in range(101,111):
	list_classes = list_classes + [course(i, classes['classes'][str(i)]['name'], classes['classes'][str(i)]['times']['time1'], classes['classes'][str(i)]['times']['time2'])]

print("#Classes start time for time1")
#Classes start time for time1
for i in range(0, 10): 

	stri = list_classes[i].time1['start']
	if stri.find('am') != -1:
		lis = stri.split('a')
		stri = lis[0]
	elif stri.find('pm') != -1:
		lis = stri.split('p')
		lis1 = lis[0].split(":")
		lis1[0] = int(lis1[0]) 
		if lis1[0] != 12:
			lis1[0] = lis1[0] + 12
		lis[0] = str(lis1[0]) + ":" + lis1[1]
		stri = lis[0]
	# print (stri)
	list_classes[i].time1["start"] = stri

print("#Classes end time for time1")
#Classes end time for time1
for i in range(0, 10): 

	stri = list_classes[i].time1['end']
	if stri.find('am') != -1:
		lis = stri.split('a')
		stri = lis[0]
	elif stri.find('pm') != -1:
		lis = stri.split('p')
		lis1 = lis[0].split(":")
		lis1[0] = int(lis1[0]) 
		if lis1[0] != 12:
			lis1[0] = lis1[0] + 12
		lis[0] = str(lis1[0]) + ":" + lis1[1]
		stri = lis[0]
	# print (stri)
	list_classes[i].time1["end"] = stri

print("#Classes start time for time2")
#Classes start time for time2
for i in range(0, 10): 

	stri = list_classes[i].time2['start']
	if stri.find('am') != -1:
		lis = stri.split('a')
		stri = lis[0]
	elif stri.find('pm') != -1:
		lis = stri.split('p')
		lis1 = lis[0].split(":")
		lis1[0] = int(lis1[0]) 
		if lis1[0] != 12:
			lis1[0] = lis1[0] + 12
		lis[0] = str(lis1[0]) + ":" + lis1[1]
		stri = lis[0]
	# print (stri)
	list_classes[i].time2["start"] = stri

print("#Classes end time for time2")
#Classes end time for time2
for i in range(0, 10): 

	stri = list_classes[i].time2['end']
	if stri.find('am') != -1:
		lis = stri.split('a')
		stri = lis[0]
	elif stri.find('pm') != -1:
		lis = stri.split('p')
		lis1 = lis[0].split(":")
		lis1[0] = int(lis1[0]) 
		if lis1[0] != 12:
			lis1[0] = lis1[0] + 12
		lis[0] = str(lis1[0]) + ":" + lis1[1]
		stri = lis[0]
	# print (stri)
	list_classes[i].time2["end"] = stri
"""first student"""

print("time 1 start")
for x in range(0, 10):
	print(list_classes[x].time1["start"])

print("time 1 end")
for x in range(0, 10):
	print(list_classes[x].time1["end"])

print("time 2 start")
for x in range(0, 10):
	print(list_classes[x].time2["start"])

print("time 2 end")
for x in range(0, 10):
	print(list_classes[x].time2["end"])
	

# for i in range(10):
	#if list_students[0].avail['avail1']['start'].find('pm') == -1:
	#	print""
	#else :
	#	lists = list_students[0].avail['avail1']['start'].split(':')
	#	list[0] = int(list[0])
	#	if lists[0] != 12: 
		
		
	 	
	# if list_students[0].avail['avail1']['start'] <= list_classes[i].time1['start'] and list_students[0].avail['avail1']['end'] >= list_classes[i].time1['end']:
	# 	print 'true'	
	


