import ply.yacc as yacc
import phplex

tokens = phplex.tokens

precedence = (
    ('left', 'PLUS'),
    ('left', 'DIVIDE'),
)

# Grammar rules
def p_program(p):
    '''program : PHP_OPEN statements PHP_CLOSE'''
    p[0] = ('program', p[2])

def p_statements(p):
    '''statements : statement statements
                   | statement'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        # If it's the last statement, it shouldn't require a semicolon
        p[0] = [p[1]]

def p_statement_print(p):
    '''statement : PRINT expression SEMI
                 | PRINT expression'''
    p[0] = ('print', p[2])

def p_statement_echo(p):
    '''statement : ECHO expression SEMI
                 | ECHO expression'''
    p[0] = ('echo', p[2])

def p_statement_assign(p):
    '''statement : VAR EQUALS expression SEMI'''
    var_name = p[1]  # Variable name without the '$'
    value = p[3]  # The value being assigned
    p[0] = ('assign', var_name, value)

def p_statement_if_else(p):
    '''statement : IF LPAREN expression RPAREN LCURLY statements RCURLY ELSE LCURLY statements RCURLY'''
    p[0] = ('ifelse', p[3], p[6], p[10])

def p_statement_while(p):
    '''statement : WHILE LPAREN expression RPAREN LCURLY statements RCURLY'''
    p[0] = ('while', p[3], p[6])

def p_statement_if(p):
    '''statement : IF LPAREN expression RPAREN LCURLY statements RCURLY'''
    p[0] = ('if', p[3], p[6])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression DIVIDE expression
                  | expression MOD expression
                  | expression LESSEQUAL expression
                  | expression GREATERTHAN expression
                  | expression NOTEQUAL expression
                  | expression CONCAT expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

def p_expression_id(p):
    '''expression : VAR'''
    var_name = p[1][1:] if p[1].startswith('$') else p[1]  # Remove '$' from VAR tokens
    p[0] = ('var', var_name)

def p_expression_string(p):
    '''expression : STRING'''
    p[0] = ('string', p[1])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

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

parser = yacc.yacc()

