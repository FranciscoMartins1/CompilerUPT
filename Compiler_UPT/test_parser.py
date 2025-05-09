from parser import parse
import pytest

#pytest os def test tem de começar por test no inicio do metodo

def test_data1():
    data = '''
    program count;
        var i: int;
        { i = 1;
        while i <= 10: {
        print(i);
        i = i + 1
        }
        }
    '''
    result = parse(data)
    print(result)
    assert "('Program', ('ProgramHeader', 'count'), ('ProgramBody', ('FuncDecls', None), ('VarDecls', ('VarDecl', 'i', ('Type', 'int')), ('VarDecls', None)), ('Cmd', ('CmdSeq', ('CmdList', ('Cmd', ('CmdAtrib', 'i', ('Expr', 'NUMBER', 1))), ('CmdList', ('Cmd', ('CmdWhile', ('Expr', ('Expr', 'ID', 'i'), ('BinOp', '<='), ('Expr', 'NUMBER', 10)), ('Cmd', ('CmdSeq', ('CmdList', ('Cmd', ('CmdPrint', 'print', ('ExprList', ('ExprList1', ('Expr', 'ID', 'i'))))), ('CmdList', ('Cmd', ('CmdAtrib', 'i', ('Expr', ('Expr', 'ID', 'i'), ('BinOp', '+'), ('Expr', 'NUMBER', 1))))))))))))))))"== str(result)

#test_data1()


def test_data2():
    data = '''
    program count_for;
        for i = 1 to 10 :
        print(i)
    '''
    result = parse(data)
    print(result)
    assert "('Program', ('ProgramHeader', 'count_for'), ('ProgramBody', ('FuncDecls', None), ('VarDecls', None), ('Cmd', ('CmdFor', ('CmdAtrib', 'i', ('Expr', 'NUMBER', 1)), ('Expr', 'NUMBER', 10), ('Cmd', ('CmdPrint', 'print', ('ExprList', ('ExprList1', ('Expr', 'ID', 'i')))))))))" == str(result)
#test_data2()

def test_data3():
    data = '''
    program square_sum ;
        var s : int;
        var n : int;
        var max : int;
        {
        max = read();
        n = 1;
        while n <= max:
        {
        s = s + n*n;
        n = n + 1
        };
        print(s)
        }
'''
    result = parse(data)
    print(result)
    assert "('Program', ('ProgramHeader', 'square_sum'), ('ProgramBody', ('FuncDecls', None), ('VarDecls', ('VarDecl', 's', ('Type', 'int')), ('VarDecls', ('VarDecl', 'n', ('Type', 'int')), ('VarDecls', ('VarDecl', 'max', ('Type', 'int')), ('VarDecls', None)))), ('Cmd', ('CmdSeq', ('CmdList', ('Cmd', ('CmdAtrib', 'max', ('Expr', 'read'))), ('CmdList', ('Cmd', ('CmdAtrib', 'n', ('Expr', 'NUMBER', 1))), ('CmdList', ('Cmd', ('CmdWhile', ('Expr', ('Expr', 'ID', 'n'), ('BinOp', '<='), ('Expr', 'ID', 'max')), ('Cmd', ('CmdSeq', ('CmdList', ('Cmd', ('CmdAtrib', 's', ('Expr', ('Expr', 'ID', 's'), ('BinOp', '+'), ('Expr', ('Expr', 'ID', 'n'), ('BinOp', '*'), ('Expr', 'ID', 'n'))))), ('CmdList', ('Cmd', ('CmdAtrib', 'n', ('Expr', ('Expr', 'ID', 'n'), ('BinOp', '+'), ('Expr', 'NUMBER', 1)))))))))), ('CmdList', ('Cmd', ('CmdPrint', 'print', ('ExprList', ('ExprList1', ('Expr', 'ID', 's')))))))))))))" == str(result)

#test_data3()

