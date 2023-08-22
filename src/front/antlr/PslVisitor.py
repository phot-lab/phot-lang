# Generated from Psl.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .PslParser import PslParser
else:
    from PslParser import PslParser

# This class defines a complete generic visitor for a parse tree produced by PslParser.

class PslVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PslParser#program.
    def visitProgram(self, ctx:PslParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#stmtList.
    def visitStmtList(self, ctx:PslParser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#stmt.
    def visitStmt(self, ctx:PslParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#letStmt.
    def visitLetStmt(self, ctx:PslParser.LetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#useStmt.
    def visitUseStmt(self, ctx:PslParser.UseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#withDef.
    def visitWithDef(self, ctx:PslParser.WithDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#funcDef.
    def visitFuncDef(self, ctx:PslParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#typeDef.
    def visitTypeDef(self, ctx:PslParser.TypeDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#enumDef.
    def visitEnumDef(self, ctx:PslParser.EnumDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#retStmt.
    def visitRetStmt(self, ctx:PslParser.RetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#exprStmt.
    def visitExprStmt(self, ctx:PslParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#carrier.
    def visitCarrier(self, ctx:PslParser.CarrierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#biasAnno.
    def visitBiasAnno(self, ctx:PslParser.BiasAnnoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#sizeAnno.
    def visitSizeAnno(self, ctx:PslParser.SizeAnnoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#annotation.
    def visitAnnotation(self, ctx:PslParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#annotations.
    def visitAnnotations(self, ctx:PslParser.AnnotationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#modifiers.
    def visitModifiers(self, ctx:PslParser.ModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#withList.
    def visitWithList(self, ctx:PslParser.WithListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#withDecl.
    def visitWithDecl(self, ctx:PslParser.WithDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#paramDef.
    def visitParamDef(self, ctx:PslParser.ParamDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#argument.
    def visitArgument(self, ctx:PslParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#typePack.
    def visitTypePack(self, ctx:PslParser.TypePackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#keyValDecl.
    def visitKeyValDecl(self, ctx:PslParser.KeyValDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#keyValExpr.
    def visitKeyValExpr(self, ctx:PslParser.KeyValExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#entityRef.
    def visitEntityRef(self, ctx:PslParser.EntityRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#listUnpack.
    def visitListUnpack(self, ctx:PslParser.ListUnpackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#dictUnpack.
    def visitDictUnpack(self, ctx:PslParser.DictUnpackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#dictPack.
    def visitDictPack(self, ctx:PslParser.DictPackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#listPack.
    def visitListPack(self, ctx:PslParser.ListPackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#stmtPack.
    def visitStmtPack(self, ctx:PslParser.StmtPackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#entityExpr.
    def visitEntityExpr(self, ctx:PslParser.EntityExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#entityChain.
    def visitEntityChain(self, ctx:PslParser.EntityChainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#chainUnit.
    def visitChainUnit(self, ctx:PslParser.ChainUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#entity.
    def visitEntity(self, ctx:PslParser.EntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#linkCall.
    def visitLinkCall(self, ctx:PslParser.LinkCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#functorRef.
    def visitFunctorRef(self, ctx:PslParser.FunctorRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#stmtEnd.
    def visitStmtEnd(self, ctx:PslParser.StmtEndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#sepMark.
    def visitSepMark(self, ctx:PslParser.SepMarkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#argsList.
    def visitArgsList(self, ctx:PslParser.ArgsListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#literal.
    def visitLiteral(self, ctx:PslParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#value.
    def visitValue(self, ctx:PslParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#formatStr.
    def visitFormatStr(self, ctx:PslParser.FormatStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#complex.
    def visitComplex(self, ctx:PslParser.ComplexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#type.
    def visitType(self, ctx:PslParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#innerType.
    def visitInnerType(self, ctx:PslParser.InnerTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#numberType.
    def visitNumberType(self, ctx:PslParser.NumberTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#scalarType.
    def visitScalarType(self, ctx:PslParser.ScalarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#vectorType.
    def visitVectorType(self, ctx:PslParser.VectorTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#structType.
    def visitStructType(self, ctx:PslParser.StructTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#nullableType.
    def visitNullableType(self, ctx:PslParser.NullableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PslParser#identRef.
    def visitIdentRef(self, ctx:PslParser.IdentRefContext):
        return self.visitChildren(ctx)



del PslParser