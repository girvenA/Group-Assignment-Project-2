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
    'RETURN',
]

# List of tokens
tokens = keywords + [
    'EQUALS', 
    'PLUS', 
    'DIVIDE',
    'LPAREN', 
    'RPAREN', 
    'RCURLY', 
    'LCURLY', 
    'LESSEQUAL', 
    'GREATERTHAN',
    'CONCAT', 
    'SEMI', 
    'NOT', 
    'MOD',
    'IDENTIFIER', 
    'NUMBER', 
    'STRING',
]

# Ignore whitespace
t_ignore = ' \t'

# Ignore PHP tags
def t_ignore_PHP_OPEN(t):
    r'\<\?php'
    pass

def t_ignore_PHP_CLOSE(t):
    r'\?\>'
    pass

# Ignore comment
t_ignore_COMMENT =r'//.*'

# Token definitions
def t_KEYWORD(t):
    r'[a-zA-Z_]+'
    if t.value in keywords:
        t.type = t.value
    return t

def t_IDENTIFIER(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'  # Identifiers start with $ followed by letters or numbers
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Convert to integer
    return t

def t_STRING(t):
    r'"([^"\\]*(\\.[^"\\]*)*)"'
    return t

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
t_NOT = r'\!'  # Not operator
t_MOD = r'\%'  # Modulo operator

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lex.lex(debug=0)

# Function to analyze input code
def analyze_code(code):
    lex.input(code)
    while True:
        token = lex.token()  # Get the next token
        if not token:  # If there are no more tokens, break
            break
        print(token)