def test_data4():
    data = '''
    program fact_iter ;
        var p : int ;
        var n : int ;
        {
        p = 1;
        n = read();
        while (n > 0):
        {
        p = p * n; n = n - 1
        };
        print(p)
        }
    '''
    result = parse(data)
    print(result)
    assert "('Program', ('ProgramHeader', 'fact_iter'), ('ProgramBody', ('FuncDecls', None), ('VarDecls', ('VarDecl', 'p', ('Type', 'int')), ('VarDecls', ('VarDecl', 'n', ('Type', 'int')), ('VarDecls', None))), ('Cmd', ('CmdSeq', ('CmdList', ('Cmd', ('CmdAtrib', 'p', ('Expr', 'NUMBER', 1))), ('CmdList', ('Cmd', ('CmdAtrib', 'n', ('Expr', 'read'))), ('CmdList', ('Cmd', ('CmdWhile', ('Expr', ('Expr', ('Expr', 'ID', 'n'), ('BinOp', '>'), ('Expr', 'NUMBER', 0))), ('Cmd', ('CmdSeq', ('CmdList', ('Cmd', ('CmdAtrib', 'p', ('Expr', ('Expr', 'ID', 'p'), ('BinOp', '*'), ('Expr', 'ID', 'n')))), ('CmdList', ('Cmd', ('CmdAtrib', 'n', ('Expr', ('Expr', 'ID', 'n'), ('BinOp', '-'), ('Expr', 'NUMBER', 1)))))))))), ('CmdList', ('Cmd', ('CmdPrint', 'print', ('ExprList', ('ExprList1', ('Expr', 'ID', 'p')))))))))))))" == str(result)
#test_data4()


def test_data5():
    data = '''
    program fact_rec ;
        int function fact( x: int ): {
        var p : int;
        p = 1 ;
        while x > 1:
        { p = p * x;
        x = x - 1
        };
        return p
        }
        var n : int;
        {
        n = read();
        print(fact(n))
        }
    '''
    result = parse(data)
    print(result)
    assert "('Program', ('ProgramHeader', 'fact_rec'), ('ProgramBody', ('FuncDecls', ('Function', ('FunctionHeader', ('FunctionType', 'int'), 'fact', ('ParamList', ('ParamList1', ('Param', 'x', ('Type', 'int'))))), ('FunctionBody', ('VarDecls', ('VarDecl', 'p', ('Type', 'int')), ('VarDecls', None)), ('CmdList', ('Cmd', ('CmdAtrib', 'p', ('Expr', 'NUMBER', 1))), ('CmdList', ('Cmd', ('CmdWhile', ('Expr', ('Expr', 'ID', 'x'), ('BinOp', '>'), ('Expr', 'NUMBER', 1)), ('Cmd', ('CmdSeq', ('CmdList', ('Cmd', ('CmdAtrib', 'p', ('Expr', ('Expr', 'ID', 'p'), ('BinOp', '*'), ('Expr', 'ID', 'x')))), ('CmdList', ('Cmd', ('CmdAtrib', 'x', ('Expr', ('Expr', 'ID', 'x'), ('BinOp', '-'), ('Expr', 'NUMBER', 1)))))))))), ('CmdList', ('Cmd', ('CmdReturn', ('Expr', 'ID', 'p')))))))), ('FuncDecls', None)), ('VarDecls', ('VarDecl', 'n', ('Type', 'int')), ('VarDecls', None)), ('Cmd', ('CmdSeq', ('CmdList', ('Cmd', ('CmdAtrib', 'n', ('Expr', 'read'))), ('CmdList', ('Cmd', ('CmdPrint', 'print', ('ExprList', ('ExprList1', ('Expr', 'fact', ('ExprList', ('ExprList1', ('Expr', 'ID', 'n'))))))))))))))" == str(result)
#test_data5()


def test_NonValid1():
    data = '''
    program error1
        {
        var x : int;
        x = 1;
        print(x)
        }
        '''

    #No with verifica se o programa manda uma exceção
    #este run vai ser bem sucedido pq vai haver uma exceçao    

    #result = parse(data)
    #print(result) 
    with pytest.raises(Exception) as exception_info: #guarda a exceçao que vai acontecer no parse dentro da variavel exception_info
        parse(data) # corre o programa
    assert exception_info.value.args[0] == "Syntax error at position:'28' line:'3' type:'LBRACE' value:'{'" # isto é o erro que da quando corre o programa
    #Erro porque falta um SEMICOLON no ProgramHeader
#test_NonValid1()


