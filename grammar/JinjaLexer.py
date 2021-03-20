# Generated from ./grammar/Jinja.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("<\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\3\2\3\2\3\2\3\3\3\3\3\3\3\4\6\4\31\n\4\r\4\16")
        buf.write("\4\32\3\5\3\5\6\5\37\n\5\r\5\16\5 \3\6\6\6$\n\6\r\6\16")
        buf.write("\6%\3\7\3\7\3\7\3\7\7\7,\n\7\f\7\16\7/\13\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\6\b9\n\b\r\b\16\b:\3-\2\t\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\3\2\6\6\2\62;C\\aac|\5\2\62;")
        buf.write("C\\c|\4\2\13\13\"\"\4\2\f\f\17\17\2A\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\3\21\3\2\2\2\5\24\3\2\2\2\7\30\3\2\2\2")
        buf.write("\t\36\3\2\2\2\13#\3\2\2\2\r\'\3\2\2\2\178\3\2\2\2\21\22")
        buf.write("\7}\2\2\22\23\7}\2\2\23\4\3\2\2\2\24\25\7\177\2\2\25\26")
        buf.write("\7\177\2\2\26\6\3\2\2\2\27\31\t\2\2\2\30\27\3\2\2\2\31")
        buf.write("\32\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\b\3\2\2\2\34")
        buf.write("\37\t\3\2\2\35\37\5\13\6\2\36\34\3\2\2\2\36\35\3\2\2\2")
        buf.write("\37 \3\2\2\2 \36\3\2\2\2 !\3\2\2\2!\n\3\2\2\2\"$\t\4\2")
        buf.write("\2#\"\3\2\2\2$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\f\3\2\2\2")
        buf.write("\'(\7}\2\2()\7%\2\2)-\3\2\2\2*,\13\2\2\2+*\3\2\2\2,/\3")
        buf.write("\2\2\2-.\3\2\2\2-+\3\2\2\2.\60\3\2\2\2/-\3\2\2\2\60\61")
        buf.write("\7%\2\2\61\62\7\177\2\2\62\63\3\2\2\2\63\64\5\17\b\2\64")
        buf.write("\65\3\2\2\2\65\66\b\7\2\2\66\16\3\2\2\2\679\t\5\2\28\67")
        buf.write("\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\20\3\2\2\2\n\2")
        buf.write("\30\32\36 %-:\3\b\2\2")
        return buf.getvalue()


class JinjaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    ID = 3
    TEXT = 4
    WS = 5
    COMMENT = 6
    NEWLINE = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{{'", "'}}'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "TEXT", "WS", "COMMENT", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "ID", "TEXT", "WS", "COMMENT", "NEWLINE" ]

    grammarFileName = "Jinja.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


