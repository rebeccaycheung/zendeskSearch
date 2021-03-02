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
        users = self.readFile('data/users.json')
        organisations = self.readFile('data/organizations.json')
        tickets = self.readFile('data/tickets.json')

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
        
        if (category == USERS):
            # Check if the user wants the terms
            if (term == TERMS):
                return searchUsers.getUsersKeysFormat()
            else:
                print(SEARCHING)
                for user in searchUsers.getUsers():
                    # Search the user data and find the user that matches the query
                    convertedValue = self.convertValue(value)
                    # Check if key value pair is string
                    if user[term] == convertedValue:
                        # If a user is found then search the rest of the data to find the organisation and tickets
                        searchUsers.getData(user, searchOrgs, searchTickets, value, term)
                        return FINISHED_SEARCHING
                    else:
                        try:
                            # Check if the key value is a list
                            if convertedValue in user[term]:
                                # If a user is found then search the rest of the data to find the organisation and tickets
                                searchUsers.getData(user, searchOrgs, searchTickets, value, term)
                                return FINISHED_SEARCHING
                        except(TypeError):
                            continue
        elif (category == ORGS):
            if (term == TERMS):
                return searchOrgs.getOrgsKeysFormat()
            else:
                print(SEARCHING)
                for organisation in searchOrgs.getOrgs():
                    convertedValue = self.convertValue(value)
                    if organisation[term] == convertedValue:
                        searchOrgs.getData(organisation, searchUsers, searchTickets, value, term)
                        return FINISHED_SEARCHING
                    else:
                        try:
                            if convertedValue in organisation[term]:
                                searchOrgs.getData(organisation, searchUsers, searchTickets, value, term)
                                return FINISHED_SEARCHING
                        except(TypeError):
                            continue
        elif (category == TICKETS):
            if (term == TERMS):
                return searchTickets.getTicketsKeysFormat()
            else:
                print(SEARCHING)
                for ticket in searchTickets.getTickets():
                    convertedValue = self.convertValue(value)
                    if ticket[term] == convertedValue:
                        searchTickets.getData(ticket, searchUsers, searchOrgs, value, term)
                        return FINISHED_SEARCHING
                    else:
                        try:
                            if convertedValue in ticket[term]:
                                searchTickets.getData(ticket, searchUsers, searchOrgs, value, term)
                                return FINISHED_SEARCHING
                        except(TypeError):
                            continue
        # If no results were found, output to user that no results were found
        return NO_RESULTS
