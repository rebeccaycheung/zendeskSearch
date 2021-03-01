import pytest
from data.data_test import userData

# Tests for the user search object
class TestSearchUsers:
    def test_user_has_data(self, searchUsers):
        response = searchUsers.getUsers()
        expectedResponse = userData
        assert response == expectedResponse
    
    def test_user_data_fetch_keys(self, searchUsers):
        response = searchUsers.getUsersKeys()
        expectedResponse = ['_id', 'url', 'organization_id']
        assert response == expectedResponse

    def test_user_data_is_fetched_with_valid_org_id(self, searchUsers):
        organisationId = 121
        response = searchUsers.getUserData(organisationId)
        expectedResponse = [{
            "_id": 1,
            "url": "http://initech.zendesk.com/api/v2/users/1.json",
            "organization_id": 121
        }]
        assert response == expectedResponse
    
    def test_user_data_cannot_be_fetched_with_invalid_org_id(self, searchUsers):
        organisationId = "testing"
        response = searchUsers.getUserData(organisationId)
        expectedResponse = "Cannot find any results"
        assert response == expectedResponse
    
    def test_fetch_data_by_user(self, searchUsers, searchOrgs, searchTickets):
        term = "_id"
        value = 1
        user = {
            "_id": 1,
            "url": "http://initech.zendesk.com/api/v2/users/1.json",
            "organization_id": 121
        }
        response = searchUsers.getData(user, searchOrgs, searchTickets, value, term)
        assert response == True

    def test_valid_user_term(self, searchUsers):
        response = searchUsers.validateTerm("_id")
        assert response == True

    def test_invalid_user_term(self, searchUsers):
        response = searchUsers.validateTerm("testing")
        assert response == False
