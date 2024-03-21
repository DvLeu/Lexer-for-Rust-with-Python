import ply.lex as lex

# Palabras reservadas de Rust
reserved = {
    'fn', 'let', 'mut', 'if', 'else', 'for', 'while', 'return', 'struct',
    'enum', 'match', 'const', 'static', 'impl', 'trait', 'true', 'false',
    'as', 'pub', 'extern', 'crate', 'mod', 'use', 'super', 'self', 'in'
}

tokens = [
    'INT',
    'FLOAT',
    'IDENTIFIER',
    'OPERATOR',
    'PUNCTUATION',
] + ['RESERVED_' + r.upper() for r in 

t_OPERATOR = r'[\+\-\*/=><!&|%^~]'
t_PUNCTUATION = r'[{}()\[\];:,\.]'


def t_INT(t):
    r'\b\d+\b'
    t.value = int(t.value)
    return t


def t_FLOAT(t):
    r'\b\d+\.\d+\b'
    t.value = float(t.value)
    return t


def t_IDENTIFIER(t):
    r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'
    if t.value in reserved:
        t.type = 'RESERVED_' + t.value.upper()  # Cambiar tipo si la palabra es reservada
    return t
    
t_ignore = ' \t'

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def lexer_action(data):
    lexer = lex.lex()
    lexer.input(data)
    token_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        token_list.append((tok.type, tok.value, tok.lineno))
    return token_list

data =\
    '''fn main() {
    let x: i32 = 10 + 20;
}
'''
print(lexer_action(data))
