students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
users = {
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
}

def print_students():
	for i in range(0, len(students)):
		print students[i]["first_name"], students[i]["last_name"]

def print_users():
	for key, data in users.items():
		print key
		for i in range(0, len(data)):
			print i+1, '-', data[i]['first_name'], data[i]['last_name'], '-', len(data[i]['first_name'])+len(data[i]['last_name'])
print_students()
print "\n"
print_users()