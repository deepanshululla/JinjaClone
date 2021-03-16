# Generated from ./grammar/Jinja.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write(";\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4 \n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4")
        buf.write("(\n\4\f\4\16\4+\13\4\3\5\3\5\3\5\5\5\60\n\5\3\5\3\5\7")
        buf.write("\5\64\n\5\f\5\16\5\67\13\5\3\6\3\6\3\6\2\3\6\7\2\4\6\b")
        buf.write("\n\2\4\3\2\13\f\3\2\r\16\2?\2\r\3\2\2\2\4\23\3\2\2\2\6")
        buf.write("\37\3\2\2\2\b,\3\2\2\2\n8\3\2\2\2\f\16\5\4\3\2\r\f\3\2")
        buf.write("\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20\21\3")
        buf.write("\2\2\2\21\22\7\2\2\3\22\3\3\2\2\2\23\24\5\b\5\2\24\5\3")
        buf.write("\2\2\2\25\26\b\4\1\2\26\27\7\3\2\2\27\30\5\6\4\2\30\31")
        buf.write("\7\4\2\2\31 \3\2\2\2\32 \5\b\5\2\33 \7\n\2\2\34 \7\b\2")
        buf.write("\2\35 \7\7\2\2\36 \7\17\2\2\37\25\3\2\2\2\37\32\3\2\2")
        buf.write("\2\37\33\3\2\2\2\37\34\3\2\2\2\37\35\3\2\2\2\37\36\3\2")
        buf.write("\2\2 )\3\2\2\2!\"\f\b\2\2\"#\t\2\2\2#(\5\6\4\t$%\f\7\2")
        buf.write("\2%&\t\3\2\2&(\5\6\4\b\'!\3\2\2\2\'$\3\2\2\2(+\3\2\2\2")
        buf.write(")\'\3\2\2\2)*\3\2\2\2*\7\3\2\2\2+)\3\2\2\2,-\7\n\2\2-")
        buf.write("/\7\5\2\2.\60\5\n\6\2/.\3\2\2\2/\60\3\2\2\2\60\61\3\2")
        buf.write("\2\2\61\65\7\6\2\2\62\64\7\20\2\2\63\62\3\2\2\2\64\67")
        buf.write("\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\t\3\2\2\2\67\65")
        buf.write("\3\2\2\289\5\6\4\29\13\3\2\2\2\b\17\37\')/\65")
        return buf.getvalue()


class JinjaParser ( Parser ):

    grammarFileName = "Jinja.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{{'", "'}}'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'*'", "'/'", 
                     "'-'", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INT", "DOUBLE", "COMMENT", "ID", "MUL", 
                      "DIV", "SUB", "ADD", "STRING", "NEWLINE", "WS", "DIGIT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expression = 2
    RULE_evaluation_statement = 3
    RULE_arguments_list = 4

    ruleNames =  [ "program", "statement", "expression", "evaluation_statement", 
                   "arguments_list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    INT=5
    DOUBLE=6
    COMMENT=7
    ID=8
    MUL=9
    DIV=10
    SUB=11
    ADD=12
    STRING=13
    NEWLINE=14
    WS=15
    DIGIT=16

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
                if not (_la==JinjaParser.ID):
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
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.evaluation_statement()
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


    class EqParContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JinjaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(JinjaParser.ExpressionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqPar" ):
                return visitor.visitEqPar(self)
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


    class EqEvaluationContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JinjaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def evaluation_statement(self):
            return self.getTypedRuleContext(JinjaParser.Evaluation_statementContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqEvaluation" ):
                return visitor.visitEqEvaluation(self)
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
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = JinjaParser.EqParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 20
                self.match(JinjaParser.T__0)
                self.state = 21
                self.expression(0)
                self.state = 22
                self.match(JinjaParser.T__1)
                pass

            elif la_ == 2:
                localctx = JinjaParser.EqEvaluationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.evaluation_statement()
                pass

            elif la_ == 3:
                localctx = JinjaParser.EqVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(JinjaParser.ID)
                pass

            elif la_ == 4:
                localctx = JinjaParser.EqDblContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(JinjaParser.DOUBLE)
                pass

            elif la_ == 5:
                localctx = JinjaParser.EqIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 27
                self.match(JinjaParser.INT)
                pass

            elif la_ == 6:
                localctx = JinjaParser.EqStrContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(JinjaParser.STRING)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = JinjaParser.EqMULContext(self, JinjaParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 31
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 32
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==JinjaParser.MUL or _la==JinjaParser.DIV):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 33
                        localctx.right = self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = JinjaParser.EqAddContext(self, JinjaParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 34
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 35
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==JinjaParser.SUB or _la==JinjaParser.ADD):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 36
                        localctx.right = self.expression(6)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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

        def ID(self):
            return self.getToken(JinjaParser.ID, 0)

        def arguments_list(self):
            return self.getTypedRuleContext(JinjaParser.Arguments_listContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(JinjaParser.NEWLINE)
            else:
                return self.getToken(JinjaParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(JinjaParser.ID)
            self.state = 43
            self.match(JinjaParser.T__2)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JinjaParser.T__0) | (1 << JinjaParser.INT) | (1 << JinjaParser.DOUBLE) | (1 << JinjaParser.ID) | (1 << JinjaParser.STRING))) != 0):
                self.state = 44
                self.arguments_list()


            self.state = 47
            self.match(JinjaParser.T__3)
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 48
                    self.match(JinjaParser.NEWLINE) 
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Arguments_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(JinjaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return JinjaParser.RULE_arguments_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments_list" ):
                return visitor.visitArguments_list(self)
            else:
                return visitor.visitChildren(self)




    def arguments_list(self):

        localctx = JinjaParser.Arguments_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arguments_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.expression(0)
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
         




