import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hawk.lexer import tokenize
from hawk.parser import parse
from hawk.interpreter import run

with open("examples/test.hawk") as f:
    code = f.read()

tokens = tokenize(code)
parsed = parse(tokens)
run(parsed)
