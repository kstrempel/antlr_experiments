grammar Math;

formula
: expression EOF
;

expression
: '(' expression ')'                                  # parensExpr
| left=expression op=('*'|'/') right=expression       # infixExpr
| left=expression op=('+'|'-') right=expression       # infixExpr
| value=NUMBER                                        # numberExpr
;

END
: ';'
;

DIV
: '/'
;


TIMES
: '*'
;

ADD
: '+'
;

MINUS
: '-'
;


NUMBER
: '0' | [1-9][0-9]*
;

WS
: [ \r\n\t] + -> skip
;