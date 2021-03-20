# Generated from ./grammar/Jinja.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("&\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\2\3\2\3\3\6\3\25\n\3\r\3\16\3\26\3\3")
        buf.write("\3\3\3\3\5\3\34\n\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\2\2\7\2\4\6\b\n\2\2\2#\2\r\3\2\2\2\4\33\3\2\2\2\6\35")
        buf.write("\3\2\2\2\b\37\3\2\2\2\n#\3\2\2\2\f\16\5\4\3\2\r\f\3\2")
        buf.write("\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\21\3")
        buf.write("\2\2\2\21\22\7\2\2\3\22\3\3\2\2\2\23\25\5\b\5\2\24\23")
        buf.write("\3\2\2\2\25\26\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27")
        buf.write("\30\3\2\2\2\30\31\7\t\2\2\31\34\3\2\2\2\32\34\5\n\6\2")
        buf.write("\33\24\3\2\2\2\33\32\3\2\2\2\34\5\3\2\2\2\35\36\7\5\2")
        buf.write("\2\36\7\3\2\2\2\37 \7\3\2\2 !\5\6\4\2!\"\7\4\2\2\"\t\3")
        buf.write("\2\2\2#$\7\6\2\2$\13\3\2\2\2\5\17\26\33")
        return buf.getvalue()


class JinjaParser ( Parser ):

    grammarFileName = "Jinja.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{{'", "'}}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ID", "TEXT", 
                      "WS", "COMMENT", "NEWLINE" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_evaluation_statement = 3
    RULE_body = 4

    ruleNames =  [ "program", "statement", "expression", "evaluation_statement", 
                   "body" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ID=3
    TEXT=4
    WS=5
    COMMENT=6
    NEWLINE=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(JinjaParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JinjaParser.StatementContext)
            else:
                return self.getTypedRuleContext(JinjaParser.StatementContext,i)


        def getRuleIndex(self):
            return JinjaParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = JinjaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.statement()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==JinjaParser.T__0 or _la==JinjaParser.TEXT):
                    break

            self.state = 15
            self.match(JinjaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(JinjaParser.NEWLINE, 0)

        def evaluation_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JinjaParser.Evaluation_statementContext)
            else:
                return self.getTypedRuleContext(JinjaParser.Evaluation_statementContext,i)


        def body(self):
            return self.getTypedRuleContext(JinjaParser.BodyContext,0)


        def getRuleIndex(self):
            return JinjaParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = JinjaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JinjaParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 17
                    self.evaluation_statement()
                    self.state = 20 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==JinjaParser.T__0):
                        break

                self.state = 22
                self.match(JinjaParser.NEWLINE)
                pass
            elif token in [JinjaParser.TEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.body()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(JinjaParser.ID, 0)

        def getRuleIndex(self):
            return JinjaParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = JinjaParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(JinjaParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Evaluation_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(JinjaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JinjaParser.RULE_evaluation_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvaluation_statement" ):
                return visitor.visitEvaluation_statement(self)
            else:
                return visitor.visitChildren(self)




    def evaluation_statement(self):

        localctx = JinjaParser.Evaluation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_evaluation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(JinjaParser.T__0)
            self.state = 30
            self.expression()
            self.state = 31
            self.match(JinjaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(JinjaParser.TEXT, 0)

        def getRuleIndex(self):
            return JinjaParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = JinjaParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(JinjaParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





