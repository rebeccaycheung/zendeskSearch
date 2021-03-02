import pytest

# Tests for the search object
class TestSearch:
    def test_fetch_user_terms(self, search, usersTermQuery):
        response = search.findData(usersTermQuery)
        expectedResponse = "Fields to search by: \n- _id\n- url\n- external_id\n- name\n- alias\n- created_at\n- active\n- verified\n- shared\n- locale\n- timezone\n- last_login_at\n- email\n- phone\n- signature\n- organization_id\n- tags\n- suspended\n- role"
        assert response == expectedResponse

    def test_fetch_org_terms(self, search, orgsTermQuery):
        response = search.findData(orgsTermQuery)
        expectedResponse = "Fields to search by: \n- _id\n- url\n- external_id\n- name\n- domain_names\n- created_at\n- details\n- shared_tickets\n- tags"
        assert response == expectedResponse

    def test_fetch_ticket_terms(self, search, ticketsTermQuery):
        response = search.findData(ticketsTermQuery)
        expectedResponse = "Fields to search by: \n- _id\n- url\n- external_id\n- created_at\n- type\n- subject\n- description\n- priority\n- status\n- submitter_id\n- assignee_id\n- organization_id\n- tags\n- has_incidents\n- due_at\n- via"
        assert response == expectedResponse
    
    def test_valid_term(self, search, userQuery):
        response = search.findData(userQuery)
        assert response != "The term you have entered does not exist, please try again."

    def test_invalid_term(self, search, invalidQuery):
        response = search.findData(invalidQuery)
        assert response == "The term you have entered does not exist, please try again."
    
    def test_search_by_user_no_errors(self, search, userQuery):
        response = search.findData(userQuery)
        assert response == "Finished searching."
    
    def test_search_by_org_no_errors(self, search, orgQuery):
        response = search.findData(orgQuery)
        assert response == "Finished searching."
    
    def test_search_by_ticket_no_errors(self, search, ticketQuery):
        response = search.findData(ticketQuery)
        assert response == "Finished searching."

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
