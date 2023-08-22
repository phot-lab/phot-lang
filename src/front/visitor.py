from antlr4 import ParseTreeVisitor
from .antlr.PslParser import PslParser


class PslVisitor(ParseTreeVisitor):
    def visitProgram(self, ctx: PslParser.ProgramContext):
        stmt_list = ctx.getChild(0)
        if stmt_list is None:
            return
        stmt_list.accept(self)

    def visitStmtList(self, ctx: PslParser.StmtListContext):
        for child in ctx.getChildren():
            child.accept(self)

    def visitStmt(self, ctx: PslParser.StmtContext):
        ctx.getChild(0).accept(self)

    def visitFuncDef(self, ctx: PslParser.FuncDefContext):
        print('func')

    def visitLetStmt(self, ctx: PslParser.LetStmtContext):
        print('let')
