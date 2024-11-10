# Tokens
T_INT = 'INT'
T_BOOL = 'BOOL'
T_PLUS = 'PLUS'
T_MINUS = 'MINUS'
T_MULT = 'MULT'
T_DIV = 'DIV'
T_LPAREN = 'LPAREN'
T_RPAREN = 'RPAREN'


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value is not None:
            return f'{self.type}:{self.value}'  # Imprime o tipo e o valor se há valor
        else:
            return f'{self.type}'  # Imprime apenas o tipo


# Classe Lexer percorre string
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1  # Posição do caractere no string, iniciamos em -1 pra avançar pra 0 no próximo método
        self.current_char = None
        self.proximo_caractere()

    # proximo_caractere avança cada caractere
    def proximo_caractere(self):
        self.pos += 1  # Inicia na posição 0
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def criar_tokens(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char in ' \t':  # Pega espaços e tabs
                self.proximo_caractere()
            elif self.current_char.isdigit():
                tokens.append(self.get_integer())
            elif self.current_char.isalpha():
                tokens.append(self.get_string())
            elif self.current_char == '+':
                tokens.append(Token(T_PLUS))
                self.proximo_caractere()
            elif self.current_char == '-':
                tokens.append(Token(T_MINUS))
                self.proximo_caractere()
            elif self.current_char == '*':
                tokens.append(Token(T_MULT))
                self.proximo_caractere()
            elif self.current_char == '/':
                tokens.append(Token(T_DIV))
                self.proximo_caractere()
            elif self.current_char == '(':
                tokens.append(Token(T_LPAREN))
                self.proximo_caractere()
            elif self.current_char == ')':
                tokens.append(Token(T_RPAREN))
                self.proximo_caractere()
            # elif self.current_char in ['True', 'False']:

            #    tokens.append(Token(T_BOOL), bool(bool_str))
            else:
                raise Exception(f"Caractere inválido: {self.current_char}")

        return tokens

    def get_integer(self):  # Guarda número inteiro de n algarismos
        num_str = ''
        while self.current_char is not None and self.current_char.isdigit():
            num_str += self.current_char
            self.proximo_caractere()
        return Token(T_INT, int(num_str))

    def get_string(self):  # Guarda booleano, string, ou bloqueia por palavra reservada
        parsed_str = ''
        while self.current_char is not None and self.current_char.isalpha():
            parsed_str += self.current_char
            self.proximo_caractere()
        if parsed_str == 'True' or 'False':
            return Token(T_BOOL, bool(parsed_str))
        # elif palavra reservada
        # elif string comum?
