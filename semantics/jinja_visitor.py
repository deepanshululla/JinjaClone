from jinjaClone.grammar.JinjaVisitor import JinjaVisitor
from jinjaClone.grammar.JinjaParser import JinjaParser
from jinjaClone.grammar.JinjaLexer import JinjaLexer


from collections import defaultdict

class JinjaAst(JinjaVisitor):


    def __init__(self):
        self.ns = {'name':'deepanshu', 'age':30}

    def visitProgram(self, ctx: JinjaParser.ProgramContext):
        return super().visitProgram(ctx)

    def visitStatement(self, ctx: JinjaParser.StatementContext):
        return super().visitStatement(ctx)

    def visitEvaluation_statement(self, ctx: JinjaParser.Evaluation_statementContext):
        templated_text = ctx.expression().getText()
        if templated_text in self.ns:
            print(self.ns[templated_text])
        else:
            print('undefined')

    def visitBody(self, ctx: JinjaParser.BodyContext):
        normalText = ctx.TEXT().getText()
        print(normalText, end='')

