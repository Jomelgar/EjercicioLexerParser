from lexer import tokenizar

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def current_token(self):
        return self.tokens[self.index] if self.index < len(self.tokens) else ('EOF', '')

    def match(self, expected_type):
        tipo, valor = self.current_token()
        if tipo == expected_type:
            self.index += 1
            return valor
        else:
            raise SyntaxError(f"Se esperaba '{expected_type}', pero se encontró '{tipo}' ({valor})")

    def parse(self):
        while self.index < len(self.tokens):
            self.statement()

    def statement(self):
        tipo, _ = self.current_token()

        if tipo == 'ID':
            self.assignment()
        elif tipo == 'IF':
            self.if_statement()
        elif tipo == 'WHILE':
            self.while_statement()
        else:
            raise SyntaxError(f"Instrucción no válida en: {self.current_token()}")

    def logic_statement(self):
        if self.current_token()[0] == 'ID':
            self.match('ID')
        else:
            self.match('NUMERO')
            
        self.match('OPERADOR_LOGICO')
        
        if self.current_token()[0] == 'ID':
            self.match('ID')
        else:
            self.match('NUMERO')

    def assignment(self):
        self.match('ID')
        self.match('EQUAL')
        self.expression()
        self.match(';')
        print("Asignación válida")

    def if_statement(self):
        self.match('IF')
        self.match('a_paren')
        self.logic_statement()
        self.match('c_paren')
        self.match('a_llave')
        while self.current_token()[0] != 'c_llave':
            self.statement()
        self.match('c_llave')
        print("Condicional IF válida")

    def while_statement(self):
        self.match('WHILE')
        self.match('a_paren')
        self.logic_statement()
        self.match('c_paren')
        self.match('a_llave')
        while self.current_token()[0] != 'c_llave':
            self.statement()
        self.match('c_llave')
        print("Bucle WHILE válido")

    def expression(self):
        self.term()
        while self.current_token()[0] == 'OPERADOR':
            self.match('OPERADOR') #Lo fuerza para que pase de al otro index
            self.term()

    def term(self):
        tipo, _ = self.current_token()
        if tipo in ('ID', 'NUMERO'):
            self.match(tipo)
        else:
            raise SyntaxError(f"Se esperaba ID o NUMERO, pero se encontró '{tipo}'")
