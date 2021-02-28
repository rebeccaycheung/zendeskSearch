from engine.color import BOLD, END, UNDERLINE

class CustomFormat:
    def __init__(self):
        pass

    def formatTerms(self, keys):
        formatKeys = '\n'.join(keys)
        return "Fields to search by: \n{}".format(formatKeys)

    def formatData(self, data, category=""):
        if (type(data) is dict):
            for key, value in data.items():
                print("{} {} {} {}".format(BOLD, key.ljust(20), END, value))
        elif (type(data) is str):
            print(data)
        else:
            for index, item in enumerate(data):
                print(UNDERLINE + "{} {}".format(category, index+1) + END)
                for key, value in item.items():
                    print("{} {} {} {}".format(BOLD, key.ljust(20), END, value))
                print("\n")
        return
