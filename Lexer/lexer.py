import re  # Importa el módulo de expresiones regulares

# Palabras reservadas del lenguaje
palabras_reservadas = {
    'fn', 'let', 'mut', 'if', 'else', 'for', 'while', 'return', 'struct',
    'enum', 'match', 'const', 'static', 'impl', 'trait', 'true', 'false',
    'as', 'pub', 'extern', 'crate', 'mod', 'use', 'super', 'self', 'in'
}

# Patrones de tokens con sus expresiones regulares correspondientes
patronTokens = {
    'INTEGER': r'\b\d+\b',  # Números enteros
    'FLOAT': r'\b\d+\.\d+\b',  # Números flotantes
    'IDENTIFIER': r'\b[a-zA-Z_][a-zA-Z_0-9]*\b',  # Identificadores (nombres de variables, funciones, etc.)
    'OPERATOR': r'[\+\-\*/=><!&|%^~]',  # Operadores (+, -, *, /, =, etc.)
    'PUNCTUATION': r'[{}()\[\];:,\.]'  # Símbolos de puntuación (, ; { } [ ] ( ) etc.)
}

# Función lexer para analizar el texto de entrada
def lexer(texto):
    tokens = []  # Lista para almacenar los tokens encontrados
    posicion = 0  # Posición actual en el texto
    while texto:
        texto = texto.lstrip()  # Elimina los espacios en blanco al inicio del texto restante
        if not texto:
            break  # Termina el bucle si no hay más texto después de eliminar espacios en blanco
        coincidencia = None
        for tipo_token, patron in patronTokens.items():
            regex = re.compile(patron)
            coincidencia = regex.match(texto)
            if coincidencia:
                valor = coincidencia.group(0)
                if tipo_token == 'IDENTIFIER' and valor in palabras_reservadas:
                    tipo_token = 'RESERVED'  # Cambia el tipo a 'RESERVED' si el identificador es una palabra reservada
                # Añade el token a la lista con su tipo, valor y posición inicial y final
                tokens.append((tipo_token, valor, posicion + coincidencia.start(), posicion + coincidencia.end() - 1))
                posicion += coincidencia.end()  # Actualiza la posición para el próximo análisis
                texto = texto[coincidencia.end():]  # Actualiza el texto restante
                break
        if not coincidencia:
            # Si no hay coincidencia, significa que hay un caracter inesperado
            raise SyntaxError(f"Error léxico: caracter inesperado '{texto[0]}' en la posición {posicion}")
    return tokens

# Código de prueba para analizar
codigoPrueba = '''
using namespace std;
int main(){
printf("Hola");
return 0;
}
}'''

# Intenta analizar el código de prueba y captura errores léxicos
try:
    tokens = lexer(codigoPrueba)
    for token in tokens:
        print(token)
except SyntaxError as e:
    print(e)
