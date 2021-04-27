from User import User

class Student(User):
    def __init__(self, name, code, score):
    	super().__init__(name, code)
    	self._score = score
        
    def getScore(self):    
    	return self._score
    def createInstance(self, name, code, score):
    	return Student(name, code, score)	
