import pytest

class TestSearch:
    def test_fetch_user_terms(self, search, usersTermQuery):
        response = search.findData(usersTermQuery)
        expectedResponse = "Fields to search by: _id\nurl\nexternal_id\nname\nalias\ncreated_at\nactive\nverified\nshared\nlocale\ntimezone\nlast_login_at\nemail\nphone\nsignature\norganization_id\ntags\nsuspended\nrole"
        assert response == expectedResponse

    def test_fetch_org_terms(self, search, orgsTermQuery):
        response = search.findData(orgsTermQuery)
        expectedResponse = "Fields to search by: _id\nurl\nexternal_id\nname\ndomain_names\ncreated_at\ndetails\nshared_tickets\ntags"
        assert response == expectedResponse

    def test_fetch_ticket_terms(self, search, ticketsTermQuery):
        response = search.findData(ticketsTermQuery)
        expectedResponse = "Fields to search by: _id\nurl\nexternal_id\ncreated_at\ntype\nsubject\ndescription\npriority\nstatus\nsubmitter_id\nassignee_id\norganization_id\ntags\nhas_incidents\ndue_at\nvia"
        assert response == expectedResponse
    
    def test_valid_term(self, search, userQuery):
        response = search.findData(userQuery)
        assert response != "The term you have entered does not exist, please try again."

    def test_invalid_term(self, search, invalidQuery):
        response = search.findData(invalidQuery)
        assert response == "The term you have entered does not exist, please try again."
    
    def test_search_by_user_no_errors(self, search, userQuery):
        response = search.findData(userQuery)
        assert response == "Finished searching"
    
    def test_search_by_org_no_errors(self, search, orgQuery):
        response = search.findData(orgQuery)
        assert response == "Finished searching"
    
    def test_search_by_ticket_no_errors(self, search, ticketQuery):
        response = search.findData(ticketQuery)
        assert response == "Finished searching"

    def test_convert_data(self, search):
        integer = search.convertValue("1")
        assert integer == 1

        boolean = search.convertValue("True")
        assert boolean == True

        string = search.convertValue("testing")
        assert string == "testing"

    def test_no_results_found(self, search, noDataQuery):
        response = search.findData(noDataQuery)
        assert response == "Cannot find any results"
