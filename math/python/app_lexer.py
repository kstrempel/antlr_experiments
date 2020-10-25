import io
import sys

from antlr4 import *
from MathLexer import MathLexer
from MathListener import MathListener
from MathParser import MathParser
from MathVisitor import MathVisitor

class NumberNode():
  def __init__(self, value):
    self.value = value

  def calc(self):
    return self.value

class OperatorNode():
  def __init__(self, operator, left, right):
    self.operator = operator
    self.left = left
    self.right = right

  def calc(self):
    right = self.right.calc()
    left = self.left.calc()

    if self.operator == '+':
      value = left + right
    elif self.operator == '*':
      value = left * right
    elif self.operator == '-':
      value = left - right
    elif self.operator == '/':
      value = left / right

    return value

class EvalVisitor(MathVisitor):

  def visitInfixExpr(self, ctx:MathParser.InfixExprContext):
    operator = 'unknown'
    if ctx.ADD():
      operator = '+'
    if ctx.MINUS():
      operator = '-'
    if ctx.TIMES():
      operator = '*'
    if ctx.DIV():
      operator = '/'

    left = self.visit(ctx.left)
    right = self.visit(ctx.right)
    result = OperatorNode(operator, left, right)
    return result

  def visitNumberExpr(self, ctx:MathParser.NumberExprContext):
    return NumberNode(int(str(ctx.NUMBER())))


def main(inputstream):
  lexer = MathLexer(inputstream)
  stream = CommonTokenStream(lexer)
  parser = MathParser(stream)
  tree = parser.formula()
  ast = EvalVisitor().visit(tree)
  print(ast.calc())

if __name__ == '__main__':
  formula = sys.argv[1]
  print(f"Calc: {formula}")
  stream = InputStream(formula)
  main(stream)