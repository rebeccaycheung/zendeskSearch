class Query:
    def __init__(self):
        self.category = None
        self.term = None
        self.value = None

    def setCategory(self, category):
        self.category = category
    
    def setTerm(self, term):
        self.term = term

    def setValue(self, value):
        self.value = value
    
    def getCategory(self):
        return self.category
    
    def getTerm(self):
        return self.term

    def getValue(self):
        return self.value
