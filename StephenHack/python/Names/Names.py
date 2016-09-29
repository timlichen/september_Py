def Names1():
	students = [{'first_name': 'Michael', 'last_name' : 'Jordan'},
   	 	 {'first_name': 'John', 'last_name' : 'Rosales'},
    	 {'first_name': 'Mark', 'last_name' : 'Guillen'},
    	 {'first_name': 'KB', 'last_name' : 'Tonel'}]
	
	for x in range(0, len(students)):
		print students[x]['first_name'] + " " + students[x]['last_name']
Names1()

def Names2():
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
	for key, data in users.items():
		print "\n%s" %key.title()
		counter = 0;

		for value in data: 
			counter = counter + 1
			full_name = value["first_name"] + " " + value["last_name"]
			full_name_upper = full_name.upper()
			name_count = len(value["first_name"]) + len(value["last_name"])

			print "%d - %s - %d" %(counter, full_name_upper, name_count)

Names2()

