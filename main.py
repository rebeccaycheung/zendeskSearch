import json
from search import Search
from query import Query

def readFile(file):
    with open(file) as jsonFile:
        data = json.load(jsonFile)
        return data

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

    users = readFile('users.json')
    organisations = readFile('organizations.json')
    tickets = readFile('tickets.json')

    search = Search(users, organisations, tickets)
    query = Query()
    
    command = getUserInput("Select which to search by 1) users, 2) organisations, 3) tickets: ")
    while command != "quit":
        #handle errors
        selectSearchType(query, int(command))
        command = getUserInput("Search by term: ")
        if (command == "terms"):
            result = search.getTerms(query)
            print(result)
        else:
            termQuery = command
            if (query.validateTerm(search, termQuery)):
                command = getUserInput("Enter a value: ")
                if (command == "quit"):
                    return
                valueQuery = command
                query.setTerm(termQuery)
                query.setValue(valueQuery)
                result = search.findData(query)
                print(result)
            else:
                print("The term you have entered does not exist, please enter another term.")
        command = getUserInput("Select which to search by 1) users, 2) organisations, 3) tickets: ")

if __name__ == "__main__":
    main()
