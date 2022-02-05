# The class section for the program
# It HAS  the classes we need to build the program
#  bank AND client which all have their own attributes AND METHODS


class Bank:
    def __init__(self, savings, current):
        self.savings = savings
        self.current = current


class Client:
    def __init__(self, id_number, name):
        self.id = id_number
        self.name = name
