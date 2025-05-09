from parser import parse

class Interpreter:
    vars = {}
    backup_vars = {}
    functions = {}
    argument = None
    return_value = None
    
    #Serve para o pytest
    def __init__(self, read_input = None) -> None:
        if read_input == None:
            self.read_input = lambda: input()
        else:
            self.read_input = read_input

    def execute(self, data):
        result = parse(data)
        if(result[0] == 'Program'):
            self.program_body(result[2])
        else:
            raise Exception("Program keyword not found!") 

    def program_body(self, result):
        self.func_decls(result[1])
        self.var_decls(result[2])
        self.cmd(result[3])

    def func_decls(self, result):
        if(result[1] == None):
            return
        else:
            self.function(result[1])
            self.func_decls(result[2])

    def var_decls(self, result):
        if(result[1] == None):
            return
        else:
            self.vardecl(result[1])
            self.var_decls(result[2])

    def cmd(self, result):
        if(result[1][0] == "CmdFor"):
            self.cmd_for(result[1])
        elif(result[1][0] == "CmdPrint"):
            self.cmd_print(result[1])
        elif(result[1][0] == "CmdSeq"):
            self.cmd_seq(result[1])
        elif(result[1][0] == "CmdWhile"):
            self.cmd_while(result[1])
        elif(result[1][0] == "CmdAtrib"):
            self.cmd_atrib(result[1])
        elif(result[1][0] == "CmdReturn"):
            self.cmd_return(result[1])
        else:   
            raise Exception("Invalid command!")     

    def cmd_for(self, result):
        var = self.cmd_atrib(result[1])
        end = int(self.expr(result[2]))
        while self.vars[var] <= end:
            self.cmd(result[3])
            self.vars[var] += 1
    
    def cmd_atrib(self, result):
        if(len(result) == 3):
            self.vars[result[1]] = self.expr(result[2])
            return result[1]
        else:
            raise Exception("Invalid comand attribute")     

    def expr(self, result):
        if(len(result) == 3):
            if(result[1] == "NUMBER"):
                return int(result[2])
            elif(result[1] == "ID"):
                return self.vars[result[2]]
            elif(result[1] == "TRUE"):
                return True
            elif(result[1] == "FALSE"):
                return False
            else:
                return self.function_call(result)
        elif(len(result) == 4 and result[2][0] == "BinOp"):
            return self.binop(result)
        elif(len(result) == 2 and result[1] == "read"):
            return self.read()
        elif(len(result) == 2):
            return self.expr(result[1])
        elif(len(result) == 3 and result[1][0] == "UnOp"):
            raise Exception("Not implemented")
        else:
            raise Exception("Invalid expression!")

    def cmd_print(self, result):
        print(self.expr_list(result[2]))

    def expr_list(self, result):
        return self.expr_list1(result[1])

    def expr_list1(self, result):
        if(len(result) == 2):
            return self.expr(result[1])
        else:
            raise Exception("Invalid expression list 1!")
        
    def cmd_seq(self, result):
        self.cmd_list(result[1])

    def cmd_list(self, result):
        if(len(result)==2):
            self.cmd(result[1])
        elif(len(result) == 3):
            self.cmd(result[1])
            self.cmd_list(result[2])
        else:
            raise Exception("Invalid command list!")

    def cmd_while(self, result):
        while self.expr(result[1]):
            self.cmd(result[2])

    def binop(self, result):
        left = self.expr(result[1])
        right = self.expr(result[3])
        if(result[2][1] == "<="):
            return left <= right
        elif(result[2][1] == "+"):
            return left + right
        elif(result[2][1] == ">"):
            return left > right
        elif(result[2][1] == "*"):
            return left * right
        elif(result[2][1] == "-"):
            return left - right
        else:
            raise Exception("Invalid binop expression!")    

    def read(self):
        result = int(self.read_input())
        return result

    def vardecl(self, result):
        vartype = self.typee(result[2])
        if(vartype == "int"):
            self.vars[result[1]] = 0
        else:
            raise Exception("Invalid type")

    def typee(self, result):
        return result[1]

    #function header
    def function_name(self, result):
        function_name = result[2]
        return function_name

    def param_list(self, result):
        self.param_list1(result[1])

    def param_list1(self, result):
        if(len(result) == 2):
            self.param(result[1])
        elif(len(result) == 3):
            self.param(result[1])
            self.param_list1(result[2])
        else:
            raise Exception("Invalid param!")

    #functions guarda function header e body
    def function(self, result):
        func_name = self.function_name(result[1])
        self.functions[func_name] = result

    def function_call(self, result):
        func_name = result[1]
        self.argument = self.expr_list(result[2])
        function = self.functions[func_name]
        self.backup_vars = dict(self.vars)
        self.vars = {}
        self.function_header(function[1])
        self.function_body(function[2])
        self.vars = dict(self.backup_vars)
        return self.return_value

    def function_header(self, result):
        self.param_list(result[3])

    def param(self, result):
        self.vars[result[1]] = self.argument

    def function_body(self, result):
        self.var_decls(result[1])
        self.cmd_list(result[2])

    def cmd_return(self, result):
        self.return_value = self.expr(result[1])





data1 = '''
program count_for;
        for i = 1 to 10 :
        print(i)
'''




data2 ='''
    program count;
        var i: int;
        { i = 1;
        while i <= 10: {
        print(i);
        i = i + 1
        }
        }
'''


data3 ='''
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


data4 = '''
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


data5 = '''
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

interpreter = Interpreter()
#interpreter.execute(data1)
#interpreter.execute(data2)
#interpreter.execute(data3)
#interpreter.execute(data4)
#interpreter.execute(data5)




