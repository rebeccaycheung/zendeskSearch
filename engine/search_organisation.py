from engine.color import BOLD, END, UNDERLINE
from engine.constants import NO_RESULTS
from engine.custom_format import CustomFormat

# Search organisation object - stores the organisation data
class SearchOrgs:
    def __init__(self, orgs):
        self.orgs = orgs
    
    # Getter
    def getOrgs(self):
        return self.orgs
    
    # Get all the terms in the organisation data
    def getOrgsKeys(self):
        # Basic solution to get the terms from the data
        return [*self.orgs[0]]

    # Format the organisation terms
    def getOrgsKeysFormat(self):
        customFormat = CustomFormat()
        return customFormat.formatTerms(self.getOrgsKeys())
    
    # Get all organisation data where the organisation id is equal to what the user search for
    def getOrgData(self, organisationId):
        for organisation in self.orgs:
            try:
                if organisation['_id'] == organisationId:
                    return organisation
            except(KeyError):
                continue
        return NO_RESULTS
    
    # Search all the data by organisation
    def getData(self, organisation, searchUsers, searchTickets, value, term):
        customFormat = CustomFormat()

        organisationId = organisation['_id']

        # Search for user data
        userData = searchUsers.getUserData(organisationId)

        # Search for ticket data
        ticketData = searchTickets.getTicketData(organisationId)

        # Output statements
        print(UNDERLINE + BOLD + "Result for organisation with {} as {}".format(term, value) + END)
        customFormat.formatData(organisation, "user")
        print(UNDERLINE + BOLD + "User results for organisation with {} as {}".format(term, value) + END)
        customFormat.formatData(userData)
        print(UNDERLINE + BOLD + "Ticket results for organisation with {} as {}".format(term, value) + END)
        customFormat.formatData(ticketData, "ticket")

        return True
    
    # Validate the term that the user search for
    def validateTerm(self, term):
        orgsKeys = self.getOrgsKeys()

        if (term in orgsKeys):
            return True
        else:
            return False
