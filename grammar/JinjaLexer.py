# Generated from ./grammar/Jinja.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2%")
        buf.write("\u0120\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6")
        buf.write("\7\6Z\n\6\f\6\16\6]\13\6\3\7\5\7`\n\7\3\7\6\7c\n\7\r\7")
        buf.write("\16\7d\3\b\5\bh\n\b\3\b\6\bk\n\b\r\b\16\bl\3\b\3\b\6\b")
        buf.write("q\n\b\r\b\16\br\3\b\5\bv\n\b\3\b\3\b\6\bz\n\b\r\b\16\b")
        buf.write("{\5\b~\n\b\3\t\3\t\3\t\7\t\u0083\n\t\f\t\16\t\u0086\13")
        buf.write("\t\3\t\3\t\3\n\3\n\5\n\u008c\n\n\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \6 \u00f0\n \r \16 \u00f1\3 \3")
        buf.write(" \3!\6!\u00f7\n!\r!\16!\u00f8\3\"\3\"\3\"\3\"\7\"\u00ff")
        buf.write("\n\"\f\"\16\"\u0102\13\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\5#\u010f\n#\3$\3$\3$\3$\6$\u0115\n$\r$\16$")
        buf.write("\u0116\3%\3%\3%\3%\5%\u011d\n%\3&\3&\4\u0084\u0100\2\'")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I\2K\2\3")
        buf.write("\2\t\3\2c|\6\2\62;C\\aac|\4\2\13\13\"\"\4\2\f\f\17\17")
        buf.write("\6\2\61\61=>@@aa\5\2\62;C\\c|\3\2\62;\2\u0133\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\3M\3\2\2\2\5O\3\2")
        buf.write("\2\2\7Q\3\2\2\2\tT\3\2\2\2\13W\3\2\2\2\r_\3\2\2\2\17}")
        buf.write("\3\2\2\2\21\177\3\2\2\2\23\u008b\3\2\2\2\25\u008d\3\2")
        buf.write("\2\2\27\u0090\3\2\2\2\31\u0093\3\2\2\2\33\u0095\3\2\2")
        buf.write("\2\35\u0097\3\2\2\2\37\u0099\3\2\2\2!\u009b\3\2\2\2#\u009f")
        buf.write("\3\2\2\2%\u00a4\3\2\2\2\'\u00aa\3\2\2\2)\u00ad\3\2\2\2")
        buf.write("+\u00b0\3\2\2\2-\u00b2\3\2\2\2/\u00b4\3\2\2\2\61\u00b7")
        buf.write("\3\2\2\2\63\u00ba\3\2\2\2\65\u00c2\3\2\2\2\67\u00cc\3")
        buf.write("\2\2\29\u00d8\3\2\2\2;\u00dd\3\2\2\2=\u00e8\3\2\2\2?\u00ef")
        buf.write("\3\2\2\2A\u00f6\3\2\2\2C\u00fa\3\2\2\2E\u010e\3\2\2\2")
        buf.write("G\u0114\3\2\2\2I\u011c\3\2\2\2K\u011e\3\2\2\2MN\7*\2\2")
        buf.write("N\4\3\2\2\2OP\7+\2\2P\6\3\2\2\2QR\7}\2\2RS\7}\2\2S\b\3")
        buf.write("\2\2\2TU\7\177\2\2UV\7\177\2\2V\n\3\2\2\2W[\t\2\2\2XZ")
        buf.write("\t\3\2\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\\f")
        buf.write("\3\2\2\2][\3\2\2\2^`\7/\2\2_^\3\2\2\2_`\3\2\2\2`b\3\2")
        buf.write("\2\2ac\5K&\2ba\3\2\2\2cd\3\2\2\2db\3\2\2\2de\3\2\2\2e")
        buf.write("\16\3\2\2\2fh\7/\2\2gf\3\2\2\2gh\3\2\2\2hj\3\2\2\2ik\5")
        buf.write("K&\2ji\3\2\2\2kl\3\2\2\2lj\3\2\2\2lm\3\2\2\2mn\3\2\2\2")
        buf.write("np\7\60\2\2oq\5K&\2po\3\2\2\2qr\3\2\2\2rp\3\2\2\2rs\3")
        buf.write("\2\2\2s~\3\2\2\2tv\7/\2\2ut\3\2\2\2uv\3\2\2\2vw\3\2\2")
        buf.write("\2wy\7\60\2\2xz\5K&\2yx\3\2\2\2z{\3\2\2\2{y\3\2\2\2{|")
        buf.write("\3\2\2\2|~\3\2\2\2}g\3\2\2\2}u\3\2\2\2~\20\3\2\2\2\177")
        buf.write("\u0084\7)\2\2\u0080\u0083\5I%\2\u0081\u0083\13\2\2\2\u0082")
        buf.write("\u0080\3\2\2\2\u0082\u0081\3\2\2\2\u0083\u0086\3\2\2\2")
        buf.write("\u0084\u0085\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0087\3")
        buf.write("\2\2\2\u0086\u0084\3\2\2\2\u0087\u0088\7)\2\2\u0088\22")
        buf.write("\3\2\2\2\u0089\u008c\5#\22\2\u008a\u008c\5%\23\2\u008b")
        buf.write("\u0089\3\2\2\2\u008b\u008a\3\2\2\2\u008c\24\3\2\2\2\u008d")
        buf.write("\u008e\7~\2\2\u008e\u008f\7~\2\2\u008f\26\3\2\2\2\u0090")
        buf.write("\u0091\7(\2\2\u0091\u0092\7(\2\2\u0092\30\3\2\2\2\u0093")
        buf.write("\u0094\7-\2\2\u0094\32\3\2\2\2\u0095\u0096\7/\2\2\u0096")
        buf.write("\34\3\2\2\2\u0097\u0098\7,\2\2\u0098\36\3\2\2\2\u0099")
        buf.write("\u009a\7\61\2\2\u009a \3\2\2\2\u009b\u009c\7P\2\2\u009c")
        buf.write("\u009d\7Q\2\2\u009d\u009e\7V\2\2\u009e\"\3\2\2\2\u009f")
        buf.write("\u00a0\7V\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2\7w\2\2\u00a2")
        buf.write("\u00a3\7g\2\2\u00a3$\3\2\2\2\u00a4\u00a5\7H\2\2\u00a5")
        buf.write("\u00a6\7c\2\2\u00a6\u00a7\7n\2\2\u00a7\u00a8\7u\2\2\u00a8")
        buf.write("\u00a9\7g\2\2\u00a9&\3\2\2\2\u00aa\u00ab\7?\2\2\u00ab")
        buf.write("\u00ac\7?\2\2\u00ac(\3\2\2\2\u00ad\u00ae\7#\2\2\u00ae")
        buf.write("\u00af\7?\2\2\u00af*\3\2\2\2\u00b0\u00b1\7@\2\2\u00b1")
        buf.write(",\3\2\2\2\u00b2\u00b3\7>\2\2\u00b3.\3\2\2\2\u00b4\u00b5")
        buf.write("\7@\2\2\u00b5\u00b6\7?\2\2\u00b6\60\3\2\2\2\u00b7\u00b8")
        buf.write("\7>\2\2\u00b8\u00b9\7?\2\2\u00b9\62\3\2\2\2\u00ba\u00bb")
        buf.write("\7}\2\2\u00bb\u00bc\7\'\2\2\u00bc\u00bd\7\"\2\2\u00bd")
        buf.write("\u00be\7k\2\2\u00be\u00bf\7h\2\2\u00bf\u00c0\7\"\2\2\u00c0")
        buf.write("\u00c1\7*\2\2\u00c1\64\3\2\2\2\u00c2\u00c3\7}\2\2\u00c3")
        buf.write("\u00c4\7\'\2\2\u00c4\u00c5\7\"\2\2\u00c5\u00c6\7g\2\2")
        buf.write("\u00c6\u00c7\7n\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9\7h")
        buf.write("\2\2\u00c9\u00ca\7\"\2\2\u00ca\u00cb\7*\2\2\u00cb\66\3")
        buf.write("\2\2\2\u00cc\u00cd\7}\2\2\u00cd\u00ce\7\'\2\2\u00ce\u00cf")
        buf.write("\7\"\2\2\u00cf\u00d0\7g\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2")
        buf.write("\7f\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4\7h\2\2\u00d4\u00d5")
        buf.write("\7\"\2\2\u00d5\u00d6\7\'\2\2\u00d6\u00d7\7\177\2\2\u00d7")
        buf.write("8\3\2\2\2\u00d8\u00d9\7+\2\2\u00d9\u00da\7\"\2\2\u00da")
        buf.write("\u00db\7\'\2\2\u00db\u00dc\7\177\2\2\u00dc:\3\2\2\2\u00dd")
        buf.write("\u00de\7}\2\2\u00de\u00df\7\'\2\2\u00df\u00e0\7\"\2\2")
        buf.write("\u00e0\u00e1\7g\2\2\u00e1\u00e2\7n\2\2\u00e2\u00e3\7u")
        buf.write("\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5\7\"\2\2\u00e5\u00e6")
        buf.write("\7\'\2\2\u00e6\u00e7\7\177\2\2\u00e7<\3\2\2\2\u00e8\u00e9")
        buf.write("\7y\2\2\u00e9\u00ea\7j\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec")
        buf.write("\7n\2\2\u00ec\u00ed\7g\2\2\u00ed>\3\2\2\2\u00ee\u00f0")
        buf.write("\t\4\2\2\u00ef\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\3\2\2\2")
        buf.write("\u00f3\u00f4\b \2\2\u00f4@\3\2\2\2\u00f5\u00f7\t\5\2\2")
        buf.write("\u00f6\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f6\3")
        buf.write("\2\2\2\u00f8\u00f9\3\2\2\2\u00f9B\3\2\2\2\u00fa\u00fb")
        buf.write("\7}\2\2\u00fb\u00fc\7%\2\2\u00fc\u0100\3\2\2\2\u00fd\u00ff")
        buf.write("\13\2\2\2\u00fe\u00fd\3\2\2\2\u00ff\u0102\3\2\2\2\u0100")
        buf.write("\u0101\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0103\3\2\2\2")
        buf.write("\u0102\u0100\3\2\2\2\u0103\u0104\7%\2\2\u0104\u0105\7")
        buf.write("\177\2\2\u0105\u0106\3\2\2\2\u0106\u0107\5A!\2\u0107\u0108")
        buf.write("\3\2\2\2\u0108\u0109\b\"\2\2\u0109D\3\2\2\2\u010a\u010f")
        buf.write("\t\6\2\2\u010b\u010c\7?\2\2\u010c\u010f\7$\2\2\u010d\u010f")
        buf.write("\7$\2\2\u010e\u010a\3\2\2\2\u010e\u010b\3\2\2\2\u010e")
        buf.write("\u010d\3\2\2\2\u010fF\3\2\2\2\u0110\u0115\t\7\2\2\u0111")
        buf.write("\u0115\5E#\2\u0112\u0115\5A!\2\u0113\u0115\t\4\2\2\u0114")
        buf.write("\u0110\3\2\2\2\u0114\u0111\3\2\2\2\u0114\u0112\3\2\2\2")
        buf.write("\u0114\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0114\3")
        buf.write("\2\2\2\u0116\u0117\3\2\2\2\u0117H\3\2\2\2\u0118\u0119")
        buf.write("\7^\2\2\u0119\u011d\7$\2\2\u011a\u011b\7^\2\2\u011b\u011d")
        buf.write("\7^\2\2\u011c\u0118\3\2\2\2\u011c\u011a\3\2\2\2\u011d")
        buf.write("J\3\2\2\2\u011e\u011f\t\b\2\2\u011fL\3\2\2\2\27\2Y[_d")
        buf.write("glru{}\u0082\u0084\u008b\u00f1\u00f8\u0100\u010e\u0114")
        buf.write("\u0116\u011c\3\b\2\2")
        return buf.getvalue()


class JinjaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    ID = 5
    INT = 6
    DOUBLE = 7
    STRING = 8
    BOOL = 9
    OR = 10
    AND = 11
    ADD = 12
    SUB = 13
    MUL = 14
    DIV = 15
    NOT = 16
    TRUE = 17
    FALSE = 18
    EQ = 19
    NEQ = 20
    GT = 21
    LT = 22
    GTEQ = 23
    LTEQ = 24
    IF = 25
    ELIF = 26
    ENDIF = 27
    BLOCK_END_IF = 28
    ELSE = 29
    WHILE = 30
    WS = 31
    NEWLINE = 32
    COMMENT = 33
    SYMBOLS = 34
    ANY = 35

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{{'", "'}}'", "'||'", "'&&'", "'+'", "'-'", 
            "'*'", "'/'", "'NOT'", "'True'", "'False'", "'=='", "'!='", 
            "'>'", "'<'", "'>='", "'<='", "'{% if ('", "'{% elif ('", "'{% endif %}'", 
            "') %}'", "'{% else %}'", "'while'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "DOUBLE", "STRING", "BOOL", "OR", "AND", "ADD", 
            "SUB", "MUL", "DIV", "NOT", "TRUE", "FALSE", "EQ", "NEQ", "GT", 
            "LT", "GTEQ", "LTEQ", "IF", "ELIF", "ENDIF", "BLOCK_END_IF", 
            "ELSE", "WHILE", "WS", "NEWLINE", "COMMENT", "SYMBOLS", "ANY" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "ID", "INT", "DOUBLE", 
                  "STRING", "BOOL", "OR", "AND", "ADD", "SUB", "MUL", "DIV", 
                  "NOT", "TRUE", "FALSE", "EQ", "NEQ", "GT", "LT", "GTEQ", 
                  "LTEQ", "IF", "ELIF", "ENDIF", "BLOCK_END_IF", "ELSE", 
                  "WHILE", "WS", "NEWLINE", "COMMENT", "SYMBOLS", "ANY", 
                  "ESC", "DIGIT" ]

    grammarFileName = "Jinja.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


