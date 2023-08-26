
// Generated from Psl.g4 by ANTLR 4.13.0


#include "PslVisitor.h"

#include "PslParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct PslParserStaticData final {
  PslParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  PslParserStaticData(const PslParserStaticData&) = delete;
  PslParserStaticData(PslParserStaticData&&) = delete;
  PslParserStaticData& operator=(const PslParserStaticData&) = delete;
  PslParserStaticData& operator=(PslParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag pslParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
PslParserStaticData *pslParserStaticData = nullptr;

void pslParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (pslParserStaticData != nullptr) {
    return;
  }
#else
  assert(pslParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<PslParserStaticData>(
    std::vector<std::string>{
      "program", "stmtList", "stmt", "letStmt", "useStmt", "withDef", "funcDef", 
      "typeDef", "enumDef", "retStmt", "exprStmt", "carrier", "biasAnno", 
      "sizeAnno", "annotation", "annotations", "modifiers", "withList", 
      "withDecl", "paramDef", "argsList", "argument", "typePack", "keyValDecl", 
      "keyValExpr", "entityRef", "functorRef", "listUnpack", "dictUnpack", 
      "dictPack", "listPack", "stmtPack", "entityExpr", "entityChain", "entity", 
      "normCall", "linkCall", "stmtEnd", "sepMark", "literal", "value", 
      "type", "innerType", "numberType", "scalarType", "complex", "vectorType", 
      "structType", "nullableType", "identRef"
    },
    std::vector<std::string>{
      "", "':'", "'='", "'('", "','", "')'", "'['", "']'", "'@'", "'<'", 
      "'>'", "'{'", "'}'", "'.'", "'->'", "';'", "'+'", "'-'", "'i'", "'\\u003F'", 
      "'as'", "'let'", "'use'", "'func'", "'type'", "'enum'", "'with'", 
      "'return'", "'inner'", "'sync'", "'scoped'", "'static'", "'atomic'", 
      "'null'", "'true'", "'false'", "'any'", "'number'", "'string'", "'bool'", 
      "'functor'", "'block'", "'int'", "'real'", "'complex'", "'array'", 
      "'matrix'", "'list'", "'dict'"
    },
    std::vector<std::string>{
      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
      "", "", "", "AS", "LET", "USE", "FUNC", "TYPE", "ENUM", "WITH", "RETURN", 
      "INNER", "SYNC", "SCOPED", "STATIC", "ATOMIC", "NULL", "TRUE", "FALSE", 
      "ANY_TYPE", "NUMBER_TYPE", "STRING_TYPE", "BOOLEAN_TYPE", "FUNCTOR_TYPE", 
      "BLOCK_TYPE", "INTEGER_TYPE", "REAL_TYPE", "COMPLEX_TYPE", "ARRAY_TYPE", 
      "MATRIX_TYPE", "LIST_TYPE", "DICT_TYPE", "SKIP_", "LINE_END", "MULTI_STR", 
      "IDENTIFIER", "UNIT", "STRING", "FSTRING", "INTEGER", "REAL"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,57,671,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,7,33,2,34,7,34,2,35,7,
  	35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,2,40,7,40,2,41,7,41,2,42,7,
  	42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,
  	49,1,0,3,0,102,8,0,1,1,3,1,105,8,1,1,1,4,1,108,8,1,11,1,12,1,109,1,2,
  	1,2,1,2,1,2,1,2,1,2,1,2,3,2,119,8,2,1,3,1,3,1,3,1,3,3,3,125,8,3,1,3,3,
  	3,128,8,3,1,3,1,3,1,3,1,4,1,4,1,4,3,4,136,8,4,1,4,1,4,1,4,1,5,1,5,1,5,
  	3,5,144,8,5,1,5,3,5,147,8,5,1,6,1,6,3,6,151,8,6,1,6,1,6,1,6,1,6,1,6,1,
  	6,3,6,159,8,6,1,6,3,6,162,8,6,1,6,3,6,165,8,6,1,6,1,6,1,6,1,7,1,7,1,7,
  	3,7,173,8,7,1,7,1,7,3,7,177,8,7,1,7,1,7,1,8,1,8,1,8,3,8,184,8,8,1,8,1,
  	8,1,8,1,9,1,9,3,9,191,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
  	3,11,202,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
  	1,13,1,14,1,14,1,14,1,14,1,14,3,14,221,8,14,1,15,1,15,1,15,5,15,226,8,
  	15,10,15,12,15,229,9,15,1,16,5,16,232,8,16,10,16,12,16,235,9,16,1,17,
  	1,17,3,17,239,8,17,1,17,1,17,1,17,3,17,244,8,17,1,17,5,17,247,8,17,10,
  	17,12,17,250,9,17,1,17,3,17,253,8,17,1,17,1,17,1,18,1,18,3,18,259,8,18,
  	1,18,1,18,1,18,3,18,264,8,18,1,18,5,18,267,8,18,10,18,12,18,270,9,18,
  	1,18,3,18,273,8,18,1,18,1,18,1,19,1,19,3,19,279,8,19,1,19,1,19,1,19,3,
  	19,284,8,19,1,19,5,19,287,8,19,10,19,12,19,290,9,19,3,19,292,8,19,1,19,
  	3,19,295,8,19,1,19,1,19,1,20,1,20,3,20,301,8,20,1,20,1,20,1,20,3,20,306,
  	8,20,1,20,5,20,309,8,20,10,20,12,20,312,9,20,3,20,314,8,20,1,20,3,20,
  	317,8,20,1,20,1,20,1,21,1,21,1,21,1,21,3,21,325,8,21,1,22,1,22,3,22,329,
  	8,22,1,22,1,22,1,22,3,22,334,8,22,1,22,5,22,337,8,22,10,22,12,22,340,
  	9,22,3,22,342,8,22,1,22,3,22,345,8,22,1,22,1,22,1,23,1,23,3,23,351,8,
  	23,1,23,1,23,1,23,1,23,3,23,357,8,23,1,24,1,24,1,24,1,24,1,25,1,25,1,
  	25,1,25,3,25,367,8,25,5,25,369,8,25,10,25,12,25,372,9,25,1,25,3,25,375,
  	8,25,1,26,1,26,3,26,379,8,26,1,26,3,26,382,8,26,1,27,1,27,3,27,386,8,
  	27,1,27,1,27,1,27,3,27,391,8,27,1,27,5,27,394,8,27,10,27,12,27,397,9,
  	27,3,27,399,8,27,1,27,3,27,402,8,27,1,27,1,27,1,28,1,28,3,28,408,8,28,
  	1,28,1,28,1,28,3,28,413,8,28,1,28,5,28,416,8,28,10,28,12,28,419,9,28,
  	3,28,421,8,28,1,28,3,28,424,8,28,1,28,1,28,1,29,1,29,3,29,430,8,29,1,
  	29,1,29,1,29,3,29,435,8,29,1,29,5,29,438,8,29,10,29,12,29,441,9,29,3,
  	29,443,8,29,1,29,3,29,446,8,29,1,29,1,29,1,30,1,30,3,30,452,8,30,1,30,
  	1,30,1,30,3,30,457,8,30,1,30,5,30,460,8,30,10,30,12,30,463,9,30,3,30,
  	465,8,30,1,30,3,30,468,8,30,1,30,1,30,1,31,1,31,3,31,474,8,31,1,31,3,
  	31,477,8,31,1,31,1,31,1,32,1,32,1,32,1,32,3,32,485,8,32,1,32,1,32,3,32,
  	489,8,32,1,33,1,33,1,33,4,33,494,8,33,11,33,12,33,495,1,34,1,34,1,34,
  	1,34,3,34,502,8,34,1,34,3,34,505,8,34,1,34,1,34,3,34,509,8,34,1,35,1,
  	35,1,35,1,36,1,36,1,36,1,36,1,36,1,36,3,36,520,8,36,1,36,1,36,1,36,1,
  	36,1,36,3,36,527,8,36,1,36,1,36,1,36,1,36,1,36,3,36,534,8,36,1,36,1,36,
  	1,36,1,36,1,36,1,36,3,36,542,8,36,5,36,544,8,36,10,36,12,36,547,9,36,
  	1,37,1,37,1,37,3,37,552,8,37,1,38,4,38,555,8,38,11,38,12,38,556,1,39,
  	1,39,1,39,1,39,1,39,1,39,1,39,3,39,566,8,39,1,40,1,40,1,40,3,40,571,8,
  	40,1,40,3,40,574,8,40,1,41,1,41,1,41,3,41,579,8,41,1,42,1,42,1,42,1,42,
  	1,42,1,42,1,42,3,42,588,8,42,1,43,1,43,3,43,592,8,43,1,44,1,44,1,45,1,
  	45,1,45,1,45,1,45,1,45,1,45,1,45,3,45,604,8,45,1,46,1,46,1,46,1,46,1,
  	46,3,46,611,8,46,1,46,1,46,1,46,3,46,616,8,46,1,46,1,46,1,46,1,46,1,46,
  	3,46,623,8,46,1,46,1,46,1,46,5,46,628,8,46,10,46,12,46,631,9,46,3,46,
  	633,8,46,1,47,1,47,1,47,1,47,1,47,5,47,640,8,47,10,47,12,47,643,9,47,
  	1,47,1,47,3,47,647,8,47,1,47,1,47,1,47,3,47,652,8,47,1,47,1,47,1,47,1,
  	47,1,47,1,47,1,47,3,47,661,8,47,3,47,663,8,47,1,48,1,48,3,48,667,8,48,
  	1,49,1,49,1,49,0,1,72,50,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
  	34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
  	80,82,84,86,88,90,92,94,96,98,0,3,1,0,28,32,1,0,42,44,1,0,16,17,766,0,
  	101,1,0,0,0,2,107,1,0,0,0,4,118,1,0,0,0,6,120,1,0,0,0,8,132,1,0,0,0,10,
  	140,1,0,0,0,12,148,1,0,0,0,14,169,1,0,0,0,16,180,1,0,0,0,18,188,1,0,0,
  	0,20,194,1,0,0,0,22,201,1,0,0,0,24,203,1,0,0,0,26,209,1,0,0,0,28,215,
  	1,0,0,0,30,227,1,0,0,0,32,233,1,0,0,0,34,236,1,0,0,0,36,256,1,0,0,0,38,
  	276,1,0,0,0,40,298,1,0,0,0,42,324,1,0,0,0,44,326,1,0,0,0,46,348,1,0,0,
  	0,48,358,1,0,0,0,50,362,1,0,0,0,52,376,1,0,0,0,54,383,1,0,0,0,56,405,
  	1,0,0,0,58,427,1,0,0,0,60,449,1,0,0,0,62,471,1,0,0,0,64,484,1,0,0,0,66,
  	493,1,0,0,0,68,508,1,0,0,0,70,510,1,0,0,0,72,533,1,0,0,0,74,551,1,0,0,
  	0,76,554,1,0,0,0,78,565,1,0,0,0,80,570,1,0,0,0,82,578,1,0,0,0,84,587,
  	1,0,0,0,86,591,1,0,0,0,88,593,1,0,0,0,90,603,1,0,0,0,92,632,1,0,0,0,94,
  	662,1,0,0,0,96,664,1,0,0,0,98,668,1,0,0,0,100,102,3,2,1,0,101,100,1,0,
  	0,0,101,102,1,0,0,0,102,1,1,0,0,0,103,105,3,76,38,0,104,103,1,0,0,0,104,
  	105,1,0,0,0,105,106,1,0,0,0,106,108,3,4,2,0,107,104,1,0,0,0,108,109,1,
  	0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,3,1,0,0,0,111,119,3,6,3,0,112,
  	119,3,8,4,0,113,119,3,12,6,0,114,119,3,14,7,0,115,119,3,16,8,0,116,119,
  	3,18,9,0,117,119,3,20,10,0,118,111,1,0,0,0,118,112,1,0,0,0,118,113,1,
  	0,0,0,118,114,1,0,0,0,118,115,1,0,0,0,118,116,1,0,0,0,118,117,1,0,0,0,
  	119,5,1,0,0,0,120,121,5,21,0,0,121,124,3,22,11,0,122,123,5,1,0,0,123,
  	125,3,82,41,0,124,122,1,0,0,0,124,125,1,0,0,0,125,127,1,0,0,0,126,128,
  	5,2,0,0,127,126,1,0,0,0,127,128,1,0,0,0,128,129,1,0,0,0,129,130,3,64,
  	32,0,130,131,3,74,37,0,131,7,1,0,0,0,132,133,5,22,0,0,133,135,3,22,11,
  	0,134,136,5,2,0,0,135,134,1,0,0,0,135,136,1,0,0,0,136,137,1,0,0,0,137,
  	138,3,64,32,0,138,139,3,74,37,0,139,9,1,0,0,0,140,143,5,26,0,0,141,144,
  	3,50,25,0,142,144,3,36,18,0,143,141,1,0,0,0,143,142,1,0,0,0,144,146,1,
  	0,0,0,145,147,5,50,0,0,146,145,1,0,0,0,146,147,1,0,0,0,147,11,1,0,0,0,
  	148,150,3,30,15,0,149,151,3,10,5,0,150,149,1,0,0,0,150,151,1,0,0,0,151,
  	152,1,0,0,0,152,153,3,32,16,0,153,154,5,23,0,0,154,155,3,98,49,0,155,
  	158,3,38,19,0,156,157,5,1,0,0,157,159,3,82,41,0,158,156,1,0,0,0,158,159,
  	1,0,0,0,159,161,1,0,0,0,160,162,5,2,0,0,161,160,1,0,0,0,161,162,1,0,0,
  	0,162,164,1,0,0,0,163,165,5,50,0,0,164,163,1,0,0,0,164,165,1,0,0,0,165,
  	166,1,0,0,0,166,167,3,62,31,0,167,168,3,74,37,0,168,13,1,0,0,0,169,170,
  	5,24,0,0,170,172,3,98,49,0,171,173,5,2,0,0,172,171,1,0,0,0,172,173,1,
  	0,0,0,173,176,1,0,0,0,174,177,3,82,41,0,175,177,3,44,22,0,176,174,1,0,
  	0,0,176,175,1,0,0,0,177,178,1,0,0,0,178,179,3,74,37,0,179,15,1,0,0,0,
  	180,181,5,25,0,0,181,183,3,98,49,0,182,184,5,2,0,0,183,182,1,0,0,0,183,
  	184,1,0,0,0,184,185,1,0,0,0,185,186,3,56,28,0,186,187,3,74,37,0,187,17,
  	1,0,0,0,188,190,5,27,0,0,189,191,3,64,32,0,190,189,1,0,0,0,190,191,1,
  	0,0,0,191,192,1,0,0,0,192,193,3,74,37,0,193,19,1,0,0,0,194,195,3,30,15,
  	0,195,196,3,64,32,0,196,197,3,74,37,0,197,21,1,0,0,0,198,202,3,98,49,
  	0,199,202,3,54,27,0,200,202,3,56,28,0,201,198,1,0,0,0,201,199,1,0,0,0,
  	201,200,1,0,0,0,202,23,1,0,0,0,203,204,5,3,0,0,204,205,5,56,0,0,205,206,
  	5,4,0,0,206,207,5,56,0,0,207,208,5,5,0,0,208,25,1,0,0,0,209,210,5,6,0,
  	0,210,211,5,56,0,0,211,212,5,4,0,0,212,213,5,56,0,0,213,214,5,7,0,0,214,
  	27,1,0,0,0,215,220,5,8,0,0,216,221,3,98,49,0,217,221,3,58,29,0,218,221,
  	3,24,12,0,219,221,3,26,13,0,220,216,1,0,0,0,220,217,1,0,0,0,220,218,1,
  	0,0,0,220,219,1,0,0,0,221,29,1,0,0,0,222,223,3,28,14,0,223,224,5,50,0,
  	0,224,226,1,0,0,0,225,222,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,
  	228,1,0,0,0,228,31,1,0,0,0,229,227,1,0,0,0,230,232,7,0,0,0,231,230,1,
  	0,0,0,232,235,1,0,0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,33,1,0,0,0,
  	235,233,1,0,0,0,236,238,5,9,0,0,237,239,3,76,38,0,238,237,1,0,0,0,238,
  	239,1,0,0,0,239,240,1,0,0,0,240,248,3,42,21,0,241,243,5,4,0,0,242,244,
  	3,76,38,0,243,242,1,0,0,0,243,244,1,0,0,0,244,245,1,0,0,0,245,247,3,42,
  	21,0,246,241,1,0,0,0,247,250,1,0,0,0,248,246,1,0,0,0,248,249,1,0,0,0,
  	249,252,1,0,0,0,250,248,1,0,0,0,251,253,3,76,38,0,252,251,1,0,0,0,252,
  	253,1,0,0,0,253,254,1,0,0,0,254,255,5,10,0,0,255,35,1,0,0,0,256,258,5,
  	9,0,0,257,259,3,76,38,0,258,257,1,0,0,0,258,259,1,0,0,0,259,260,1,0,0,
  	0,260,268,3,46,23,0,261,263,5,4,0,0,262,264,3,76,38,0,263,262,1,0,0,0,
  	263,264,1,0,0,0,264,265,1,0,0,0,265,267,3,46,23,0,266,261,1,0,0,0,267,
  	270,1,0,0,0,268,266,1,0,0,0,268,269,1,0,0,0,269,272,1,0,0,0,270,268,1,
  	0,0,0,271,273,3,76,38,0,272,271,1,0,0,0,272,273,1,0,0,0,273,274,1,0,0,
  	0,274,275,5,10,0,0,275,37,1,0,0,0,276,278,5,3,0,0,277,279,3,76,38,0,278,
  	277,1,0,0,0,278,279,1,0,0,0,279,291,1,0,0,0,280,288,3,46,23,0,281,283,
  	5,4,0,0,282,284,3,76,38,0,283,282,1,0,0,0,283,284,1,0,0,0,284,285,1,0,
  	0,0,285,287,3,46,23,0,286,281,1,0,0,0,287,290,1,0,0,0,288,286,1,0,0,0,
  	288,289,1,0,0,0,289,292,1,0,0,0,290,288,1,0,0,0,291,280,1,0,0,0,291,292,
  	1,0,0,0,292,294,1,0,0,0,293,295,3,76,38,0,294,293,1,0,0,0,294,295,1,0,
  	0,0,295,296,1,0,0,0,296,297,5,5,0,0,297,39,1,0,0,0,298,300,5,3,0,0,299,
  	301,3,76,38,0,300,299,1,0,0,0,300,301,1,0,0,0,301,313,1,0,0,0,302,310,
  	3,42,21,0,303,305,5,4,0,0,304,306,3,76,38,0,305,304,1,0,0,0,305,306,1,
  	0,0,0,306,307,1,0,0,0,307,309,3,42,21,0,308,303,1,0,0,0,309,312,1,0,0,
  	0,310,308,1,0,0,0,310,311,1,0,0,0,311,314,1,0,0,0,312,310,1,0,0,0,313,
  	302,1,0,0,0,313,314,1,0,0,0,314,316,1,0,0,0,315,317,3,76,38,0,316,315,
  	1,0,0,0,316,317,1,0,0,0,317,318,1,0,0,0,318,319,5,5,0,0,319,41,1,0,0,
  	0,320,325,3,98,49,0,321,325,3,68,34,0,322,325,3,48,24,0,323,325,3,64,
  	32,0,324,320,1,0,0,0,324,321,1,0,0,0,324,322,1,0,0,0,324,323,1,0,0,0,
  	325,43,1,0,0,0,326,328,5,11,0,0,327,329,3,76,38,0,328,327,1,0,0,0,328,
  	329,1,0,0,0,329,341,1,0,0,0,330,338,3,46,23,0,331,333,5,4,0,0,332,334,
  	3,76,38,0,333,332,1,0,0,0,333,334,1,0,0,0,334,335,1,0,0,0,335,337,3,46,
  	23,0,336,331,1,0,0,0,337,340,1,0,0,0,338,336,1,0,0,0,338,339,1,0,0,0,
  	339,342,1,0,0,0,340,338,1,0,0,0,341,330,1,0,0,0,341,342,1,0,0,0,342,344,
  	1,0,0,0,343,345,3,76,38,0,344,343,1,0,0,0,344,345,1,0,0,0,345,346,1,0,
  	0,0,346,347,5,12,0,0,347,45,1,0,0,0,348,350,3,98,49,0,349,351,3,28,14,
  	0,350,349,1,0,0,0,350,351,1,0,0,0,351,352,1,0,0,0,352,353,5,1,0,0,353,
  	356,3,96,48,0,354,355,5,2,0,0,355,357,3,64,32,0,356,354,1,0,0,0,356,357,
  	1,0,0,0,357,47,1,0,0,0,358,359,3,98,49,0,359,360,5,2,0,0,360,361,3,64,
  	32,0,361,49,1,0,0,0,362,370,3,98,49,0,363,366,5,13,0,0,364,367,5,56,0,
  	0,365,367,3,98,49,0,366,364,1,0,0,0,366,365,1,0,0,0,367,369,1,0,0,0,368,
  	363,1,0,0,0,369,372,1,0,0,0,370,368,1,0,0,0,370,371,1,0,0,0,371,374,1,
  	0,0,0,372,370,1,0,0,0,373,375,3,28,14,0,374,373,1,0,0,0,374,375,1,0,0,
  	0,375,51,1,0,0,0,376,378,3,98,49,0,377,379,3,34,17,0,378,377,1,0,0,0,
  	378,379,1,0,0,0,379,381,1,0,0,0,380,382,3,28,14,0,381,380,1,0,0,0,381,
  	382,1,0,0,0,382,53,1,0,0,0,383,385,5,6,0,0,384,386,3,76,38,0,385,384,
  	1,0,0,0,385,386,1,0,0,0,386,398,1,0,0,0,387,395,3,98,49,0,388,390,5,4,
  	0,0,389,391,3,76,38,0,390,389,1,0,0,0,390,391,1,0,0,0,391,392,1,0,0,0,
  	392,394,3,98,49,0,393,388,1,0,0,0,394,397,1,0,0,0,395,393,1,0,0,0,395,
  	396,1,0,0,0,396,399,1,0,0,0,397,395,1,0,0,0,398,387,1,0,0,0,398,399,1,
  	0,0,0,399,401,1,0,0,0,400,402,3,76,38,0,401,400,1,0,0,0,401,402,1,0,0,
  	0,402,403,1,0,0,0,403,404,5,7,0,0,404,55,1,0,0,0,405,407,5,11,0,0,406,
  	408,3,76,38,0,407,406,1,0,0,0,407,408,1,0,0,0,408,420,1,0,0,0,409,417,
  	3,98,49,0,410,412,5,4,0,0,411,413,3,76,38,0,412,411,1,0,0,0,412,413,1,
  	0,0,0,413,414,1,0,0,0,414,416,3,98,49,0,415,410,1,0,0,0,416,419,1,0,0,
  	0,417,415,1,0,0,0,417,418,1,0,0,0,418,421,1,0,0,0,419,417,1,0,0,0,420,
  	409,1,0,0,0,420,421,1,0,0,0,421,423,1,0,0,0,422,424,3,76,38,0,423,422,
  	1,0,0,0,423,424,1,0,0,0,424,425,1,0,0,0,425,426,5,12,0,0,426,57,1,0,0,
  	0,427,429,5,11,0,0,428,430,3,76,38,0,429,428,1,0,0,0,429,430,1,0,0,0,
  	430,442,1,0,0,0,431,439,3,48,24,0,432,434,5,4,0,0,433,435,3,76,38,0,434,
  	433,1,0,0,0,434,435,1,0,0,0,435,436,1,0,0,0,436,438,3,48,24,0,437,432,
  	1,0,0,0,438,441,1,0,0,0,439,437,1,0,0,0,439,440,1,0,0,0,440,443,1,0,0,
  	0,441,439,1,0,0,0,442,431,1,0,0,0,442,443,1,0,0,0,443,445,1,0,0,0,444,
  	446,3,76,38,0,445,444,1,0,0,0,445,446,1,0,0,0,446,447,1,0,0,0,447,448,
  	5,12,0,0,448,59,1,0,0,0,449,451,5,6,0,0,450,452,3,76,38,0,451,450,1,0,
  	0,0,451,452,1,0,0,0,452,464,1,0,0,0,453,461,3,64,32,0,454,456,5,4,0,0,
  	455,457,3,76,38,0,456,455,1,0,0,0,456,457,1,0,0,0,457,458,1,0,0,0,458,
  	460,3,64,32,0,459,454,1,0,0,0,460,463,1,0,0,0,461,459,1,0,0,0,461,462,
  	1,0,0,0,462,465,1,0,0,0,463,461,1,0,0,0,464,453,1,0,0,0,464,465,1,0,0,
  	0,465,467,1,0,0,0,466,468,3,76,38,0,467,466,1,0,0,0,467,468,1,0,0,0,468,
  	469,1,0,0,0,469,470,5,7,0,0,470,61,1,0,0,0,471,473,5,11,0,0,472,474,3,
  	2,1,0,473,472,1,0,0,0,473,474,1,0,0,0,474,476,1,0,0,0,475,477,3,76,38,
  	0,476,475,1,0,0,0,476,477,1,0,0,0,477,478,1,0,0,0,478,479,5,12,0,0,479,
  	63,1,0,0,0,480,485,3,68,34,0,481,485,3,70,35,0,482,485,3,72,36,0,483,
  	485,3,66,33,0,484,480,1,0,0,0,484,481,1,0,0,0,484,482,1,0,0,0,484,483,
  	1,0,0,0,485,488,1,0,0,0,486,487,5,20,0,0,487,489,3,82,41,0,488,486,1,
  	0,0,0,488,489,1,0,0,0,489,65,1,0,0,0,490,494,3,98,49,0,491,494,3,68,34,
  	0,492,494,3,72,36,0,493,490,1,0,0,0,493,491,1,0,0,0,493,492,1,0,0,0,494,
  	495,1,0,0,0,495,493,1,0,0,0,495,496,1,0,0,0,496,67,1,0,0,0,497,502,3,
  	98,49,0,498,502,3,78,39,0,499,502,3,60,30,0,500,502,3,58,29,0,501,497,
  	1,0,0,0,501,498,1,0,0,0,501,499,1,0,0,0,501,500,1,0,0,0,502,504,1,0,0,
  	0,503,505,3,28,14,0,504,503,1,0,0,0,504,505,1,0,0,0,505,509,1,0,0,0,506,
  	509,3,50,25,0,507,509,3,52,26,0,508,501,1,0,0,0,508,506,1,0,0,0,508,507,
  	1,0,0,0,509,69,1,0,0,0,510,511,3,52,26,0,511,512,3,40,20,0,512,71,1,0,
  	0,0,513,519,6,36,-1,0,514,520,3,98,49,0,515,520,3,50,25,0,516,520,3,68,
  	34,0,517,520,3,52,26,0,518,520,3,70,35,0,519,514,1,0,0,0,519,515,1,0,
  	0,0,519,516,1,0,0,0,519,517,1,0,0,0,519,518,1,0,0,0,520,521,1,0,0,0,521,
  	526,5,14,0,0,522,527,3,98,49,0,523,527,3,52,26,0,524,527,3,68,34,0,525,
  	527,3,70,35,0,526,522,1,0,0,0,526,523,1,0,0,0,526,524,1,0,0,0,526,525,
  	1,0,0,0,527,534,1,0,0,0,528,534,3,98,49,0,529,534,3,50,25,0,530,534,3,
  	68,34,0,531,534,3,52,26,0,532,534,3,70,35,0,533,513,1,0,0,0,533,528,1,
  	0,0,0,533,529,1,0,0,0,533,530,1,0,0,0,533,531,1,0,0,0,533,532,1,0,0,0,
  	534,545,1,0,0,0,535,536,10,7,0,0,536,541,5,14,0,0,537,542,3,98,49,0,538,
  	542,3,52,26,0,539,542,3,68,34,0,540,542,3,70,35,0,541,537,1,0,0,0,541,
  	538,1,0,0,0,541,539,1,0,0,0,541,540,1,0,0,0,542,544,1,0,0,0,543,535,1,
  	0,0,0,544,547,1,0,0,0,545,543,1,0,0,0,545,546,1,0,0,0,546,73,1,0,0,0,
  	547,545,1,0,0,0,548,552,3,76,38,0,549,552,5,15,0,0,550,552,5,0,0,1,551,
  	548,1,0,0,0,551,549,1,0,0,0,551,550,1,0,0,0,552,75,1,0,0,0,553,555,5,
  	50,0,0,554,553,1,0,0,0,555,556,1,0,0,0,556,554,1,0,0,0,556,557,1,0,0,
  	0,557,77,1,0,0,0,558,566,3,80,40,0,559,566,5,54,0,0,560,566,5,51,0,0,
  	561,566,5,55,0,0,562,566,5,33,0,0,563,566,5,34,0,0,564,566,5,35,0,0,565,
  	558,1,0,0,0,565,559,1,0,0,0,565,560,1,0,0,0,565,561,1,0,0,0,565,562,1,
  	0,0,0,565,563,1,0,0,0,565,564,1,0,0,0,566,79,1,0,0,0,567,571,5,56,0,0,
  	568,571,5,57,0,0,569,571,3,90,45,0,570,567,1,0,0,0,570,568,1,0,0,0,570,
  	569,1,0,0,0,571,573,1,0,0,0,572,574,5,53,0,0,573,572,1,0,0,0,573,574,
  	1,0,0,0,574,81,1,0,0,0,575,579,3,84,42,0,576,579,3,98,49,0,577,579,5,
  	36,0,0,578,575,1,0,0,0,578,576,1,0,0,0,578,577,1,0,0,0,579,83,1,0,0,0,
  	580,588,5,37,0,0,581,588,5,38,0,0,582,588,5,39,0,0,583,588,5,40,0,0,584,
  	588,5,41,0,0,585,588,3,86,43,0,586,588,3,94,47,0,587,580,1,0,0,0,587,
  	581,1,0,0,0,587,582,1,0,0,0,587,583,1,0,0,0,587,584,1,0,0,0,587,585,1,
  	0,0,0,587,586,1,0,0,0,588,85,1,0,0,0,589,592,3,88,44,0,590,592,3,92,46,
  	0,591,589,1,0,0,0,591,590,1,0,0,0,592,87,1,0,0,0,593,594,7,1,0,0,594,
  	89,1,0,0,0,595,596,5,56,0,0,596,597,7,2,0,0,597,598,5,56,0,0,598,604,
  	5,18,0,0,599,600,5,57,0,0,600,601,7,2,0,0,601,602,5,57,0,0,602,604,5,
  	18,0,0,603,595,1,0,0,0,603,599,1,0,0,0,604,91,1,0,0,0,605,610,5,45,0,
  	0,606,607,5,9,0,0,607,608,3,88,44,0,608,609,5,10,0,0,609,611,1,0,0,0,
  	610,606,1,0,0,0,610,611,1,0,0,0,611,615,1,0,0,0,612,613,5,6,0,0,613,614,
  	5,56,0,0,614,616,5,7,0,0,615,612,1,0,0,0,615,616,1,0,0,0,616,633,1,0,
  	0,0,617,622,5,46,0,0,618,619,5,9,0,0,619,620,3,88,44,0,620,621,5,10,0,
  	0,621,623,1,0,0,0,622,618,1,0,0,0,622,623,1,0,0,0,623,629,1,0,0,0,624,
  	625,5,6,0,0,625,626,5,56,0,0,626,628,5,7,0,0,627,624,1,0,0,0,628,631,
  	1,0,0,0,629,627,1,0,0,0,629,630,1,0,0,0,630,633,1,0,0,0,631,629,1,0,0,
  	0,632,605,1,0,0,0,632,617,1,0,0,0,633,93,1,0,0,0,634,646,5,47,0,0,635,
  	636,5,9,0,0,636,641,3,96,48,0,637,638,5,4,0,0,638,640,3,96,48,0,639,637,
  	1,0,0,0,640,643,1,0,0,0,641,639,1,0,0,0,641,642,1,0,0,0,642,644,1,0,0,
  	0,643,641,1,0,0,0,644,645,5,10,0,0,645,647,1,0,0,0,646,635,1,0,0,0,646,
  	647,1,0,0,0,647,651,1,0,0,0,648,649,5,6,0,0,649,650,5,56,0,0,650,652,
  	5,7,0,0,651,648,1,0,0,0,651,652,1,0,0,0,652,663,1,0,0,0,653,660,5,48,
  	0,0,654,655,5,9,0,0,655,656,3,82,41,0,656,657,5,4,0,0,657,658,3,96,48,
  	0,658,659,5,10,0,0,659,661,1,0,0,0,660,654,1,0,0,0,660,661,1,0,0,0,661,
  	663,1,0,0,0,662,634,1,0,0,0,662,653,1,0,0,0,663,95,1,0,0,0,664,666,3,
  	82,41,0,665,667,5,19,0,0,666,665,1,0,0,0,666,667,1,0,0,0,667,97,1,0,0,
  	0,668,669,5,52,0,0,669,99,1,0,0,0,106,101,104,109,118,124,127,135,143,
  	146,150,158,161,164,172,176,183,190,201,220,227,233,238,243,248,252,258,
  	263,268,272,278,283,288,291,294,300,305,310,313,316,324,328,333,338,341,
  	344,350,356,366,370,374,378,381,385,390,395,398,401,407,412,417,420,423,
  	429,434,439,442,445,451,456,461,464,467,473,476,484,488,493,495,501,504,
  	508,519,526,533,541,545,551,556,565,570,573,578,587,591,603,610,615,622,
  	629,632,641,646,651,660,662,666
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  pslParserStaticData = staticData.release();
}

}

PslParser::PslParser(TokenStream *input) : PslParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

PslParser::PslParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  PslParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *pslParserStaticData->atn, pslParserStaticData->decisionToDFA, pslParserStaticData->sharedContextCache, options);
}

