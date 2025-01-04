from phpparser import parser

variables = {}
class Interpreter:
    def eval(self, node):
        if isinstance(node, tuple):
            if node[0] == 'program':
                for statement in node[1]:
                    self.eval(statement)
            elif node[0] == 'assign':
                var_name = node[1]
                value = self.eval(node[2])
                variables[var_name] = value
            elif node[0] == 'binop':
                left = self.eval(node[2])
                right = self.eval(node[3])
                op = node[1]
                if isinstance(left, str) and left.replace('.', '', 1).isdigit():
                    left = float(left) if '.' in left else int(left)
                if isinstance(right, str) and right.replace('.', '', 1).isdigit():
                    right = float(right) if '.' in right else int(right)
                if op == '+':
                    return left + right
                elif op == '/':
                    result = left / right
                    return int(result) if result.is_integer() else result
                elif op == '%':
                    return left % right
                elif op == '>':
                    return left > right
                elif op == '<=':
                    return left <= right
                elif op == '!=':
                    return left != right
                elif op == '.':
                    return str(left) + str(right)

            elif node[0] == 'number':
                return node[1]
            elif node[0] == 'string':
                return node[1]
            elif node[0] == 'var':
                var_name = node[1]
                if var_name in variables:
                    value = variables[var_name]
                    # Convert to number if possible
                    if isinstance(value, str) and value.replace('.', '', 1).isdigit():
                        return float(value) if '.' in value else int(value)
                    return value
                else:
                    raise ValueError(f"Undefined variable '{var_name}'")
            elif node[0] == 'print':
                value = self.eval(node[1]) 
                print(value, end='')  
                return value 
            elif node[0] == 'echo':
                value = self.eval(node[1])
                print(value, end='') 
                return value
            
            elif node[0] == 'ifelse': 
                condition = self.eval(node[1])
                if condition:
                    # Execute the 'if' block if the condition is true
                    for statement in node[2]:
                        self.eval(statement)
                else:
                    for statement in node[3]:
                        self.eval(statement)
            elif node[0] == 'if': 
                condition = self.eval(node[1])
                if condition:
                    for statement in node[2]:
                        self.eval(statement)
            elif node[0] == 'while':
                while self.eval(node[1]):
                    for statement in node[2]:
                        self.eval(statement)
        else:
            return node
