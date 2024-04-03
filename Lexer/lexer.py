import re

# Palabras reservadas del lenguaje
palabras_reservadas = {
    'fn', 'let', 'mut', 'if', 'else', 'for', 'while', 'return', 'struct',
    'enum', 'match', 'const', 'static', 'impl', 'trait', 'true', 'false',
    'as', 'pub', 'extern', 'crate', 'mod', 'use', 'super', 'self', 'in'
}


patronTokens = {
    'INTEGER': re.compile(r'\b\d+\b'),  #
    'FLOAT': re.compile(r'\b\d+\.\d+([eE][-+]?\d+)?\b'),
    'STRING': re.compile(r'"(?:\\.|[^"\\])*"'),
    'COMMENT': re.compile(r'//.*|/\*[^*]*\*+(?:[^/*][^*]*\*+)*/'),
    'IDENTIFIER': re.compile(r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'),
    'OPERATOR': re.compile(r'[\+\-\*/=><!&|%^~]'),
    'PUNCTUATION': re.compile(r'[{}()\[\];:,\.]')
}


def lexer(texto):
    tokens = []
    posicion = 0
    while texto:
        texto = texto.lstrip()
        if not texto:
            break
        coincidencia = None
        for tipo_token, regex in patronTokens.items():
            coincidencia = regex.match(texto)
            if coincidencia:
                valor = coincidencia.group(0)
                if tipo_token == 'COMMENT':
                    posicion += len(valor)
                    texto = texto[len(valor):]
                    break
                if tipo_token == 'IDENTIFIER' and valor in palabras_reservadas:
                    tipo_token = 'RESERVED'
                tokens.append((tipo_token, valor, posicion, posicion + len(valor) - 1))
                posicion += len(valor)
                texto = texto[len(valor):]
                break
        if not coincidencia:
            posicion += 1
            texto = texto[1:]
    return tokens

# Código de prueba para analizar
codigoPrueba = '''
fn main() {
    println!("Hola Mundo");
    // Esto es un comentario
    let x = 1.23e+10;
}

'''


try:
    tokens = lexer(codigoPrueba)
    for token in tokens:
        print(token)
except SyntaxError as e:
    print(e)
