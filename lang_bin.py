from jinjaClone.semantics.jinja_visitor import JinjaAst, JinjaLexer, JinjaParser
from antlr4 import InputStream, CommonTokenStream
from argparse import ArgumentParser
import os
from jinjaClone.semantics.code_generator import CodeGenerator


import json


def parse_args():
    parser = ArgumentParser(description='Pythonic DSL interpreter')
    parser.add_argument("-d","--directory", type=str, help="Directory to parse")
    return parser.parse_args()

def parse_json(json_file):
    with open(json_file) as f:
        data = json.load(f)
        return data

if __name__ == '__main__':
    args = parse_args()

    if not args.directory:
        directory = 'test_files/basics'
    else:
        directory = args.directory
    template_file = 'f{directory}/'
    html_file_loc = ''
    json_file_loc = ''
    for root, dirnames, filenames in os.walk(directory):
         for filename in filenames:
             if filename.endswith("html"):
                 html_file_loc = os.path.join(root, filename)
             elif filename.endswith("json"):
                 json_file_loc = os.path.join(root, filename)
    json_contents = parse_json(json_file_loc)
    code_gen = CodeGenerator()
    with open(html_file_loc) as f:
        text = f.read()
        inp_stream = InputStream(text)
        lexer = JinjaLexer(inp_stream)
        tokens = CommonTokenStream(lexer)
        parser = JinjaParser(tokens)
        visitor = JinjaAst(code_gen, namespace=json_contents)
        visitor.visit(parser.program())
        # print(code_gen.generate_code())
        code_gen.write_to(f"{directory}/outputfile.html")
