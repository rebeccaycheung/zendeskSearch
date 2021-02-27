import pytest
from main import main
from main import getUserInput
from main import selectSearchType
import constants

class TestMain:
    def test_user_input(self, monkeypatch):
        # Mock the user input using monkeypatch
        monkeypatch.setattr('builtins.input', lambda _: "1")
        user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        assert user_input == "1"
    
    def test_valid_user_input(self, monkeypatch, emptyQuery):
        pass
    #     monkeypatch.setattr('builtins.input', lambda _: "1")
    #     user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
    #     command = main.getUserInput(constants.CATEGORY_SELECTION)
    #     main.selectSearchType(emptyQuery, command)
    #     assert emptyQuery.getCategory() == 'users'

    #     monkeypatch.setattr('builtins.input', lambda _: "_id")
    #     user_input = input("Search by term: ")
    #     assert emptyQuery.getTerm() == '_id'

    #     monkeypatch.setattr('builtins.input', lambda _: "1")
    #     user_input = input("Enter a value: ")
    #     assert emptyQuery.getValue() == '1'

    def test_valid_category_selection(self, monkeypatch, emptyQuery):
        pass
        # monkeypatch.setattr('builtins.input', lambda _: "1")
        # user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        # command = getUserInput(constants.CATEGORY_SELECTION)
        # selectSearchType(emptyQuery, command)
        # assert emptyQuery.getCategory() == 'users'

        # monkeypatch.setattr('builtins.input', lambda _: "2")
        # user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        # command = getUserInput(constants.CATEGORY_SELECTION)
        # selectSearchType(emptyQuery, command)
        # assert emptyQuery.getCategory() == 'organisations'

        # monkeypatch.setattr('builtins.input', lambda _: "3")
        # user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        # command = getUserInput(constants.CATEGORY_SELECTION)
        # selectSearchType(emptyQuery, command)
        # assert emptyQuery.getCategory() == 'tickets'
    
    def test_invalid_user_input(self, monkeypatch, emptyQuery):
        pass
    
    def test_quit_input(self, monkeypatch, emptyQuery):
        monkeypatch.setattr('builtins.input', lambda _: "quit")

        user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        with pytest.raises(SystemExit) as e:
            main()
            assert e.type == SystemExit
            assert e.value.code == 0