PslParser::~PslParser() {
  delete _interpreter;
}

const atn::ATN& PslParser::getATN() const {
  return *pslParserStaticData->atn;
}

std::string PslParser::getGrammarFileName() const {
  return "Psl.g4";
}

const std::vector<std::string>& PslParser::getRuleNames() const {
  return pslParserStaticData->ruleNames;
}

const dfa::Vocabulary& PslParser::getVocabulary() const {
  return pslParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView PslParser::getSerializedATN() const {
  return pslParserStaticData->serializedATN;
}


//----------------- ProgramContext ------------------------------------------------------------------

PslParser::ProgramContext::ProgramContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::StmtListContext* PslParser::ProgramContext::stmtList() {
  return getRuleContext<PslParser::StmtListContext>(0);
}


size_t PslParser::ProgramContext::getRuleIndex() const {
  return PslParser::RuleProgram;
}


std::any PslParser::ProgramContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitProgram(this);
  else
    return visitor->visitChildren(this);
}

PslParser::ProgramContext* PslParser::program() {
  ProgramContext *_localctx = _tracker.createInstance<ProgramContext>(_ctx, getState());
  enterRule(_localctx, 0, PslParser::RuleProgram);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(101);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 278097345707510080) != 0)) {
      setState(100);
      stmtList();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- StmtListContext ------------------------------------------------------------------

PslParser::StmtListContext::StmtListContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<PslParser::StmtContext *> PslParser::StmtListContext::stmt() {
  return getRuleContexts<PslParser::StmtContext>();
}

PslParser::StmtContext* PslParser::StmtListContext::stmt(size_t i) {
  return getRuleContext<PslParser::StmtContext>(i);
}

std::vector<PslParser::SepMarkContext *> PslParser::StmtListContext::sepMark() {
  return getRuleContexts<PslParser::SepMarkContext>();
}

PslParser::SepMarkContext* PslParser::StmtListContext::sepMark(size_t i) {
  return getRuleContext<PslParser::SepMarkContext>(i);
}


size_t PslParser::StmtListContext::getRuleIndex() const {
  return PslParser::RuleStmtList;
}


std::any PslParser::StmtListContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitStmtList(this);
  else
    return visitor->visitChildren(this);
}

