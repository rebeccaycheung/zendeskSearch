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

    def validateTerm(self, search, term):
        usersKeys = set(search.getUsersKeys())
        organisationsKeys = set(search.getOrganisationsKeys())
        ticketsKeys = set(search.getTicketsKeys())

        if (self.category == 'users' and term in usersKeys) or (self.category == 'organisations' and term in organisationsKeys) or (self.category == 'tickets' and term in ticketsKeys):
            return True
        else:
            return False
