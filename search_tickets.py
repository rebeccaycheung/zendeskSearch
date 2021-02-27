import color
import json
from custom_format import CustomFormat

class SearchTickets:
    def __init__(self, tickets):
        self.tickets = tickets

    def getTickets(self):
        return self.tickets

    #Temporary solution - need to figure out how to get all possible keys
    def getTicketsKeys(self):
        return self.tickets[0]

    def getTicketsKeysFormat(self):
        customFormat = CustomFormat()
        return customFormat.formatTerms(self.getTicketsKeys())

    def getTicketData(self, organisationId):
        ticketData = []
        for ticket in self.tickets:
            try:
                if ticket['organization_id'] == organisationId:
                    ticketData.append(ticket)
            except(KeyError):
                continue
        if (len(ticketData) == 0):
            return "No results for tickets found"
        return ticketData

    def getData(self, currentTicket, searchUsers, searchOrgs, value, term):
        customFormat = CustomFormat()

        organisationId = currentTicket['organization_id']
        userData = searchUsers.getUserData(organisationId)
        organisationData = searchOrgs.getOrganisationData(organisationId)
        ticketData = [currentTicket]

        for ticket in self.tickets:
            try:
                if ticket['organization_id'] == organisationId and ticket['_id'] != currentTicket['_id']:
                    ticketData.append(ticket)
            except(KeyError):
                continue

        print(color.UNDERLINE + color.BOLD + "Ticket results for ticket with {} as {}".format(term, value) + color.END)
        print(customFormat.formatData(ticketData, "ticket"))
        print(color.UNDERLINE + color.BOLD + "Organisation result for ticket with {} as {}".format(term, value) + color.END)
        print(customFormat.formatData(organisationData))
        print(color.UNDERLINE + color.BOLD + "User results for ticket with {} as {}".format(term, value) + color.END)
        print(customFormat.formatData(userData, "user"))
        return
    
    def validateTerm(self, term):
        ticketsKeys = set(self.getTicketsKeys())

        if (term in ticketsKeys):
            return True
        else:
            return False
