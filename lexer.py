import re

TOKEN_REGEX = [
    ('IF', r'\bif\b'),            
    ('WHILE', r'\bwhile\b'),
    ('a_paren', r'\('),           
    ('c_paren', r'\)'),
    ('a_llave', r'\{'),
    ('c_llave', r'\}'),           
    ('EQUAL', r'='),              
    ('OPERADOR', r'\+|\-|\*|\/'),
    ('NUMERO', r'\b\d+\b'),
    ('ID', r'\b[A-Za-z]+\b'),         
    (';', r';'),
    ('ESPACIO', r'\s+'),
    ('OPERADOR_LOGICO',r'<|>|==|!='),
    ('DESCONOCIDO', r'.'),
]

def tokenizar(codigo):
    tokens = []
    index = 0
    while index < len(codigo):
        for token_name, token_regex in TOKEN_REGEX:
            regex = re.compile(token_regex)
            match = regex.match(codigo, index)
            if match:
                lexema = match.group(0)
                if token_name != 'ESPACIO':
                    tokens.append((token_name, lexema))
                index = match.end()
                break
        else:
            raise RuntimeError(f"Error de tokenización en: '{codigo[index:]}'")
    return tokens
