import json
from engine.constants import USERS, ORGS, TICKETS, TERMS, TERM_INVALID, SEARCHING, FINISHED_SEARCHING, NO_RESULTS
from engine.search_user import SearchUsers
from engine.search_organisation import SearchOrgs
from engine.search_tickets import SearchTickets

# Search object
class Search:
    def __init__(self):
        pass

    def readFile(self, file):
        with open(file) as jsonFile:
            data = json.load(jsonFile)
            return data
    
    # Convert the value the user has given (since it is a string from input) to the correct type
    def convertValue(self, value):
        if (value.isdigit()):
            return int(value)
        elif (value.lower() == "true" or value.lower() == "false"):
            return bool(value)
        else:
            return value
    
    # Main function to search the data
    def findData(self, query):
        # Read all data files
        users = self.readFile('data/users.json')
        organisations = self.readFile('data/organizations.json')
        tickets = self.readFile('data/tickets.json')

        # Instantiate all search objects
        searchUsers = SearchUsers(users)
        searchOrgs = SearchOrgs(organisations)
        searchTickets = SearchTickets(tickets)

        # Get the user's query
        term = query.getTerm()
        value = query.getValue()
        category = query.getCategory()

        # Check if the term the user has given is valid, i.e. can be searched by
        if (term != TERMS) and not (searchUsers.validateTerm(term) or searchOrgs.validateTerm(term) or searchTickets.validateTerm(term)):
            return TERM_INVALID
        
        # If the category is users
        if (category == USERS):
            # Check if the user wants the terms
            if (term == TERMS):
                return searchUsers.getUsersKeysFormat()
            else:
                for user in searchUsers.getUsers():
                    # Search the user data and find the user that matches the query
                    if user[term] == self.convertValue(value):
                        print(SEARCHING)
                        # If a user is found then search the rest of the data to find the organisation and tickets
                        searchUsers.getData(user, searchOrgs, searchTickets, value, term)
                        return FINISHED_SEARCHING
        # If the category is organisations
        elif (category == ORGS):
            # Check if the user wants the terms
            if (term == TERMS):
                return searchOrgs.getOrgsKeysFormat()
            else:
                for organisation in searchOrgs.getOrgs():
                    # Search the organisation data and find the organisation that matches the query
                    if organisation[term] == self.convertValue(value):
                        print(SEARCHING)
                        # If a organisation is found then search the rest of the data to find the users and tickets
                        searchOrgs.getData(organisation, searchUsers, searchTickets, value, term)
                        return FINISHED_SEARCHING
        # If the category is tickets
        elif (category == TICKETS):
            # Check if the user wants the terms
            if (term == TERMS):
                return searchTickets.getTicketsKeysFormat()
            else:
                for ticket in searchTickets.getTickets():
                    # Search the ticket data and find the ticket that matches the query
                    if ticket[term] == self.convertValue(value):
                        print(SEARCHING)
                        # If a ticket is found then search the rest of the data to find the organisation and users
                        searchTickets.getData(ticket, searchUsers, searchOrgs, value, term)
                        return FINISHED_SEARCHING
        # If no results were found, output to user that no results were found
        return NO_RESULTS
