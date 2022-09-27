from token import Token
from interpreter import Interpreter


def main():

    while True:
        try:
            text = input(" > ")
        except EOFError:
            break
        if text == "exit":
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == "__main__":
    main()
