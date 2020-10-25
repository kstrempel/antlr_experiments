# Generated from Math.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MathParser import MathParser
else:
    from MathParser import MathParser

# This class defines a complete generic visitor for a parse tree produced by MathParser.

class MathVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MathParser#formula.
    def visitFormula(self, ctx:MathParser.FormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#infixExpr.
    def visitInfixExpr(self, ctx:MathParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#numberExpr.
    def visitNumberExpr(self, ctx:MathParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#parensExpr.
    def visitParensExpr(self, ctx:MathParser.ParensExprContext):
        return self.visitChildren(ctx)



del MathParser