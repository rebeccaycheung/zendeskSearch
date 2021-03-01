import pytest
from main import main
from main import getUserInput
from main import setSearchType
from main import searchEngine
from main import validateCategorySelection

# Tests for the Main file
class TestMain:
    def test_user_input(self, monkeypatch):
        # Mock the user input using monkeypatch
        monkeypatch.setattr('builtins.input', lambda _: "1")
        user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        assert user_input == "1"
    
    def test_valid_category_selection(self, monkeypatch, emptyQuery):
        monkeypatch.setattr('builtins.input', lambda _: "1")
        user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        setSearchType(emptyQuery, int(user_input))
        assert emptyQuery.getCategory() == 'users'

        monkeypatch.setattr('builtins.input', lambda _: "2")
        user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        setSearchType(emptyQuery, int(user_input))
        assert emptyQuery.getCategory() == 'organisations'

        monkeypatch.setattr('builtins.input', lambda _: "3")
        user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        setSearchType(emptyQuery, int(user_input))
        assert emptyQuery.getCategory() == 'tickets'
    
    def test_invalid_range_category_selection(self, monkeypatch, emptyQuery):
        monkeypatch.setattr('builtins.input', lambda _: "123")
        user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        response = setSearchType(emptyQuery, int(user_input))
        assert response == "Please enter a number between 1 and 3"

        monkeypatch.setattr('builtins.input', lambda _: "4")
        user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        response = setSearchType(emptyQuery, int(user_input))
        assert response == "Please enter a number between 1 and 3"

        monkeypatch.setattr('builtins.input', lambda _: "0")
        user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        response = setSearchType(emptyQuery, int(user_input))
        assert response == "Please enter a number between 1 and 3"

    def test_invalid_category_selection(self, monkeypatch, emptyQuery):
        monkeypatch.setattr('builtins.input', lambda _: "testing")
        user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        response = validateCategorySelection(emptyQuery, user_input)
        assert response == "Input was not a number between 1-3, please try again."

        monkeypatch.setattr('builtins.input', lambda _: "!@#$$%#")
        user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        response = validateCategorySelection(emptyQuery, user_input)
        assert response == "Input was not a number between 1-3, please try again."

        monkeypatch.setattr('builtins.input', lambda _: "         ")
        user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        response = validateCategorySelection(emptyQuery, user_input)
        assert response == "Input was not a number between 1-3, please try again."
    
    def test_quit_input(self, monkeypatch, emptyQuery):
        monkeypatch.setattr('builtins.input', lambda _: "quit")

        with pytest.raises(SystemExit) as e:
            main()
            assert e.type == SystemExit
            assert e.value.code == 0

    def test_get_data_by_users(self, monkeypatch, search, userSelectedQuery):
        monkeypatch.setattr('builtins.input', lambda _: "1")
        valueInput = input("Enter a value: ")

        response = searchEngine(search, userSelectedQuery)
        assert userSelectedQuery.getTerm() == "_id"
        assert userSelectedQuery.getCategory() == "users"
        assert userSelectedQuery.getValue() == "1"
        assert response == "Finished searching."

    def test_get_data_by_organisation(self, monkeypatch, search, orgSelectedQuery):
        monkeypatch.setattr('builtins.input', lambda _: "119")
        valueInput = input("Enter a value: ")

        response = searchEngine(search, orgSelectedQuery)
        assert orgSelectedQuery.getTerm() == "_id"
        assert orgSelectedQuery.getCategory() == "organisations"
        assert orgSelectedQuery.getValue() == "119"
        assert response == "Finished searching."

    def test_get_data_by_ticket(self, monkeypatch, search, ticketSelectedQuery):
        monkeypatch.setattr('builtins.input', lambda _: "119")
        valueInput = input("Enter a value: ")

        response = searchEngine(search, ticketSelectedQuery)
        assert ticketSelectedQuery.getTerm() == "organization_id"
        assert ticketSelectedQuery.getCategory() == "tickets"
        assert ticketSelectedQuery.getValue() == "119"
        assert response == "Finished searching."
