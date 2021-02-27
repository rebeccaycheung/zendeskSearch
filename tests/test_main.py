import pytest

class TestMain:
    def test_user_input(self, monkeypatch):
        # Mock the user input using monkeypatch
        monkeypatch.setattr('builtins.input', lambda _: "1")

        user_input = input("Select which to search by 1) users, 2) organisations, 3) tickets: ")
        assert user_input == "1"

        monkeypatch.setattr('builtins.input', lambda _: "_id")

        user_input = input("Search by term: ")
        assert user_input == "_id"

        monkeypatch.setattr('builtins.input', lambda _: "1")

        user_input = input("Enter a value: ")
        assert user_input == "1"
