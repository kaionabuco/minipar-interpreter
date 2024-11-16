import lexico
import sintatico


def rodar(text):
    # Gerar tokens
    lexer = lexico.Lexer(text)
    tokens = lexer.criar_tokens()

    # Gerar árvore sintática
    parser = sintatico.Parser(tokens)
    arvore = parser.parse()

    # Rodar
    # interpreter = sintatico.Interpreter()
    # interpreter.visit(arvore.node)

    return arvore


while True:
    texto = input('MiniPar > ')
    result = rodar(texto)

    print(result)
