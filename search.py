class Search:
    def __init__(self, users, organisations, tickets):
        self.users = users
        self.organisations = organisations
        self.tickets = tickets

    def getUsersKeys(self):
        return self.users[0]

    def getOrganisationsKeys(self):
        return self.organisations[0]

    def getTicketsKeys(self):
        return self.tickets[0]
    
    def formatTerms(self, keys):
        formatKeys = '\n'.join([*keys])
        return f"""
            Fields to search by:
            {formatKeys}
        """

    def getTerms(self, query):
        category = query.getCategory()

        if (category == 'users'):
            users = self.getUsersKeys()
            return self.formatTerms(users)
        elif (category == 'organisations'):
            organisations = self.getOrganisationsKeys()
            return self.formatTerms(organisations)
        elif (category == 'tickets'):
            tickets = self.getTicketsKeys()
            return self.formatTerms(tickets)
        return

    def convertValue(self, value):
        if (value.isdigit()):
            return int(value)
        elif (value == "True" or value == "False"):
            return bool(value)
        else:
            return value

    def findData(self, query):
        term = query.getTerm()
        value = query.getValue()
        category = query.getCategory()

        if (category == 'users'):
            userQuery = any(x for x in self.users if x[term] == self.convertValue(value))
            if (userQuery):
                return "Searching users..."
        elif (category == 'organisations'):
            organisationsQuery = any(x for x in self.organisations if x[term] == self.convertValue(value))
            if (organisationsQuery):
                return "Searching organisations..."
        elif (category == 'tickets'):
            ticketsQuery = any(x for x in self.tickets if x[term] == self.convertValue(value))
            if (ticketsQuery):
                return "Searching tickets..."
        
        return "Cannot find any results"
        