PslParser::StmtListContext* PslParser::stmtList() {
  StmtListContext *_localctx = _tracker.createInstance<StmtListContext>(_ctx, getState());
  enterRule(_localctx, 2, PslParser::RuleStmtList);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(107); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(104);
              _errHandler->sync(this);

              _la = _input->LA(1);
              if (_la == PslParser::LINE_END) {
                setState(103);
                sepMark();
              }
              setState(106);
              stmt();
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(109); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 2, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- StmtContext ------------------------------------------------------------------

PslParser::StmtContext::StmtContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::LetStmtContext* PslParser::StmtContext::letStmt() {
  return getRuleContext<PslParser::LetStmtContext>(0);
}

PslParser::UseStmtContext* PslParser::StmtContext::useStmt() {
  return getRuleContext<PslParser::UseStmtContext>(0);
}

PslParser::FuncDefContext* PslParser::StmtContext::funcDef() {
  return getRuleContext<PslParser::FuncDefContext>(0);
}

PslParser::TypeDefContext* PslParser::StmtContext::typeDef() {
  return getRuleContext<PslParser::TypeDefContext>(0);
}

PslParser::EnumDefContext* PslParser::StmtContext::enumDef() {
  return getRuleContext<PslParser::EnumDefContext>(0);
}

PslParser::RetStmtContext* PslParser::StmtContext::retStmt() {
  return getRuleContext<PslParser::RetStmtContext>(0);
}

PslParser::ExprStmtContext* PslParser::StmtContext::exprStmt() {
  return getRuleContext<PslParser::ExprStmtContext>(0);
}


size_t PslParser::StmtContext::getRuleIndex() const {
  return PslParser::RuleStmt;
}


std::any PslParser::StmtContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitStmt(this);
  else
    return visitor->visitChildren(this);
}

PslParser::StmtContext* PslParser::stmt() {
  StmtContext *_localctx = _tracker.createInstance<StmtContext>(_ctx, getState());
  enterRule(_localctx, 4, PslParser::RuleStmt);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(118);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(111);
      letStmt();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(112);
      useStmt();
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(113);
      funcDef();
      break;
    }

    case 4: {
      enterOuterAlt(_localctx, 4);
      setState(114);
      typeDef();
      break;
    }

    case 5: {
      enterOuterAlt(_localctx, 5);
      setState(115);
      enumDef();
      break;
    }

    case 6: {
      enterOuterAlt(_localctx, 6);
      setState(116);
      retStmt();
      break;
    }

    case 7: {
      enterOuterAlt(_localctx, 7);
      setState(117);
      exprStmt();
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- LetStmtContext ------------------------------------------------------------------

PslParser::LetStmtContext::LetStmtContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PslParser::LetStmtContext::LET() {
  return getToken(PslParser::LET, 0);
}

PslParser::CarrierContext* PslParser::LetStmtContext::carrier() {
  return getRuleContext<PslParser::CarrierContext>(0);
}

PslParser::EntityExprContext* PslParser::LetStmtContext::entityExpr() {
  return getRuleContext<PslParser::EntityExprContext>(0);
}

PslParser::StmtEndContext* PslParser::LetStmtContext::stmtEnd() {
  return getRuleContext<PslParser::StmtEndContext>(0);
}

PslParser::TypeContext* PslParser::LetStmtContext::type() {
  return getRuleContext<PslParser::TypeContext>(0);
}


size_t PslParser::LetStmtContext::getRuleIndex() const {
  return PslParser::RuleLetStmt;
}


std::any PslParser::LetStmtContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitLetStmt(this);
  else
    return visitor->visitChildren(this);
}

PslParser::LetStmtContext* PslParser::letStmt() {
  LetStmtContext *_localctx = _tracker.createInstance<LetStmtContext>(_ctx, getState());
  enterRule(_localctx, 6, PslParser::RuleLetStmt);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(120);
    match(PslParser::LET);
    setState(121);
    carrier();
    setState(124);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::T__0) {
      setState(122);
      match(PslParser::T__0);
      setState(123);
      type();
    }
    setState(127);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::T__1) {
      setState(126);
      match(PslParser::T__1);
    }
    setState(129);
    entityExpr();
    setState(130);
    stmtEnd();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- UseStmtContext ------------------------------------------------------------------

PslParser::UseStmtContext::UseStmtContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PslParser::UseStmtContext::USE() {
  return getToken(PslParser::USE, 0);
}

PslParser::CarrierContext* PslParser::UseStmtContext::carrier() {
  return getRuleContext<PslParser::CarrierContext>(0);
}

PslParser::EntityExprContext* PslParser::UseStmtContext::entityExpr() {
  return getRuleContext<PslParser::EntityExprContext>(0);
}

PslParser::StmtEndContext* PslParser::UseStmtContext::stmtEnd() {
  return getRuleContext<PslParser::StmtEndContext>(0);
}


size_t PslParser::UseStmtContext::getRuleIndex() const {
  return PslParser::RuleUseStmt;
}


std::any PslParser::UseStmtContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitUseStmt(this);
  else
    return visitor->visitChildren(this);
}

PslParser::UseStmtContext* PslParser::useStmt() {
  UseStmtContext *_localctx = _tracker.createInstance<UseStmtContext>(_ctx, getState());
  enterRule(_localctx, 8, PslParser::RuleUseStmt);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(132);
    match(PslParser::USE);
    setState(133);
    carrier();
    setState(135);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::T__1) {
      setState(134);
      match(PslParser::T__1);
    }
    setState(137);
    entityExpr();
    setState(138);
    stmtEnd();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- WithDefContext ------------------------------------------------------------------

PslParser::WithDefContext::WithDefContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PslParser::WithDefContext::WITH() {
  return getToken(PslParser::WITH, 0);
}

PslParser::EntityRefContext* PslParser::WithDefContext::entityRef() {
  return getRuleContext<PslParser::EntityRefContext>(0);
}

PslParser::WithDeclContext* PslParser::WithDefContext::withDecl() {
  return getRuleContext<PslParser::WithDeclContext>(0);
}

tree::TerminalNode* PslParser::WithDefContext::LINE_END() {
  return getToken(PslParser::LINE_END, 0);
}


size_t PslParser::WithDefContext::getRuleIndex() const {
  return PslParser::RuleWithDef;
}


std::any PslParser::WithDefContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitWithDef(this);
  else
    return visitor->visitChildren(this);
}

PslParser::WithDefContext* PslParser::withDef() {
  WithDefContext *_localctx = _tracker.createInstance<WithDefContext>(_ctx, getState());
  enterRule(_localctx, 10, PslParser::RuleWithDef);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(140);
    match(PslParser::WITH);
    setState(143);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case PslParser::IDENTIFIER: {
        setState(141);
        entityRef();
        break;
      }

      case PslParser::T__8: {
        setState(142);
        withDecl();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(146);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::LINE_END) {
      setState(145);
      match(PslParser::LINE_END);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- FuncDefContext ------------------------------------------------------------------

PslParser::FuncDefContext::FuncDefContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::AnnotationsContext* PslParser::FuncDefContext::annotations() {
  return getRuleContext<PslParser::AnnotationsContext>(0);
}

PslParser::ModifiersContext* PslParser::FuncDefContext::modifiers() {
  return getRuleContext<PslParser::ModifiersContext>(0);
}

tree::TerminalNode* PslParser::FuncDefContext::FUNC() {
  return getToken(PslParser::FUNC, 0);
}

PslParser::IdentRefContext* PslParser::FuncDefContext::identRef() {
  return getRuleContext<PslParser::IdentRefContext>(0);
}

PslParser::ParamDefContext* PslParser::FuncDefContext::paramDef() {
  return getRuleContext<PslParser::ParamDefContext>(0);
}

PslParser::StmtPackContext* PslParser::FuncDefContext::stmtPack() {
  return getRuleContext<PslParser::StmtPackContext>(0);
}

PslParser::StmtEndContext* PslParser::FuncDefContext::stmtEnd() {
  return getRuleContext<PslParser::StmtEndContext>(0);
}

PslParser::WithDefContext* PslParser::FuncDefContext::withDef() {
  return getRuleContext<PslParser::WithDefContext>(0);
}

PslParser::TypeContext* PslParser::FuncDefContext::type() {
  return getRuleContext<PslParser::TypeContext>(0);
}

tree::TerminalNode* PslParser::FuncDefContext::LINE_END() {
  return getToken(PslParser::LINE_END, 0);
}


size_t PslParser::FuncDefContext::getRuleIndex() const {
  return PslParser::RuleFuncDef;
}


std::any PslParser::FuncDefContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitFuncDef(this);
  else
    return visitor->visitChildren(this);
}

PslParser::FuncDefContext* PslParser::funcDef() {
  FuncDefContext *_localctx = _tracker.createInstance<FuncDefContext>(_ctx, getState());
  enterRule(_localctx, 12, PslParser::RuleFuncDef);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(148);
    annotations();
    setState(150);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::WITH) {
      setState(149);
      withDef();
    }
    setState(152);
    modifiers();
    setState(153);
    match(PslParser::FUNC);
    setState(154);
    identRef();
    setState(155);
    paramDef();
    setState(158);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::T__0) {
      setState(156);
      match(PslParser::T__0);
      setState(157);
      type();
    }
    setState(161);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::T__1) {
      setState(160);
      match(PslParser::T__1);
    }
    setState(164);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::LINE_END) {
      setState(163);
      match(PslParser::LINE_END);
    }
    setState(166);
    stmtPack();
    setState(167);
    stmtEnd();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- TypeDefContext ------------------------------------------------------------------

