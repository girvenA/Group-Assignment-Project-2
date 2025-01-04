
from phplex import lex
from phpparser import parser
from phpinter import Interpreter
import sys

if __name__ == "__main__":
    php_code = open(sys.argv[1]).read()
    
    # Tokenize the PHP code
    lex.input(php_code)
    tokens = list(lex.token() for _ in range(len(php_code)))

    # Parse the tokens
    code = parser.parse(php_code)

    # Interpret the parsed code
    interpreter = Interpreter()
    interpreter.eval(code)
    