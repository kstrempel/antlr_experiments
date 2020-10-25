from antlr4 import *
from MathLexer import MathLexer
from MathListener import MathListener
from MathParser import MathParser
import io

class MathPrintListener(MathListener):

  def enterFormula(self, ctx : MathParser.FormulaContext):
    print(f"Formula {ctx.getText()}")

  def enterOperator(self, ctx):
    print(f"Operator {ctx.getText()}")

  def enterHighoperator(self, ctx):
    print(f"Operator {ctx.getText()}")

  def enterNumber(self, ctx):
    print(f"Number {ctx.getText()}")

def main(inputstream):
  lexer = MathLexer(inputstream)
  stream = CommonTokenStream(lexer)
  parser = MathParser(stream)
  tree = parser.formula()
  printer = MathPrintListener()
  walker = ParseTreeWalker()
  walker.walk(printer, tree)

if __name__ == '__main__':
  stream = InputStream("(10+20*30-40)/50;")
  main(stream)