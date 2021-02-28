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
        elif (value == "True" or value == "False"):
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

        if (term != 'terms') and not (searchUsers.validateTerm(term) or searchOrgs.validateTerm(term) or searchTickets.validateTerm(term)):
            return constants.TERM_INVALID

        if (category == 'users'):
            if (term == 'terms'):
                return searchUsers.getUsersKeysFormat()
            else:
                for user in searchUsers.getUsers():
                    if user[term] == self.convertValue(value):
                        print("Searching users...")
                        searchUsers.getData(user, searchOrgs, searchTickets, value, term)
                        return "Finished searching"

        elif (category == 'organisations'):
            if (term == 'terms'):
                return searchOrgs.getOrgsKeysFormat()
            else:
                for organisation in searchOrgs.getOrgs():
                    if organisation[term] == self.convertValue(value):
                        print("Searching organisations...")
                        searchOrgs.getData(organisation, searchUsers, searchTickets, value, term)
                        return "Finished searching"

        elif (category == 'tickets'):
            if (term == 'terms'):
                return searchTickets.getTicketsKeysFormat()
            else:
                for ticket in searchTickets.getTickets():
                    if ticket[term] == self.convertValue(value):
                        print("Searching tickets...")
                        searchTickets.getData(ticket, searchUsers, searchOrgs, value, term)
                        return "Finished searching"

        return "Cannot find any results"
