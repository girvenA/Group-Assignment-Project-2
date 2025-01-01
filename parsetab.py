
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSleftDIVIDEMODleftCONCATCONCAT DIVIDE ECHO ELSE EQUALS GREATERTHAN IDENTIFIER IF LCURLY LESSEQUAL LPAREN MOD NOT NUMBER PLUS PRINT RCURLY RETURN RPAREN SEMI STRING WHILEprogram : statementsstatements : statements statement\n                  | statementstatement : PRINT STRING SEMIstatement : ECHO STRING SEMIstatement : IDENTIFIER EQUALS expression SEMIstatement : WHILE LPAREN condition RPAREN LCURLY statements RCURLYstatement : IF LPAREN condition RPAREN LCURLY statements RCURLY\n                 | IF LPAREN condition RPAREN LCURLY statements RCURLY ELSE LCURLY statements RCURLYcondition : IDENTIFIER GREATERTHAN IDENTIFIER\n                 | IDENTIFIER LESSEQUAL IDENTIFIER\n                 | IDENTIFIER MOD NUMBER EQUALS NUMBERexpression : expression PLUS expression\n                  | expression DIVIDE expression\n                  | expression MOD expression\n                  | expression CONCAT expressionexpression : NOT expressionexpression : LPAREN expression RPARENexpression : NUMBERexpression : IDENTIFIERstatement : RETURN expression SEMI'
    
_lr_action_items = {'PRINT':([0,2,3,10,21,22,27,34,45,49,50,52,53,55,57,58,59,],[4,4,-3,-2,-4,-5,-21,-6,4,4,4,4,-7,-8,4,4,-9,]),'ECHO':([0,2,3,10,21,22,27,34,45,49,50,52,53,55,57,58,59,],[5,5,-3,-2,-4,-5,-21,-6,5,5,5,5,-7,-8,5,5,-9,]),'IDENTIFIER':([0,2,3,9,10,13,14,15,17,18,21,22,27,28,29,30,31,34,36,37,45,49,50,52,53,55,57,58,59,],[6,6,-3,20,-2,20,25,25,20,20,-4,-5,-21,20,20,20,20,-6,46,47,6,6,6,6,-7,-8,6,6,-9,]),'WHILE':([0,2,3,10,21,22,27,34,45,49,50,52,53,55,57,58,59,],[7,7,-3,-2,-4,-5,-21,-6,7,7,7,7,-7,-8,7,7,-9,]),'IF':([0,2,3,10,21,22,27,34,45,49,50,52,53,55,57,58,59,],[8,8,-3,-2,-4,-5,-21,-6,8,8,8,8,-7,-8,8,8,-9,]),'RETURN':([0,2,3,10,21,22,27,34,45,49,50,52,53,55,57,58,59,],[9,9,-3,-2,-4,-5,-21,-6,9,9,9,9,-7,-8,9,9,-9,]),'$end':([1,2,3,10,21,22,27,34,53,55,59,],[0,-1,-3,-2,-4,-5,-21,-6,-7,-8,-9,]),'RCURLY':([3,10,21,22,27,34,50,52,53,55,58,59,],[-3,-2,-4,-5,-21,-6,53,55,-7,-8,59,-9,]),'STRING':([4,5,],[11,12,]),'EQUALS':([6,48,],[13,51,]),'LPAREN':([7,8,9,13,17,18,28,29,30,31,],[14,15,18,18,18,18,18,18,18,18,]),'NOT':([9,13,17,18,28,29,30,31,],[17,17,17,17,17,17,17,17,]),'NUMBER':([9,13,17,18,28,29,30,31,38,51,],[19,19,19,19,19,19,19,19,48,54,]),'SEMI':([11,12,16,19,20,23,32,40,41,42,43,44,],[21,22,27,-19,-20,34,-17,-13,-14,-15,-16,-18,]),'PLUS':([16,19,20,23,32,33,40,41,42,43,44,],[28,-19,-20,28,28,28,-13,-14,-15,-16,-18,]),'DIVIDE':([16,19,20,23,32,33,40,41,42,43,44,],[29,-19,-20,29,29,29,29,-14,-15,-16,-18,]),'MOD':([16,19,20,23,25,32,33,40,41,42,43,44,],[30,-19,-20,30,38,30,30,30,-14,-15,-16,-18,]),'CONCAT':([16,19,20,23,32,33,40,41,42,43,44,],[31,-19,-20,31,31,31,31,31,31,-16,-18,]),'RPAREN':([19,20,24,26,32,33,40,41,42,43,44,46,47,54,],[-19,-20,35,39,-17,44,-13,-14,-15,-16,-18,-10,-11,-12,]),'GREATERTHAN':([25,],[36,]),'LESSEQUAL':([25,],[37,]),'LCURLY':([35,39,56,],[45,49,57,]),'ELSE':([55,],[56,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statements':([0,45,49,57,],[2,50,52,58,]),'statement':([0,2,45,49,50,52,57,58,],[3,10,3,3,10,10,3,10,]),'expression':([9,13,17,18,28,29,30,31,],[16,23,32,33,40,41,42,43,]),'condition':([14,15,],[24,26,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statements','program',1,'p_program','phpparser.py',15),
  ('statements -> statements statement','statements',2,'p_statements','phpparser.py',19),
  ('statements -> statement','statements',1,'p_statements','phpparser.py',20),
  ('statement -> PRINT STRING SEMI','statement',3,'p_statement_print','phpparser.py',27),
  ('statement -> ECHO STRING SEMI','statement',3,'p_statement_echo','phpparser.py',31),
  ('statement -> IDENTIFIER EQUALS expression SEMI','statement',4,'p_statement_assign','phpparser.py',35),
  ('statement -> WHILE LPAREN condition RPAREN LCURLY statements RCURLY','statement',7,'p_statement_while','phpparser.py',39),
  ('statement -> IF LPAREN condition RPAREN LCURLY statements RCURLY','statement',7,'p_statement_if','phpparser.py',44),
  ('statement -> IF LPAREN condition RPAREN LCURLY statements RCURLY ELSE LCURLY statements RCURLY','statement',11,'p_statement_if','phpparser.py',45),
  ('condition -> IDENTIFIER GREATERTHAN IDENTIFIER','condition',3,'p_condition','phpparser.py',52),
  ('condition -> IDENTIFIER LESSEQUAL IDENTIFIER','condition',3,'p_condition','phpparser.py',53),
  ('condition -> IDENTIFIER MOD NUMBER EQUALS NUMBER','condition',5,'p_condition','phpparser.py',54),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','phpparser.py',58),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','phpparser.py',59),
  ('expression -> expression MOD expression','expression',3,'p_expression_binop','phpparser.py',60),
  ('expression -> expression CONCAT expression','expression',3,'p_expression_binop','phpparser.py',61),
  ('expression -> NOT expression','expression',2,'p_expression_not','phpparser.py',72),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','phpparser.py',76),
  ('expression -> NUMBER','expression',1,'p_expression_number','phpparser.py',80),
  ('expression -> IDENTIFIER','expression',1,'p_expression_identifier','phpparser.py',84),
  ('statement -> RETURN expression SEMI','statement',3,'p_statement_return','phpparser.py',88),
]