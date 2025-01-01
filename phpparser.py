import ply.yacc as yacc
import phplex

tokens = phplex.tokens

# Precedence rules for the parser
precedence = (
    ('left', 'PLUS'),
    ('left', 'DIVIDE', 'MOD'),
    ('left', 'CONCAT')
)

# Grammar rules for the parser
def p_program(p):
    '''program : statements'''
    p[0] = p[1]

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_print(p):
    'statement : PRINT STRING SEMI'
    print(p[2].strip('"'))

def p_statement_echo(p):
    'statement : ECHO STRING SEMI'
    print(p[2].strip('"'))

def p_statement_assign(p):
    'statement : IDENTIFIER EQUALS expression SEMI'
    p[0] = (p[1], p[3])  # Store variable assignment

def p_statement_while(p):
    'statement : WHILE LPAREN condition RPAREN LCURLY statements RCURLY'
    while eval_condition(p[3]):
        p[0] = p[6]  # Execute the block

def p_statement_if(p):
    '''statement : IF LPAREN condition RPAREN LCURLY statements RCURLY
                 | IF LPAREN condition RPAREN LCURLY statements RCURLY ELSE LCURLY statements RCURLY'''
    if eval_condition(p[3]):
        p[0] = p[6]  # Execute the if block
    elif len(p) == 12:  # If there's an else block
        p[0] = p[10]  # Execute the else block

def p_condition(p):
    '''condition : IDENTIFIER GREATERTHAN IDENTIFIER
                 | IDENTIFIER LESSEQUAL IDENTIFIER
                 | IDENTIFIER MOD NUMBER EQUALS NUMBER'''
    p[0] = (p[1], p[2], p[3])  # Store the condition

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression CONCAT expression'''
    if p[2] == '+':
        # p[0] = p[1] + p[3]
        p[0] = str(p[1]) + str(p[3])
    elif p[2] == '/':
        p[0] = str(p[1]) / str(p[3])
    elif p[2] == '%':
        p[0] = str(p[1]) % str(p[3])
    elif p[2] == '.':
        p[0] = str(p[1]) + str(p[3])  # Concatenate two strings

def p_expression_not(p):
    'expression : NOT expression'
    p[0] = not p[2]  # Logical NOT

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = p[1]  # Return the identifier

def p_statement_return(p):
    'statement : RETURN expression SEMI'
    return_value = p[2]
    print(f"Return value: {return_value}")

def p_error(p):
    print("Syntax error at '%s'" % p)

# Function to evaluate conditions
def eval_condition(condition):
    if isinstance(condition, tuple):
        left = condition[0]
        operator = condition[1]
        right = condition[2]
        if operator == '>':
            return left > right
        elif operator == '<=':
            return left <= right
    return False

# Build the parser
parser = yacc.yacc()

def parse(data, debug=0):
    parser.error = 0
    p = parser.parse(data, debug=debug)
    if parser.error:
        return None
    return p