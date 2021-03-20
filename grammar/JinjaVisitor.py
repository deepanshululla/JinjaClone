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


    # Visit a parse tree produced by JinjaParser#eqInt.
    def visitEqInt(self, ctx:JinjaParser.EqIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#eqDbl.
    def visitEqDbl(self, ctx:JinjaParser.EqDblContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#eqStr.
    def visitEqStr(self, ctx:JinjaParser.EqStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#eqAdd.
    def visitEqAdd(self, ctx:JinjaParser.EqAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#eqVar.
    def visitEqVar(self, ctx:JinjaParser.EqVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#eqMUL.
    def visitEqMUL(self, ctx:JinjaParser.EqMULContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#evaluation_statement.
    def visitEvaluation_statement(self, ctx:JinjaParser.Evaluation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#body.
    def visitBody(self, ctx:JinjaParser.BodyContext):
        return self.visitChildren(ctx)



del JinjaParser