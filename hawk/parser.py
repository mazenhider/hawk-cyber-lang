# hawk/parser.py

def parse(tokens):
    if len(tokens) >= 4 and tokens[0][1] == "scan_ports" and tokens[1][1] == "(" and tokens[3][1] == ")":
        ip = tokens[2][1]
        return {"command": "scan_ports", "args": [ip]}
    
    elif len(tokens) >= 4 and tokens[0][1] == "log" and tokens[1][1] == "(" and tokens[3][1] == ")":
        msg = tokens[2][1]
        return {"command": "log", "args": [msg]}
    
    else:
        raise SyntaxError("Invalid syntax")


