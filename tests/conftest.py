import pytest

@pytest.fixture
def emptyQuery():
    from query import Query
    query = Query(None, None, None)
    yield query

@pytest.fixture
def query():
    from query import Query
    query = Query('1', '_id', '1')
    yield query

@pytest.fixture
def search():
    from search import Search
    search = Search()
    yield search

@pytest.fixture
def searchUsers():
    from search_user import SearchUsers
    users = [{
        "_id": 1,
        "url": "http://initech.zendesk.com/api/v2/users/1.json",
        "organization_id": 121
    }],
    searchUsers = SearchUsers(users)
    yield searchUsers

@pytest.fixture
def searchOrgs():
    from search_organisation import SearchOrgs
    orgs = [{
        "_id": 121,
        "url": "http://initech.zendesk.com/api/v2/organizations/121.json"
    }],
    searchOrgs = SearchOrgs(orgs)
    yield searchOrgs

@pytest.fixture
def searchTickets():
    from search_tickets import SearchTickets
    tickets = [{
        "_id": "c527e065-ec62-40ed-aa72-136f5ab0eb89",
        "organization_id": 121,
    }],
    searchTickets = SearchTickets(tickets)
    yield searchTickets
