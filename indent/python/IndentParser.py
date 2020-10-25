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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("$\4\2\t\2\4\3\t\3\3\2\7\2\b\n\2\f\2\16\2\13\13\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3\"\n\3\3\3\2\2\4\2\4\2\3\3")
        buf.write("\2\b\t\2&\2\t\3\2\2\2\4!\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2")
        buf.write("\2\b\13\3\2\2\2\t\7\3\2\2\2\t\n\3\2\2\2\n\f\3\2\2\2\13")
        buf.write("\t\3\2\2\2\f\r\7\2\2\3\r\3\3\2\2\2\16\"\t\2\2\2\17\20")
        buf.write("\7\6\2\2\20\"\7\5\2\2\21\22\7\3\2\2\22\23\7\5\2\2\23\24")
        buf.write("\7\b\2\2\24\25\7\6\2\2\25\"\7\5\2\2\26\27\7\3\2\2\27\30")
        buf.write("\7\5\2\2\30\31\7\b\2\2\31\32\7\6\2\2\32\33\7\5\2\2\33")
        buf.write("\34\7\t\2\2\34\35\7\4\2\2\35\36\7\5\2\2\36\37\7\b\2\2")
        buf.write("\37\"\7\6\2\2 \"\7\5\2\2!\16\3\2\2\2!\17\3\2\2\2!\21\3")
        buf.write("\2\2\2!\26\3\2\2\2! \3\2\2\2\"\5\3\2\2\2\4\t!")
        return buf.getvalue()


class IndentParser ( Parser ):

    grammarFileName = "Indent.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'\n'", "<INVALID>", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "NEWLINE", 
                      "VARIABLE", "TABS", "INDENT", "DEDENT" ]

    RULE_program = 0
    RULE_commands = 1

    ruleNames =  [ "program", "commands" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    NEWLINE=3
    VARIABLE=4
    TABS=5
    INDENT=6
    DEDENT=7

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << IndentParser.T__0) | (1 << IndentParser.NEWLINE) | (1 << IndentParser.VARIABLE) | (1 << IndentParser.INDENT) | (1 << IndentParser.DEDENT))) != 0):
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


    class CommandIfContext(CommandsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IndentParser.CommandsContext
            super().__init__(parser)
            self.var = None # Token
            self.trueP = None # Token
            self.falseP = None # Token
            self.copyFrom(ctx)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(IndentParser.NEWLINE)
            else:
                return self.getToken(IndentParser.NEWLINE, i)
        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(IndentParser.INDENT)
            else:
                return self.getToken(IndentParser.INDENT, i)
        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(IndentParser.VARIABLE)
            else:
                return self.getToken(IndentParser.VARIABLE, i)
        def DEDENT(self):
            return self.getToken(IndentParser.DEDENT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandIf" ):
                return visitor.visitCommandIf(self)
            else:
                return visitor.visitChildren(self)



    def commands(self):

        localctx = IndentParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commands)
        self._la = 0 # Token type
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
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

            elif la_ == 2:
                localctx = IndentParser.CommandExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                localctx.var = self.match(IndentParser.VARIABLE)
                self.state = 14
                self.match(IndentParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = IndentParser.CommandIfContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 15
                self.match(IndentParser.T__0)
                self.state = 16
                self.match(IndentParser.NEWLINE)
                self.state = 17
                self.match(IndentParser.INDENT)
                self.state = 18
                localctx.var = self.match(IndentParser.VARIABLE)
                self.state = 19
                self.match(IndentParser.NEWLINE)
                pass

            elif la_ == 4:
                localctx = IndentParser.CommandIfContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 20
                self.match(IndentParser.T__0)
                self.state = 21
                self.match(IndentParser.NEWLINE)
                self.state = 22
                self.match(IndentParser.INDENT)
                self.state = 23
                localctx.trueP = self.match(IndentParser.VARIABLE)
                self.state = 24
                self.match(IndentParser.NEWLINE)
                self.state = 25
                self.match(IndentParser.DEDENT)
                self.state = 26
                self.match(IndentParser.T__1)
                self.state = 27
                self.match(IndentParser.NEWLINE)
                self.state = 28
                self.match(IndentParser.INDENT)
                self.state = 29
                localctx.falseP = self.match(IndentParser.VARIABLE)
                pass

            elif la_ == 5:
                localctx = IndentParser.CommandEmptyLineContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 30
                self.match(IndentParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





