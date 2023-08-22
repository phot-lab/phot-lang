from .antlr.PslParser import PslParser
from .antlr.PslVisitor import PslVisitor


class Visitor(PslVisitor):
    def visitProgram(self, ctx: PslParser.ProgramContext):
        stmt_list = ctx.stmtList()
        res = self.visit(stmt_list)

    def visitStmtList(self, ctx: PslParser.StmtListContext):
        stmt_list = ctx.getChildren()
        for stmt in stmt_list:
            self.visit(stmt)

    def visitStmt(self, ctx: PslParser.StmtContext):
        stmt = ctx.getText()
        print(stmt)