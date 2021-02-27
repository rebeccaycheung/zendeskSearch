import constants
from search import Search
from query import Query

def getUserInput(prompt):
    userInput = input(prompt)
    return userInput

def selectSearchType(query, command):
    if (command == 1):
        query.setCategory('users')
    elif (command == 2):
        query.setCategory('organisations')
    elif (command == 3):
        query.setCategory('tickets')
    else:
        return "Please enter a number between 1 and 3"
    return

def main():
    print("""
        Welcome to Zendesk Search!

        Type 'quit' to exit the program at any time.
        Type 'terms' to view a list of terms you can search by for each category.

        Start by searching the term and value.
    """)

    search = Search()
    query = Query(None, None, None)
    
    command = getUserInput(constants.CATEGORY_SELECTION)
    while command != "quit":
        try:
            selectSearchType(query, int(command))
        except(ValueError):
            print(constants.CATEGORY_SELECTION_TRY_AGAIN)
            command = getUserInput(constants.CATEGORY_SELECTION)
            continue

        command = getUserInput(constants.SEARCH_TERM)
        if (command == "terms"):
            query.setTerm(command)
            result = search.findData(query)
            if (result != None):
                print(result)
        else:
            termQuery = command
            command = getUserInput(constants.SEARCH_VALUE)
            valueQuery = command
            query.setTerm(termQuery)
            query.setValue(valueQuery)
            result = search.findData(query)
            if (result != None):
                print(result)
        command = getUserInput(constants.CATEGORY_SELECTION)
    try:
        exit(0)
    except:
        exit(1)
        raise

if __name__ == "__main__":
    main()
