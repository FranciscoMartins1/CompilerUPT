import ply.lex as lex
import ply.yacc as yacc

# TOKENS
tokens = (
    'NUMBER','PLUS', 'MINUS', 'TIMES', 'DIV', 
    'EQUALS','ASSIGN','VOID','GREATER', 'LESS', 
    'EXPO','DIF', 'LESS_EQUAL', 'GREATER_EQUAL',
    'PAR_OPEN', 'PAR_CLOSE', 'LBRACE', 'RBRACE', 
    'SEMICOLON', 'COLON','IF', 'ELSE', 'WHILE', 
    'PROGRAM', 'FUNCTION','INT', 'BOOL', 'VAR', 
    'TO', 'TRUE', 'FALSE', 'BREAK','PRINT', 
    'READ', 'RETURN', 'OR', 'NOT', 'AND','ID', 
    'FOR' , 'COMMA' , 'MOD'
)
reserved = {
    'program': 'PROGRAM',
    'function': 'FUNCTION',
    'int': 'INT',
    'bool': 'BOOL',
    'void': 'VOID',
    'var': 'VAR',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'to': 'TO',
    'true': 'TRUE',
    'false': 'FALSE',
    'break': 'BREAK',
    'print': 'PRINT',
    'read': 'READ',
    'return': 'RETURN',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT'
}

# REGULAR EXPRESSIONS
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_MOD = r'%'
t_DIV = r'/'
t_EQUALS = r'=='
t_ASSIGN = r'='
t_GREATER = r'>'
t_LESS = r'<'
t_EXPO = r'\*\*'
t_DIF = r'!='
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_PAR_OPEN = r'\('
t_PAR_CLOSE = r'\)'
t_ignore = ' \t'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_COLON = r':'
t_COMMA = r','


# COUNT LINES isto faz com que ele encontre as novas linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    #t.lexer.lineno += 1 isto se tiver mais que uma linha em \n so conta como um


# token vai buscar pelas reserved words e se nao existir é um ID
def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID') #procura nas reserved pelo codigo se nao existir é um ID
    return t


# NUMBERS se for um numero entra neste codigo
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#. dá match a qualquer caratere exeto mudança de linhas
#Ignore comments
def t_Coment(t):
    r'\#.*'
    pass



#Ignore multi line comments
def t_CommentMultiLine(t):
    #r'\*(?:.|\n)*?\*'
    #r'\(\*(?:.|\n)*\*\)'
    r'\(\*[\s\S]*?\*\)'
    pass

# ERROR HANDLING caso encontre algum erro
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)




#t -> (tokens)varios tokens p -> (parser) apanha tudo e coloca tudo junto

# p -> parse junta as palavras e ve se fazem sentido juntas


#programs
#commands
#expressions
#declarations




#PROGRAMS

def p_Program(p):
    '''Program : ProgramHeader ProgramBody'''
    p[0] = ('Program', p[1], p[2])

def p_ProgramHeader(p):
    '''ProgramHeader : PROGRAM ID SEMICOLON'''
    p[0] = ('ProgramHeader', p[2])

def p_ProgramBody(p):
    '''ProgramBody : FuncDecls VarDecls Cmd'''
    p[0] = ('ProgramBody', p[1], p[2], p[3])

def p_FuncDecls(p):
    '''FuncDecls : empty
                | Function FuncDecls'''
    if len(p) == 2:
        p[0] = ('FuncDecls', p[1])
    elif len(p) == 3:
        p[0] = ('FuncDecls', p[1], p[2])
    else:
        raise Exception("Bad function declarations")
    
    

#cmd + shift + 7 para comentar mais que uma linha de codigo

#FUNCTIONS
def p_Function(p):
    '''Function : FunctionHeader FunctionBody'''
    p[0] = ('Function', p[1], p[2])

def p_FunctionHeader(p):
    '''FunctionHeader : FunctionType FUNCTION ID PAR_OPEN ParamList PAR_CLOSE COLON'''
    p[0] = ('FunctionHeader', p[1], p[3], p[5])

def p_FunctionType(p):
    '''FunctionType : INT
                    | BOOL
                    | VOID''' 
    p[0] = ('FunctionType', p[1])

def p_FunctionBody(p):
    '''FunctionBody : LBRACE VarDecls CmdList RBRACE'''
    p[0] = ('FunctionBody', p[2], p[3])

def p_ParamList(p):
    '''ParamList : empty
                | ParamList1'''
    p[0] = ('ParamList', p[1])


def p_ParamList1(p):
    '''ParamList1 : Param COMMA ParamList1
                    | Param '''
    if len(p) == 2:
        p[0] = ('ParamList1', p[1])
    elif len(p) == 4:
        p[0] = ('ParamList1', p[1], p[3])
    else:
        raise Exception("Bad param list1")


def p_Param(p):
    '''Param : ID COLON Type'''
    p[0] = ('Param', p[1], p[3])



def p_empty(p):
    'empty :'
    pass

def p_VarDecls(p): 
    '''VarDecls : empty
                | VarDecl VarDecls '''
    if len(p) == 2:
        p[0] = ('VarDecls', p[1])
    elif len(p) == 3:
        p[0] = ('VarDecls', p[1], p[2])
    else:
        raise Exception("Bad var declaration")


