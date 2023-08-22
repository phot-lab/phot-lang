# Generated from Psl.g4 by ANTLR 4.13.0
from antlr4 import *

if "." in __name__:
    from .PslParser import PslParser
else:
    from PslParser import PslParser


# This class defines a complete listener for a parse tree produced by PslParser.
class PslListener(ParseTreeListener):

    # Enter a parse tree produced by PslParser#program.
    def enterProgram(self, ctx: PslParser.ProgramContext):
        pass

    # Exit a parse tree produced by PslParser#program.
    def exitProgram(self, ctx: PslParser.ProgramContext):
        pass

    # Enter a parse tree produced by PslParser#stmtList.
    def enterStmtList(self, ctx: PslParser.StmtListContext):
        pass

    # Exit a parse tree produced by PslParser#stmtList.
    def exitStmtList(self, ctx: PslParser.StmtListContext):
        pass

    # Enter a parse tree produced by PslParser#stmt.
    def enterStmt(self, ctx: PslParser.StmtContext):
        pass

    # Exit a parse tree produced by PslParser#stmt.
    def exitStmt(self, ctx: PslParser.StmtContext):
        pass

    # Enter a parse tree produced by PslParser#letStmt.
    def enterLetStmt(self, ctx: PslParser.LetStmtContext):
        pass

    # Exit a parse tree produced by PslParser#letStmt.
    def exitLetStmt(self, ctx: PslParser.LetStmtContext):
        pass

    # Enter a parse tree produced by PslParser#useStmt.
    def enterUseStmt(self, ctx: PslParser.UseStmtContext):
        pass

    # Exit a parse tree produced by PslParser#useStmt.
    def exitUseStmt(self, ctx: PslParser.UseStmtContext):
        pass

    # Enter a parse tree produced by PslParser#withDef.
    def enterWithDef(self, ctx: PslParser.WithDefContext):
        pass

    # Exit a parse tree produced by PslParser#withDef.
    def exitWithDef(self, ctx: PslParser.WithDefContext):
        pass

    # Enter a parse tree produced by PslParser#funcDef.
    def enterFuncDef(self, ctx: PslParser.FuncDefContext):
        pass

    # Exit a parse tree produced by PslParser#funcDef.
    def exitFuncDef(self, ctx: PslParser.FuncDefContext):
        pass

    # Enter a parse tree produced by PslParser#typeDef.
    def enterTypeDef(self, ctx: PslParser.TypeDefContext):
        pass

    # Exit a parse tree produced by PslParser#typeDef.
    def exitTypeDef(self, ctx: PslParser.TypeDefContext):
        pass

    # Enter a parse tree produced by PslParser#enumDef.
    def enterEnumDef(self, ctx: PslParser.EnumDefContext):
        pass

    # Exit a parse tree produced by PslParser#enumDef.
    def exitEnumDef(self, ctx: PslParser.EnumDefContext):
        pass

    # Enter a parse tree produced by PslParser#retStmt.
    def enterRetStmt(self, ctx: PslParser.RetStmtContext):
        pass

    # Exit a parse tree produced by PslParser#retStmt.
    def exitRetStmt(self, ctx: PslParser.RetStmtContext):
        pass

    # Enter a parse tree produced by PslParser#exprStmt.
    def enterExprStmt(self, ctx: PslParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by PslParser#exprStmt.
    def exitExprStmt(self, ctx: PslParser.ExprStmtContext):
        pass

    # Enter a parse tree produced by PslParser#carrier.
    def enterCarrier(self, ctx: PslParser.CarrierContext):
        pass

    # Exit a parse tree produced by PslParser#carrier.
    def exitCarrier(self, ctx: PslParser.CarrierContext):
        pass

    # Enter a parse tree produced by PslParser#biasAnno.
    def enterBiasAnno(self, ctx: PslParser.BiasAnnoContext):
        pass

    # Exit a parse tree produced by PslParser#biasAnno.
    def exitBiasAnno(self, ctx: PslParser.BiasAnnoContext):
        pass

    # Enter a parse tree produced by PslParser#sizeAnno.
    def enterSizeAnno(self, ctx: PslParser.SizeAnnoContext):
        pass

    # Exit a parse tree produced by PslParser#sizeAnno.
    def exitSizeAnno(self, ctx: PslParser.SizeAnnoContext):
        pass

    # Enter a parse tree produced by PslParser#annotation.
    def enterAnnotation(self, ctx: PslParser.AnnotationContext):
        pass

    # Exit a parse tree produced by PslParser#annotation.
    def exitAnnotation(self, ctx: PslParser.AnnotationContext):
        pass

    # Enter a parse tree produced by PslParser#annotations.
    def enterAnnotations(self, ctx: PslParser.AnnotationsContext):
        pass

    # Exit a parse tree produced by PslParser#annotations.
    def exitAnnotations(self, ctx: PslParser.AnnotationsContext):
        pass

    # Enter a parse tree produced by PslParser#modifiers.
    def enterModifiers(self, ctx: PslParser.ModifiersContext):
        pass

    # Exit a parse tree produced by PslParser#modifiers.
    def exitModifiers(self, ctx: PslParser.ModifiersContext):
        pass

    # Enter a parse tree produced by PslParser#withList.
    def enterWithList(self, ctx: PslParser.WithListContext):
        pass

    # Exit a parse tree produced by PslParser#withList.
    def exitWithList(self, ctx: PslParser.WithListContext):
        pass

    # Enter a parse tree produced by PslParser#withDecl.
    def enterWithDecl(self, ctx: PslParser.WithDeclContext):
        pass

    # Exit a parse tree produced by PslParser#withDecl.
    def exitWithDecl(self, ctx: PslParser.WithDeclContext):
        pass

    # Enter a parse tree produced by PslParser#paramDef.
    def enterParamDef(self, ctx: PslParser.ParamDefContext):
        pass

    # Exit a parse tree produced by PslParser#paramDef.
    def exitParamDef(self, ctx: PslParser.ParamDefContext):
        pass

    # Enter a parse tree produced by PslParser#argument.
    def enterArgument(self, ctx: PslParser.ArgumentContext):
        pass

    # Exit a parse tree produced by PslParser#argument.
    def exitArgument(self, ctx: PslParser.ArgumentContext):
        pass

    # Enter a parse tree produced by PslParser#typePack.
    def enterTypePack(self, ctx: PslParser.TypePackContext):
        pass

    # Exit a parse tree produced by PslParser#typePack.
    def exitTypePack(self, ctx: PslParser.TypePackContext):
        pass

    # Enter a parse tree produced by PslParser#keyValDecl.
    def enterKeyValDecl(self, ctx: PslParser.KeyValDeclContext):
        pass

    # Exit a parse tree produced by PslParser#keyValDecl.
    def exitKeyValDecl(self, ctx: PslParser.KeyValDeclContext):
        pass

    # Enter a parse tree produced by PslParser#keyValExpr.
    def enterKeyValExpr(self, ctx: PslParser.KeyValExprContext):
        pass

    # Exit a parse tree produced by PslParser#keyValExpr.
    def exitKeyValExpr(self, ctx: PslParser.KeyValExprContext):
        pass

    # Enter a parse tree produced by PslParser#entityRef.
    def enterEntityRef(self, ctx: PslParser.EntityRefContext):
        pass

    # Exit a parse tree produced by PslParser#entityRef.
    def exitEntityRef(self, ctx: PslParser.EntityRefContext):
        pass

    # Enter a parse tree produced by PslParser#listUnpack.
    def enterListUnpack(self, ctx: PslParser.ListUnpackContext):
        pass

    # Exit a parse tree produced by PslParser#listUnpack.
    def exitListUnpack(self, ctx: PslParser.ListUnpackContext):
        pass

    # Enter a parse tree produced by PslParser#dictUnpack.
    def enterDictUnpack(self, ctx: PslParser.DictUnpackContext):
        pass

    # Exit a parse tree produced by PslParser#dictUnpack.
    def exitDictUnpack(self, ctx: PslParser.DictUnpackContext):
        pass

    # Enter a parse tree produced by PslParser#dictPack.
    def enterDictPack(self, ctx: PslParser.DictPackContext):
        pass

    # Exit a parse tree produced by PslParser#dictPack.
    def exitDictPack(self, ctx: PslParser.DictPackContext):
        pass

    # Enter a parse tree produced by PslParser#listPack.
    def enterListPack(self, ctx: PslParser.ListPackContext):
        pass

    # Exit a parse tree produced by PslParser#listPack.
    def exitListPack(self, ctx: PslParser.ListPackContext):
        pass

    # Enter a parse tree produced by PslParser#stmtPack.
    def enterStmtPack(self, ctx: PslParser.StmtPackContext):
        pass

    # Exit a parse tree produced by PslParser#stmtPack.
    def exitStmtPack(self, ctx: PslParser.StmtPackContext):
        pass

    # Enter a parse tree produced by PslParser#entityExpr.
    def enterEntityExpr(self, ctx: PslParser.EntityExprContext):
        pass

    # Exit a parse tree produced by PslParser#entityExpr.
    def exitEntityExpr(self, ctx: PslParser.EntityExprContext):
        pass

    # Enter a parse tree produced by PslParser#entityChain.
    def enterEntityChain(self, ctx: PslParser.EntityChainContext):
        pass

    # Exit a parse tree produced by PslParser#entityChain.
    def exitEntityChain(self, ctx: PslParser.EntityChainContext):
        pass

    # Enter a parse tree produced by PslParser#chainUnit.
    def enterChainUnit(self, ctx: PslParser.ChainUnitContext):
        pass

    # Exit a parse tree produced by PslParser#chainUnit.
    def exitChainUnit(self, ctx: PslParser.ChainUnitContext):
        pass

    # Enter a parse tree produced by PslParser#entity.
    def enterEntity(self, ctx: PslParser.EntityContext):
        pass

    # Exit a parse tree produced by PslParser#entity.
    def exitEntity(self, ctx: PslParser.EntityContext):
        pass

    # Enter a parse tree produced by PslParser#linkCall.
    def enterLinkCall(self, ctx: PslParser.LinkCallContext):
        pass

    # Exit a parse tree produced by PslParser#linkCall.
    def exitLinkCall(self, ctx: PslParser.LinkCallContext):
        pass

    # Enter a parse tree produced by PslParser#functorRef.
    def enterFunctorRef(self, ctx: PslParser.FunctorRefContext):
        pass

    # Exit a parse tree produced by PslParser#functorRef.
    def exitFunctorRef(self, ctx: PslParser.FunctorRefContext):
        pass

    # Enter a parse tree produced by PslParser#stmtEnd.
    def enterStmtEnd(self, ctx: PslParser.StmtEndContext):
        pass

    # Exit a parse tree produced by PslParser#stmtEnd.
    def exitStmtEnd(self, ctx: PslParser.StmtEndContext):
        pass

    # Enter a parse tree produced by PslParser#sepMark.
    def enterSepMark(self, ctx: PslParser.SepMarkContext):
        pass

    # Exit a parse tree produced by PslParser#sepMark.
    def exitSepMark(self, ctx: PslParser.SepMarkContext):
        pass

    # Enter a parse tree produced by PslParser#argsList.
    def enterArgsList(self, ctx: PslParser.ArgsListContext):
        pass

    # Exit a parse tree produced by PslParser#argsList.
    def exitArgsList(self, ctx: PslParser.ArgsListContext):
        pass

    # Enter a parse tree produced by PslParser#literal.
    def enterLiteral(self, ctx: PslParser.LiteralContext):
        pass

    # Exit a parse tree produced by PslParser#literal.
    def exitLiteral(self, ctx: PslParser.LiteralContext):
        pass

    # Enter a parse tree produced by PslParser#value.
    def enterValue(self, ctx: PslParser.ValueContext):
        pass

    # Exit a parse tree produced by PslParser#value.
    def exitValue(self, ctx: PslParser.ValueContext):
        pass

    # Enter a parse tree produced by PslParser#formatStr.
    def enterFormatStr(self, ctx: PslParser.FormatStrContext):
        pass

    # Exit a parse tree produced by PslParser#formatStr.
    def exitFormatStr(self, ctx: PslParser.FormatStrContext):
        pass

    # Enter a parse tree produced by PslParser#complex.
    def enterComplex(self, ctx: PslParser.ComplexContext):
        pass

    # Exit a parse tree produced by PslParser#complex.
    def exitComplex(self, ctx: PslParser.ComplexContext):
        pass

    # Enter a parse tree produced by PslParser#type.
    def enterType(self, ctx: PslParser.TypeContext):
        pass

    # Exit a parse tree produced by PslParser#type.
    def exitType(self, ctx: PslParser.TypeContext):
        pass

    # Enter a parse tree produced by PslParser#innerType.
    def enterInnerType(self, ctx: PslParser.InnerTypeContext):
        pass

    # Exit a parse tree produced by PslParser#innerType.
    def exitInnerType(self, ctx: PslParser.InnerTypeContext):
        pass

    # Enter a parse tree produced by PslParser#numberType.
    def enterNumberType(self, ctx: PslParser.NumberTypeContext):
        pass

    # Exit a parse tree produced by PslParser#numberType.
    def exitNumberType(self, ctx: PslParser.NumberTypeContext):
        pass

    # Enter a parse tree produced by PslParser#scalarType.
    def enterScalarType(self, ctx: PslParser.ScalarTypeContext):
        pass

    # Exit a parse tree produced by PslParser#scalarType.
    def exitScalarType(self, ctx: PslParser.ScalarTypeContext):
        pass

    # Enter a parse tree produced by PslParser#vectorType.
    def enterVectorType(self, ctx: PslParser.VectorTypeContext):
        pass

    # Exit a parse tree produced by PslParser#vectorType.
    def exitVectorType(self, ctx: PslParser.VectorTypeContext):
        pass

    # Enter a parse tree produced by PslParser#structType.
    def enterStructType(self, ctx: PslParser.StructTypeContext):
        pass

    # Exit a parse tree produced by PslParser#structType.
    def exitStructType(self, ctx: PslParser.StructTypeContext):
        pass

    # Enter a parse tree produced by PslParser#nullableType.
    def enterNullableType(self, ctx: PslParser.NullableTypeContext):
        pass

    # Exit a parse tree produced by PslParser#nullableType.
    def exitNullableType(self, ctx: PslParser.NullableTypeContext):
        pass

    # Enter a parse tree produced by PslParser#identRef.
    def enterIdentRef(self, ctx: PslParser.IdentRefContext):
        pass

    # Exit a parse tree produced by PslParser#identRef.
    def exitIdentRef(self, ctx: PslParser.IdentRefContext):
        pass


del PslParser
