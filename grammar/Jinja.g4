grammar Jinja;

program: statement*? EOF;

statement
    : evaluation_statement
    | body
    | if_statement
    | assignment_statement
    | while_statement
    ;

assignment_statement
    : SET_BLOCK '('ID'='expression')' BLOCK_END NEWLINE?
    ;
expression
    : '(' expression ')'                                               #eqPar
    | left = expression operator = (MUL|DIV) right = expression        #eqMUL
    | left = expression operator = (ADD|SUB) right = expression        #eqAdd
    | DOUBLE                                                           #eqDbl
    | INT                                                              #eqInt
    | STRING                                                           #eqStr
    | ID                                                               #eqVar
    ;

boolean_expression
    : '(' boolean_expression ')'                                               #eqBoolPar
    | left = expression operator=(GT|GTEQ|LT|LTEQ) right = expression          #relationExpr
    | left = expression operator=(EQ|NEQ) right = expression                   #boolEq
    | BOOL                                                                     #eqBool
    ;

evaluation_statement
    : '{{'expression'}}'
    | '{{'boolean_expression'}}'
    ;



if_statement
    : if_fragment code_block (elif_statement | else_statement)? endif_fragment
    ;
elif_statement: elif_fragment code_block (elif_statement | else_statement)? ;
else_statement: else_fragment code_block ;

if_fragment: IF '('boolean_expression')' BLOCK_END NEWLINE? ;
elif_fragment: ELIF '('boolean_expression')' BLOCK_END NEWLINE?;
else_fragment: ELSE NEWLINE? ;
endif_fragment: ENDIF NEWLINE?;
code_block: NEWLINE? body NEWLINE?;

while_statement: while_fragment statement*? endwhile_fragment ;

while_fragment: WHILE '('boolean_expression')' BLOCK_END NEWLINE? ;
endwhile_fragment: END_WHILE NEWLINE?;

body: contents;
contents
    : html_element
    | TEXT+
    ;

html_element: HTML_TAG_OPEN statement+ NEWLINE*? HTML_TAG_CLOSE;


HTML_TAG_OPEN: '<'ID'>' NEWLINE?;
HTML_TAG_CLOSE: '</'ID'>'NEWLINE?;
ID: ([a-z]) ([a-z] | [A-Z] | [0-9] | '_')* ;

INT: '-'? DIGIT+ ;
DOUBLE: '-'? DIGIT+ '.' DIGIT+
    | '-'? '.' DIGIT+
    ;

STRING : '\'' (ESC|.)*? '\'' ;
BOOL : TRUE | FALSE;



ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
NOT : 'NOT';
TRUE : 'True';
FALSE : 'False';
EQ: '==';
NEQ: '!=';

GT : '>';
LT : '<';
GTEQ : '>=';
LTEQ : '<=';


IF : '{% if';
ELIF: '{% elif';
ENDIF: '{% endif %}';
BLOCK_START: '{%';
BLOCK_END: '%}';
ELSE : '{% else %}';
WHILE : '{% while';
END_WHILE: '{% endwhile %}';
SET_BLOCK: '{% set';

WS: [ \t]->skip;

NEWLINE: [\r\n]+;

COMMENT: '{#' .*? '#}' NEWLINE ->skip;

SYMBOLS: ('_'  | '/' | ';' | '="' | '"');
TEXT : ([a-zA-Z0-9] | SYMBOLS |NEWLINE | [ \t])+;

fragment
ESC: '\\"'|'\\\\';
fragment
DIGIT: [0-9];
