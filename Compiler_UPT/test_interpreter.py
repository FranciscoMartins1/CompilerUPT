from interpreter import Interpreter

def test_data1(capsys):
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
    
    Interpreter().execute(data)
    captured = capsys.readouterr()
    assert captured.out == '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'

def test_data2(capsys):
    data = '''
    program count_for;
        for i = 1 to 10 :
        print(i)
    '''
    Interpreter().execute(data)
    captured = capsys.readouterr()
    assert captured.out == '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n'

def test_data3(capsys):
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
    Interpreter(lambda: "4").execute(data)
    captured = capsys.readouterr()
    assert captured.out == '30\n'

def test_data4(capsys):
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
    Interpreter(lambda: "4").execute(data)
    captured = capsys.readouterr()
    assert captured.out == '24\n'

def test_data5(capsys):
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
    Interpreter(lambda: "4").execute(data)
    captured = capsys.readouterr()
    assert captured.out == '24\n'