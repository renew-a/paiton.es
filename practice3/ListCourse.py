class ListCourse:
    def __init__ (self, course):
        self.i = 0
        self.students = course.getStudents()

    def __iter__ (self):
        return self

    def __next__ (self):
        try:
            item = self.students[self.i]
        except IndexError:
            raise StopIteration()
        self.i += 1
        return item

    def __len__(self):
    	return len(self.students)
    def highest(self):
    	return max(student._score for student in self.students)	