# Generated from ./grammar/Jinja.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JinjaParser import JinjaParser
else:
    from JinjaParser import JinjaParser

# This class defines a complete generic visitor for a parse tree produced by JinjaParser.

class JinjaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by JinjaParser#program.
    def visitProgram(self, ctx:JinjaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#statement.
    def visitStatement(self, ctx:JinjaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#expression.
    def visitExpression(self, ctx:JinjaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#evaluation_statement.
    def visitEvaluation_statement(self, ctx:JinjaParser.Evaluation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#body.
    def visitBody(self, ctx:JinjaParser.BodyContext):
        return self.visitChildren(ctx)



del JinjaParser