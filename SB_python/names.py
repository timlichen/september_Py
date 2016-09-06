def names(a):
	for i in range(0, len(a)):
		print a[i]["first_name"], a[i]["last_name"]
'''
names([{'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}])
'''
#Almost did it in one line
def names2(a):
	for k in range(0, (len(a['Students']) + len(a['Instructors']))):
		print k + 1 if k < len(a['Students']) else k - len(a['Students']) + 1, '-', a['Students' if k < len(a['Students']) else 'Instructors'][k if k < len(a['Students']) else k - len(a['Students'])]['first_name'], a['Students' if k < len(a['Students']) else 'Instructors'][k if k < len(a['Students']) else k - len(a['Students'])]['last_name'], '-', len(a['Students' if k < len(a['Students']) else 'Instructors'][k if k < len(a['Students']) else k - len(a['Students'])]['first_name']) + len(a['Students' if k < len(a['Students']) else 'Instructors'][k if k < len(a['Students']) else k - len(a['Students'])]['last_name'])

#Real format
def names3(a):
	for k in range(0, len(a['Students']) + len(a['Instructors']) + 2):
		if k == 0:
			print 'Students'
		elif k == len(a['Students']) + 1:
			print 'Instructors'
		elif k <= len(a['Students']):
			print k, '-', a['Students'][k - 1]['first_name'].upper(), a['Students'][k-1]['last_name'].upper(), '-', len(a['Students'][k - 1]['first_name']) + len(a['Students'][k-1]['last_name'])
		else:
			print k - 1 - len(a['Students']), '-', a['Instructors'][k - 2 - len(a['Students'])]['first_name'].upper(), a['Instructors'][k - 2 - len(a['Students'])]['last_name'].upper(), '-', len(a['Instructors'][k - 2 - len(a['Students'])]['first_name']) + len(a['Instructors'][k - 2 - len(a['Students'])]['last_name'])

names3({
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 })