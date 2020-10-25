grammar Indent;

tokens { INDENT, DEDENT }

program
: commands* EOF
;

commands
: inden=(INDENT|DEDENT)* var=VARIABLE (TABS)* NEWLINE  # commandExpr
| (TABS)* NEWLINE                                      # commandNewline
;

NEWLINE
: '\n'
;

VARIABLE
: [a-z]+
;

TABS
: '-'
;
