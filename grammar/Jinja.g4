grammar Jinja;

program: statement+ EOF;

statement
    : evaluation_statement + NEWLINE
    | body
    ;

expression
    : ID
    ;

evaluation_statement
    : '{{'expression'}}'
    ;

body: TEXT;

ID: ([a-z] | [A-Z] | [0-9] | '_')+ ;

TEXT: ([a-z] | [A-Z] | [0-9] | WS)+ ;

WS: [ \t]+;
COMMENT: '{#' .*? '#}' NEWLINE ->skip;
NEWLINE: [\r\n]+ ;
