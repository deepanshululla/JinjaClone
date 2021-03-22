from jinjaClone.grammar.JinjaLexer import JinjaLexer
from jinjaClone.grammar.JinjaParser import JinjaParser
from jinjaClone.grammar.JinjaVisitor import JinjaVisitor


class JinjaAst(JinjaVisitor):
    def __init__(self):
        self.ns = {'name': 'deepanshu', 'age': 30,
                   'image': "https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072823_1280.jpg"}

    def visitProgram(self, ctx: JinjaParser.ProgramContext):
        return super().visitProgram(ctx)

    def visitStatement(self, ctx: JinjaParser.StatementContext):
        return super().visitStatement(ctx)

    def visitEvaluation_statement(self, ctx: JinjaParser.Evaluation_statementContext):
        value = self.visit(ctx.expression())
        print(value, end='')
        return value

    def visitBody(self, ctx: JinjaParser.BodyContext):
        normalText = ctx.contents().getText()
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

    def visitEqMUL(self, ctx: JinjaParser.EqMULContext):
        operator = ctx.operator
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if operator.type == JinjaLexer.MUL:
            return left * right
        else:
            return float(left) / float(right)

    def visitIf_statement(self, ctx: JinjaParser.If_statementContext):
        elif_statement = ctx.elif_statement()
        else_statement = ctx.else_statement()
        if self.visit(ctx.if_fragment()):
            return self.visit(ctx.code_block())
        elif elif_statement is not None:
            return self.visit(elif_statement)
        elif else_statement is not None:
            return self.visit(else_statement)

    def visitIf_fragment(self, ctx: JinjaParser.If_fragmentContext):
        return self.visit(ctx.boolean_expression())

    def visitElif_fragment(self, ctx: JinjaParser.Elif_fragmentContext):
        return self.visit(ctx.boolean_expression())

    def visitElif_statement(self, ctx: JinjaParser.Elif_statementContext):
        elif_statement = ctx.elif_statement()
        else_statement = ctx.else_statement()
        if self.visit(ctx.elif_fragment()):
            return self.visit(ctx.code_block())
        elif elif_statement is not None:
            return self.visit(elif_statement)
        elif else_statement is not None:
            return self.visit(else_statement)

    def visitElse_statement(self, ctx: JinjaParser.Else_statementContext):
        return self.visit(ctx.code_block())

    # def visitAndExpr(self, ctx: JinjaParser.AndExprContext):
    #     left = self.visit(ctx.left)
    #     right = self.visit(ctx.right)
    #     return left and right
    #
    # def visitOrExpr(self, ctx: JinjaParser.OrExprContext):
    #     left = self.visit(ctx.left)
    #     right = self.visit(ctx.right)
    #     return left or right

    def visitElse_fragment(self, ctx: JinjaParser.Else_fragmentContext):
        return super().visitElse_fragment(ctx)

    def visitCode_block(self, ctx: JinjaParser.Code_blockContext):
        return super().visitCode_block(ctx)

    def visitBoolEq(self, ctx: JinjaParser.BoolEqContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        operand = ctx.operator
        if operand == JinjaLexer.EQ:
            return left == right
        else:
            return left != right

    def visitEndif_fragment(self, ctx: JinjaParser.Endif_fragmentContext):
        return super().visitEndif_fragment(ctx)

    def visitEqBool(self, ctx: JinjaParser.EqBoolContext):
        if ctx.BOOL().getText() == 'True':
            return True
        else:
            return False

    def visitRelationExpr(self, ctx: JinjaParser.RelationExprContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        operator = ctx.operator
        if operator.type == JinjaLexer.GT:
            return left > right
        elif operator.type == JinjaLexer.GTEQ:
            return left >= right
        elif operator.type == JinjaLexer.LT:
            return left < right
        else:
            return left <= right

    def visitContents(self, ctx: JinjaParser.ContentsContext):
        return super().visitContents(ctx)

    def visitEqPar(self, ctx:JinjaParser.EqParContext):
        return self.visit(ctx.expression())

    def visitEqBoolPar(self, ctx: JinjaParser.EqBoolParContext):
        return self.visit(ctx.boolean_expression())

    def visitAssignment_statement(self, ctx:JinjaParser.Assignment_statementContext):
        variable_name = str(ctx.ID().getText())
        variable_value = self.visit(ctx.expression())
        self.ns[variable_name] = variable_value
