from token import Token


class Interpreter:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("Input Parsing error")

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                token = Token("INTEGER", self.integer())
                return token
            if self.current_char == "+":
                token = Token("ADD", "+")
                self.advance()
                return token
            if self.current_char == "-":
                token = Token("SUB", "-")
                self.advance()
                return token
            if self.current_char == "*":
                token = Token("MUL", "*")
                self.advance()
                return token
            if self.current_char == "/":
                token = Token("DIV", "/")
                self.advance()
                return token
            if self.current_char == "//":
                token = Token("INDIV", "//")
                self.advance()
                return token

            self.error()

        return Token("EOF", None)

    def eat(self, token_name):
        # print(self.current_token.token_name, token_name)
        if self.current_token.token_name == token_name:
            self.current_token = self.get_next_token()
            # print("after", self.current_token.attribute_value)
        else:
            self.error()

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def integer(self):
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat("INTEGER")

        op = self.current_token
        if op.token_name == "ADD":
            self.eat("ADD")
        elif op.token_name == "MUL":
            self.eat("MUL")
        elif op.token_name == "DIV":
            self.eat("DIV")
        elif op.token_name == "SUB":
            self.eat("SUB")
        elif op.token_name == "INDIV":
            self.eat("INDIV")

        right = self.current_token
        self.eat("INTEGER")
        if op.token_name == "ADD":
            result = left.attribute_value + right.attribute_value
        elif op.token_name == "SUB":
            result = left.attribute_value - right.attribute_value
        elif op.token_name == "MUL":
            result = left.attribute_value * right.attribute_value
        elif op.token_name == "DIV":
            result = left.attribute_value / right.attribute_value
        elif op.token_name == "INDIV":
            result = left.attribute_value // right.attribute_value

        return result
