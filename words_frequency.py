def words_frequency():
    handle = open('text.txt', 'r')
    text = handle.read().split('\n')
    dict = {}
    for lines in text:
        line = lines.split(' ')
        for word in line:
##            print(word)
            if(word in dict):
                dict[word] += 1
            else:
                dict[word] = 1
##    dict.sorted
##    for k,v in dict.items():
##        print(k + "  :  " + str(v))
##
    bigcount = None
    bigword = None
    for word, count in dict.items():
        if bigcount is None or bigcount < count:
            bigcount = count
            bigword = word
    print("The most common word is : %s  --> %s"%(bigword, str(bigcount)))
    

words_frequency()
