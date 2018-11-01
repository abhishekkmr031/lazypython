#Given two strings, a and b, return the result of putting them together in the order abba
## print given strings in a pattern
#"abba" --> is the pattern
#   make_abba('Hi', 'Bye') → 'HiByeByeHi'
#   make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
#   make_abba('What', 'Up') → 'WhatUpUpWhat'
def make_abba(a, b):
    pattern = "abba"
    var = ""
    for p in pattern:
        if(p=="a"):
            var = var + a
        else:
            var = var + b
    print(var)


make_abba("Hi", "Bye")
make_abba('Yo', 'Alice')
make_abba('What', 'Up')
        
        
    
