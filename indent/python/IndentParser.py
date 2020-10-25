# Generated from Indent.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\7")
        buf.write(" \4\2\t\2\4\3\t\3\3\2\7\2\b\n\2\f\2\16\2\13\13\2\3\2\3")
        buf.write("\2\3\3\7\3\20\n\3\f\3\16\3\23\13\3\3\3\3\3\7\3\27\n\3")
        buf.write("\f\3\16\3\32\13\3\3\3\3\3\5\3\36\n\3\3\3\2\2\4\2\4\2\3")
        buf.write("\3\2\6\7\2!\2\t\3\2\2\2\4\35\3\2\2\2\6\b\5\4\3\2\7\6\3")
        buf.write("\2\2\2\b\13\3\2\2\2\t\7\3\2\2\2\t\n\3\2\2\2\n\f\3\2\2")
        buf.write("\2\13\t\3\2\2\2\f\r\7\2\2\3\r\3\3\2\2\2\16\20\t\2\2\2")
        buf.write("\17\16\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2")
        buf.write("\2\22\24\3\2\2\2\23\21\3\2\2\2\24\30\7\4\2\2\25\27\7\5")
        buf.write("\2\2\26\25\3\2\2\2\27\32\3\2\2\2\30\26\3\2\2\2\30\31\3")
        buf.write("\2\2\2\31\33\3\2\2\2\32\30\3\2\2\2\33\36\7\3\2\2\34\36")
        buf.write("\7\3\2\2\35\21\3\2\2\2\35\34\3\2\2\2\36\5\3\2\2\2\6\t")
        buf.write("\21\30\35")
        return buf.getvalue()


class IndentParser ( Parser ):

    grammarFileName = "Indent.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\n'", "<INVALID>", "'-'" ]

    symbolicNames = [ "<INVALID>", "NEWLINE", "VARIABLE", "TABS", "INDENT", 
                      "DEDENT" ]

    RULE_program = 0
    RULE_commands = 1

    ruleNames =  [ "program", "commands" ]

    EOF = Token.EOF
    NEWLINE=1
    VARIABLE=2
    TABS=3
    INDENT=4
    DEDENT=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(IndentParser.EOF, 0)

        def commands(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IndentParser.CommandsContext)
            else:
                return self.getTypedRuleContext(IndentParser.CommandsContext,i)


        def getRuleIndex(self):
            return IndentParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = IndentParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IndentParser.NEWLINE) | (1 << IndentParser.VARIABLE) | (1 << IndentParser.INDENT) | (1 << IndentParser.DEDENT))) != 0):
                self.state = 4
                self.commands()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(IndentParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IndentParser.RULE_commands

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CommandExprContext(CommandsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IndentParser.CommandsContext
            super().__init__(parser)
            self.inden = None # Token
            self.var = None # Token
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(IndentParser.NEWLINE, 0)
        def VARIABLE(self):
            return self.getToken(IndentParser.VARIABLE, 0)
        def TABS(self, i:int=None):
            if i is None:
                return self.getTokens(IndentParser.TABS)
            else:
                return self.getToken(IndentParser.TABS, i)
        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(IndentParser.INDENT)
            else:
                return self.getToken(IndentParser.INDENT, i)
        def DEDENT(self, i:int=None):
            if i is None:
                return self.getTokens(IndentParser.DEDENT)
            else:
                return self.getToken(IndentParser.DEDENT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandExpr" ):
                return visitor.visitCommandExpr(self)
            else:
                return visitor.visitChildren(self)


    class CommandNewlineContext(CommandsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IndentParser.CommandsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(IndentParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandNewline" ):
                return visitor.visitCommandNewline(self)
            else:
                return visitor.visitChildren(self)



    def commands(self):

        localctx = IndentParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commands)
        self._la = 0 # Token type
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IndentParser.VARIABLE, IndentParser.INDENT, IndentParser.DEDENT]:
                localctx = IndentParser.CommandExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==IndentParser.INDENT or _la==IndentParser.DEDENT:
                    self.state = 12
                    localctx.inden = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==IndentParser.INDENT or _la==IndentParser.DEDENT):
                        localctx.inden = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 17
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 18
                localctx.var = self.match(IndentParser.VARIABLE)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==IndentParser.TABS:
                    self.state = 19
                    self.match(IndentParser.TABS)
                    self.state = 24
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 25
                self.match(IndentParser.NEWLINE)
                pass
            elif token in [IndentParser.NEWLINE]:
                localctx = IndentParser.CommandNewlineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(IndentParser.NEWLINE)
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




