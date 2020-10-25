# Generated from Indent.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .IndentParser import IndentParser
else:
    from IndentParser import IndentParser

# This class defines a complete generic visitor for a parse tree produced by IndentParser.

class IndentVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IndentParser#program.
    def visitProgram(self, ctx:IndentParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IndentParser#commandExpr.
    def visitCommandExpr(self, ctx:IndentParser.CommandExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IndentParser#commandNewline.
    def visitCommandNewline(self, ctx:IndentParser.CommandNewlineContext):
        return self.visitChildren(ctx)



del IndentParser