PslParser::TypeDefContext::TypeDefContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PslParser::TypeDefContext::TYPE() {
  return getToken(PslParser::TYPE, 0);
}

PslParser::IdentRefContext* PslParser::TypeDefContext::identRef() {
  return getRuleContext<PslParser::IdentRefContext>(0);
}

PslParser::StmtEndContext* PslParser::TypeDefContext::stmtEnd() {
  return getRuleContext<PslParser::StmtEndContext>(0);
}

PslParser::TypeContext* PslParser::TypeDefContext::type() {
  return getRuleContext<PslParser::TypeContext>(0);
}

PslParser::TypePackContext* PslParser::TypeDefContext::typePack() {
  return getRuleContext<PslParser::TypePackContext>(0);
}


size_t PslParser::TypeDefContext::getRuleIndex() const {
  return PslParser::RuleTypeDef;
}


std::any PslParser::TypeDefContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitTypeDef(this);
  else
    return visitor->visitChildren(this);
}

PslParser::TypeDefContext* PslParser::typeDef() {
  TypeDefContext *_localctx = _tracker.createInstance<TypeDefContext>(_ctx, getState());
  enterRule(_localctx, 14, PslParser::RuleTypeDef);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(169);
    match(PslParser::TYPE);
    setState(170);
    identRef();
    setState(172);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::T__1) {
      setState(171);
      match(PslParser::T__1);
    }
    setState(176);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case PslParser::ANY_TYPE:
      case PslParser::NUMBER_TYPE:
      case PslParser::STRING_TYPE:
      case PslParser::BOOLEAN_TYPE:
      case PslParser::FUNCTOR_TYPE:
      case PslParser::BLOCK_TYPE:
      case PslParser::INTEGER_TYPE:
      case PslParser::REAL_TYPE:
      case PslParser::COMPLEX_TYPE:
      case PslParser::ARRAY_TYPE:
      case PslParser::MATRIX_TYPE:
      case PslParser::LIST_TYPE:
      case PslParser::DICT_TYPE:
      case PslParser::IDENTIFIER: {
        setState(174);
        type();
        break;
      }

      case PslParser::T__10: {
        setState(175);
        typePack();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
    setState(178);
    stmtEnd();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- EnumDefContext ------------------------------------------------------------------

PslParser::EnumDefContext::EnumDefContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PslParser::EnumDefContext::ENUM() {
  return getToken(PslParser::ENUM, 0);
}

PslParser::IdentRefContext* PslParser::EnumDefContext::identRef() {
  return getRuleContext<PslParser::IdentRefContext>(0);
}

PslParser::DictUnpackContext* PslParser::EnumDefContext::dictUnpack() {
  return getRuleContext<PslParser::DictUnpackContext>(0);
}

PslParser::StmtEndContext* PslParser::EnumDefContext::stmtEnd() {
  return getRuleContext<PslParser::StmtEndContext>(0);
}


size_t PslParser::EnumDefContext::getRuleIndex() const {
  return PslParser::RuleEnumDef;
}


std::any PslParser::EnumDefContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitEnumDef(this);
  else
    return visitor->visitChildren(this);
}

PslParser::EnumDefContext* PslParser::enumDef() {
  EnumDefContext *_localctx = _tracker.createInstance<EnumDefContext>(_ctx, getState());
  enterRule(_localctx, 16, PslParser::RuleEnumDef);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(180);
    match(PslParser::ENUM);
    setState(181);
    identRef();
    setState(183);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::T__1) {
      setState(182);
      match(PslParser::T__1);
    }
    setState(185);
    dictUnpack();
    setState(186);
    stmtEnd();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- RetStmtContext ------------------------------------------------------------------

PslParser::RetStmtContext::RetStmtContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PslParser::RetStmtContext::RETURN() {
  return getToken(PslParser::RETURN, 0);
}

PslParser::StmtEndContext* PslParser::RetStmtContext::stmtEnd() {
  return getRuleContext<PslParser::StmtEndContext>(0);
}

PslParser::EntityExprContext* PslParser::RetStmtContext::entityExpr() {
  return getRuleContext<PslParser::EntityExprContext>(0);
}


size_t PslParser::RetStmtContext::getRuleIndex() const {
  return PslParser::RuleRetStmt;
}


std::any PslParser::RetStmtContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitRetStmt(this);
  else
    return visitor->visitChildren(this);
}

PslParser::RetStmtContext* PslParser::retStmt() {
  RetStmtContext *_localctx = _tracker.createInstance<RetStmtContext>(_ctx, getState());
  enterRule(_localctx, 18, PslParser::RuleRetStmt);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(188);
    match(PslParser::RETURN);
    setState(190);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 276971437212829760) != 0)) {
      setState(189);
      entityExpr();
    }
    setState(192);
    stmtEnd();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ExprStmtContext ------------------------------------------------------------------

PslParser::ExprStmtContext::ExprStmtContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::AnnotationsContext* PslParser::ExprStmtContext::annotations() {
  return getRuleContext<PslParser::AnnotationsContext>(0);
}

PslParser::EntityExprContext* PslParser::ExprStmtContext::entityExpr() {
  return getRuleContext<PslParser::EntityExprContext>(0);
}

PslParser::StmtEndContext* PslParser::ExprStmtContext::stmtEnd() {
  return getRuleContext<PslParser::StmtEndContext>(0);
}


size_t PslParser::ExprStmtContext::getRuleIndex() const {
  return PslParser::RuleExprStmt;
}


std::any PslParser::ExprStmtContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitExprStmt(this);
  else
    return visitor->visitChildren(this);
}

PslParser::ExprStmtContext* PslParser::exprStmt() {
  ExprStmtContext *_localctx = _tracker.createInstance<ExprStmtContext>(_ctx, getState());
  enterRule(_localctx, 20, PslParser::RuleExprStmt);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(194);
    annotations();
    setState(195);
    entityExpr();
    setState(196);
    stmtEnd();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CarrierContext ------------------------------------------------------------------

PslParser::CarrierContext::CarrierContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::IdentRefContext* PslParser::CarrierContext::identRef() {
  return getRuleContext<PslParser::IdentRefContext>(0);
}

PslParser::ListUnpackContext* PslParser::CarrierContext::listUnpack() {
  return getRuleContext<PslParser::ListUnpackContext>(0);
}

PslParser::DictUnpackContext* PslParser::CarrierContext::dictUnpack() {
  return getRuleContext<PslParser::DictUnpackContext>(0);
}


size_t PslParser::CarrierContext::getRuleIndex() const {
  return PslParser::RuleCarrier;
}


std::any PslParser::CarrierContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitCarrier(this);
  else
    return visitor->visitChildren(this);
}

PslParser::CarrierContext* PslParser::carrier() {
  CarrierContext *_localctx = _tracker.createInstance<CarrierContext>(_ctx, getState());
  enterRule(_localctx, 22, PslParser::RuleCarrier);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(201);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case PslParser::IDENTIFIER: {
        enterOuterAlt(_localctx, 1);
        setState(198);
        identRef();
        break;
      }

      case PslParser::T__5: {
        enterOuterAlt(_localctx, 2);
        setState(199);
        listUnpack();
        break;
      }

      case PslParser::T__10: {
        enterOuterAlt(_localctx, 3);
        setState(200);
        dictUnpack();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- BiasAnnoContext ------------------------------------------------------------------

PslParser::BiasAnnoContext::BiasAnnoContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> PslParser::BiasAnnoContext::INTEGER() {
  return getTokens(PslParser::INTEGER);
}

tree::TerminalNode* PslParser::BiasAnnoContext::INTEGER(size_t i) {
  return getToken(PslParser::INTEGER, i);
}


size_t PslParser::BiasAnnoContext::getRuleIndex() const {
  return PslParser::RuleBiasAnno;
}


std::any PslParser::BiasAnnoContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitBiasAnno(this);
  else
    return visitor->visitChildren(this);
}

PslParser::BiasAnnoContext* PslParser::biasAnno() {
  BiasAnnoContext *_localctx = _tracker.createInstance<BiasAnnoContext>(_ctx, getState());
  enterRule(_localctx, 24, PslParser::RuleBiasAnno);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(203);
    match(PslParser::T__2);
    setState(204);
    match(PslParser::INTEGER);
    setState(205);
    match(PslParser::T__3);
    setState(206);
    match(PslParser::INTEGER);
    setState(207);
    match(PslParser::T__4);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- SizeAnnoContext ------------------------------------------------------------------

PslParser::SizeAnnoContext::SizeAnnoContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> PslParser::SizeAnnoContext::INTEGER() {
  return getTokens(PslParser::INTEGER);
}

tree::TerminalNode* PslParser::SizeAnnoContext::INTEGER(size_t i) {
  return getToken(PslParser::INTEGER, i);
}


size_t PslParser::SizeAnnoContext::getRuleIndex() const {
  return PslParser::RuleSizeAnno;
}


std::any PslParser::SizeAnnoContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitSizeAnno(this);
  else
    return visitor->visitChildren(this);
}

PslParser::SizeAnnoContext* PslParser::sizeAnno() {
  SizeAnnoContext *_localctx = _tracker.createInstance<SizeAnnoContext>(_ctx, getState());
  enterRule(_localctx, 26, PslParser::RuleSizeAnno);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(209);
    match(PslParser::T__5);
    setState(210);
    match(PslParser::INTEGER);
    setState(211);
    match(PslParser::T__3);
    setState(212);
    match(PslParser::INTEGER);
    setState(213);
    match(PslParser::T__6);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- AnnotationContext ------------------------------------------------------------------

PslParser::AnnotationContext::AnnotationContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::IdentRefContext* PslParser::AnnotationContext::identRef() {
  return getRuleContext<PslParser::IdentRefContext>(0);
}

PslParser::DictPackContext* PslParser::AnnotationContext::dictPack() {
  return getRuleContext<PslParser::DictPackContext>(0);
}

PslParser::BiasAnnoContext* PslParser::AnnotationContext::biasAnno() {
  return getRuleContext<PslParser::BiasAnnoContext>(0);
}

PslParser::SizeAnnoContext* PslParser::AnnotationContext::sizeAnno() {
  return getRuleContext<PslParser::SizeAnnoContext>(0);
}


size_t PslParser::AnnotationContext::getRuleIndex() const {
  return PslParser::RuleAnnotation;
}


std::any PslParser::AnnotationContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitAnnotation(this);
  else
    return visitor->visitChildren(this);
}

PslParser::AnnotationContext* PslParser::annotation() {
  AnnotationContext *_localctx = _tracker.createInstance<AnnotationContext>(_ctx, getState());
  enterRule(_localctx, 28, PslParser::RuleAnnotation);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(215);
    match(PslParser::T__7);
    setState(220);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case PslParser::IDENTIFIER: {
        setState(216);
        identRef();
        break;
      }

      case PslParser::T__10: {
        setState(217);
        dictPack();
        break;
      }

      case PslParser::T__2: {
        setState(218);
        biasAnno();
        break;
      }

      case PslParser::T__5: {
        setState(219);
        sizeAnno();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- AnnotationsContext ------------------------------------------------------------------

PslParser::AnnotationsContext::AnnotationsContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<PslParser::AnnotationContext *> PslParser::AnnotationsContext::annotation() {
  return getRuleContexts<PslParser::AnnotationContext>();
}

PslParser::AnnotationContext* PslParser::AnnotationsContext::annotation(size_t i) {
  return getRuleContext<PslParser::AnnotationContext>(i);
}

std::vector<tree::TerminalNode *> PslParser::AnnotationsContext::LINE_END() {
  return getTokens(PslParser::LINE_END);
}

tree::TerminalNode* PslParser::AnnotationsContext::LINE_END(size_t i) {
  return getToken(PslParser::LINE_END, i);
}


size_t PslParser::AnnotationsContext::getRuleIndex() const {
  return PslParser::RuleAnnotations;
}


std::any PslParser::AnnotationsContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitAnnotations(this);
  else
    return visitor->visitChildren(this);
}

PslParser::AnnotationsContext* PslParser::annotations() {
  AnnotationsContext *_localctx = _tracker.createInstance<AnnotationsContext>(_ctx, getState());
  enterRule(_localctx, 30, PslParser::RuleAnnotations);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(227);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == PslParser::T__7) {
      setState(222);
      annotation();
      setState(223);
      match(PslParser::LINE_END);
      setState(229);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ModifiersContext ------------------------------------------------------------------

PslParser::ModifiersContext::ModifiersContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> PslParser::ModifiersContext::INNER() {
  return getTokens(PslParser::INNER);
}

tree::TerminalNode* PslParser::ModifiersContext::INNER(size_t i) {
  return getToken(PslParser::INNER, i);
}

std::vector<tree::TerminalNode *> PslParser::ModifiersContext::SYNC() {
  return getTokens(PslParser::SYNC);
}

tree::TerminalNode* PslParser::ModifiersContext::SYNC(size_t i) {
  return getToken(PslParser::SYNC, i);
}

std::vector<tree::TerminalNode *> PslParser::ModifiersContext::SCOPED() {
  return getTokens(PslParser::SCOPED);
}

tree::TerminalNode* PslParser::ModifiersContext::SCOPED(size_t i) {
  return getToken(PslParser::SCOPED, i);
}

std::vector<tree::TerminalNode *> PslParser::ModifiersContext::STATIC() {
  return getTokens(PslParser::STATIC);
}

tree::TerminalNode* PslParser::ModifiersContext::STATIC(size_t i) {
  return getToken(PslParser::STATIC, i);
}

std::vector<tree::TerminalNode *> PslParser::ModifiersContext::ATOMIC() {
  return getTokens(PslParser::ATOMIC);
}

tree::TerminalNode* PslParser::ModifiersContext::ATOMIC(size_t i) {
  return getToken(PslParser::ATOMIC, i);
}


size_t PslParser::ModifiersContext::getRuleIndex() const {
  return PslParser::RuleModifiers;
}


std::any PslParser::ModifiersContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitModifiers(this);
  else
    return visitor->visitChildren(this);
}

PslParser::ModifiersContext* PslParser::modifiers() {
  ModifiersContext *_localctx = _tracker.createInstance<ModifiersContext>(_ctx, getState());
  enterRule(_localctx, 32, PslParser::RuleModifiers);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(233);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8321499136) != 0)) {
      setState(230);
      _la = _input->LA(1);
      if (!((((_la & ~ 0x3fULL) == 0) &&
        ((1ULL << _la) & 8321499136) != 0))) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(235);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- WithListContext ------------------------------------------------------------------

PslParser::WithListContext::WithListContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<PslParser::ArgumentContext *> PslParser::WithListContext::argument() {
  return getRuleContexts<PslParser::ArgumentContext>();
}

PslParser::ArgumentContext* PslParser::WithListContext::argument(size_t i) {
  return getRuleContext<PslParser::ArgumentContext>(i);
}

std::vector<PslParser::SepMarkContext *> PslParser::WithListContext::sepMark() {
  return getRuleContexts<PslParser::SepMarkContext>();
}

PslParser::SepMarkContext* PslParser::WithListContext::sepMark(size_t i) {
  return getRuleContext<PslParser::SepMarkContext>(i);
}


size_t PslParser::WithListContext::getRuleIndex() const {
  return PslParser::RuleWithList;
}


std::any PslParser::WithListContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitWithList(this);
  else
    return visitor->visitChildren(this);
}

