from antlr4 import CommonTokenStream
from .antlr.PslVisitor import PslVisitor
from .antlr.PslLexer import PslLexer
from .antlr.PslParser import PslParser

from .visitor import Visitor


def parseSource(srcStream):
    lexer = PslLexer(srcStream)
    tokens = CommonTokenStream(lexer)
    parser = PslParser(tokens)
    visitor = Visitor()
    visitor.visit(parser.program())
    return visitor