def test_NonValid2():
    data = '''
    program error2 ;
        {
        var x : int;
        x = 1;
        print(x)
        }
    '''
    
    #result = parse(data)
    #print(result)

    with pytest.raises(Exception) as exception_info:
        parse(data)
    assert exception_info.value.args[0] == "Syntax error at position:'40' line:'4' type:'VAR' value:'var'"
    #Erro porque nao da para declarar nenhuma variavel depois dos {}
#test_NonValid2()


def test_NonValid3():
    data = '''
    program error3 ;
        var x : int;
        void dummy ( ) :
        {
        print (1)
        }
        {
        x = 1;
        print(x)
        }
'''

    #result = parse(data)
    #print(result)

    with pytest.raises(Exception) as exception_info:
        parse(data)
    assert exception_info.value.args[0] == "Syntax error at position:'51' line:'4' type:'VOID' value:'void'"
    #Erro porque nao esta declarado o nome function entre void e dummy
#test_NonValid3()




def test_NonValid4():
    data = '''
    program error4 ;
        int dummy () :
        {
        print (1)
        }
        var x : int
        {
        x = 1;
        print(x)
        };
'''
    #result = parse(data)
    #print(result)
    with pytest.raises(Exception) as exception_info:
        parse(data)
    assert exception_info.value.args[0] =="Syntax error at position:'34' line:'3' type:'ID' value:'dummy'"
    #Erro porque nao esta declarado o nome function entre int e dummy
#test_NonValid4()


#testing read func

def test_read():
    data = '''
    program count_for;
        data()
    '''
    result = parse(data)
    print(result)
    assert "('Program', ('ProgramHeader', 'count_for'), ('ProgramBody', ('FuncDecls', None), ('VarDecls', None), ('Cmd', ('CmdAtrib', ('Expr', 'data', ('ExprList', None))))))"== str(result)
    
#test_read()





#testings COMMENTS

def test_Comment():
    data = '''
    program fact_rec ;
        int function fact( x: int ): {
        var p : int;
        p = 1 ;
        #adasdasdasd
        while x > 1:
        { p = p * x;
        x = x - 1
        };
        return p
        }
        var n : int;
        {
        n = read();
        print(fact(n))
        }
    '''
    result = parse(data)
    print(result)
    assert "('Program', ('ProgramHeader', 'fact_rec'), ('ProgramBody', ('FuncDecls', ('Function', ('FunctionHeader', ('FunctionType', 'int'), 'fact', ('ParamList', ('ParamList1', ('Param', 'x', ('Type', 'int'))))), ('FunctionBody', ('VarDecls', ('VarDecl', 'p', ('Type', 'int')), ('VarDecls', None)), ('CmdList', ('Cmd', ('CmdAtrib', 'p', ('Expr', 'NUMBER', 1))), ('CmdList', ('Cmd', ('CmdWhile', ('Expr', ('Expr', 'ID', 'x'), ('BinOp', '>'), ('Expr', 'NUMBER', 1)), ('Cmd', ('CmdSeq', ('CmdList', ('Cmd', ('CmdAtrib', 'p', ('Expr', ('Expr', 'ID', 'p'), ('BinOp', '*'), ('Expr', 'ID', 'x')))), ('CmdList', ('Cmd', ('CmdAtrib', 'x', ('Expr', ('Expr', 'ID', 'x'), ('BinOp', '-'), ('Expr', 'NUMBER', 1)))))))))), ('CmdList', ('Cmd', ('CmdReturn', ('Expr', 'ID', 'p')))))))), ('FuncDecls', None)), ('VarDecls', ('VarDecl', 'n', ('Type', 'int')), ('VarDecls', None)), ('Cmd', ('CmdSeq', ('CmdList', ('Cmd', ('CmdAtrib', 'n', ('Expr', 'read'))), ('CmdList', ('Cmd', ('CmdPrint', 'print', ('ExprList', ('ExprList1', ('Expr', 'fact', ('ExprList', ('ExprList1', ('Expr', 'ID', 'n'))))))))))))))" == str(result)
#test_Comment()


