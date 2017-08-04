#! python3
from functools import reduce
import sys

def switch(base):
    return [i for i in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"][:base]

def decToBase(num,base):
    if num==0:
        return ''
    else:
        quo = num//base
        rem = num%base
        return decToBase(quo,base)+switch(base)[rem]

def baseToDec(num,base):
    num_list = list(map(lambda x: switch(base).index(x),[i for i in num]))
    converted_list = [num_list[i]*base**(len(num_list)-1-i) for i in range(len(num_list))]
    return reduce(lambda x,y:x+y,converted_list)

def helptext():
    return """

    Usage:
        python main.py [OPTION] [from] [to] [number]
        OPTION :
            -h      : displays the helptext
            -c      : converts the given number
            from    : origin base (except 0 and 1 and a maximum of 36)
            to      : to base (except 0 and 1 and a maximum of 36)
            number  : number in the origin base

            """
try:
    if sys.argv[1]=='-h':
        print(helptext())
    elif sys.argv[1]=='-c':

        fromBase = int(sys.argv[2])
        toBase = int(sys.argv[3])

        if toBase == 1 or toBase == 0 or fromBase == 1 or fromBase == 0:
            print(helptext())
            sys.exit(0)

        number = sys.argv[4]
        print("Result :",decToBase(baseToDec(number,fromBase),toBase))

    else:
        print(helptext())
except IndexError:
    print(helptext())
