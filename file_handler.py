def file_handler():
    handle = open('substring.py', 'r')
    text = handle.read().split('\n')
    text_write = ''
    #print(text)
    for lines in text:
        text_write += lines
        if(' email =' in lines):
            at_pos = lines.find('@')
            space_pos = lines.find(' ', at_pos)
            print("****************************************************")
            print(lines[at_pos+1:space_pos])
            print("****************************************************")

    handle2 = open('test.txt', 'w')
    handle2.write(str(text))
    print(handle.closed)
    handle.close()
    print(handle.closed)
    handle2.close()


file_handler()
