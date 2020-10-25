# Generated from Math.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MathParser import MathParser
else:
    from MathParser import MathParser

# This class defines a complete listener for a parse tree produced by MathParser.
class MathListener(ParseTreeListener):

    # Enter a parse tree produced by MathParser#formula.
    def enterFormula(self, ctx:MathParser.FormulaContext):
        pass

    # Exit a parse tree produced by MathParser#formula.
    def exitFormula(self, ctx:MathParser.FormulaContext):
        pass


    # Enter a parse tree produced by MathParser#infixExpr.
    def enterInfixExpr(self, ctx:MathParser.InfixExprContext):
        pass

    # Exit a parse tree produced by MathParser#infixExpr.
    def exitInfixExpr(self, ctx:MathParser.InfixExprContext):
        pass


    # Enter a parse tree produced by MathParser#numberExpr.
    def enterNumberExpr(self, ctx:MathParser.NumberExprContext):
        pass

    # Exit a parse tree produced by MathParser#numberExpr.
    def exitNumberExpr(self, ctx:MathParser.NumberExprContext):
        pass


    # Enter a parse tree produced by MathParser#parensExpr.
    def enterParensExpr(self, ctx:MathParser.ParensExprContext):
        pass

    # Exit a parse tree produced by MathParser#parensExpr.
    def exitParensExpr(self, ctx:MathParser.ParensExprContext):
        pass



del MathParser