import json
from engine.constants import USERS, ORGS, TICKETS, TERMS, TERM_INVALID, SEARCHING, FINISHED_SEARCHING, NO_RESULTS
from engine.search_user import SearchUsers
from engine.search_organisation import SearchOrgs
from engine.search_tickets import SearchTickets

class Search:
    def __init__(self):
        pass

    def readFile(self, file):
        with open(file) as jsonFile:
            data = json.load(jsonFile)
            return data

    def convertValue(self, value):
        if (value.isdigit()):
            return int(value)
        elif (value.lower() == "true" or value.lower() == "false"):
            return bool(value)
        else:
            return value

    def findData(self, query):
        users = self.readFile('data/users.json')
        organisations = self.readFile('data/organizations.json')
        tickets = self.readFile('data/tickets.json')

        searchUsers = SearchUsers(users)
        searchOrgs = SearchOrgs(organisations)
        searchTickets = SearchTickets(tickets)

        term = query.getTerm()
        value = query.getValue()
        category = query.getCategory()

        if (term != TERMS) and not (searchUsers.validateTerm(term) or searchOrgs.validateTerm(term) or searchTickets.validateTerm(term)):
            return TERM_INVALID

        if (category == USERS):
            if (term == TERMS):
                return searchUsers.getUsersKeysFormat()
            else:
                for user in searchUsers.getUsers():
                    if user[term] == self.convertValue(value):
                        print(SEARCHING)
                        searchUsers.getData(user, searchOrgs, searchTickets, value, term)
                        return FINISHED_SEARCHING

        elif (category == ORGS):
            if (term == TERMS):
                return searchOrgs.getOrgsKeysFormat()
            else:
                for organisation in searchOrgs.getOrgs():
                    if organisation[term] == self.convertValue(value):
                        print(SEARCHING)
                        searchOrgs.getData(organisation, searchUsers, searchTickets, value, term)
                        return FINISHED_SEARCHING

        elif (category == TICKETS):
            if (term == TERMS):
                return searchTickets.getTicketsKeysFormat()
            else:
                for ticket in searchTickets.getTickets():
                    if ticket[term] == self.convertValue(value):
                        print(SEARCHING)
                        searchTickets.getData(ticket, searchUsers, searchOrgs, value, term)
                        return FINISHED_SEARCHING

        return NO_RESULTS
