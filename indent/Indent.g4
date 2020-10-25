grammar Indent;

tokens { INDENT, DEDENT }

program
: commands* EOF
;

commands
: inden=(INDENT|DEDENT)                        # commandExpr
| var=VARIABLE NEWLINE                         # commandExpr
| 'if' NEWLINE INDENT var=VARIABLE NEWLINE     # commandIf
| 'if' NEWLINE INDENT trueP=VARIABLE NEWLINE
  DEDENT 'else' NEWLINE INDENT falseP=VARIABLE   # commandIf
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
