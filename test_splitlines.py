def test_splitlines():
    var = """or say, from right side of string
One way to loop over a string is to what's Up!!! use the range(n) function which given a number, e.g. 5, returns the sequence 0, 1, 2, 3 ... n-1.
Those values work perfectly to index into a string, so the loop for i in range(len(s)):
will loop the variable i through the index values 0, 1, 2, ... len(s)-1, essentially looking at each char once.
"""
    str_splitlines = var.splitlines()
    for lines in str_splitlines:
        print("-->" + lines.swapcase())

test_splitlines()
