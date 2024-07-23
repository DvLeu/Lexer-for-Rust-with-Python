import ply.lex as lex

reserved = [ 'break', 'const', 'continue', 'crate', 'else',
    'enum', 'extern', 'false', 'fn', 'for', 'if', 'impl',
    'in', 'let', 'loop', 'match', 'mod', 'move', 'mut',
    'pub', 'ref', 'return', 'self', 'Self',
    'struct', 'super', 'trait', 'true',  'while'
]

#Tokenizar cada una de los simbolos del alfabeto de Rust
tokens = (
    'INT', 'PARENTESIS_IZQ', 'PARENTESIS_DER', 'FLOAT', 'STRING',
    'IDENTIFIER', 'CORCHETE_DER', 'CORCHETE_IZQ', 'LLAVE_IZQ',
    'LLAVE_DER', 'OPERATOR', 'COMA', 'PUNTOYCOMA', 'EXCLAMACION','RESERVED'
)

t_ignore = ' \t'
t_CORCHETE_DER = r'\]'
t_CORCHETE_IZQ = r'\['
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_COMA = r'\,'
t_PUNTOYCOMA = r';'
t_EXCLAMACION = r'!'


def t_COMMENT_MULTILINEA(t):#Ignorar comentarios multilinea.
    r'/\*(.|\n)*?\*/'
    pass

def t_COMMENT(t):#Ignorar comentario de una sola linea
    r'//.*'
    pass

def t_OPERATOR(t):#Expresion regular que delimita cuales son operadores.
    r'[+\-*/=><~%^\$:]'
    t.type = 'OPERATOR'
    return t
def t_IDENTIFIER(t):#Expresion regular la cual determina si son palabras reservadas o identificadores
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.lower() in reserved:
        t.type = 'RESERVED'
    else:
        t.type = 'IDENTIFIER'
    return t
def t_STRING(t):#Expresion regular de Strings solo se tomara en cuenta los "EL CONTENIDO AQUI ES IRRELEVANTE XD "
    r'\"(\\.|[^\"])*\"'
    t.value = t.value.strip('"')
    return t
def t_FLOAT(t):#Expresion para digitos con decimal
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_INT(t):#Expresion para digitos int no pueden tener decimales
    r'\d+(?![\.\d])'
    t.value = int(t.value)
    return t
def t_linea(t):#contador de líneas del lexer cada vez que encuentra un salto de línea (\n).
    r'\n+'
    t.lexer.lineno += len(t.value)
def t_error(t):
    print("Caracter invalido '%s'" % t.value[0] + ", in line: " + str(t.lexer.lineno))
    t.lexer.skip(1)
    raise Exception(
        "Error lexico.\n  Caracter invalido '%s'" %
        t.value[0] + ", en la linea: " + str(t.lexer.lineno))

def lexer_action(data):
    token_list = []
    lexer = lex.lex()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        token_list.append((tok.type, tok.value, tok.lineno))
    return token_list


if __name__ == "__main__":
    def imprimir_tokens(tokens):
        print("{:<15} {:<20}".format("Tipo", "Valor"))
        print("-" * 55)
        for token in tokens:
            tipo_token, valor, posicion = token
            print("{:<15} {:<20} ".format(tipo_token, valor, posicion))

    def analizar_archivo_rust(ruta_archivo):
        try:
            with open(ruta_archivo, "r") as archivo:
                codigo = archivo.read()
                tokens = lexer_action(codigo)
                imprimir_tokens(tokens)
        except FileNotFoundError:
            print(f"El archivo '{ruta_archivo}' no fue encontrado.")
            exit(1)
        except Exception as e:
            print(e)
            exit(1)

    ruta_archivo = "codigosPrueba/codigoerror2.rs"
    analizar_archivo_rust(ruta_archivo)


