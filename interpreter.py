from token import Token

operations = [
    "ADD",
    "SUB",
    "MUL",
    "DIV",
    "INDIV",
]


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

    def term(self):
        token = self.current_token
        self.eat("INTEGER")
        return token.attribute_value

    def expr(self):
        self.current_token = self.get_next_token()

        result = self.term()

        while self.current_token.token_name in operations:
            op = self.current_token
            if op.token_name == "ADD":
                self.eat("ADD")
                result += self.term()

            elif op.token_name == "MUL":
                self.eat("MUL")
                result *= self.term()

            elif op.token_name == "DIV":
                self.eat("DIV")
                result /= self.term()

            elif op.token_name == "SUB":
                self.eat("SUB")
                result -= self.term()

            elif op.token_name == "INDIV":
                self.eat("INDIV")
                result = result // self.term()

        return result
