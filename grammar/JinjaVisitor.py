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


    # Visit a parse tree produced by JinjaParser#eqPar.
    def visitEqPar(self, ctx:JinjaParser.EqParContext):
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


    # Visit a parse tree produced by JinjaParser#eqBool.
    def visitEqBool(self, ctx:JinjaParser.EqBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#orExpr.
    def visitOrExpr(self, ctx:JinjaParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#boolEq.
    def visitBoolEq(self, ctx:JinjaParser.BoolEqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#relationExpr.
    def visitRelationExpr(self, ctx:JinjaParser.RelationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#andExpr.
    def visitAndExpr(self, ctx:JinjaParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#evaluation_statement.
    def visitEvaluation_statement(self, ctx:JinjaParser.Evaluation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#if_statement.
    def visitIf_statement(self, ctx:JinjaParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#elif_statement.
    def visitElif_statement(self, ctx:JinjaParser.Elif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#else_statement.
    def visitElse_statement(self, ctx:JinjaParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#if_fragment.
    def visitIf_fragment(self, ctx:JinjaParser.If_fragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#elif_fragment.
    def visitElif_fragment(self, ctx:JinjaParser.Elif_fragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#else_fragment.
    def visitElse_fragment(self, ctx:JinjaParser.Else_fragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#endif_fragment.
    def visitEndif_fragment(self, ctx:JinjaParser.Endif_fragmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#code_block.
    def visitCode_block(self, ctx:JinjaParser.Code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#body.
    def visitBody(self, ctx:JinjaParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by JinjaParser#contents.
    def visitContents(self, ctx:JinjaParser.ContentsContext):
        return self.visitChildren(ctx)



del JinjaParser