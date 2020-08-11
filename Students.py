import school





class Students():
	def __init__(self):
		# self.name = name
		# self.surname = surname
		# self.roll_no = roll_no
		pass
	name = []
	surname=[]
	roll_no = []
	for i in range((school.total)):
		name.append(input("First name : "))
		surname.append(input("Last name : "))
		roll_no.append(input("Enter roll number : "))
		

students_database = Students()

print(students_database.name)





















	# def myfunction(self):
	# 	print("My name is " + self.name + " " + self.surname)
		

# p1= Students("Gaurav", "Patil")
# p1.myfunction()

# p1.name = "Ved"
# p1.myfunction()


# p1.name = "Jeetesh"
# p1.myfunction()


# p1.name = "Aarati"
# p1.myfunction()

# class school9(Students):
# 	pass

# p2 = school9("Usha","Mahajan")
# p2.myfunction()
