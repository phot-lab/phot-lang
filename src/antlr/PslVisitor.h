
// Generated from Psl.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "PslParser.h"



/**
 * This class defines an abstract visitor for a parse tree
 * produced by PslParser.
 */
class  PslVisitor : public antlr4::tree::AbstractParseTreeVisitor {
public:

  /**
   * Visit parse trees produced by PslParser.
   */
    virtual std::any visitProgram(PslParser::ProgramContext *context) = 0;

    virtual std::any visitStmtList(PslParser::StmtListContext *context) = 0;

    virtual std::any visitStmt(PslParser::StmtContext *context) = 0;

    virtual std::any visitLetStmt(PslParser::LetStmtContext *context) = 0;

    virtual std::any visitUseStmt(PslParser::UseStmtContext *context) = 0;

    virtual std::any visitWithDef(PslParser::WithDefContext *context) = 0;

    virtual std::any visitFuncDef(PslParser::FuncDefContext *context) = 0;

    virtual std::any visitTypeDef(PslParser::TypeDefContext *context) = 0;

    virtual std::any visitEnumDef(PslParser::EnumDefContext *context) = 0;

    virtual std::any visitRetStmt(PslParser::RetStmtContext *context) = 0;

    virtual std::any visitExprStmt(PslParser::ExprStmtContext *context) = 0;

    virtual std::any visitCarrier(PslParser::CarrierContext *context) = 0;

    virtual std::any visitBiasAnno(PslParser::BiasAnnoContext *context) = 0;

    virtual std::any visitSizeAnno(PslParser::SizeAnnoContext *context) = 0;

    virtual std::any visitAnnotation(PslParser::AnnotationContext *context) = 0;

    virtual std::any visitAnnotations(PslParser::AnnotationsContext *context) = 0;

    virtual std::any visitModifiers(PslParser::ModifiersContext *context) = 0;

    virtual std::any visitWithList(PslParser::WithListContext *context) = 0;

    virtual std::any visitWithDecl(PslParser::WithDeclContext *context) = 0;

    virtual std::any visitParamDef(PslParser::ParamDefContext *context) = 0;

    virtual std::any visitArgsList(PslParser::ArgsListContext *context) = 0;

    virtual std::any visitArgument(PslParser::ArgumentContext *context) = 0;

    virtual std::any visitTypePack(PslParser::TypePackContext *context) = 0;

    virtual std::any visitKeyValDecl(PslParser::KeyValDeclContext *context) = 0;

    virtual std::any visitKeyValExpr(PslParser::KeyValExprContext *context) = 0;

    virtual std::any visitEntityRef(PslParser::EntityRefContext *context) = 0;

    virtual std::any visitFunctorRef(PslParser::FunctorRefContext *context) = 0;

    virtual std::any visitListUnpack(PslParser::ListUnpackContext *context) = 0;

    virtual std::any visitDictUnpack(PslParser::DictUnpackContext *context) = 0;

    virtual std::any visitDictPack(PslParser::DictPackContext *context) = 0;

    virtual std::any visitListPack(PslParser::ListPackContext *context) = 0;

    virtual std::any visitStmtPack(PslParser::StmtPackContext *context) = 0;

    virtual std::any visitEntityExpr(PslParser::EntityExprContext *context) = 0;

    virtual std::any visitEntityChain(PslParser::EntityChainContext *context) = 0;

    virtual std::any visitEntity(PslParser::EntityContext *context) = 0;

    virtual std::any visitNormCall(PslParser::NormCallContext *context) = 0;

    virtual std::any visitLinkCall(PslParser::LinkCallContext *context) = 0;

    virtual std::any visitStmtEnd(PslParser::StmtEndContext *context) = 0;

    virtual std::any visitSepMark(PslParser::SepMarkContext *context) = 0;

    virtual std::any visitLiteral(PslParser::LiteralContext *context) = 0;

    virtual std::any visitValue(PslParser::ValueContext *context) = 0;

    virtual std::any visitType(PslParser::TypeContext *context) = 0;

    virtual std::any visitInnerType(PslParser::InnerTypeContext *context) = 0;

    virtual std::any visitNumberType(PslParser::NumberTypeContext *context) = 0;

    virtual std::any visitScalarType(PslParser::ScalarTypeContext *context) = 0;

    virtual std::any visitComplex(PslParser::ComplexContext *context) = 0;

    virtual std::any visitVectorType(PslParser::VectorTypeContext *context) = 0;

    virtual std::any visitStructType(PslParser::StructTypeContext *context) = 0;

    virtual std::any visitNullableType(PslParser::NullableTypeContext *context) = 0;

    virtual std::any visitIdentRef(PslParser::IdentRefContext *context) = 0;


};

