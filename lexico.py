from enum import Enum, auto


class TokenType(Enum):
    INTEGER = auto()
    STRING = auto()
    BOOLEAN = auto()
    KEYWORD = auto()
    OPERADOR = auto()
    SEPARADOR = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    ATRIBUICAO = auto()


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"


# Classe Lexer percorre string
# TODO: get_boolean para 'true' e 'false'
# TODO: separar cada operador em um tipo diferente
# TODO: adicionar operadores de comparação lógica tipo "maior que" e "igual a" (requer tratamento)
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    # proximo_caractere avança cada caractere
    def proximo_caractere(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    # pular_espaco ignora espaço em branco " "
    def pular_espaco(self):
        while self.current_char is not None and self.current_char.isspace():
            self.proximo_caractere()

    # get_integer guarda número inteiro de n algarismos
    def get_integer(self):
        num_str = ''
        while self.current_char is not None and self.current_char.isdigit():
            num_str += self.current_char
            self.proximo_caractere()
        return Token(TokenType.INTEGER, int(num_str))

    # get_palavrareservada guarda as palavras "if, else, while"
    def get_palavrareservada(self):
        id_str = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            id_str += self.current_char
            self.proximo_caractere()
        # Checar qual palavra reservada
        if id_str == 'if':
            return Token(TokenType.IF, id_str)
        elif id_str == 'else':
            return Token(TokenType.ELSE, id_str)
        elif id_str == 'while':
            return Token(TokenType.WHILE, id_str)

    def tokenize(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char.isspace():
                self.pular_espaco()
            elif self.current_char.isdigit():
                tokens.append(self.get_integer())
            elif self.current_char.isalpha():
                tokens.append(self.get_palavrareservada())
            elif self.current_char in '+-*/=':
                tokens.append(Token(TokenType.OPERADOR, self.current_char))
                self.proximo_caractere()
            elif self.current_char in '();':
                tokens.append(Token(TokenType.SEPARADOR, self.current_char))
                self.proximo_caractere()
            else:
                raise Exception(f"Caractere inválido: {self.current_char}")

        return tokens
