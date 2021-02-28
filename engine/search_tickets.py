from engine.color import BOLD, END, UNDERLINE
from engine.constants import NO_RESULTS
from engine.custom_format import CustomFormat

# Search tickets object - stores the tickets data
class SearchTickets:
    def __init__(self, tickets):
        self.tickets = tickets
    
    # Getter
    def getTickets(self):
        return self.tickets
    
    # Get all the terms in the ticket data
    def getTicketsKeys(self):
        # Basic solution to get the terms from the data
        return [*self.tickets[0]]
    
    # Format the ticket terms
    def getTicketsKeysFormat(self):
        customFormat = CustomFormat()
        return customFormat.formatTerms(self.getTicketsKeys())
    
    # Get all ticket data where the organisation id is equal to what the user search for
    def getTicketData(self, organisationId):
        # Result should be a list because there can be many tickets for one organisation
        ticketData = []
        for ticket in self.tickets:
            try:
                if ticket['organization_id'] == organisationId:
                    ticketData.append(ticket)
            except(KeyError):
                continue
        if (len(ticketData) == 0):
            return NO_RESULTS
        return ticketData
    
    # Search all the data by ticket
    def getData(self, currentTicket, searchUsers, searchOrgs, value, term):
        customFormat = CustomFormat()

        organisationId = currentTicket['organization_id']
        userData = searchUsers.getUserData(organisationId)
        organisationData = searchOrgs.getOrgData(organisationId)

        # Start with the current ticket in the final list of tickets
        ticketData = [currentTicket]

        # Search for the remaining tickets that match the query
        for ticket in self.tickets:
            try:
                if ticket['organization_id'] == organisationId and ticket['_id'] != currentTicket['_id']:
                    ticketData.append(ticket)
            except(KeyError):
                continue
        
        # Output statements
        print(UNDERLINE + BOLD + "Ticket results for ticket with {} as {}".format(term, value) + END)
        customFormat.formatData(ticketData, "ticket")
        print(UNDERLINE + BOLD + "Organisation result for ticket with {} as {}".format(term, value) + END)
        customFormat.formatData(organisationData)
        print(UNDERLINE + BOLD + "User results for ticket with {} as {}".format(term, value) + END)
        customFormat.formatData(userData, "user")

        return True
    
    # Validate the term that the user search for
    def validateTerm(self, term):
        ticketsKeys = self.getTicketsKeys()

        if (term in ticketsKeys):
            return True
        else:
            return False
