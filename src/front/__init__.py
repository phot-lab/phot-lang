from antlr4 import CommonTokenStream
from .antlr.PslLexer import PslLexer
from .antlr.PslParser import PslParser

from .visitor import PslVisitor


def parseSource(srcStream):
    lexer = PslLexer(srcStream)
    tokens = CommonTokenStream(lexer)
    parser = PslParser(tokens)
    visitor = PslVisitor()
    visitor.visit(parser.program())
    return visitor
