# A simple lexical analyzer for PHP source code using PLY
#import lex from python lex yacc
from ply import lex

# List of PHP keywords
keywords = [
    'PRINT',
    'ECHO',
    'IF',
    'ELSE',
    'WHILE',
]

reserved = {
    'echo': 'ECHO',
    'print': 'PRINT',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
}

# List of tokens
tokens = keywords + [
    'PHP_OPEN',
    'PHP_CLOSE',
    'EQUALS', 
    'PLUS', 
    'DIVIDE',
    'LPAREN', 
    'RPAREN', 
    'RCURLY', 
    'LCURLY', 
    'LESSEQUAL', 
    'GREATERTHAN',
    'NOTEQUAL',
    'CONCAT', 
    'SEMI',  
    'MOD',
    'IDENTIFIER', 
    'NUMBER', 
    'STRING',
    'VAR'
]

# Ignore whitespace
t_ignore = ' \t'

t_PHP_OPEN = r'<\?php|<\?'
t_PHP_CLOSE = r'\?>'

# Ignore comment
t_ignore_COMMENT =r'//.*'

# Token definitions
def t_IDENTIFER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = t.value.lower()  # Convert to lowercase
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check against reserved keywords
    return t

def t_VAR(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'  # Identifiers start with $ followed by letters or numbers
    t.value = t.value[1:]
    return t

def t_STRING(t):
    r'"([^"\\]*(\\.[^"\\]*)*)"'
    t.value = t.value[1:-1]
    t.value = bytes(t.value, "utf-8").decode("unicode_escape")  
    return t

t_NUMBER = r'\d+'
t_EQUALS = r'\='
t_PLUS = r'\+'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_LESSEQUAL = r'\<='
t_GREATERTHAN = r'\>'
t_CONCAT = r'\.'  # Concatenation operator
t_SEMI = r'\;'
t_NOTEQUAL = r'\!='  # Not operator
t_MOD = r'\%'  # Modulo operator

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lex.lex(debug=0)

# # Function to analyze input code
# def analyze_code(code):
#     lex.input(code)
#     while True:
#         token = lex.token()  # Get the next token
#         if not token:  # If there are no more tokens, break
#             break
#         print(token)
