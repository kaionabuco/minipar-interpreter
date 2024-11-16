import lexico


class NumberNode:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f'{self.tok}'


class OperationNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'


class Parser:
    def __init__(self, tokens):
        self.current_tok = None
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

    def parse(self):
        res = self.expr()
        return res

    def factor(self):
        tok = self.current_tok

        if tok.type is lexico.T_INT:
            self.advance()
            return NumberNode(tok)

    def term(self):
        return self.operation(self.factor, (lexico.T_MULT, lexico.T_DIV))

    def expr(self):
        return self.operation(self.term, (lexico.T_PLUS, lexico.T_MINUS))

    def operation(self, func, ops):
        left = func()

        while self.current_tok.type in ops:
            op_tok = self.current_tok
            self.advance()
            right = func()
            left = OperationNode(left, op_tok, right)
        return left


'''
class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f'Método de visita indefinido')

    def visit_integer(node):
        print("Número inteiro")

    def visit_operator(self, node):
        print("Operador")
'''