PslParser::WithListContext* PslParser::withList() {
  WithListContext *_localctx = _tracker.createInstance<WithListContext>(_ctx, getState());
  enterRule(_localctx, 34, PslParser::RuleWithList);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(236);
    match(PslParser::T__8);
    setState(238);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::LINE_END) {
      setState(237);
      sepMark();
    }
    setState(240);
    argument();
    setState(248);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == PslParser::T__3) {
      setState(241);
      match(PslParser::T__3);
      setState(243);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == PslParser::LINE_END) {
        setState(242);
        sepMark();
      }
      setState(245);
      argument();
      setState(250);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(252);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::LINE_END) {
      setState(251);
      sepMark();
    }
    setState(254);
    match(PslParser::T__9);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- WithDeclContext ------------------------------------------------------------------

PslParser::WithDeclContext::WithDeclContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<PslParser::KeyValDeclContext *> PslParser::WithDeclContext::keyValDecl() {
  return getRuleContexts<PslParser::KeyValDeclContext>();
}

PslParser::KeyValDeclContext* PslParser::WithDeclContext::keyValDecl(size_t i) {
  return getRuleContext<PslParser::KeyValDeclContext>(i);
}

std::vector<PslParser::SepMarkContext *> PslParser::WithDeclContext::sepMark() {
  return getRuleContexts<PslParser::SepMarkContext>();
}

PslParser::SepMarkContext* PslParser::WithDeclContext::sepMark(size_t i) {
  return getRuleContext<PslParser::SepMarkContext>(i);
}


size_t PslParser::WithDeclContext::getRuleIndex() const {
  return PslParser::RuleWithDecl;
}


std::any PslParser::WithDeclContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitWithDecl(this);
  else
    return visitor->visitChildren(this);
}

PslParser::WithDeclContext* PslParser::withDecl() {
  WithDeclContext *_localctx = _tracker.createInstance<WithDeclContext>(_ctx, getState());
  enterRule(_localctx, 36, PslParser::RuleWithDecl);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(256);
    match(PslParser::T__8);
    setState(258);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::LINE_END) {
      setState(257);
      sepMark();
    }
    setState(260);
    keyValDecl();
    setState(268);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == PslParser::T__3) {
      setState(261);
      match(PslParser::T__3);
      setState(263);
      _errHandler->sync(this);

      _la = _input->LA(1);
      if (_la == PslParser::LINE_END) {
        setState(262);
        sepMark();
      }
      setState(265);
      keyValDecl();
      setState(270);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(272);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::LINE_END) {
      setState(271);
      sepMark();
    }
    setState(274);
    match(PslParser::T__9);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ParamDefContext ------------------------------------------------------------------

PslParser::ParamDefContext::ParamDefContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<PslParser::SepMarkContext *> PslParser::ParamDefContext::sepMark() {
  return getRuleContexts<PslParser::SepMarkContext>();
}

PslParser::SepMarkContext* PslParser::ParamDefContext::sepMark(size_t i) {
  return getRuleContext<PslParser::SepMarkContext>(i);
}

std::vector<PslParser::KeyValDeclContext *> PslParser::ParamDefContext::keyValDecl() {
  return getRuleContexts<PslParser::KeyValDeclContext>();
}

PslParser::KeyValDeclContext* PslParser::ParamDefContext::keyValDecl(size_t i) {
  return getRuleContext<PslParser::KeyValDeclContext>(i);
}


size_t PslParser::ParamDefContext::getRuleIndex() const {
  return PslParser::RuleParamDef;
}


std::any PslParser::ParamDefContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitParamDef(this);
  else
    return visitor->visitChildren(this);
}

PslParser::ParamDefContext* PslParser::paramDef() {
  ParamDefContext *_localctx = _tracker.createInstance<ParamDefContext>(_ctx, getState());
  enterRule(_localctx, 38, PslParser::RuleParamDef);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(276);
    match(PslParser::T__2);
    setState(278);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 29, _ctx)) {
    case 1: {
      setState(277);
      sepMark();
      break;
    }

    default:
      break;
    }
    setState(291);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::IDENTIFIER) {
      setState(280);
      keyValDecl();
      setState(288);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == PslParser::T__3) {
        setState(281);
        match(PslParser::T__3);
        setState(283);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == PslParser::LINE_END) {
          setState(282);
          sepMark();
        }
        setState(285);
        keyValDecl();
        setState(290);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
    }
    setState(294);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::LINE_END) {
      setState(293);
      sepMark();
    }
    setState(296);
    match(PslParser::T__4);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ArgsListContext ------------------------------------------------------------------

PslParser::ArgsListContext::ArgsListContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<PslParser::SepMarkContext *> PslParser::ArgsListContext::sepMark() {
  return getRuleContexts<PslParser::SepMarkContext>();
}

PslParser::SepMarkContext* PslParser::ArgsListContext::sepMark(size_t i) {
  return getRuleContext<PslParser::SepMarkContext>(i);
}

std::vector<PslParser::ArgumentContext *> PslParser::ArgsListContext::argument() {
  return getRuleContexts<PslParser::ArgumentContext>();
}

PslParser::ArgumentContext* PslParser::ArgsListContext::argument(size_t i) {
  return getRuleContext<PslParser::ArgumentContext>(i);
}


size_t PslParser::ArgsListContext::getRuleIndex() const {
  return PslParser::RuleArgsList;
}


std::any PslParser::ArgsListContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitArgsList(this);
  else
    return visitor->visitChildren(this);
}

PslParser::ArgsListContext* PslParser::argsList() {
  ArgsListContext *_localctx = _tracker.createInstance<ArgsListContext>(_ctx, getState());
  enterRule(_localctx, 40, PslParser::RuleArgsList);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(298);
    match(PslParser::T__2);
    setState(300);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 34, _ctx)) {
    case 1: {
      setState(299);
      sepMark();
      break;
    }

    default:
      break;
    }
    setState(313);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 276971437212829760) != 0)) {
      setState(302);
      argument();
      setState(310);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == PslParser::T__3) {
        setState(303);
        match(PslParser::T__3);
        setState(305);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == PslParser::LINE_END) {
          setState(304);
          sepMark();
        }
        setState(307);
        argument();
        setState(312);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
    }
    setState(316);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::LINE_END) {
      setState(315);
      sepMark();
    }
    setState(318);
    match(PslParser::T__4);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ArgumentContext ------------------------------------------------------------------

PslParser::ArgumentContext::ArgumentContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::IdentRefContext* PslParser::ArgumentContext::identRef() {
  return getRuleContext<PslParser::IdentRefContext>(0);
}

PslParser::EntityContext* PslParser::ArgumentContext::entity() {
  return getRuleContext<PslParser::EntityContext>(0);
}

PslParser::KeyValExprContext* PslParser::ArgumentContext::keyValExpr() {
  return getRuleContext<PslParser::KeyValExprContext>(0);
}

PslParser::EntityExprContext* PslParser::ArgumentContext::entityExpr() {
  return getRuleContext<PslParser::EntityExprContext>(0);
}


size_t PslParser::ArgumentContext::getRuleIndex() const {
  return PslParser::RuleArgument;
}


std::any PslParser::ArgumentContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitArgument(this);
  else
    return visitor->visitChildren(this);
}

PslParser::ArgumentContext* PslParser::argument() {
  ArgumentContext *_localctx = _tracker.createInstance<ArgumentContext>(_ctx, getState());
  enterRule(_localctx, 42, PslParser::RuleArgument);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(324);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 39, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(320);
      identRef();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(321);
      entity();
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(322);
      keyValExpr();
      break;
    }

    case 4: {
      enterOuterAlt(_localctx, 4);
      setState(323);
      entityExpr();
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- TypePackContext ------------------------------------------------------------------

PslParser::TypePackContext::TypePackContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<PslParser::SepMarkContext *> PslParser::TypePackContext::sepMark() {
  return getRuleContexts<PslParser::SepMarkContext>();
}

PslParser::SepMarkContext* PslParser::TypePackContext::sepMark(size_t i) {
  return getRuleContext<PslParser::SepMarkContext>(i);
}

std::vector<PslParser::KeyValDeclContext *> PslParser::TypePackContext::keyValDecl() {
  return getRuleContexts<PslParser::KeyValDeclContext>();
}

PslParser::KeyValDeclContext* PslParser::TypePackContext::keyValDecl(size_t i) {
  return getRuleContext<PslParser::KeyValDeclContext>(i);
}


size_t PslParser::TypePackContext::getRuleIndex() const {
  return PslParser::RuleTypePack;
}


std::any PslParser::TypePackContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitTypePack(this);
  else
    return visitor->visitChildren(this);
}

PslParser::TypePackContext* PslParser::typePack() {
  TypePackContext *_localctx = _tracker.createInstance<TypePackContext>(_ctx, getState());
  enterRule(_localctx, 44, PslParser::RuleTypePack);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(326);
    match(PslParser::T__10);
    setState(328);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 40, _ctx)) {
    case 1: {
      setState(327);
      sepMark();
      break;
    }

    default:
      break;
    }
    setState(341);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::IDENTIFIER) {
      setState(330);
      keyValDecl();
      setState(338);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == PslParser::T__3) {
        setState(331);
        match(PslParser::T__3);
        setState(333);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == PslParser::LINE_END) {
          setState(332);
          sepMark();
        }
        setState(335);
        keyValDecl();
        setState(340);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
    }
    setState(344);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::LINE_END) {
      setState(343);
      sepMark();
    }
    setState(346);
    match(PslParser::T__11);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- KeyValDeclContext ------------------------------------------------------------------

PslParser::KeyValDeclContext::KeyValDeclContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::IdentRefContext* PslParser::KeyValDeclContext::identRef() {
  return getRuleContext<PslParser::IdentRefContext>(0);
}

PslParser::NullableTypeContext* PslParser::KeyValDeclContext::nullableType() {
  return getRuleContext<PslParser::NullableTypeContext>(0);
}

PslParser::AnnotationContext* PslParser::KeyValDeclContext::annotation() {
  return getRuleContext<PslParser::AnnotationContext>(0);
}

PslParser::EntityExprContext* PslParser::KeyValDeclContext::entityExpr() {
  return getRuleContext<PslParser::EntityExprContext>(0);
}


size_t PslParser::KeyValDeclContext::getRuleIndex() const {
  return PslParser::RuleKeyValDecl;
}


std::any PslParser::KeyValDeclContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitKeyValDecl(this);
  else
    return visitor->visitChildren(this);
}

PslParser::KeyValDeclContext* PslParser::keyValDecl() {
  KeyValDeclContext *_localctx = _tracker.createInstance<KeyValDeclContext>(_ctx, getState());
  enterRule(_localctx, 46, PslParser::RuleKeyValDecl);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(348);
    identRef();
    setState(350);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::T__7) {
      setState(349);
      annotation();
    }
    setState(352);
    match(PslParser::T__0);
    setState(353);
    nullableType();
    setState(356);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::T__1) {
      setState(354);
      match(PslParser::T__1);
      setState(355);
      entityExpr();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- KeyValExprContext ------------------------------------------------------------------

PslParser::KeyValExprContext::KeyValExprContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::IdentRefContext* PslParser::KeyValExprContext::identRef() {
  return getRuleContext<PslParser::IdentRefContext>(0);
}

PslParser::EntityExprContext* PslParser::KeyValExprContext::entityExpr() {
  return getRuleContext<PslParser::EntityExprContext>(0);
}


size_t PslParser::KeyValExprContext::getRuleIndex() const {
  return PslParser::RuleKeyValExpr;
}


std::any PslParser::KeyValExprContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitKeyValExpr(this);
  else
    return visitor->visitChildren(this);
}

PslParser::KeyValExprContext* PslParser::keyValExpr() {
  KeyValExprContext *_localctx = _tracker.createInstance<KeyValExprContext>(_ctx, getState());
  enterRule(_localctx, 48, PslParser::RuleKeyValExpr);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(358);
    identRef();
    setState(359);
    match(PslParser::T__1);
    setState(360);
    entityExpr();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- EntityRefContext ------------------------------------------------------------------

PslParser::EntityRefContext::EntityRefContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<PslParser::IdentRefContext *> PslParser::EntityRefContext::identRef() {
  return getRuleContexts<PslParser::IdentRefContext>();
}

PslParser::IdentRefContext* PslParser::EntityRefContext::identRef(size_t i) {
  return getRuleContext<PslParser::IdentRefContext>(i);
}

PslParser::AnnotationContext* PslParser::EntityRefContext::annotation() {
  return getRuleContext<PslParser::AnnotationContext>(0);
}

std::vector<tree::TerminalNode *> PslParser::EntityRefContext::INTEGER() {
  return getTokens(PslParser::INTEGER);
}

tree::TerminalNode* PslParser::EntityRefContext::INTEGER(size_t i) {
  return getToken(PslParser::INTEGER, i);
}


size_t PslParser::EntityRefContext::getRuleIndex() const {
  return PslParser::RuleEntityRef;
}


std::any PslParser::EntityRefContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitEntityRef(this);
  else
    return visitor->visitChildren(this);
}

