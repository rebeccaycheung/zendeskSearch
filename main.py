import json

def getUserInput(prompt):
    user_input = input(prompt)
    return user_input

def getTerms():
    with open('users.json') as users_file:
        data = json.load(users_file)
        users = data[0]
        print(users.keys())
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
            return getTerms()
        else:
            return
        command = getUserInput("Search: ")

if __name__ == "__main__":
    main()
