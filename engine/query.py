# Query object to contain the user's inputs
class Query:
    def __init__(self, category, term, value):
        self.category = category
        self.term = term
        self.value = value
    
    # Setters
    def setCategory(self, category):
        self.category = category
    
    def setTerm(self, term):
        self.term = term

    def setValue(self, value):
        self.value = value
    
    # Getters
    def getCategory(self):
        return self.category
    
    def getTerm(self):
        return self.term

    def getValue(self):
        return self.value
