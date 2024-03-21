import re

reserved = {
    'fn', 'let', 'mut', 'if', 'else', 'for', 'while', 'return', 'struct',
    'enum', 'match', 'const', 'static', 'impl', 'trait', 'true', 'false',
    'as', 'pub', 'extern', 'crate', 'mod', 'use', 'super', 'self', 'in'
}

patronTokens = {
    'INTEGER': r'\b\d+\b',
    'FLOAT': r'\b\d+\.\d+\b',
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z_0-9]*\b',
    'OPERATOR': r'[\+\-\*/=><!&|%^~]',
    'PUNCTUATION': r'[{}()\[\];:,\.]'
}
def lexer(text):
    tokens = []
    position = 0
    while text:
        text = text.lstrip()
        if not text:
            break
        match = None
        for token_type, pattern in patronTokens.items():
            regex = re.compile(pattern)
            match = regex.match(text)
            if match:
                value = match.group(0)
                if token_type == 'IDENTIFIER' and value in reserved:
                    token_type = 'RESERVED'
                tokens.append((token_type, value, position + match.start(), position + match.end() - 1))
                position += match.end()
                text = text[match.end():]
                break
        if not match:
            raise SyntaxError(f"Error léxico: caracter inesperado '{text[0]}' en la posición {position}")
    return tokens

codigoPrueba = '''

using namespace std;
int main(){
printf("Hola");
return 0;
}
}'''
try:
    tokens = lexer(codigoPrueba)
    for token in tokens:
        print(token)
except SyntaxError as e:
    print(e)
