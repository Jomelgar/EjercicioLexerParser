from lexer import tokenizar
from parser import Parser

def main():
    codigo = '''
    a = b + 3;
    if (a > 5) { c = 1 + a;}
    while (a < 10) { a = a + 1;}
    '''
    print("Tokenizando...")
    tokens = tokenizar(codigo)
    print("Iniciando parser...\n")

    try:
        parser = Parser(tokens)
        parser.parse()
        print("\n✅ Código válido sintácticamente.")
    except SyntaxError as e:
        print(f"\n❌ Error de sintaxis: {e}")

if __name__ == "__main__":
    main()
