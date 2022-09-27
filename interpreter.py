from token import Token


class Interpreter:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = ""

    def error(self):
        raise Exception("Input Parsing error")

    def get_next_token(self):

        if self.pos > len(self.text) - 1:
            return Token("EOF", None)
        self.current_char = self.text[self.pos]

        if self.current_char.isdigit():
            token = Token("INTEGER", int(self.current_char))
            self.pos += 1
            return token

        if self.current_char == "+":
            token = Token("ADD", "+")
            self.pos += 1
            return token

        self.error()

    def eat(self, token_name):
        # print(self.current_token.token_name, token_name)
        if self.current_token.token_name == token_name:
            self.current_token = self.get_next_token()
            # print("after", self.current_token.attribute_value)
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat("INTEGER")

        op = self.current_token
        self.eat("ADD")

        right = self.current_token
        self.eat("INTEGER")

        result = left.attribute_value + right.attribute_value

        return result
