grammar Jinja;

program: statement+ EOF ;

statement
    : evaluation_statement
    ;



expression
    : '(' expression ')'                                        #eqPar
    | evaluation_statement                                      #eqEvaluation
    | left = expression operator = (MUL|DIV) right = expression #eqMUL
    | left = expression operator = (ADD|SUB) right = expression #eqAdd
    | ID                                                        #eqVar
    | DOUBLE                                                    #eqDbl
    | INT                                                       #eqInt
    | STRING                                                    #eqStr
    ;



evaluation_statement: ID '{{' arguments_list? '}}' NEWLINE*;
arguments_list: expression;



INT: '-'? DIGIT+ ;

DOUBLE: '-'? DIGIT+ '.' DIGIT+
    | '-'? '.' DIGIT+
    ;


COMMENT: '{#' .*? '#}' NEWLINE ->skip;

ID: ([a-z]) ([a-z] | [A-Z] | [0-9] | '_')* ;



MUL: '*';
DIV: '/';
SUB: '-';
ADD: '+';

STRING : '"' (ESC|.)*? '"' ;

NEWLINE: [\r\n]+ ;

WS: [ \t]+ -> skip;

fragment
ESC: '\\"'|'\\\\';
DIGIT: [0-9];
