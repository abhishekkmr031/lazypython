import re
def attendance():
    handle = open("file.txt", "r")
    text = handle.read().split("\n")
    num = len(text)
    regex = '\d+'
    count = 0
    num_list = [ ]
    for i in range(1, 58, 3):
        num_list.append(re.findall(regex,text[i]))
        count += 1

    print("Count of attendees is :- %s"%  str(count))
    print(num_list)

    handle.close()

    write_handle = open("emp_ids.txt", "w")
    for id in num_list:
        
        write_handle.write(str(id).replace("['", "").replace("']", "") + "\n")
    write_handle.close()
    

    
##    num = len(text)
##    for line in text:
    

attendance()
