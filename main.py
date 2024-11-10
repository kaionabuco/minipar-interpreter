import lexico


def rodar(text):
    lexer = lexico.Lexer(text)
    tokens = lexer.criar_tokens()

    return tokens


while True:
    texto = input('MiniPar > ')
    result = rodar(texto)

    print(result)
