import json
import constants
from search_user import SearchUsers
from search_organisation import SearchOrgs
from search_tickets import SearchTickets

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

        if (term != constants.TERMS) and not (searchUsers.validateTerm(term) or searchOrgs.validateTerm(term) or searchTickets.validateTerm(term)):
            return constants.TERM_INVALID

        if (category == constants.USERS):
            if (term == constants.TERMS):
                return searchUsers.getUsersKeysFormat()
            else:
                for user in searchUsers.getUsers():
                    if user[term] == self.convertValue(value):
                        print(constants.SEARCHING)
                        searchUsers.getData(user, searchOrgs, searchTickets, value, term)
                        return constants.FINISHED_SEARCHING

        elif (category == constants.ORGS):
            if (term == constants.TERMS):
                return searchOrgs.getOrgsKeysFormat()
            else:
                for organisation in searchOrgs.getOrgs():
                    if organisation[term] == self.convertValue(value):
                        print(constants.SEARCHING)
                        searchOrgs.getData(organisation, searchUsers, searchTickets, value, term)
                        return constants.FINISHED_SEARCHING

        elif (category == constants.TICKETS):
            if (term == constants.TERMS):
                return searchTickets.getTicketsKeysFormat()
            else:
                for ticket in searchTickets.getTickets():
                    if ticket[term] == self.convertValue(value):
                        print(constants.SEARCHING)
                        searchTickets.getData(ticket, searchUsers, searchOrgs, value, term)
                        return constants.FINISHED_SEARCHING

        return constants.NO_RESULTS
