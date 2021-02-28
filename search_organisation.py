import color
import json
import constants
from custom_format import CustomFormat

class SearchOrgs:
    def __init__(self, orgs):
        self.orgs = orgs
    
    def getOrgs(self):
        return self.orgs

    def getOrgsKeys(self):
        return [*self.orgs[0]]

    def getOrgsKeysFormat(self):
        customFormat = CustomFormat()
        return customFormat.formatTerms(self.getOrgsKeys())

    def getOrgData(self, organisationId):
        for organisation in self.orgs:
            try:
                if organisation['_id'] == organisationId:
                    return organisation
            except(KeyError):
                continue
        return constants.NO_RESULTS

    def getData(self, organisation, searchUsers, searchTickets, value, term):
        customFormat = CustomFormat()

        organisationId = organisation['_id']
        userData = searchUsers.getUserData(organisationId)
        ticketData = searchTickets.getTicketData(organisationId)

        print(color.UNDERLINE + color.BOLD + "Result for organisation with {} as {}".format(term, value) + color.END)
        customFormat.formatData(organisation, "user")
        print(color.UNDERLINE + color.BOLD + "User results for organisation with {} as {}".format(term, value) + color.END)
        customFormat.formatData(userData)
        print(color.UNDERLINE + color.BOLD + "Ticket results for organisation with {} as {}".format(term, value) + color.END)
        customFormat.formatData(ticketData, "ticket")

        return True
    
    def validateTerm(self, term):
        orgsKeys = self.getOrgsKeys()

        if (term in orgsKeys):
            return True
        else:
            return False
