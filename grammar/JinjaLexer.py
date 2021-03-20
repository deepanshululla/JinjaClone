# Generated from ./grammar/Jinja.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("*\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\4\6\4\27\n\4\r\4\16\4\30\3")
        buf.write("\5\3\5\6\5\35\n\5\r\5\16\5\36\3\6\6\6\"\n\6\r\6\16\6#")
        buf.write("\3\7\6\7\'\n\7\r\7\16\7(\2\2\b\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\3\2\6\6\2\62;C\\aac|\5\2\62;C\\c|\4\2\13\13\"\"\4\2")
        buf.write("\f\f\17\17\2.\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5\22\3")
        buf.write("\2\2\2\7\26\3\2\2\2\t\34\3\2\2\2\13!\3\2\2\2\r&\3\2\2")
        buf.write("\2\17\20\7}\2\2\20\21\7}\2\2\21\4\3\2\2\2\22\23\7\177")
        buf.write("\2\2\23\24\7\177\2\2\24\6\3\2\2\2\25\27\t\2\2\2\26\25")
        buf.write("\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31")
        buf.write("\b\3\2\2\2\32\35\t\3\2\2\33\35\5\13\6\2\34\32\3\2\2\2")
        buf.write("\34\33\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37\3\2\2")
        buf.write("\2\37\n\3\2\2\2 \"\t\4\2\2! \3\2\2\2\"#\3\2\2\2#!\3\2")
        buf.write("\2\2#$\3\2\2\2$\f\3\2\2\2%\'\t\5\2\2&%\3\2\2\2\'(\3\2")
        buf.write("\2\2(&\3\2\2\2()\3\2\2\2)\16\3\2\2\2\t\2\26\30\34\36#")
        buf.write("(\2")
        return buf.getvalue()


class JinjaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    ID = 3
    TEXT = 4
    WS = 5
    NEWLINE = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'{{'", "'}}'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "TEXT", "WS", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "ID", "TEXT", "WS", "NEWLINE" ]

    grammarFileName = "Jinja.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


