
import pprint as pp
from RLE import RLE
import os
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format
os.system('cls')
width = os.get_terminal_size().columns
#Custom color print functions
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk).center(width+10))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk).center(width+10))
cprint(figlet_format('Welcome!',justify="center",width = width), 'yellow', attrs=['bold'])
while True:
    print("\033[93m Choose the desired functionality: \033[00m".center(width+10))
    print("\033[93m  -enter 0 to encode \033[00m".center(width+10))
    print("\033[93m -enter 1 to decode \033[00m".center(width+10))
    Choice=input()
    #encoding
    if Choice=='0':
        prCyan("Welcome To RLE Encoder!")
        prCyan('#'*100)
        msg=input('Enter The Message you want to encode:')
        prCyan('#'*100)
        print('Dictionary:')
        code=RLE.encode(msg)
        prYellow('Coded Message:')
        prGreen(code)
        break
    #Decoding
    elif Choice=='1':
        prCyan("Welcome To RLE decoder!")
        prCyan('#'*100)
        separator=input('enter a separator (leave empty and no separator will be used):')
        if separator is None:
            #if no seprator is entred then don't use one 
            code=input('enter the code:')
            prYellow('Original Message:')
            prGreen(RLE.decode(code,separator))
        else:
            #use the provided seprator 
            code=input('enter the code(separating couples with a separator):')
            prYellow('Original Message:')
            prGreen(RLE.decode(code))
        
        
        break
    else: 
        os.system('cls')
        prRed('wrong Functionality pls try again!')
        


