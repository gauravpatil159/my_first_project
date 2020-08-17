import Students
import school
import statistics 
import os



class grade():
	def __init__(self):
		pass

	marks = []
	grade = []


	# Removing privious data.txt file 

	path = os.getcwd()
	print(path)
	path = path + "/data.txt"
	print(path)
	try:
		os.remove(path)
	except FileNotFoundError:
		print("File is not avilable")


# writing final results
	file = open("data.txt", "a")
	file.write("name,surname,Rollno,Grade")
	file.write("\n")

	no_of_subjects = int(input("Enter number of subjets : "))
	for number in range(school.total):	
		print("Enter marks of {}".format(Students.students_database.name[number]))
		marks1 = []
		for subjet in range(no_of_subjects):
			marks1.append(int(input("Enter marks ")))
		grade.append(statistics.mean(marks1))
		marks.append(marks1)
		file.write(Students.students_database.name[number]+ ","+ Students.students_database.surname[number]+ ","+ Students.students_database.roll_no[number]+ ","+ str(grade[number]) )
		file.write("\n")
	print(marks)
	file.close()	

#print(grade.grade)




