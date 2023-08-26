
// Generated from Psl.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  PslLexer : public antlr4::Lexer {
public:
  enum {
    T__0 = 1, T__1 = 2, T__2 = 3, T__3 = 4, T__4 = 5, T__5 = 6, T__6 = 7, 
    T__7 = 8, T__8 = 9, T__9 = 10, T__10 = 11, T__11 = 12, T__12 = 13, T__13 = 14, 
    T__14 = 15, T__15 = 16, T__16 = 17, T__17 = 18, T__18 = 19, AS = 20, 
    LET = 21, USE = 22, FUNC = 23, TYPE = 24, ENUM = 25, WITH = 26, RETURN = 27, 
    INNER = 28, SYNC = 29, SCOPED = 30, STATIC = 31, ATOMIC = 32, NULL_ = 33, 
    TRUE = 34, FALSE = 35, ANY_TYPE = 36, NUMBER_TYPE = 37, STRING_TYPE = 38, 
    BOOLEAN_TYPE = 39, FUNCTOR_TYPE = 40, BLOCK_TYPE = 41, INTEGER_TYPE = 42, 
    REAL_TYPE = 43, COMPLEX_TYPE = 44, ARRAY_TYPE = 45, MATRIX_TYPE = 46, 
    LIST_TYPE = 47, DICT_TYPE = 48, SKIP_ = 49, LINE_END = 50, MULTI_STR = 51, 
    IDENTIFIER = 52, UNIT = 53, STRING = 54, FSTRING = 55, INTEGER = 56, 
    REAL = 57
  };

  explicit PslLexer(antlr4::CharStream *input);

  ~PslLexer() override;


  std::string getGrammarFileName() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const std::vector<std::string>& getChannelNames() const override;

  const std::vector<std::string>& getModeNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;

  const antlr4::atn::ATN& getATN() const override;

  // By default the static state used to implement the lexer is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:

  // Individual action functions triggered by action() above.

  // Individual semantic predicate functions triggered by sempred() above.

};