def test_CommentSingleLine():
    data = '''
    program fact_rec ;
        int function fact( x: int ): {
        var p : int;
        p = 1 ;
        (*dasdasdasd*)
        while x > 1:
        { p = p * x;
        x = x - 1
        };
        return p
        }
        var n : int;
        {
        n = read();
        print(fact(n))
        }
    '''
    result = parse(data)
    print(result)
    assert "('Program', ('ProgramHeader', 'fact_rec'), ('ProgramBody', ('FuncDecls', ('Function', ('FunctionHeader', ('FunctionType', 'int'), 'fact', ('ParamList', ('ParamList1', ('Param', 'x', ('Type', 'int'))))), ('FunctionBody', ('VarDecls', ('VarDecl', 'p', ('Type', 'int')), ('VarDecls', None)), ('CmdList', ('Cmd', ('CmdAtrib', 'p', ('Expr', 'NUMBER', 1))), ('CmdList', ('Cmd', ('CmdWhile', ('Expr', ('Expr', 'ID', 'x'), ('BinOp', '>'), ('Expr', 'NUMBER', 1)), ('Cmd', ('CmdSeq', ('CmdList', ('Cmd', ('CmdAtrib', 'p', ('Expr', ('Expr', 'ID', 'p'), ('BinOp', '*'), ('Expr', 'ID', 'x')))), ('CmdList', ('Cmd', ('CmdAtrib', 'x', ('Expr', ('Expr', 'ID', 'x'), ('BinOp', '-'), ('Expr', 'NUMBER', 1)))))))))), ('CmdList', ('Cmd', ('CmdReturn', ('Expr', 'ID', 'p')))))))), ('FuncDecls', None)), ('VarDecls', ('VarDecl', 'n', ('Type', 'int')), ('VarDecls', None)), ('Cmd', ('CmdSeq', ('CmdList', ('Cmd', ('CmdAtrib', 'n', ('Expr', 'read'))), ('CmdList', ('Cmd', ('CmdPrint', 'print', ('ExprList', ('ExprList1', ('Expr', 'fact', ('ExprList', ('ExprList1', ('Expr', 'ID', 'n'))))))))))))))" == str(result)
#test_CommentSingleLine()


def test_CommentMultiLine():
    data = '''
    program fact_rec ;
        int function fact( x: int ): {
        var p : int;
        p = 1 ;
        (*dasdasdasd
        asdasdasdsad*)
        while x > 1:
        { p = p * x;
        x = x - 1
        };
        return p
        }
        var n : int;
        {
        n = read();
        print(fact(n))
        }
    '''
    result = parse(data)
    print(result)
    assert "('Program', ('ProgramHeader', 'fact_rec'), ('ProgramBody', ('FuncDecls', ('Function', ('FunctionHeader', ('FunctionType', 'int'), 'fact', ('ParamList', ('ParamList1', ('Param', 'x', ('Type', 'int'))))), ('FunctionBody', ('VarDecls', ('VarDecl', 'p', ('Type', 'int')), ('VarDecls', None)), ('CmdList', ('Cmd', ('CmdAtrib', 'p', ('Expr', 'NUMBER', 1))), ('CmdList', ('Cmd', ('CmdWhile', ('Expr', ('Expr', 'ID', 'x'), ('BinOp', '>'), ('Expr', 'NUMBER', 1)), ('Cmd', ('CmdSeq', ('CmdList', ('Cmd', ('CmdAtrib', 'p', ('Expr', ('Expr', 'ID', 'p'), ('BinOp', '*'), ('Expr', 'ID', 'x')))), ('CmdList', ('Cmd', ('CmdAtrib', 'x', ('Expr', ('Expr', 'ID', 'x'), ('BinOp', '-'), ('Expr', 'NUMBER', 1)))))))))), ('CmdList', ('Cmd', ('CmdReturn', ('Expr', 'ID', 'p')))))))), ('FuncDecls', None)), ('VarDecls', ('VarDecl', 'n', ('Type', 'int')), ('VarDecls', None)), ('Cmd', ('CmdSeq', ('CmdList', ('Cmd', ('CmdAtrib', 'n', ('Expr', 'read'))), ('CmdList', ('Cmd', ('CmdPrint', 'print', ('ExprList', ('ExprList1', ('Expr', 'fact', ('ExprList', ('ExprList1', ('Expr', 'ID', 'n'))))))))))))))" == str(result)
#test_CommentMultiLine()


