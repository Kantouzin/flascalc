import tatsu


class ArithSemantics:
    def addition(self, ast):
        return ast.left + ast.right

    def subtraction(self, ast):
        return ast.left - ast.right

    def multiplication(self, ast):
        return ast.left * ast.right

    def division(self, ast):
        return ast.left / ast.right

    def unary_positive(self, ast):
        return + ast.exp

    def unary_negative(self, ast):
        return - ast.exp

    def power(self, ast):
        return ast.left ** ast.right

    def number(self, ast):
        return int(ast)


class ArithParser:
    def __init__(self):
        self._parser = self._init_parser()
        self._semantics = ArithSemantics()

    def _init_parser(self):
        with open("flascalc/grammars/arith.ebnf",
                  mode="r", encoding="utf-8") as file:
            grammar = file.read()

        return tatsu.compile(grammar)

    def parse(self, exp):
        ast = self._parser.parse(exp, semantics=self._semantics)

        if isinstance(ast, float):
            if ast.is_integer():
                ast = int(ast)

        return ast
