grammar Indent;

tokens { INDENT, DEDENT }

program
: commands* EOF
;

commands
: inden=(INDENT|DEDENT)                        # commandExpr
| var=VARIABLE NEWLINE                         # commandExpr
| NEWLINE                                      # commandEmptyLine
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
