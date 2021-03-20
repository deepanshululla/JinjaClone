from jinjaClone.semantics.jinja_visitor import JinjaAst, JinjaLexer, JinjaParser
from antlr4 import InputStream, CommonTokenStream
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description='Pythonic DSL interpreter')
    parser.add_argument("-f","--filename", type=str, help="Filename to parse")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    if not args.filename:
        filename = 'test_files/basics/input_lang.html'
    else:
        filename = args.filename
    with open(filename) as f:
        text = f.read()
        inp_stream = InputStream(text)
        lexer = JinjaLexer(inp_stream)
        tokens = CommonTokenStream(lexer)
        parser = JinjaParser(tokens)
        visitor = JinjaAst()
        visitor.visit(parser.program())
