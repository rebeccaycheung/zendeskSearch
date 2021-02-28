#!/usr/bin/env python3

from search import Search
from query import Query
from constants import USERS, ORGS, TICKETS, RANGE_ERROR, CATEGORY_SELECTION_TRY_AGAIN, SEARCH_VALUE, CATEGORY_SELECTION, SEARCH_TERM

def getUserInput(prompt):
    userInput = input(prompt)
    return userInput

def selectSearchType(query, command):
    if (command == 1):
        query.setCategory(USERS)
    elif (command == 2):
        query.setCategory(ORGS)
    elif (command == 3):
        query.setCategory(TICKETS)
    else:
        return RANGE_ERROR
    return

def validateCategorySelection(query, command):
    try:
        selectSearchType(query, int(command))
    except(ValueError):
        return CATEGORY_SELECTION_TRY_AGAIN

def searchEngine(search, query):
    term = query.getTerm()
    if (term == "terms"):
        result = search.findData(query)
        return result
    else:
        command = getUserInput(SEARCH_VALUE)
        query.setValue(command)
        result = search.findData(query)
        return result

def main():
    print("""
        Welcome to Zendesk Search!

        Type 'quit' to exit the program at any time.
        Type 'terms' to view a list of terms you can search by for each category.

        Start by searching the term and value.
    """)

    search = Search()
    query = Query(None, None, None)
    
    command = getUserInput(CATEGORY_SELECTION)
    while command != "quit":
        selectionResult = validateCategorySelection(query, command)
        if (selectionResult != None):
            print(selectionResult)

        command = getUserInput(SEARCH_TERM)
        query.setTerm(command)
        result = searchEngine(search, query)
        if (result != None):
            print(result)

        command = getUserInput(CATEGORY_SELECTION)
    try:
        exit(0)
    except:
        exit(1)
        raise

if __name__ == "__main__":
    main()
