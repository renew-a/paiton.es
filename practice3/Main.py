#Diffrent courses, each one has a list of students and one professor, 
#the list can calculate the average score from all the students and the highest grade.
#Each student has a name, score, code.

from Course import Course
from User import User
from Profesor import Profesor
from Student import Student
from ListCourse import ListCourse

class Main(object):
	def main(self):
			a=Student.createInstance(self,'beckyG','001',51)
			b=Student.createInstance(self,'DonOmar','001',65)
			c=Student.createInstance(self,'Anuel','001',78)
			studentList1 = [a,b,c]
			profesor =  Profesor('Maluma','998')
			courseA  =  Course('science', studentList1, profesor)

			lCourse = ListCourse(courseA)
			average=0
			for item in lCourse:
				average+=item._score
			average= average/len(lCourse)
			print('Average',average)
			print('Highest grade', lCourse.highest())
			

if __name__ == "__main__":
    Main().main()
