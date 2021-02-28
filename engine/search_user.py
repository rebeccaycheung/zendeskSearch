from engine.color import BOLD, END, UNDERLINE
from engine.constants import NO_RESULTS
from engine.custom_format import CustomFormat

# Search users object - stores the user data
class SearchUsers:
    def __init__(self, users):
        self.users = users
    
    # Getter
    def getUsers(self):
        return self.users
    
    # Get all the terms in the user data
    def getUsersKeys(self):
        # Basic solution to get the terms from the data
        return [*self.users[0]]
    
    # Format the user terms
    def getUsersKeysFormat(self):
        customFormat = CustomFormat()
        return customFormat.formatTerms(self.getUsersKeys())
    
    # Get all user data where the organisation id is equal to what the user search for
    def getUserData(self, organisationId):
        # Result should be a list because there can be many users for one organisation
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
    
    # Search all the data by user
    def getData(self, user, searchOrgs, searchTickets, value, term):
        customFormat = CustomFormat()

        organisationId = user['organization_id']

        # Search for organisation data
        organisationData = searchOrgs.getOrgData(organisationId)

        # Search for ticket data
        ticketData = searchTickets.getTicketData(organisationId)

        # Output statements
        print(UNDERLINE + BOLD + "Result for user with {} as {}".format(term, value) + END)
        customFormat.formatData(user)
        print(UNDERLINE + BOLD + "Organisation result for user with {} as {}".format(term, value) + END)
        customFormat.formatData(organisationData)
        print(UNDERLINE + BOLD + "Ticket results for user with {} as {}".format(term, value) + END)
        customFormat.formatData(ticketData, "ticket")

        return True
    
    # Validate the term that the user search for
    def validateTerm(self, term):
        usersKeys = self.getUsersKeys()

        if (term in usersKeys):
            return True
        else:
            return False