PslParser::EntityRefContext* PslParser::entityRef() {
  EntityRefContext *_localctx = _tracker.createInstance<EntityRefContext>(_ctx, getState());
  enterRule(_localctx, 50, PslParser::RuleEntityRef);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(362);
    identRef();
    setState(370);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 48, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        setState(363);
        match(PslParser::T__12);
        setState(366);
        _errHandler->sync(this);
        switch (_input->LA(1)) {
          case PslParser::INTEGER: {
            setState(364);
            match(PslParser::INTEGER);
            break;
          }

          case PslParser::IDENTIFIER: {
            setState(365);
            identRef();
            break;
          }

        default:
          throw NoViableAltException(this);
        } 
      }
      setState(372);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 48, _ctx);
    }
    setState(374);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 49, _ctx)) {
    case 1: {
      setState(373);
      annotation();
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- FunctorRefContext ------------------------------------------------------------------

PslParser::FunctorRefContext::FunctorRefContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::IdentRefContext* PslParser::FunctorRefContext::identRef() {
  return getRuleContext<PslParser::IdentRefContext>(0);
}

PslParser::WithListContext* PslParser::FunctorRefContext::withList() {
  return getRuleContext<PslParser::WithListContext>(0);
}

PslParser::AnnotationContext* PslParser::FunctorRefContext::annotation() {
  return getRuleContext<PslParser::AnnotationContext>(0);
}


size_t PslParser::FunctorRefContext::getRuleIndex() const {
  return PslParser::RuleFunctorRef;
}


std::any PslParser::FunctorRefContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitFunctorRef(this);
  else
    return visitor->visitChildren(this);
}

PslParser::FunctorRefContext* PslParser::functorRef() {
  FunctorRefContext *_localctx = _tracker.createInstance<FunctorRefContext>(_ctx, getState());
  enterRule(_localctx, 52, PslParser::RuleFunctorRef);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(376);
    identRef();
    setState(378);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 50, _ctx)) {
    case 1: {
      setState(377);
      withList();
      break;
    }

    default:
      break;
    }
    setState(381);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 51, _ctx)) {
    case 1: {
      setState(380);
      annotation();
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ListUnpackContext ------------------------------------------------------------------

PslParser::ListUnpackContext::ListUnpackContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<PslParser::SepMarkContext *> PslParser::ListUnpackContext::sepMark() {
  return getRuleContexts<PslParser::SepMarkContext>();
}

PslParser::SepMarkContext* PslParser::ListUnpackContext::sepMark(size_t i) {
  return getRuleContext<PslParser::SepMarkContext>(i);
}

std::vector<PslParser::IdentRefContext *> PslParser::ListUnpackContext::identRef() {
  return getRuleContexts<PslParser::IdentRefContext>();
}

PslParser::IdentRefContext* PslParser::ListUnpackContext::identRef(size_t i) {
  return getRuleContext<PslParser::IdentRefContext>(i);
}


size_t PslParser::ListUnpackContext::getRuleIndex() const {
  return PslParser::RuleListUnpack;
}


std::any PslParser::ListUnpackContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitListUnpack(this);
  else
    return visitor->visitChildren(this);
}

PslParser::ListUnpackContext* PslParser::listUnpack() {
  ListUnpackContext *_localctx = _tracker.createInstance<ListUnpackContext>(_ctx, getState());
  enterRule(_localctx, 54, PslParser::RuleListUnpack);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(383);
    match(PslParser::T__5);
    setState(385);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 52, _ctx)) {
    case 1: {
      setState(384);
      sepMark();
      break;
    }

    default:
      break;
    }
    setState(398);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::IDENTIFIER) {
      setState(387);
      identRef();
      setState(395);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == PslParser::T__3) {
        setState(388);
        match(PslParser::T__3);
        setState(390);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == PslParser::LINE_END) {
          setState(389);
          sepMark();
        }
        setState(392);
        identRef();
        setState(397);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
    }
    setState(401);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::LINE_END) {
      setState(400);
      sepMark();
    }
    setState(403);
    match(PslParser::T__6);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- DictUnpackContext ------------------------------------------------------------------

PslParser::DictUnpackContext::DictUnpackContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<PslParser::SepMarkContext *> PslParser::DictUnpackContext::sepMark() {
  return getRuleContexts<PslParser::SepMarkContext>();
}

PslParser::SepMarkContext* PslParser::DictUnpackContext::sepMark(size_t i) {
  return getRuleContext<PslParser::SepMarkContext>(i);
}

std::vector<PslParser::IdentRefContext *> PslParser::DictUnpackContext::identRef() {
  return getRuleContexts<PslParser::IdentRefContext>();
}

PslParser::IdentRefContext* PslParser::DictUnpackContext::identRef(size_t i) {
  return getRuleContext<PslParser::IdentRefContext>(i);
}


size_t PslParser::DictUnpackContext::getRuleIndex() const {
  return PslParser::RuleDictUnpack;
}


std::any PslParser::DictUnpackContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitDictUnpack(this);
  else
    return visitor->visitChildren(this);
}

PslParser::DictUnpackContext* PslParser::dictUnpack() {
  DictUnpackContext *_localctx = _tracker.createInstance<DictUnpackContext>(_ctx, getState());
  enterRule(_localctx, 56, PslParser::RuleDictUnpack);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(405);
    match(PslParser::T__10);
    setState(407);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 57, _ctx)) {
    case 1: {
      setState(406);
      sepMark();
      break;
    }

    default:
      break;
    }
    setState(420);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::IDENTIFIER) {
      setState(409);
      identRef();
      setState(417);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == PslParser::T__3) {
        setState(410);
        match(PslParser::T__3);
        setState(412);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == PslParser::LINE_END) {
          setState(411);
          sepMark();
        }
        setState(414);
        identRef();
        setState(419);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
    }
    setState(423);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::LINE_END) {
      setState(422);
      sepMark();
    }
    setState(425);
    match(PslParser::T__11);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- DictPackContext ------------------------------------------------------------------

PslParser::DictPackContext::DictPackContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<PslParser::SepMarkContext *> PslParser::DictPackContext::sepMark() {
  return getRuleContexts<PslParser::SepMarkContext>();
}

PslParser::SepMarkContext* PslParser::DictPackContext::sepMark(size_t i) {
  return getRuleContext<PslParser::SepMarkContext>(i);
}

std::vector<PslParser::KeyValExprContext *> PslParser::DictPackContext::keyValExpr() {
  return getRuleContexts<PslParser::KeyValExprContext>();
}

PslParser::KeyValExprContext* PslParser::DictPackContext::keyValExpr(size_t i) {
  return getRuleContext<PslParser::KeyValExprContext>(i);
}


size_t PslParser::DictPackContext::getRuleIndex() const {
  return PslParser::RuleDictPack;
}


std::any PslParser::DictPackContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitDictPack(this);
  else
    return visitor->visitChildren(this);
}

PslParser::DictPackContext* PslParser::dictPack() {
  DictPackContext *_localctx = _tracker.createInstance<DictPackContext>(_ctx, getState());
  enterRule(_localctx, 58, PslParser::RuleDictPack);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(427);
    match(PslParser::T__10);
    setState(429);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 62, _ctx)) {
    case 1: {
      setState(428);
      sepMark();
      break;
    }

    default:
      break;
    }
    setState(442);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::IDENTIFIER) {
      setState(431);
      keyValExpr();
      setState(439);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == PslParser::T__3) {
        setState(432);
        match(PslParser::T__3);
        setState(434);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == PslParser::LINE_END) {
          setState(433);
          sepMark();
        }
        setState(436);
        keyValExpr();
        setState(441);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
    }
    setState(445);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::LINE_END) {
      setState(444);
      sepMark();
    }
    setState(447);
    match(PslParser::T__11);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ListPackContext ------------------------------------------------------------------

PslParser::ListPackContext::ListPackContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<PslParser::SepMarkContext *> PslParser::ListPackContext::sepMark() {
  return getRuleContexts<PslParser::SepMarkContext>();
}

PslParser::SepMarkContext* PslParser::ListPackContext::sepMark(size_t i) {
  return getRuleContext<PslParser::SepMarkContext>(i);
}

std::vector<PslParser::EntityExprContext *> PslParser::ListPackContext::entityExpr() {
  return getRuleContexts<PslParser::EntityExprContext>();
}

PslParser::EntityExprContext* PslParser::ListPackContext::entityExpr(size_t i) {
  return getRuleContext<PslParser::EntityExprContext>(i);
}


size_t PslParser::ListPackContext::getRuleIndex() const {
  return PslParser::RuleListPack;
}


std::any PslParser::ListPackContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitListPack(this);
  else
    return visitor->visitChildren(this);
}

PslParser::ListPackContext* PslParser::listPack() {
  ListPackContext *_localctx = _tracker.createInstance<ListPackContext>(_ctx, getState());
  enterRule(_localctx, 60, PslParser::RuleListPack);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(449);
    match(PslParser::T__5);
    setState(451);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 67, _ctx)) {
    case 1: {
      setState(450);
      sepMark();
      break;
    }

    default:
      break;
    }
    setState(464);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 276971437212829760) != 0)) {
      setState(453);
      entityExpr();
      setState(461);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while (_la == PslParser::T__3) {
        setState(454);
        match(PslParser::T__3);
        setState(456);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == PslParser::LINE_END) {
          setState(455);
          sepMark();
        }
        setState(458);
        entityExpr();
        setState(463);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
    }
    setState(467);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::LINE_END) {
      setState(466);
      sepMark();
    }
    setState(469);
    match(PslParser::T__6);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- StmtPackContext ------------------------------------------------------------------

PslParser::StmtPackContext::StmtPackContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::StmtListContext* PslParser::StmtPackContext::stmtList() {
  return getRuleContext<PslParser::StmtListContext>(0);
}

PslParser::SepMarkContext* PslParser::StmtPackContext::sepMark() {
  return getRuleContext<PslParser::SepMarkContext>(0);
}


size_t PslParser::StmtPackContext::getRuleIndex() const {
  return PslParser::RuleStmtPack;
}


std::any PslParser::StmtPackContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitStmtPack(this);
  else
    return visitor->visitChildren(this);
}

PslParser::StmtPackContext* PslParser::stmtPack() {
  StmtPackContext *_localctx = _tracker.createInstance<StmtPackContext>(_ctx, getState());
  enterRule(_localctx, 62, PslParser::RuleStmtPack);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(471);
    match(PslParser::T__10);
    setState(473);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 72, _ctx)) {
    case 1: {
      setState(472);
      stmtList();
      break;
    }

    default:
      break;
    }
    setState(476);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::LINE_END) {
      setState(475);
      sepMark();
    }
    setState(478);
    match(PslParser::T__11);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- EntityExprContext ------------------------------------------------------------------

PslParser::EntityExprContext::EntityExprContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::EntityContext* PslParser::EntityExprContext::entity() {
  return getRuleContext<PslParser::EntityContext>(0);
}

PslParser::NormCallContext* PslParser::EntityExprContext::normCall() {
  return getRuleContext<PslParser::NormCallContext>(0);
}

PslParser::LinkCallContext* PslParser::EntityExprContext::linkCall() {
  return getRuleContext<PslParser::LinkCallContext>(0);
}

PslParser::EntityChainContext* PslParser::EntityExprContext::entityChain() {
  return getRuleContext<PslParser::EntityChainContext>(0);
}

tree::TerminalNode* PslParser::EntityExprContext::AS() {
  return getToken(PslParser::AS, 0);
}

PslParser::TypeContext* PslParser::EntityExprContext::type() {
  return getRuleContext<PslParser::TypeContext>(0);
}


size_t PslParser::EntityExprContext::getRuleIndex() const {
  return PslParser::RuleEntityExpr;
}


std::any PslParser::EntityExprContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitEntityExpr(this);
  else
    return visitor->visitChildren(this);
}

PslParser::EntityExprContext* PslParser::entityExpr() {
  EntityExprContext *_localctx = _tracker.createInstance<EntityExprContext>(_ctx, getState());
  enterRule(_localctx, 64, PslParser::RuleEntityExpr);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(484);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 74, _ctx)) {
    case 1: {
      setState(480);
      entity();
      break;
    }

    case 2: {
      setState(481);
      normCall();
      break;
    }

    case 3: {
      setState(482);
      linkCall(0);
      break;
    }

    case 4: {
      setState(483);
      entityChain();
      break;
    }

    default:
      break;
    }
    setState(488);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::AS) {
      setState(486);
      match(PslParser::AS);
      setState(487);
      type();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- EntityChainContext ------------------------------------------------------------------

PslParser::EntityChainContext::EntityChainContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<PslParser::IdentRefContext *> PslParser::EntityChainContext::identRef() {
  return getRuleContexts<PslParser::IdentRefContext>();
}

PslParser::IdentRefContext* PslParser::EntityChainContext::identRef(size_t i) {
  return getRuleContext<PslParser::IdentRefContext>(i);
}

std::vector<PslParser::EntityContext *> PslParser::EntityChainContext::entity() {
  return getRuleContexts<PslParser::EntityContext>();
}

PslParser::EntityContext* PslParser::EntityChainContext::entity(size_t i) {
  return getRuleContext<PslParser::EntityContext>(i);
}

std::vector<PslParser::LinkCallContext *> PslParser::EntityChainContext::linkCall() {
  return getRuleContexts<PslParser::LinkCallContext>();
}

PslParser::LinkCallContext* PslParser::EntityChainContext::linkCall(size_t i) {
  return getRuleContext<PslParser::LinkCallContext>(i);
}


size_t PslParser::EntityChainContext::getRuleIndex() const {
  return PslParser::RuleEntityChain;
}


std::any PslParser::EntityChainContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitEntityChain(this);
  else
    return visitor->visitChildren(this);
}

PslParser::EntityChainContext* PslParser::entityChain() {
  EntityChainContext *_localctx = _tracker.createInstance<EntityChainContext>(_ctx, getState());
  enterRule(_localctx, 66, PslParser::RuleEntityChain);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(493); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(493);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 76, _ctx)) {
      case 1: {
        setState(490);
        identRef();
        break;
      }

      case 2: {
        setState(491);
        entity();
        break;
      }

      case 3: {
        setState(492);
        linkCall(0);
        break;
      }

      default:
        break;
      }
      setState(495); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 276971437212829760) != 0));
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- EntityContext ------------------------------------------------------------------

PslParser::EntityContext::EntityContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::IdentRefContext* PslParser::EntityContext::identRef() {
  return getRuleContext<PslParser::IdentRefContext>(0);
}

PslParser::LiteralContext* PslParser::EntityContext::literal() {
  return getRuleContext<PslParser::LiteralContext>(0);
}

PslParser::ListPackContext* PslParser::EntityContext::listPack() {
  return getRuleContext<PslParser::ListPackContext>(0);
}

PslParser::DictPackContext* PslParser::EntityContext::dictPack() {
  return getRuleContext<PslParser::DictPackContext>(0);
}

PslParser::AnnotationContext* PslParser::EntityContext::annotation() {
  return getRuleContext<PslParser::AnnotationContext>(0);
}

PslParser::EntityRefContext* PslParser::EntityContext::entityRef() {
  return getRuleContext<PslParser::EntityRefContext>(0);
}

PslParser::FunctorRefContext* PslParser::EntityContext::functorRef() {
  return getRuleContext<PslParser::FunctorRefContext>(0);
}


size_t PslParser::EntityContext::getRuleIndex() const {
  return PslParser::RuleEntity;
}


std::any PslParser::EntityContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitEntity(this);
  else
    return visitor->visitChildren(this);
}

