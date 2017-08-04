#! python3
from functools import reduce
import sys

def switch(base):
    """This function returns a list of possible digits depending on the base that is
    passed as an argument to the function"""
    return [i for i in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"][:base]

def decToBase(num,base):
    """This function takes in two arguments - a number and the target base - and converts
    the number from it's decimal form to it's target base"""
    if num==0:
        return ''
    else:
        quo = num//base
        rem = num%base
        #a recursion call recursively finds the quotient and remainder and stores the
        #remainder when the quotient is sent as the argument for the recursion call
        return decToBase(quo,base)+switch(base)[rem]

def baseToDec(num,base):
    """This function takes in two arguments - a number and the base in which it is written
    in. It then converts that number to decimal."""

    #takes the number, turns it into an array, and switches the strings to numbers
    num_list = list(map(lambda x: switch(base).index(x),[i for i in num]))
    #converts each and every one of the digits to decimal
    converted_list = [num_list[i]*base**(len(num_list)-1-i) for i in range(len(num_list))]
    #returns the sum of all the numbers in the list
    return reduce(lambda x,y:x+y,converted_list)

def helptext():
    """Prints the helptext"""
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

        #to avoid any lunatics from entering invalid bases
        if toBase == 1 or toBase == 0 or fromBase == 1 or fromBase == 0:
            print(helptext())
            sys.exit(0)

        number = sys.argv[4]
        #it takes the number in the origin base, converts it into decimal
        #and then converts it into the target base
        #this process makes it universal for all bases (from 2 to 36) with
        #the biggest expense being computational power

        print("Result :",decToBase(baseToDec(number,fromBase),toBase))

    else:
        print(helptext())

except IndexError:
    print(helptext())
