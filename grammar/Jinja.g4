grammar Jinja;

program: statement+ EOF;

statement
    : evaluation_statement
    | body
    ;

expression
    : left = expression operator = (MUL|DIV) right = expression #eqMUL
    | left = expression operator = (ADD|SUB) right = expression #eqAdd
    | DOUBLE                                                    #eqDbl
    | INT                                                       #eqInt
    | STRING                                                    #eqStr
    | ID                                                        #eqVar
    ;

evaluation_statement : '{{'expression'}}';

ID: ([a-zA-Z]) ([a-z] | [A-Z] | [0-9] | '_')* ;

INT: '-'? DIGIT+ ;
DOUBLE: '-'? DIGIT+ '.' DIGIT+
    | '-'? '.' DIGIT+
    ;

MUL: '*';
DIV: '/';
SUB: '-';
ADD: '+';

STRING : '\'' (ESC|.)*? '\'' ;

WS: [ \t]+;

NEWLINE: [\r\n]+ ;

COMMENT: '{#' .*? '#}' NEWLINE ->skip;


body: CONTENTS;
CONTENTS: ANY+ ;
SYMBOLS: ('_'| ')' | '<' | '>' | '/' | '='| ':'| ';' | '"');
ANY : ([a-z] |DIGIT| [A-Z] | SYMBOLS | WS| NEWLINE)+;
fragment
ESC: '\\"'|'\\\\';
fragment
DIGIT: [0-9];
