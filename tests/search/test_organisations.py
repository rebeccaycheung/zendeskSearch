import pytest
from data_test import orgData

class TestOrgs:
    def test_org_has_data(self, searchOrgs):
        response = searchOrgs.getOrgs()
        expectedResponse = orgData
        assert response == expectedResponse
    
    def test_org_data_fetch_keys(self, searchOrgs):
        response = searchOrgs.getOrgsKeys()
        expectedResponse = ['_id', 'url']
        assert response == expectedResponse

    def test_org_data_is_fetched_with_valid_org_id(self, searchOrgs):
        organisationId = 121
        response = searchOrgs.getOrgData(organisationId)
        expectedResponse = {
            "_id": 121,
            "url": "http://initech.zendesk.com/api/v2/organizations/121.json"
        }
        assert response == expectedResponse
    
    def test_org_data_cannot_be_fetched_with_invalid_org_id(self, searchOrgs):
        organisationId = "testing"
        response = searchOrgs.getOrgData(organisationId)
        expectedResponse = "No organisation data found"
        assert response == expectedResponse
    
    def test_fetch_data_by_org(self, capfd, searchUsers, searchOrgs, searchTickets):
        term = "_id"
        value = 121
        org = {
            "_id": 121,
            "url": "http://initech.zendesk.com/api/v2/organizations/121.json"
        }
        response = searchOrgs.getData(org, searchUsers, searchTickets, value, term)
        assert response == True

    def test_valid_org_term(self, searchOrgs):
        response = searchOrgs.validateTerm("_id")
        assert response == True

    def test_invalid_org_term(self, searchOrgs):
        response = searchOrgs.validateTerm("testing")
        assert response == False
