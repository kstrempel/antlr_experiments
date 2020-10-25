import io
import sys

from antlr4 import *
from antlr4.Token import CommonToken
from IndentLexer import IndentLexer
from IndentParser import IndentParser
from IndentVisitor import IndentVisitor

program = """
a
-b
-c
d
-e
--f
--g
--h
---i
---j
--k
--l
---m
---n
z
"""

class MyIndentLexer(IndentLexer):

  def init_first(self):
    if not hasattr(self, 'indentiations'):
      self.indentiations = 0
      self.newline_start = False
      self.first = True
      self.next_token = []

  def currentToken(self):
    return self.next_token[-1]

  def nextToken(self):
    self.init_first()

    if self.first:
      self.first = False
      return super().nextToken()

    if self.next_token:
      return self.next_token.pop()

    token = super().nextToken()

    # Fresh line fresh indentiation analyses
    if self.newline_start:
      indentiations_level = 0
      while token.type == IndentLexer.TABS:
        token = super().nextToken()
        indentiations_level+=1

      self.next_token.append(token)
      # Is the indentiation level different from the previous line
      if self.indentiations > indentiations_level:
        # identiation is smaller
        for _ in range(indentiations_level, self.indentiations):
          self.next_token.append(CommonToken(type=IndentParser.DEDENT))
      elif self.indentiations < indentiations_level:
        # identiation is bigger
        for _ in range(self.indentiations, indentiations_level):
          self.next_token.append(CommonToken(type=IndentParser.INDENT))

      # set the current indentiation for the next line
      self.indentiations = indentiations_level

      self.newline_start = False

      return self.next_token.pop()

    # A newline
    if token.type == IndentLexer.NEWLINE:
      self.newline_start = True

    return token



class EvalVisitor(IndentVisitor):

  def __init__(self):
    self.result = None

  # Visit a parse tree produced by IndentParser#program.
  def visitProgram(self, ctx:IndentParser.ProgramContext):
      self.result = "["
      result = self.visitChildren(ctx)
      self.result += "]"
      return result

  # Visit a parse tree produced by IndentParser#commandExpr.
  def visitCommandExpr(self, ctx:IndentParser.CommandExprContext):
    if ctx.inden:
      if ctx.inden.type == IndentParser.INDENT:
        self.result += "{"
      elif ctx.inden.type == IndentParser.DEDENT:
        self.result += "}"
    if ctx.var:
      variable = ctx.var.text
      self.result += f" {variable}  "
    return self.visitChildren(ctx)

def main(inputstream):
  lexer = MyIndentLexer(inputstream)
  stream = CommonTokenStream(lexer)
  parser = IndentParser(stream)
  tree = parser.program()
  visitor = EvalVisitor()
  visitor.visit(tree)
  print(f"Parsed Blocks\n{visitor.result}")

if __name__ == '__main__':
  print(f"Calc:\n{program}")
  stream = InputStream(program[1:])
  main(stream)