PslParser::EntityContext* PslParser::entity() {
  EntityContext *_localctx = _tracker.createInstance<EntityContext>(_ctx, getState());
  enterRule(_localctx, 68, PslParser::RuleEntity);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(508);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 80, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(501);
      _errHandler->sync(this);
      switch (_input->LA(1)) {
        case PslParser::IDENTIFIER: {
          setState(497);
          identRef();
          break;
        }

        case PslParser::NULL_:
        case PslParser::TRUE:
        case PslParser::FALSE:
        case PslParser::MULTI_STR:
        case PslParser::STRING:
        case PslParser::FSTRING:
        case PslParser::INTEGER:
        case PslParser::REAL: {
          setState(498);
          literal();
          break;
        }

        case PslParser::T__5: {
          setState(499);
          listPack();
          break;
        }

        case PslParser::T__10: {
          setState(500);
          dictPack();
          break;
        }

      default:
        throw NoViableAltException(this);
      }
      setState(504);
      _errHandler->sync(this);

      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 79, _ctx)) {
      case 1: {
        setState(503);
        annotation();
        break;
      }

      default:
        break;
      }
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(506);
      entityRef();
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(507);
      functorRef();
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NormCallContext ------------------------------------------------------------------

PslParser::NormCallContext::NormCallContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::FunctorRefContext* PslParser::NormCallContext::functorRef() {
  return getRuleContext<PslParser::FunctorRefContext>(0);
}

PslParser::ArgsListContext* PslParser::NormCallContext::argsList() {
  return getRuleContext<PslParser::ArgsListContext>(0);
}


size_t PslParser::NormCallContext::getRuleIndex() const {
  return PslParser::RuleNormCall;
}


std::any PslParser::NormCallContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitNormCall(this);
  else
    return visitor->visitChildren(this);
}

PslParser::NormCallContext* PslParser::normCall() {
  NormCallContext *_localctx = _tracker.createInstance<NormCallContext>(_ctx, getState());
  enterRule(_localctx, 70, PslParser::RuleNormCall);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(510);
    functorRef();
    setState(511);
    argsList();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- LinkCallContext ------------------------------------------------------------------

PslParser::LinkCallContext::LinkCallContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<PslParser::IdentRefContext *> PslParser::LinkCallContext::identRef() {
  return getRuleContexts<PslParser::IdentRefContext>();
}

PslParser::IdentRefContext* PslParser::LinkCallContext::identRef(size_t i) {
  return getRuleContext<PslParser::IdentRefContext>(i);
}

PslParser::EntityRefContext* PslParser::LinkCallContext::entityRef() {
  return getRuleContext<PslParser::EntityRefContext>(0);
}

std::vector<PslParser::EntityContext *> PslParser::LinkCallContext::entity() {
  return getRuleContexts<PslParser::EntityContext>();
}

PslParser::EntityContext* PslParser::LinkCallContext::entity(size_t i) {
  return getRuleContext<PslParser::EntityContext>(i);
}

std::vector<PslParser::FunctorRefContext *> PslParser::LinkCallContext::functorRef() {
  return getRuleContexts<PslParser::FunctorRefContext>();
}

PslParser::FunctorRefContext* PslParser::LinkCallContext::functorRef(size_t i) {
  return getRuleContext<PslParser::FunctorRefContext>(i);
}

std::vector<PslParser::NormCallContext *> PslParser::LinkCallContext::normCall() {
  return getRuleContexts<PslParser::NormCallContext>();
}

PslParser::NormCallContext* PslParser::LinkCallContext::normCall(size_t i) {
  return getRuleContext<PslParser::NormCallContext>(i);
}

PslParser::LinkCallContext* PslParser::LinkCallContext::linkCall() {
  return getRuleContext<PslParser::LinkCallContext>(0);
}


size_t PslParser::LinkCallContext::getRuleIndex() const {
  return PslParser::RuleLinkCall;
}


std::any PslParser::LinkCallContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitLinkCall(this);
  else
    return visitor->visitChildren(this);
}


PslParser::LinkCallContext* PslParser::linkCall() {
   return linkCall(0);
}

PslParser::LinkCallContext* PslParser::linkCall(int precedence) {
  ParserRuleContext *parentContext = _ctx;
  size_t parentState = getState();
  PslParser::LinkCallContext *_localctx = _tracker.createInstance<LinkCallContext>(_ctx, parentState);
  PslParser::LinkCallContext *previousContext = _localctx;
  (void)previousContext; // Silence compiler, in case the context is not used by generated code.
  size_t startState = 72;
  enterRecursionRule(_localctx, 72, PslParser::RuleLinkCall, precedence);

    

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    unrollRecursionContexts(parentContext);
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(533);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 83, _ctx)) {
    case 1: {
      setState(519);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 81, _ctx)) {
      case 1: {
        setState(514);
        identRef();
        break;
      }

      case 2: {
        setState(515);
        entityRef();
        break;
      }

      case 3: {
        setState(516);
        entity();
        break;
      }

      case 4: {
        setState(517);
        functorRef();
        break;
      }

      case 5: {
        setState(518);
        normCall();
        break;
      }

      default:
        break;
      }
      setState(521);
      match(PslParser::T__13);
      setState(526);
      _errHandler->sync(this);
      switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 82, _ctx)) {
      case 1: {
        setState(522);
        identRef();
        break;
      }

      case 2: {
        setState(523);
        functorRef();
        break;
      }

      case 3: {
        setState(524);
        entity();
        break;
      }

      case 4: {
        setState(525);
        normCall();
        break;
      }

      default:
        break;
      }
      break;
    }

    case 2: {
      setState(528);
      identRef();
      break;
    }

    case 3: {
      setState(529);
      entityRef();
      break;
    }

    case 4: {
      setState(530);
      entity();
      break;
    }

    case 5: {
      setState(531);
      functorRef();
      break;
    }

    case 6: {
      setState(532);
      normCall();
      break;
    }

    default:
      break;
    }
    _ctx->stop = _input->LT(-1);
    setState(545);
    _errHandler->sync(this);
    alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 85, _ctx);
    while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
      if (alt == 1) {
        if (!_parseListeners.empty())
          triggerExitRuleEvent();
        previousContext = _localctx;
        _localctx = _tracker.createInstance<LinkCallContext>(parentContext, parentState);
        pushNewRecursionContext(_localctx, startState, RuleLinkCall);
        setState(535);

        if (!(precpred(_ctx, 7))) throw FailedPredicateException(this, "precpred(_ctx, 7)");
        setState(536);
        match(PslParser::T__13);
        setState(541);
        _errHandler->sync(this);
        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 84, _ctx)) {
        case 1: {
          setState(537);
          identRef();
          break;
        }

        case 2: {
          setState(538);
          functorRef();
          break;
        }

        case 3: {
          setState(539);
          entity();
          break;
        }

        case 4: {
          setState(540);
          normCall();
          break;
        }

        default:
          break;
        } 
      }
      setState(547);
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 85, _ctx);
    }
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }
  return _localctx;
}

//----------------- StmtEndContext ------------------------------------------------------------------

PslParser::StmtEndContext::StmtEndContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::SepMarkContext* PslParser::StmtEndContext::sepMark() {
  return getRuleContext<PslParser::SepMarkContext>(0);
}

tree::TerminalNode* PslParser::StmtEndContext::EOF() {
  return getToken(PslParser::EOF, 0);
}


size_t PslParser::StmtEndContext::getRuleIndex() const {
  return PslParser::RuleStmtEnd;
}


std::any PslParser::StmtEndContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitStmtEnd(this);
  else
    return visitor->visitChildren(this);
}

PslParser::StmtEndContext* PslParser::stmtEnd() {
  StmtEndContext *_localctx = _tracker.createInstance<StmtEndContext>(_ctx, getState());
  enterRule(_localctx, 74, PslParser::RuleStmtEnd);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(551);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case PslParser::LINE_END: {
        enterOuterAlt(_localctx, 1);
        setState(548);
        sepMark();
        break;
      }

      case PslParser::T__14: {
        enterOuterAlt(_localctx, 2);
        setState(549);
        match(PslParser::T__14);
        break;
      }

      case PslParser::EOF: {
        enterOuterAlt(_localctx, 3);
        setState(550);
        match(PslParser::EOF);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- SepMarkContext ------------------------------------------------------------------

PslParser::SepMarkContext::SepMarkContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> PslParser::SepMarkContext::LINE_END() {
  return getTokens(PslParser::LINE_END);
}

tree::TerminalNode* PslParser::SepMarkContext::LINE_END(size_t i) {
  return getToken(PslParser::LINE_END, i);
}


size_t PslParser::SepMarkContext::getRuleIndex() const {
  return PslParser::RuleSepMark;
}


std::any PslParser::SepMarkContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitSepMark(this);
  else
    return visitor->visitChildren(this);
}

PslParser::SepMarkContext* PslParser::sepMark() {
  SepMarkContext *_localctx = _tracker.createInstance<SepMarkContext>(_ctx, getState());
  enterRule(_localctx, 76, PslParser::RuleSepMark);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    enterOuterAlt(_localctx, 1);
    setState(554); 
    _errHandler->sync(this);
    alt = 1;
    do {
      switch (alt) {
        case 1: {
              setState(553);
              match(PslParser::LINE_END);
              break;
            }

      default:
        throw NoViableAltException(this);
      }
      setState(556); 
      _errHandler->sync(this);
      alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 87, _ctx);
    } while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- LiteralContext ------------------------------------------------------------------

PslParser::LiteralContext::LiteralContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::ValueContext* PslParser::LiteralContext::value() {
  return getRuleContext<PslParser::ValueContext>(0);
}

tree::TerminalNode* PslParser::LiteralContext::STRING() {
  return getToken(PslParser::STRING, 0);
}

tree::TerminalNode* PslParser::LiteralContext::MULTI_STR() {
  return getToken(PslParser::MULTI_STR, 0);
}

tree::TerminalNode* PslParser::LiteralContext::FSTRING() {
  return getToken(PslParser::FSTRING, 0);
}

tree::TerminalNode* PslParser::LiteralContext::NULL_() {
  return getToken(PslParser::NULL_, 0);
}

tree::TerminalNode* PslParser::LiteralContext::TRUE() {
  return getToken(PslParser::TRUE, 0);
}

tree::TerminalNode* PslParser::LiteralContext::FALSE() {
  return getToken(PslParser::FALSE, 0);
}


size_t PslParser::LiteralContext::getRuleIndex() const {
  return PslParser::RuleLiteral;
}


std::any PslParser::LiteralContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitLiteral(this);
  else
    return visitor->visitChildren(this);
}

