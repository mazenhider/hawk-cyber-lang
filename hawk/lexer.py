# hawk/lexer.py

def tokenize(code):
    tokens = []
    words = code.replace('(', ' ( ').replace(')', ' ) ').split()
    for word in words:
        if word == '(' or word == ')':
            tokens.append(('PAREN', word))
        elif word.startswith('"') and word.endswith('"'):
            tokens.append(('STRING', word.strip('"')))
        else:
            tokens.append(('IDENTIFIER', word))
    return tokens
