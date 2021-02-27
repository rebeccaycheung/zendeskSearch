import color
import json
from custom_format import CustomFormat

class SearchUsers:
    def __init__(self, users):
        self.users = users

    def getUsers(self):
        return self.users

    #Temporary solution - need to figure out how to get all possible keys
    def getUsersKeys(self):
        return self.users[0]

    def getUsersKeysFormat(self):
        customFormat = CustomFormat()
        return customFormat.formatTerms(self.getUsersKeys())

    def getUserData(self, organisationId):
        userData = []
        for user in self.users:
            try:
                if user['organization_id'] == organisationId:
                    userData.append(user)
            except(KeyError):
                continue
        if (len(userData) == 0):
            return "No results for users found"
        return userData

    def getData(self, user, searchOrgs, searchTickets, value, term):
        customFormat = CustomFormat()

        organisationId = user['organization_id']
        organisationData = searchOrgs.getOrganisationData(organisationId)
        ticketData = searchTickets.getTicketData(organisationId)

        print(color.UNDERLINE + color.BOLD + "Result for user with {} as {}".format(term, value) + color.END)
        print(customFormat.formatData(user))
        print(color.UNDERLINE + color.BOLD + "Organisation result for user with {} as {}".format(term, value) + color.END)
        print(customFormat.formatData(organisationData))
        print(color.UNDERLINE + color.BOLD + "Ticket results for user with {} as {}".format(term, value) + color.END)
        print(customFormat.formatData(ticketData, "ticket"))
        return
    
    def validateTerm(self, term):
        usersKeys = set(self.getUsersKeys())

        if (term in usersKeys):
            return True
        else:
            return False