PslParser::LiteralContext* PslParser::literal() {
  LiteralContext *_localctx = _tracker.createInstance<LiteralContext>(_ctx, getState());
  enterRule(_localctx, 78, PslParser::RuleLiteral);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(565);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case PslParser::INTEGER:
      case PslParser::REAL: {
        enterOuterAlt(_localctx, 1);
        setState(558);
        value();
        break;
      }

      case PslParser::STRING: {
        enterOuterAlt(_localctx, 2);
        setState(559);
        match(PslParser::STRING);
        break;
      }

      case PslParser::MULTI_STR: {
        enterOuterAlt(_localctx, 3);
        setState(560);
        match(PslParser::MULTI_STR);
        break;
      }

      case PslParser::FSTRING: {
        enterOuterAlt(_localctx, 4);
        setState(561);
        match(PslParser::FSTRING);
        break;
      }

      case PslParser::NULL_: {
        enterOuterAlt(_localctx, 5);
        setState(562);
        match(PslParser::NULL_);
        break;
      }

      case PslParser::TRUE: {
        enterOuterAlt(_localctx, 6);
        setState(563);
        match(PslParser::TRUE);
        break;
      }

      case PslParser::FALSE: {
        enterOuterAlt(_localctx, 7);
        setState(564);
        match(PslParser::FALSE);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ValueContext ------------------------------------------------------------------

PslParser::ValueContext::ValueContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PslParser::ValueContext::INTEGER() {
  return getToken(PslParser::INTEGER, 0);
}

tree::TerminalNode* PslParser::ValueContext::REAL() {
  return getToken(PslParser::REAL, 0);
}

PslParser::ComplexContext* PslParser::ValueContext::complex() {
  return getRuleContext<PslParser::ComplexContext>(0);
}

tree::TerminalNode* PslParser::ValueContext::UNIT() {
  return getToken(PslParser::UNIT, 0);
}


size_t PslParser::ValueContext::getRuleIndex() const {
  return PslParser::RuleValue;
}


std::any PslParser::ValueContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitValue(this);
  else
    return visitor->visitChildren(this);
}

PslParser::ValueContext* PslParser::value() {
  ValueContext *_localctx = _tracker.createInstance<ValueContext>(_ctx, getState());
  enterRule(_localctx, 80, PslParser::RuleValue);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(570);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 89, _ctx)) {
    case 1: {
      setState(567);
      match(PslParser::INTEGER);
      break;
    }

    case 2: {
      setState(568);
      match(PslParser::REAL);
      break;
    }

    case 3: {
      setState(569);
      complex();
      break;
    }

    default:
      break;
    }
    setState(573);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 90, _ctx)) {
    case 1: {
      setState(572);
      match(PslParser::UNIT);
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- TypeContext ------------------------------------------------------------------

PslParser::TypeContext::TypeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::InnerTypeContext* PslParser::TypeContext::innerType() {
  return getRuleContext<PslParser::InnerTypeContext>(0);
}

PslParser::IdentRefContext* PslParser::TypeContext::identRef() {
  return getRuleContext<PslParser::IdentRefContext>(0);
}

tree::TerminalNode* PslParser::TypeContext::ANY_TYPE() {
  return getToken(PslParser::ANY_TYPE, 0);
}


size_t PslParser::TypeContext::getRuleIndex() const {
  return PslParser::RuleType;
}


std::any PslParser::TypeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitType(this);
  else
    return visitor->visitChildren(this);
}

PslParser::TypeContext* PslParser::type() {
  TypeContext *_localctx = _tracker.createInstance<TypeContext>(_ctx, getState());
  enterRule(_localctx, 82, PslParser::RuleType);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(578);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case PslParser::NUMBER_TYPE:
      case PslParser::STRING_TYPE:
      case PslParser::BOOLEAN_TYPE:
      case PslParser::FUNCTOR_TYPE:
      case PslParser::BLOCK_TYPE:
      case PslParser::INTEGER_TYPE:
      case PslParser::REAL_TYPE:
      case PslParser::COMPLEX_TYPE:
      case PslParser::ARRAY_TYPE:
      case PslParser::MATRIX_TYPE:
      case PslParser::LIST_TYPE:
      case PslParser::DICT_TYPE: {
        enterOuterAlt(_localctx, 1);
        setState(575);
        innerType();
        break;
      }

      case PslParser::IDENTIFIER: {
        enterOuterAlt(_localctx, 2);
        setState(576);
        identRef();
        break;
      }

      case PslParser::ANY_TYPE: {
        enterOuterAlt(_localctx, 3);
        setState(577);
        match(PslParser::ANY_TYPE);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- InnerTypeContext ------------------------------------------------------------------

PslParser::InnerTypeContext::InnerTypeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PslParser::InnerTypeContext::NUMBER_TYPE() {
  return getToken(PslParser::NUMBER_TYPE, 0);
}

tree::TerminalNode* PslParser::InnerTypeContext::STRING_TYPE() {
  return getToken(PslParser::STRING_TYPE, 0);
}

tree::TerminalNode* PslParser::InnerTypeContext::BOOLEAN_TYPE() {
  return getToken(PslParser::BOOLEAN_TYPE, 0);
}

tree::TerminalNode* PslParser::InnerTypeContext::FUNCTOR_TYPE() {
  return getToken(PslParser::FUNCTOR_TYPE, 0);
}

tree::TerminalNode* PslParser::InnerTypeContext::BLOCK_TYPE() {
  return getToken(PslParser::BLOCK_TYPE, 0);
}

PslParser::NumberTypeContext* PslParser::InnerTypeContext::numberType() {
  return getRuleContext<PslParser::NumberTypeContext>(0);
}

PslParser::StructTypeContext* PslParser::InnerTypeContext::structType() {
  return getRuleContext<PslParser::StructTypeContext>(0);
}


size_t PslParser::InnerTypeContext::getRuleIndex() const {
  return PslParser::RuleInnerType;
}


std::any PslParser::InnerTypeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitInnerType(this);
  else
    return visitor->visitChildren(this);
}

PslParser::InnerTypeContext* PslParser::innerType() {
  InnerTypeContext *_localctx = _tracker.createInstance<InnerTypeContext>(_ctx, getState());
  enterRule(_localctx, 84, PslParser::RuleInnerType);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(587);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case PslParser::NUMBER_TYPE: {
        enterOuterAlt(_localctx, 1);
        setState(580);
        match(PslParser::NUMBER_TYPE);
        break;
      }

      case PslParser::STRING_TYPE: {
        enterOuterAlt(_localctx, 2);
        setState(581);
        match(PslParser::STRING_TYPE);
        break;
      }

      case PslParser::BOOLEAN_TYPE: {
        enterOuterAlt(_localctx, 3);
        setState(582);
        match(PslParser::BOOLEAN_TYPE);
        break;
      }

      case PslParser::FUNCTOR_TYPE: {
        enterOuterAlt(_localctx, 4);
        setState(583);
        match(PslParser::FUNCTOR_TYPE);
        break;
      }

      case PslParser::BLOCK_TYPE: {
        enterOuterAlt(_localctx, 5);
        setState(584);
        match(PslParser::BLOCK_TYPE);
        break;
      }

      case PslParser::INTEGER_TYPE:
      case PslParser::REAL_TYPE:
      case PslParser::COMPLEX_TYPE:
      case PslParser::ARRAY_TYPE:
      case PslParser::MATRIX_TYPE: {
        enterOuterAlt(_localctx, 6);
        setState(585);
        numberType();
        break;
      }

      case PslParser::LIST_TYPE:
      case PslParser::DICT_TYPE: {
        enterOuterAlt(_localctx, 7);
        setState(586);
        structType();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NumberTypeContext ------------------------------------------------------------------

PslParser::NumberTypeContext::NumberTypeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::ScalarTypeContext* PslParser::NumberTypeContext::scalarType() {
  return getRuleContext<PslParser::ScalarTypeContext>(0);
}

PslParser::VectorTypeContext* PslParser::NumberTypeContext::vectorType() {
  return getRuleContext<PslParser::VectorTypeContext>(0);
}


size_t PslParser::NumberTypeContext::getRuleIndex() const {
  return PslParser::RuleNumberType;
}


std::any PslParser::NumberTypeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitNumberType(this);
  else
    return visitor->visitChildren(this);
}

PslParser::NumberTypeContext* PslParser::numberType() {
  NumberTypeContext *_localctx = _tracker.createInstance<NumberTypeContext>(_ctx, getState());
  enterRule(_localctx, 86, PslParser::RuleNumberType);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(591);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case PslParser::INTEGER_TYPE:
      case PslParser::REAL_TYPE:
      case PslParser::COMPLEX_TYPE: {
        enterOuterAlt(_localctx, 1);
        setState(589);
        scalarType();
        break;
      }

      case PslParser::ARRAY_TYPE:
      case PslParser::MATRIX_TYPE: {
        enterOuterAlt(_localctx, 2);
        setState(590);
        vectorType();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ScalarTypeContext ------------------------------------------------------------------

PslParser::ScalarTypeContext::ScalarTypeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PslParser::ScalarTypeContext::INTEGER_TYPE() {
  return getToken(PslParser::INTEGER_TYPE, 0);
}

tree::TerminalNode* PslParser::ScalarTypeContext::REAL_TYPE() {
  return getToken(PslParser::REAL_TYPE, 0);
}

tree::TerminalNode* PslParser::ScalarTypeContext::COMPLEX_TYPE() {
  return getToken(PslParser::COMPLEX_TYPE, 0);
}


size_t PslParser::ScalarTypeContext::getRuleIndex() const {
  return PslParser::RuleScalarType;
}


std::any PslParser::ScalarTypeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitScalarType(this);
  else
    return visitor->visitChildren(this);
}

PslParser::ScalarTypeContext* PslParser::scalarType() {
  ScalarTypeContext *_localctx = _tracker.createInstance<ScalarTypeContext>(_ctx, getState());
  enterRule(_localctx, 88, PslParser::RuleScalarType);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(593);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 30786325577728) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ComplexContext ------------------------------------------------------------------

PslParser::ComplexContext::ComplexContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<tree::TerminalNode *> PslParser::ComplexContext::INTEGER() {
  return getTokens(PslParser::INTEGER);
}

tree::TerminalNode* PslParser::ComplexContext::INTEGER(size_t i) {
  return getToken(PslParser::INTEGER, i);
}

std::vector<tree::TerminalNode *> PslParser::ComplexContext::REAL() {
  return getTokens(PslParser::REAL);
}

tree::TerminalNode* PslParser::ComplexContext::REAL(size_t i) {
  return getToken(PslParser::REAL, i);
}


size_t PslParser::ComplexContext::getRuleIndex() const {
  return PslParser::RuleComplex;
}


std::any PslParser::ComplexContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitComplex(this);
  else
    return visitor->visitChildren(this);
}

PslParser::ComplexContext* PslParser::complex() {
  ComplexContext *_localctx = _tracker.createInstance<ComplexContext>(_ctx, getState());
  enterRule(_localctx, 90, PslParser::RuleComplex);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(603);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case PslParser::INTEGER: {
        enterOuterAlt(_localctx, 1);
        setState(595);
        match(PslParser::INTEGER);
        setState(596);
        _la = _input->LA(1);
        if (!(_la == PslParser::T__15

        || _la == PslParser::T__16)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(597);
        match(PslParser::INTEGER);
        setState(598);
        match(PslParser::T__17);
        break;
      }

      case PslParser::REAL: {
        enterOuterAlt(_localctx, 2);
        setState(599);
        match(PslParser::REAL);
        setState(600);
        _la = _input->LA(1);
        if (!(_la == PslParser::T__15

        || _la == PslParser::T__16)) {
        _errHandler->recoverInline(this);
        }
        else {
          _errHandler->reportMatch(this);
          consume();
        }
        setState(601);
        match(PslParser::REAL);
        setState(602);
        match(PslParser::T__17);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- VectorTypeContext ------------------------------------------------------------------

PslParser::VectorTypeContext::VectorTypeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PslParser::VectorTypeContext::ARRAY_TYPE() {
  return getToken(PslParser::ARRAY_TYPE, 0);
}

PslParser::ScalarTypeContext* PslParser::VectorTypeContext::scalarType() {
  return getRuleContext<PslParser::ScalarTypeContext>(0);
}

std::vector<tree::TerminalNode *> PslParser::VectorTypeContext::INTEGER() {
  return getTokens(PslParser::INTEGER);
}

tree::TerminalNode* PslParser::VectorTypeContext::INTEGER(size_t i) {
  return getToken(PslParser::INTEGER, i);
}

tree::TerminalNode* PslParser::VectorTypeContext::MATRIX_TYPE() {
  return getToken(PslParser::MATRIX_TYPE, 0);
}


size_t PslParser::VectorTypeContext::getRuleIndex() const {
  return PslParser::RuleVectorType;
}


std::any PslParser::VectorTypeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitVectorType(this);
  else
    return visitor->visitChildren(this);
}

PslParser::VectorTypeContext* PslParser::vectorType() {
  VectorTypeContext *_localctx = _tracker.createInstance<VectorTypeContext>(_ctx, getState());
  enterRule(_localctx, 92, PslParser::RuleVectorType);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    size_t alt;
    setState(632);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case PslParser::ARRAY_TYPE: {
        enterOuterAlt(_localctx, 1);
        setState(605);
        match(PslParser::ARRAY_TYPE);
        setState(610);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == PslParser::T__8) {
          setState(606);
          match(PslParser::T__8);
          setState(607);
          scalarType();
          setState(608);
          match(PslParser::T__9);
        }
        setState(615);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 96, _ctx)) {
        case 1: {
          setState(612);
          match(PslParser::T__5);
          setState(613);
          match(PslParser::INTEGER);
          setState(614);
          match(PslParser::T__6);
          break;
        }

        default:
          break;
        }
        break;
      }

      case PslParser::MATRIX_TYPE: {
        enterOuterAlt(_localctx, 2);
        setState(617);
        match(PslParser::MATRIX_TYPE);
        setState(622);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == PslParser::T__8) {
          setState(618);
          match(PslParser::T__8);
          setState(619);
          scalarType();
          setState(620);
          match(PslParser::T__9);
        }
        setState(629);
        _errHandler->sync(this);
        alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 98, _ctx);
        while (alt != 2 && alt != atn::ATN::INVALID_ALT_NUMBER) {
          if (alt == 1) {
            setState(624);
            match(PslParser::T__5);
            setState(625);
            match(PslParser::INTEGER);
            setState(626);
            match(PslParser::T__6); 
          }
          setState(631);
          _errHandler->sync(this);
          alt = getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 98, _ctx);
        }
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- StructTypeContext ------------------------------------------------------------------

PslParser::StructTypeContext::StructTypeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PslParser::StructTypeContext::LIST_TYPE() {
  return getToken(PslParser::LIST_TYPE, 0);
}

std::vector<PslParser::NullableTypeContext *> PslParser::StructTypeContext::nullableType() {
  return getRuleContexts<PslParser::NullableTypeContext>();
}

PslParser::NullableTypeContext* PslParser::StructTypeContext::nullableType(size_t i) {
  return getRuleContext<PslParser::NullableTypeContext>(i);
}

tree::TerminalNode* PslParser::StructTypeContext::INTEGER() {
  return getToken(PslParser::INTEGER, 0);
}

tree::TerminalNode* PslParser::StructTypeContext::DICT_TYPE() {
  return getToken(PslParser::DICT_TYPE, 0);
}

PslParser::TypeContext* PslParser::StructTypeContext::type() {
  return getRuleContext<PslParser::TypeContext>(0);
}


size_t PslParser::StructTypeContext::getRuleIndex() const {
  return PslParser::RuleStructType;
}


std::any PslParser::StructTypeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitStructType(this);
  else
    return visitor->visitChildren(this);
}

PslParser::StructTypeContext* PslParser::structType() {
  StructTypeContext *_localctx = _tracker.createInstance<StructTypeContext>(_ctx, getState());
  enterRule(_localctx, 94, PslParser::RuleStructType);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(662);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case PslParser::LIST_TYPE: {
        enterOuterAlt(_localctx, 1);
        setState(634);
        match(PslParser::LIST_TYPE);
        setState(646);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == PslParser::T__8) {
          setState(635);
          match(PslParser::T__8);
          setState(636);
          nullableType();
          setState(641);
          _errHandler->sync(this);
          _la = _input->LA(1);
          while (_la == PslParser::T__3) {
            setState(637);
            match(PslParser::T__3);
            setState(638);
            nullableType();
            setState(643);
            _errHandler->sync(this);
            _la = _input->LA(1);
          }
          setState(644);
          match(PslParser::T__9);
        }
        setState(651);
        _errHandler->sync(this);

        switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 102, _ctx)) {
        case 1: {
          setState(648);
          match(PslParser::T__5);
          setState(649);
          match(PslParser::INTEGER);
          setState(650);
          match(PslParser::T__6);
          break;
        }

        default:
          break;
        }
        break;
      }

      case PslParser::DICT_TYPE: {
        enterOuterAlt(_localctx, 2);
        setState(653);
        match(PslParser::DICT_TYPE);
        setState(660);
        _errHandler->sync(this);

        _la = _input->LA(1);
        if (_la == PslParser::T__8) {
          setState(654);
          match(PslParser::T__8);
          setState(655);
          type();
          setState(656);
          match(PslParser::T__3);
          setState(657);
          nullableType();
          setState(658);
          match(PslParser::T__9);
        }
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- NullableTypeContext ------------------------------------------------------------------

PslParser::NullableTypeContext::NullableTypeContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

PslParser::TypeContext* PslParser::NullableTypeContext::type() {
  return getRuleContext<PslParser::TypeContext>(0);
}


size_t PslParser::NullableTypeContext::getRuleIndex() const {
  return PslParser::RuleNullableType;
}


std::any PslParser::NullableTypeContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitNullableType(this);
  else
    return visitor->visitChildren(this);
}

PslParser::NullableTypeContext* PslParser::nullableType() {
  NullableTypeContext *_localctx = _tracker.createInstance<NullableTypeContext>(_ctx, getState());
  enterRule(_localctx, 96, PslParser::RuleNullableType);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(664);
    type();
    setState(666);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == PslParser::T__18) {
      setState(665);
      match(PslParser::T__18);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- IdentRefContext ------------------------------------------------------------------

PslParser::IdentRefContext::IdentRefContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* PslParser::IdentRefContext::IDENTIFIER() {
  return getToken(PslParser::IDENTIFIER, 0);
}


size_t PslParser::IdentRefContext::getRuleIndex() const {
  return PslParser::RuleIdentRef;
}


std::any PslParser::IdentRefContext::accept(tree::ParseTreeVisitor *visitor) {
  if (auto parserVisitor = dynamic_cast<PslVisitor*>(visitor))
    return parserVisitor->visitIdentRef(this);
  else
    return visitor->visitChildren(this);
}

PslParser::IdentRefContext* PslParser::identRef() {
  IdentRefContext *_localctx = _tracker.createInstance<IdentRefContext>(_ctx, getState());
  enterRule(_localctx, 98, PslParser::RuleIdentRef);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(668);
    match(PslParser::IDENTIFIER);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

bool PslParser::sempred(RuleContext *context, size_t ruleIndex, size_t predicateIndex) {
  switch (ruleIndex) {
    case 36: return linkCallSempred(antlrcpp::downCast<LinkCallContext *>(context), predicateIndex);

  default:
    break;
  }
  return true;
}

bool PslParser::linkCallSempred(LinkCallContext *_localctx, size_t predicateIndex) {
  switch (predicateIndex) {
    case 0: return precpred(_ctx, 7);

  default:
    break;
  }
  return true;
}

void PslParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  pslParserInitialize();
#else
  ::antlr4::internal::call_once(pslParserOnceFlag, pslParserInitialize);
#endif
}
