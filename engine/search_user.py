from engine.color import BOLD, END, UNDERLINE
from engine.constants import NO_RESULTS
from engine.custom_format import CustomFormat

class SearchUsers:
    def __init__(self, users):
        self.users = users

    def getUsers(self):
        return self.users

    def getUsersKeys(self):
        return [*self.users[0]]

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
            return NO_RESULTS
        return userData

    def getData(self, user, searchOrgs, searchTickets, value, term):
        customFormat = CustomFormat()

        organisationId = user['organization_id']
        organisationData = searchOrgs.getOrgData(organisationId)
        ticketData = searchTickets.getTicketData(organisationId)

        print(UNDERLINE + BOLD + "Result for user with {} as {}".format(term, value) + END)
        customFormat.formatData(user)
        print(UNDERLINE + BOLD + "Organisation result for user with {} as {}".format(term, value) + END)
        customFormat.formatData(organisationData)
        print(UNDERLINE + BOLD + "Ticket results for user with {} as {}".format(term, value) + END)
        customFormat.formatData(ticketData, "ticket")

        return True

    def validateTerm(self, term):
        usersKeys = self.getUsersKeys()

        if (term in usersKeys):
            return True
        else:
            return False
