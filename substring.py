# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# str =  'X-DSPAM-Confidence: 0.8475 '

def substring():
    text =  'X-DSPAM-Confidence: 0.8475 '
    colon_pos = text.find(':')
    space_pos = text.find(' ', colon_pos+2)
    #num = text[colon_pos+2:space_pos]
    num = float(text[colon_pos+2:space_pos])
    print(type(num))
    print (num)
##    email = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
##    atpos = email.find('@')
##    print(atpos)
##
##    space_pos = email.find(' ', atpos+1)
##    print(space_pos)
##
##    print(email[atpos+1:space_pos])



substring()
