# Generated from Indent.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("\36\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\6\5\31\n\5\r\5")
        buf.write("\16\5\32\3\6\3\6\2\2\7\3\3\5\4\7\5\t\6\13\7\3\2\3\3\2")
        buf.write("c|\2\36\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\3\r\3\2\2\2\5\20\3\2\2\2\7\25\3\2\2\2")
        buf.write("\t\30\3\2\2\2\13\34\3\2\2\2\r\16\7k\2\2\16\17\7h\2\2\17")
        buf.write("\4\3\2\2\2\20\21\7g\2\2\21\22\7n\2\2\22\23\7u\2\2\23\24")
        buf.write("\7g\2\2\24\6\3\2\2\2\25\26\7\f\2\2\26\b\3\2\2\2\27\31")
        buf.write("\t\2\2\2\30\27\3\2\2\2\31\32\3\2\2\2\32\30\3\2\2\2\32")
        buf.write("\33\3\2\2\2\33\n\3\2\2\2\34\35\7/\2\2\35\f\3\2\2\2\4\2")
        buf.write("\32\2")
        return buf.getvalue()


class IndentLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    NEWLINE = 3
    VARIABLE = 4
    TABS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'\n'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "VARIABLE", "TABS" ]

    ruleNames = [ "T__0", "T__1", "NEWLINE", "VARIABLE", "TABS" ]

    grammarFileName = "Indent.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


