import color

class CustomFormat:
    def __init__(self):
        pass

    def formatTerms(self, keys):
        formatKeys = '\n'.join([*keys])
        return f"""
            Fields to search by:
            {formatKeys}
        """

    def formatData(self, data, category=""):
        if (type(data) is dict):
            for key, value in data.items():
                print("{} {} {} {}".format(color.BOLD, key.ljust(20), color.END, value))
        else:
            for index, item in enumerate(data):
                print(color.UNDERLINE + "{} {}".format(category, index+1) + color.END)
                for key, value in item.items():
                    print("{} {} {} {}".format(color.BOLD, key.ljust(20), color.END, value))
                print("\n")
        return
