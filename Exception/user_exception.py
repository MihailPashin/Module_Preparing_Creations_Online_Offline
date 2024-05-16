class Varierty_of_Errors(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
