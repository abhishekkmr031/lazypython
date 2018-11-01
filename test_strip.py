def func_test_strip():
    var = "\t\n\n             hello space and tabs                         \n\n"
    print (var)
    print (var.strip())
    # Now there are two types of strip() functios
    # 1. leading strip --> var.lstrip() ==>>  removes whitespaces from front or lead or say, from left side of string
    print (var.lstrip())
    # 2. trailing strip --> var.rstrip() ==>> removes whitespaces from tail or trailing or say, from right side of string
    print(var.rstrip())
    

func_test_strip()
