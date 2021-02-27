from pprint import pprint
import color

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

    def formatTerms(self, keys):
        formatKeys = '\n'.join([*keys])
        return f"""
            Fields to search by:
            {formatKeys}
        """

    def convertValue(self, value):
        if (value.isdigit()):
            return int(value)
        elif (value == "True" or value == "False"):
            return bool(value)
        else:
            return value
    
    def getUserData(self, organisationId):
        userData = []
        for user in self.users:
            try:
                if user['organization_id'] == organisationId:
                    userData.append(user)
            except(KeyError):
                continue
        return userData

    def getOrganisationData(self, organisationId):
        for organisation in self.organisations:
            try:
                if organisation['_id'] == organisationId:
                    return organisation
            except(KeyError):
                continue
        return "No organisation data found"

    def getTicketData(self, organisationId):
        ticketData = []
        for ticket in self.tickets:
            try:
                if ticket['organization_id'] == organisationId:
                    ticketData.append(ticket)
            except(KeyError):
                continue
        return ticketData

    def formatData(self, data, category=""):
        if (type(data) is dict):
            for key, value in data.items():
                print("{} {} {} {}".format(color.BOLD, key.ljust(20), color.END, value))
        else:
            for index, item in enumerate(data):
                print(color.UNDERLINE + "{} {}".format(category, index+1) + color.END)
                for key, value in item.items():
                    print("{} {} {} {}".format(color.BOLD, key.ljust(20), color.END, value))
                print("\n")
        return

    def getDataByUser(self, user, value, term):
        organisationId = user['organization_id']
        organisationData = self.getOrganisationData(organisationId)
        ticketData = self.getTicketData(organisationId)

        print(color.UNDERLINE + color.BOLD + "Result for user with {} as {}".format(term, value) + color.END)
        print(self.formatData(user))
        print(color.UNDERLINE + color.BOLD + "Organisation result for user with {} as {}".format(term, value) + color.END)
        print(self.formatData(organisationData))
        print(color.UNDERLINE + color.BOLD + "Ticket results for user with {} as {}".format(term, value) + color.END)
        print(self.formatData(ticketData, "ticket"))
        return

    def getDataByOrganisation(self, organisation, value, term):
        organisationId = organisation['_id']
        userData = self.getUserData(organisationId)
        ticketData = self.getTicketData(organisationId)

        print(color.UNDERLINE + color.BOLD + "Result for organisation with {} as {}".format(term, value) + color.END)
        print(self.formatData(organisation, "user"))
        print(color.UNDERLINE + color.BOLD + "User results for organisation with {} as {}".format(term, value) + color.END)
        print(self.formatData(userData))
        print(color.UNDERLINE + color.BOLD + "Ticket results for organisation with {} as {}".format(term, value) + color.END)
        print(self.formatData(ticketData, "ticket"))
        return

    def getDataByTicket(self, currentTicket, value, term):
        organisationId = currentTicket['organization_id']
        userData = self.getUserData(organisationId)
        organisationData = self.getOrganisationData(organisationId)
        ticketData = [currentTicket]

        for ticket in self.tickets:
            try:
                if ticket['organization_id'] == organisationId and ticket['_id'] != currentTicket['_id']:
                    ticketData.append(ticket)
            except(KeyError):
                continue

        print(color.UNDERLINE + color.BOLD + "Ticket results for ticket with {} as {}".format(term, value) + color.END)
        print(self.formatData(ticketData, "ticket"))
        print(color.UNDERLINE + color.BOLD + "Organisation result for ticket with {} as {}".format(term, value) + color.END)
        print(self.formatData(organisationData))
        print(color.UNDERLINE + color.BOLD + "User results for ticket with {} as {}".format(term, value) + color.END)
        print(self.formatData(userData, "user"))
        return

    def findData(self, query):
        term = query.getTerm()
        value = query.getValue()
        category = query.getCategory()

        if (category == 'users'):
            for user in self.users:
                if user[term] == self.convertValue(value):
                    print("Searching users...")
                    self.getDataByUser(user, value, term)
                    return "Finished searching"
        elif (category == 'organisations'):
            for organisation in self.organisations:
                if organisation[term] == self.convertValue(value):
                    print("Searching organisations...")
                    self.getDataByOrganisation(organisation, value, term)
                    return "Finished searching"
        elif (category == 'tickets'):
            for ticket in self.tickets:
                if ticket[term] == self.convertValue(value):
                    print("Searching tickets...")
                    self.getDataByTicket(ticket, value, term)
                    return "Finished searching"

        return "Cannot find any results"
