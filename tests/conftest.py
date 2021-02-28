import pytest
from data.data_test import userData
from data.data_test import orgData
from data.data_test import ticketData

@pytest.fixture
def emptyQuery():
    from engine.query import Query
    query = Query(None, None, None)
    yield query

@pytest.fixture
def userSelectedQuery():
    from engine.query import Query
    userSelectedQuery = Query('users', '_id', None)
    yield userSelectedQuery

@pytest.fixture
def orgSelectedQuery():
    from engine.query import Query
    orgSelectedQuery = Query('organisations', '_id', None)
    yield orgSelectedQuery

@pytest.fixture
def ticketSelectedQuery():
    from engine.query import Query
    ticketSelectedQuery = Query('tickets', 'organization_id', None)
    yield ticketSelectedQuery

@pytest.fixture
def userQuery():
    from engine.query import Query
    userQuery = Query('users', '_id', '1')
    yield userQuery

@pytest.fixture
def orgQuery():
    from engine.query import Query
    orgQuery = Query('organisations', '_id', '122')
    yield orgQuery

@pytest.fixture
def ticketQuery():
    from engine.query import Query
    ticketQuery = Query('tickets', 'organization_id', '122')
    yield ticketQuery

@pytest.fixture
def noDataQuery():
    from engine.query import Query
    noDataQuery = Query('users', '_id', '123')
    yield noDataQuery

@pytest.fixture
def invalidQuery():
    from engine.query import Query
    invalidQuery = Query('users', 'testing', '123456')
    yield invalidQuery

@pytest.fixture
def usersTermQuery():
    from engine.query import Query
    usersTermQuery = Query('users', 'terms', 'None')
    yield usersTermQuery

@pytest.fixture
def orgsTermQuery():
    from engine.query import Query
    orgsTermQuery = Query('organisations', 'terms', 'None')
    yield orgsTermQuery

@pytest.fixture
def ticketsTermQuery():
    from engine.query import Query
    ticketsTermQuery = Query('tickets', 'terms', 'None')
    yield ticketsTermQuery

@pytest.fixture
def search():
    from engine.search import Search
    search = Search()
    yield search

@pytest.fixture
def searchUsers():
    from engine.search_user import SearchUsers
    users = userData
    searchUsers = SearchUsers(users)
    yield searchUsers

@pytest.fixture
def searchOrgs():
    from engine.search_organisation import SearchOrgs
    orgs = orgData
    searchOrgs = SearchOrgs(orgs)
    yield searchOrgs

@pytest.fixture
def searchTickets():
    from engine.search_tickets import SearchTickets
    tickets = ticketData
    searchTickets = SearchTickets(tickets)
    yield searchTickets
