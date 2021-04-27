class Course:
 	def __init__(self, name, students, profesor):
 		self._students = students
 		self._profesor = profesor
 		self._name = name
 	def getStudents(self):
 		return self._students
 	def createInstance(self):
 		return Course(self._name, self._students, self._profesor)	
