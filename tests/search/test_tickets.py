import pytest
from data_test import ticketData

class TestSearchTickets:
    def test_tickets_has_data(self, searchTickets):
        response = searchTickets.getTickets()
        expectedResponse = ticketData
        assert response == expectedResponse
    
    def test_tickets_data_fetch_keys(self, searchTickets):
        response = searchTickets.getTicketsKeys()
        expectedResponse = ['_id', 'organization_id']
        assert response == expectedResponse

    def test_tickets_data_is_fetched_with_valid_org_id(self, searchTickets):
        organisationId = 121
        response = searchTickets.getTicketData(organisationId)
        expectedResponse = [{
            "_id": "c527e065-ec62-40ed-aa72-136f5ab0eb89",
            "organization_id": 121
        }]
        assert response == expectedResponse
    
    def test_tickets_data_cannot_be_fetched_with_invalid_org_id(self, searchTickets):
        organisationId = "testing"
        response = searchTickets.getTicketData(organisationId)
        expectedResponse = "No results for tickets found"
        assert response == expectedResponse
    
    def test_fetch_data_by_tickets(self, capfd, searchUsers, searchOrgs, searchTickets):
        term = "organization_id"
        value = 121
        tickets = {
            "_id": "c527e065-ec62-40ed-aa72-136f5ab0eb89",
            "organization_id": 121
        }
        response = searchTickets.getData(tickets, searchUsers, searchOrgs, value, term)
        assert response == True

    def test_valid_tickets_term(self, searchTickets):
        response = searchTickets.validateTerm("_id")
        assert response == True

    def test_invalid_tickets_term(self, searchTickets):
        response = searchTickets.validateTerm("testing")
        assert response == False
