grammar Psl;
import PslLexerRules;

program : stmtList? ;

stmtList : (sepMark? stmt)+ ;

stmt : letStmt
     | useStmt
     | funcDef
     | typeDef
     | enumDef
     | retStmt
     | exprStmt
     ;

letStmt : LET carrier (':' type)? '='? entityExpr stmtEnd ;
useStmt : USE carrier '='? entityExpr stmtEnd ;
withDef : WITH (identRef | withDecl) LINE_END? ;
funcDef : annotations withDef? modifiers FUNC identRef paramDef (':' type)? '='? LINE_END? stmtPack stmtEnd ;
typeDef : TYPE identRef '='? (type | typePack) stmtEnd ;
enumDef : ENUM identRef '='? dictUnpack stmtEnd ;
retStmt : RETURN entityExpr? stmtEnd ;
exprStmt : annotations entityExpr stmtEnd ;

carrier : entityRef
        | listUnpack
        | dictUnpack
        ;

biasAnno : '(' INTEGER ',' INTEGER ')' ;
sizeAnno : '[' INTEGER ',' INTEGER ']' ;
annotation : '@' (identRef | dictPack | biasAnno | sizeAnno) ;
annotations : (annotation LINE_END)* ;
modifiers : (INNER | SYNC | SCOPED | STATIC | ATOMIC)* ;
withList : '<' sepMark? argument (',' sepMark? argument)* sepMark? '>' ;
withDecl : '<' sepMark? keyValDecl (',' sepMark? keyValDecl)* sepMark? '>' ;
paramDef : '(' sepMark? (keyValDecl (',' sepMark? keyValDecl)*)? sepMark? ')' ;
argument : entityExpr
         | keyValExpr
         ;

typePack : '{' sepMark? (keyValDecl (',' sepMark? keyValDecl)*)? sepMark? '}' ;
keyValDecl : identRef (annotation)? ':' nullableType ('=' entityExpr)? ;
keyValExpr : identRef '=' entityExpr ;

entityRef : identRef (('[' (INTEGER | identRef) ']')* | '.' (INTEGER | identRef)) ;
listUnpack : '[' sepMark? (identRef (',' sepMark? identRef)*)? sepMark? ']' ;
dictUnpack : '{' sepMark? (identRef (',' sepMark? identRef)*)? sepMark? '}' ;
dictPack : '{' sepMark? (keyValExpr (',' sepMark? keyValExpr)*)? sepMark? '}' ;
listPack : '[' sepMark? (entityExpr (',' sepMark? entityExpr)*)? sepMark? ']' ;
stmtPack : '{' stmtList? sepMark? '}' ;

entityExpr : entityChain (AS type)? ;
entityChain : chainUnit+ ;
chainUnit : entity
          | linkCall
          ;
entity : (entityRef | functorRef | literal | listPack | dictPack) annotation? ;
linkCall : linkCall '->' entity
          | functorRef argsList
          | entity
          ;
functorRef: identRef (withList)? ;

stmtEnd : sepMark | ';' | EOF ;
sepMark : (LINE_END)+ ;


argsList : '(' sepMark? (argument (',' sepMark? argument)*)? sepMark? ')' ;


literal : value
        | STRING
        | MULTI_STR
        | FSTRING
        | NULL
        | TRUE
        | FALSE
        ;
value : (INTEGER | REAL | COMPLEX) UNIT? ;


type : innerType
     | identRef
     | ANY_TYPE
     ;

innerType : NUMBER_TYPE
          | STRING_TYPE
          | BOOLEAN_TYPE
          | FUNCTOR_TYPE
          | BLOCK_TYPE
          | numberType
          | structType
          ;
numberType : scalarType
           | vectorType
           ;
scalarType : INTEGER_TYPE
           | REAL_TYPE
           | COMPLEX_TYPE
           ;
vectorType : ARRAY_TYPE ('<' scalarType '>')? ('[' INTEGER ']')?
           | MATRIX_TYPE ('<' scalarType '>')? ('[' INTEGER']')*
              ;
structType : LIST_TYPE ('<' nullableType (',' nullableType)* '>')? ('[' INTEGER ']')?
           | DICT_TYPE ('<' type ',' nullableType '>')?
           ;
nullableType : type '?'? ;

identRef : IDENTIFIER ;
