grammar Python;

prog: (function | variable)+ EOF;

expr: ID | NUMBER;

function: main_function | built_function | custom_function;

main_function: MAIN_FUNCTION;
custom_function: FUNCTION expr;
built_function: print;

variable: var_decl | var_assign;

var_decl: VARIABLE_DECLARATIONS expr VARIABLE_TYPE;
var_assign: expr ASSIGN expr;

print: PRINT expr
    | PRINT VARIABLE_TYPE expr
    ;

TAB : '<TAB>' -> skip;
VARIABLE_DECLARATIONS : '<VAR_DECLARATION>';
VARIABLE_TYPE : '<INT>' | '<STRING>';
PRINT : '<PRINT>';
SCAN : '<SCAN>';
FUNCTION : '<FUNC>';
MAIN_FUNCTION : '<BASE_FUNC>';
IF : '<IF>';
IF_TRUE_START : '<IF_TRUE>';
IF_TRUE_END : '</IF_TRUE>';
IF_FALSE_START : '<IF_FALSE>';
IF_FALSE_END : '</IF_FALSE>';
END_CODE : '<END>' -> skip;

PLUS : '+';
MINUS : '-';
MULT : '*';
DIV : '/';

AND : '&&';
OR : '||';
NOT : '!';

GT : '>';
LET : '<';
GEQ : '>=';
LEQ : '<=';
EQ : '==';
NEQ : '!=';

ASSIGN : '=';

ID : [a-zA-Z_][a-zA-Z0-9_]*;
// todo: agregar strings
NUMBER : [0-9]+;

WS : [ \t\n]+ -> skip;