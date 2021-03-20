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
        value = self.visit(ctx.expression())
        print(value, end='')
        return value

    def visitBody(self, ctx: JinjaParser.BodyContext):
        normalText = ctx.CONTENTS().getText()
        print(normalText, end='')
        return normalText

    def visitEqVar(self, ctx: JinjaParser.EqVarContext):
        templated_text = ctx.ID().getText()
        if templated_text in self.ns:
            return self.ns[templated_text]


    def visitEqDbl(self, ctx: JinjaParser.EqDblContext):
        return float(ctx.DOUBLE().getText())

    def visitEqInt(self, ctx: JinjaParser.EqIntContext):
        return int(ctx.INT().getText())

    def visitEqStr(self, ctx: JinjaParser.EqStrContext):
        return str(ctx.STRING().getText().strip("'"))

    def visitEqAdd(self, ctx:JinjaParser.EqAddContext):
        operator = ctx.operator
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if operator.type == JinjaLexer.ADD:
            return left + right
        else:
            return left - right

    def visitEqMUL(self, ctx:JinjaParser.EqMULContext):
        operator = ctx.operator
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if operator.type == JinjaLexer.MUL:
            return left * right
        else:
            return float(left) / float(right)

