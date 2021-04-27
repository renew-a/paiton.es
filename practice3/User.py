class User:
    def __init__(self, name, code):
        self._name = name
        self._code = code

    def getName(self):    
    	return self._name

    def getCode(self):    
    	return self._code