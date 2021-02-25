class Search:
    def __init__(self, users, organisations, tickets):
        self.users = users
        self.organisations = organisations
        self.tickets = tickets

    #Temporary solution - need to figure out how to get all possible keys
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
    
    def getDataByUser(self, user):
        organisationId = user['organization_id']
        organisationData = None
        ticketData = []

        for org in self.organisations:
            if org['_id'] == organisationId:
                organisationData = org
        
        for ticket in self.tickets:
            try:
                if ticket['organization_id'] == organisationId:
                    ticketData.append(ticket)
            except(KeyError):
                continue

        print(user)
        print(organisationData)
        print(ticketData)
        return
    
    def getDataByOrganisation(self, organisation):
        organisationId = organisation['_id']
        userData = None
        ticketData = []

        for user in self.users:
            if user['organization_id'] == organisationId:
                userData = user
        
        for ticket in self.tickets:
            try:
                if ticket['organization_id'] == organisationId:
                    ticketData.append(ticket)
            except(KeyError):
                continue

        print(userData)
        print(organisation)
        print(ticketData)
        return
    
    def getUserTicket(self, ticket):
        organisationId = ticket['organization_id']
        userData = None
        organisationData = None
        ticketData = [ticket]

        for org in self.organisations:
            if org['_id'] == organisationId:
                organisationData = org
        
        for user in self.users:
            if user['organization_id'] == organisationId:
                userData = user
        
        for ticket in self.tickets:
            try:
                if ticket['organization_id'] == organisationId:
                    ticketData.append(ticket)
            except(KeyError):
                continue

        print(userData)
        print(organisationData)
        print(ticketData)
        return

    def findData(self, query):
        term = query.getTerm()
        value = query.getValue()
        category = query.getCategory()

        if (category == 'users'):
            for user in self.users:
                if user[term] == self.convertValue(value):
                    print("Searching users...")
                    return self.getDataByUser(user)
        elif (category == 'organisations'):
            for organisation in self.organisations:
                if organisation[term] == self.convertValue(value):
                    print("Searching organisations...")
                    return self.getDataByOrganisation(organisation)
        elif (category == 'tickets'):
            for ticket in self.tickets:
                if ticket[term] == self.convertValue(value):
                    print("Searching tickets...")
                    return self.getDataByTicket(ticket)
        
        return "Cannot find any results"
        
