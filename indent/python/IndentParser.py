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
        buf.write("\25\4\2\t\2\4\3\t\3\3\2\7\2\b\n\2\f\2\16\2\13\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\5\3\23\n\3\3\3\2\2\4\2\4\2\3\3\2")
        buf.write("\6\7\2\25\2\t\3\2\2\2\4\22\3\2\2\2\6\b\5\4\3\2\7\6\3\2")
        buf.write("\2\2\b\13\3\2\2\2\t\7\3\2\2\2\t\n\3\2\2\2\n\f\3\2\2\2")
        buf.write("\13\t\3\2\2\2\f\r\7\2\2\3\r\3\3\2\2\2\16\23\t\2\2\2\17")
        buf.write("\20\7\4\2\2\20\23\7\3\2\2\21\23\7\3\2\2\22\16\3\2\2\2")
        buf.write("\22\17\3\2\2\2\22\21\3\2\2\2\23\5\3\2\2\2\4\t\22")
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

        def INDENT(self):
            return self.getToken(IndentParser.INDENT, 0)
        def DEDENT(self):
            return self.getToken(IndentParser.DEDENT, 0)
        def NEWLINE(self):
            return self.getToken(IndentParser.NEWLINE, 0)
        def VARIABLE(self):
            return self.getToken(IndentParser.VARIABLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandExpr" ):
                return visitor.visitCommandExpr(self)
            else:
                return visitor.visitChildren(self)


    class CommandEmptyLineContext(CommandsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IndentParser.CommandsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(IndentParser.NEWLINE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandEmptyLine" ):
                return visitor.visitCommandEmptyLine(self)
            else:
                return visitor.visitChildren(self)



    def commands(self):

        localctx = IndentParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commands)
        self._la = 0 # Token type
        try:
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [IndentParser.INDENT, IndentParser.DEDENT]:
                localctx = IndentParser.CommandExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                localctx.inden = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==IndentParser.INDENT or _la==IndentParser.DEDENT):
                    localctx.inden = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [IndentParser.VARIABLE]:
                localctx = IndentParser.CommandExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                localctx.var = self.match(IndentParser.VARIABLE)
                self.state = 14
                self.match(IndentParser.NEWLINE)
                pass
            elif token in [IndentParser.NEWLINE]:
                localctx = IndentParser.CommandEmptyLineContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 15
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





