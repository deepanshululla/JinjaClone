# Generated from ./grammar/Jinja.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("\60\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16")
        buf.write("\n\2\r\2\16\2\17\3\2\3\2\3\3\3\3\5\3\26\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\5\4\35\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4%\n\4")
        buf.write("\f\4\16\4(\13\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\2\3\6\7\2")
        buf.write("\4\6\b\n\2\4\3\2\b\t\3\2\n\13\2\61\2\r\3\2\2\2\4\25\3")
        buf.write("\2\2\2\6\34\3\2\2\2\b)\3\2\2\2\n-\3\2\2\2\f\16\5\4\3\2")
        buf.write("\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2")
        buf.write("\20\21\3\2\2\2\21\22\7\2\2\3\22\3\3\2\2\2\23\26\5\b\5")
        buf.write("\2\24\26\5\n\6\2\25\23\3\2\2\2\25\24\3\2\2\2\26\5\3\2")
        buf.write("\2\2\27\30\b\4\1\2\30\35\7\7\2\2\31\35\7\6\2\2\32\35\7")
        buf.write("\f\2\2\33\35\7\5\2\2\34\27\3\2\2\2\34\31\3\2\2\2\34\32")
        buf.write("\3\2\2\2\34\33\3\2\2\2\35&\3\2\2\2\36\37\f\b\2\2\37 \t")
        buf.write("\2\2\2 %\5\6\4\t!\"\f\7\2\2\"#\t\3\2\2#%\5\6\4\b$\36\3")
        buf.write("\2\2\2$!\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\7\3")
        buf.write("\2\2\2(&\3\2\2\2)*\7\3\2\2*+\5\6\4\2+,\7\4\2\2,\t\3\2")
        buf.write("\2\2-.\7\20\2\2.\13\3\2\2\2\7\17\25\34$&")
        return buf.getvalue()


class JinjaParser ( Parser ):

    grammarFileName = "Jinja.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{{'", "'}}'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'*'", "'/'", "'-'", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "DOUBLE", "MUL", "DIV", "SUB", "ADD", "STRING", "WS", 
                      "NEWLINE", "COMMENT", "CONTENTS", "SYMBOLS", "ANY" ]

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
    INT=4
    DOUBLE=5
    MUL=6
    DIV=7
    SUB=8
    ADD=9
    STRING=10
    WS=11
    NEWLINE=12
    COMMENT=13
    CONTENTS=14
    SYMBOLS=15
    ANY=16

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
                if not (_la==JinjaParser.T__0 or _la==JinjaParser.CONTENTS):
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

        def evaluation_statement(self):
            return self.getTypedRuleContext(JinjaParser.Evaluation_statementContext,0)


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
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JinjaParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.evaluation_statement()
                pass
            elif token in [JinjaParser.CONTENTS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
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


        def getRuleIndex(self):
            return JinjaParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class EqIntContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JinjaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(JinjaParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqInt" ):
                return visitor.visitEqInt(self)
            else:
                return visitor.visitChildren(self)


    class EqDblContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JinjaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DOUBLE(self):
            return self.getToken(JinjaParser.DOUBLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqDbl" ):
                return visitor.visitEqDbl(self)
            else:
                return visitor.visitChildren(self)


    class EqStrContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JinjaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(JinjaParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqStr" ):
                return visitor.visitEqStr(self)
            else:
                return visitor.visitChildren(self)


    class EqAddContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JinjaParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.operator = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JinjaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JinjaParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(JinjaParser.ADD, 0)
        def SUB(self):
            return self.getToken(JinjaParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqAdd" ):
                return visitor.visitEqAdd(self)
            else:
                return visitor.visitChildren(self)


    class EqVarContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JinjaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(JinjaParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqVar" ):
                return visitor.visitEqVar(self)
            else:
                return visitor.visitChildren(self)


    class EqMULContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JinjaParser.ExpressionContext
            super().__init__(parser)
            self.left = None # ExpressionContext
            self.operator = None # Token
            self.right = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JinjaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(JinjaParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(JinjaParser.MUL, 0)
        def DIV(self):
            return self.getToken(JinjaParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqMUL" ):
                return visitor.visitEqMUL(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = JinjaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JinjaParser.DOUBLE]:
                localctx = JinjaParser.EqDblContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 22
                self.match(JinjaParser.DOUBLE)
                pass
            elif token in [JinjaParser.INT]:
                localctx = JinjaParser.EqIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                self.match(JinjaParser.INT)
                pass
            elif token in [JinjaParser.STRING]:
                localctx = JinjaParser.EqStrContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(JinjaParser.STRING)
                pass
            elif token in [JinjaParser.ID]:
                localctx = JinjaParser.EqVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(JinjaParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = JinjaParser.EqMULContext(self, JinjaParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 28
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 29
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==JinjaParser.MUL or _la==JinjaParser.DIV):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 30
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = JinjaParser.EqAddContext(self, JinjaParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 31
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 32
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==JinjaParser.SUB or _la==JinjaParser.ADD):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        localctx.right = self.expression(6)
                        pass

             
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 39
            self.match(JinjaParser.T__0)
            self.state = 40
            self.expression(0)
            self.state = 41
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

        def CONTENTS(self):
            return self.getToken(JinjaParser.CONTENTS, 0)

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
            self.state = 43
            self.match(JinjaParser.CONTENTS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




