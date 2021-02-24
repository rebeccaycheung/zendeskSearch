import json

def getUserInput(prompt):
    user_input = input(prompt)
    return user_input

def readFile(file):
    with open(file) as json_file:
        data = json.load(json_file)
        return data[0]

def getAllTerms():
    users = readFile('users.json')
    organisations = readFile('organizations.json')
    tickets = readFile('tickets.json')
    
    format_users = '\n'.join([*users])
    format_organisations = '\n'.join([*organisations])
    format_tickets = '\n'.join([*tickets])

    print(f"""
Users
Fields to search by:
{format_users}


Organisations
Fields to search by:
{format_organisations}


Tickets
Fields to search by:
{format_tickets}
    """)

    return

def main():
    print("""
        Welcome to Zendesk Search!

        Type 'quit' to exit the program at any time.
        Type 'terms' to view a list of terms you can search by.

        Start by searching the term and value.
    """)
    
    command = getUserInput("Search: ")
    while command != "quit":
        if (command == "terms"):
            return getAllTerms()
        else:
            return
        command = getUserInput("Search: ")

if __name__ == "__main__":
    main()