def p_VarDecl(p): 
    '''VarDecl : VAR ID COLON Type SEMICOLON'''
    p[0] = ('VarDecl', p[2], p[4])


def p_Type(p): 
    '''Type : INT
            | BOOL'''     
    p[0] = ('Type', p[1])

def p_Expr(p): 
    '''Expr : NUMBER
            | TRUE
            | FALSE
            | ID
            | Expr BinOp Expr
            | UnOp Expr
            | PAR_OPEN Expr PAR_CLOSE
            | ID PAR_OPEN ExprList PAR_CLOSE
            | READ PAR_OPEN PAR_CLOSE'''
    if len(p) == 2:
        p[0] = ('Expr', p.slice[1].type , p[1]) # Adicionei p.slice[1].type
    elif len(p) == 3:
        p[0] = ('Expr', p[1], p[2]) 
    elif len(p) == 4 and p[2][0] == 'BinOp': # verifica Expr BinOp Expr
        p[0] = ('Expr', p[1],p [2], p[3])
    elif len(p) == 4 and p[1] == 'read': # verifica READ PAR_OPEN PAR_CLOSE
        p[0] = ('Expr', p[1])
    elif len(p) == 4 and p[1] == '(' and p[3] == ')': # verifica PAR_OPEN Expr PAR_CLOSE
        p[0] = ('Expr', p[2])    
    elif len(p) == 5 : 
        p[0] = ('Expr', p[1], p[3])
    else:
        raise Exception("Bad expression")
    



def p_BinOp(p): 
    '''BinOp : PLUS
            | MINUS
            | TIMES
            | EXPO 
            | MOD
            | DIF
            | EQUALS
            | LESS
            | GREATER
            | LESS_EQUAL
            | GREATER_EQUAL
            | AND
            | OR'''
    p[0] = ('BinOp', p[1])

def p_UnOp(p): 
    '''UnOp : MINUS
            | NOT'''
    p[0] = ('UnOp', p[1])

def p_ExprList(p): 
    '''ExprList : empty
                | ExprList1'''
    p[0] = ('ExprList', p[1]) 


def p_ExprList1(p): 
    '''ExprList1 : Expr
                | Expr COMMA ExprList1'''
    if len(p) == 2:
        p[0] = ('ExprList1', p[1]) 
    elif len(p) == 4:
        p[0] = ('ExprList1', p[1], p[3])
    else:
        raise Exception("Bad expression list")


def p_Cmd(p):
    '''Cmd : CmdAtrib
            | CmdIf
            | CmdWhile
            | CmdFor
            | CmdBreak
            | CmdPrint
            | CmdReturn
            | CmdSeq'''

    p[0] = ('Cmd', p[1])

def p_CmdAtrib(p):
    '''CmdAtrib : ID
                | Expr
                | ID ASSIGN Expr'''
    if len(p) == 2:
        p[0] = ('CmdAtrib', p[1])
    elif len(p) == 4:
        p[0] = ('CmdAtrib', p[1], p[3])
    else:
        raise Exception("Bad command attribute")

def p_CmdIf(p):
    '''CmdIf : IF Expr COLON Cmd 
            | IF Expr COLON Cmd ELSE COLON'''
    p[0] = ('CmdIf', p[2],p[4])

    
def p_CmdWhile(p):
    '''CmdWhile : WHILE Expr COLON Cmd'''
    p[0] = ('CmdWhile', p[2], p[4])

def p_CmdFor(p):
    '''CmdFor : FOR CmdAtrib TO Expr COLON Cmd'''
    p[0] = ('CmdFor', p[2], p[4], p[6])

def p_CmdBreak(p):
    '''CmdBreak : BREAK'''
    p[0] = ('CmdBreak', p[1])

def p_CmdPrint(p):
    '''CmdPrint : PRINT PAR_OPEN ExprList PAR_CLOSE '''
    p[0] = ('CmdPrint', p[1],p[3])

def p_CmdReturn(p):
    '''CmdReturn : RETURN Expr'''
    p[0] = ('CmdReturn', p[2])

def p_CmdSeq(p):
    '''CmdSeq : LBRACE CmdList RBRACE'''
    p[0] = ('CmdSeq', p[2])

def p_CmdList(p):
    '''CmdList : Cmd SEMICOLON CmdList
                | Cmd'''
    if len(p) == 2:
        p[0] = ('CmdList', p[1])
    elif len(p) == 4:
        p[0] = ('CmdList', p[1], p[3])
    else:
        raise Exception("Bad command list")

#tuples é uma lista 

def p_error(p):
    raise Exception("Syntax error at position:'%s' line:'%s' type:'%s' value:'%s'" % (p.lexpos, p.lineno, p.type, p.value))
#estas exceptions faz com que o programa parta e diga o que aconteceu
# exemplo SEMICOLON SEMICOLON , o programa nao aceita e manda uma exceção (print do erro)




def parse(data):
    lexer = lex.lex() # vai buscar palavra a palavra // lexico
    parser = yacc.yacc() # sintatico
    result = parser.parse(data) # retorna o resultado que aparece no terminal
    return result


