
// Generated from Psl.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"
#include "PslVisitor.h"


/**
 * This class provides an empty implementation of PslVisitor, which can be
 * extended to create a visitor which only needs to handle a subset of the available methods.
 */
class  PslBaseVisitor : public PslVisitor {
public:

  virtual std::any visitProgram(PslParser::ProgramContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitStmtList(PslParser::StmtListContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitStmt(PslParser::StmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLetStmt(PslParser::LetStmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitUseStmt(PslParser::UseStmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitWithDef(PslParser::WithDefContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFuncDef(PslParser::FuncDefContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTypeDef(PslParser::TypeDefContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitEnumDef(PslParser::EnumDefContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitRetStmt(PslParser::RetStmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitExprStmt(PslParser::ExprStmtContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitCarrier(PslParser::CarrierContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitBiasAnno(PslParser::BiasAnnoContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSizeAnno(PslParser::SizeAnnoContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAnnotation(PslParser::AnnotationContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitAnnotations(PslParser::AnnotationsContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitModifiers(PslParser::ModifiersContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitWithList(PslParser::WithListContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitWithDecl(PslParser::WithDeclContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitParamDef(PslParser::ParamDefContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitArgsList(PslParser::ArgsListContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitArgument(PslParser::ArgumentContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitTypePack(PslParser::TypePackContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitKeyValDecl(PslParser::KeyValDeclContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitKeyValExpr(PslParser::KeyValExprContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitEntityRef(PslParser::EntityRefContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitFunctorRef(PslParser::FunctorRefContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitListUnpack(PslParser::ListUnpackContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDictUnpack(PslParser::DictUnpackContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitDictPack(PslParser::DictPackContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitListPack(PslParser::ListPackContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitStmtPack(PslParser::StmtPackContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitEntityExpr(PslParser::EntityExprContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitEntityChain(PslParser::EntityChainContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitEntity(PslParser::EntityContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNormCall(PslParser::NormCallContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLinkCall(PslParser::LinkCallContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitStmtEnd(PslParser::StmtEndContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitSepMark(PslParser::SepMarkContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitLiteral(PslParser::LiteralContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitValue(PslParser::ValueContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitType(PslParser::TypeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitInnerType(PslParser::InnerTypeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNumberType(PslParser::NumberTypeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitScalarType(PslParser::ScalarTypeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitComplex(PslParser::ComplexContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitVectorType(PslParser::VectorTypeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitStructType(PslParser::StructTypeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitNullableType(PslParser::NullableTypeContext *ctx) override {
    return visitChildren(ctx);
  }

  virtual std::any visitIdentRef(PslParser::IdentRefContext *ctx) override {
    return visitChildren(ctx);
  }


};

