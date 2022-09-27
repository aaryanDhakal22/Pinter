class Token:
    def __init__(self, token_name, attribute_value):
        self.token_name = token_name
        self.attribute_value = attribute_value

    def __str__(self):
        return f"<Token ({self.token_name},{self.attribute_value})>"

    def __repr__(self):
        return self.__str__()
