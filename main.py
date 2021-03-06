#!/usr/bin/env python3

from engine.search import Search
from engine.query import Query
from engine.constants import USERS, ORGS, TICKETS, RANGE_ERROR, CATEGORY_SELECTION_TRY_AGAIN, SEARCH_VALUE, CATEGORY_SELECTION, SEARCH_TERM

def getUserInput(prompt):
    userInput = input(prompt)
    return userInput

# Check the category selection and set the query's category
def setSearchType(query, command):
    if (command == 1):
        query.setCategory(USERS)
    elif (command == 2):
        query.setCategory(ORGS)
    elif (command == 3):
        query.setCategory(TICKETS)
    else:
        print(RANGE_ERROR)
        return False
    return True

# Validate that the user input is a number when asked to select the category to search for
def validateCategorySelection(query, command):
    try:
        return setSearchType(query, int(command))
    except(ValueError):
        print(CATEGORY_SELECTION_TRY_AGAIN)
        return False

#Main function to search the data
def searchEngine(search, query):
    term = query.getTerm()
    #If the user enters 'terms' when asked for a term to search by then don't ask for the value to search by
    #Go straight to finding the data, e.g. a list of terms for the category the user has chosen
    if (term == "terms"):
        result = search.findData(query)
        return result
    else:
        #Otherwise, ask for a value then go find the data
        command = getUserInput(SEARCH_VALUE)
        query.setValue(command)
        result = search.findData(query)
        return result

#Entry point to program
def main():
    print("""
        Welcome to Zendesk Search!

        Type 'quit' to exit the program at any time.

        Start by selecting a category to search by:
            - Type 1 for users
            - Type 2 for organisations
            - Type 3 for tickets
        Then search by term and value

        When prompted for a term type 'terms' to view a list of terms you can search by for each category.
    """)

    #Instantiate search and query object
    search = Search()
    query = Query(None, None, None)
    
    #Ask the user which category they want to search by
    command = getUserInput(CATEGORY_SELECTION)
    #Quit is the command to exit out of the program
    while command != "quit":
        #Validate the user input
        selectionResult = validateCategorySelection(query, command)
        if (not selectionResult):
            #Repeat the search until user quits
            command = getUserInput(CATEGORY_SELECTION)
            continue

        #Ask the user what term to search by
        command = getUserInput(SEARCH_TERM)
        query.setTerm(command)
        #Find the data for the search
        result = searchEngine(search, query)
        if (result != None):
            print(result)
        
        #Repeat the search until user quits
        command = getUserInput(CATEGORY_SELECTION)
    try:
        exit(0)
    except:
        exit(1)
        raise

if __name__ == "__main__":
    main()
