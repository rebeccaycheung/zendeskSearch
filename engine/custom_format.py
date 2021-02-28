from engine.color import BOLD, END, UNDERLINE

# This class holds functions to format the data so that it is readable in the output
class CustomFormat:
    def __init__(self):
        pass

    def formatTerms(self, keys):
        formatKeys = '\n'.join(keys)
        # Join the items in the list with a new line so it outputs nicely for the user
        return "Fields to search by: \n{}".format(formatKeys)

    def formatData(self, data, category=""):
        if (type(data) is dict):
            for key, value in data.items():
                # Print the key and values of the dictionary with padding between the 2 items when outputted
                print("{} {} {} {}".format(BOLD, key.ljust(20), END, value))
        elif (type(data) is str):
            # If the data is a string then just print it out
            print(data)
        else:
            # If the data is a list
            for index, item in enumerate(data):
                # Print out each item in the list, e.g. ticket 1
                print(UNDERLINE + "{} {}".format(category, index+1) + END)
                for key, value in item.items():
                    # Print the key and values of the dictionary with padding between the 2 items when outputted
                    print("{} {} {} {}".format(BOLD, key.ljust(20), END, value))
                print("\n")
        return
