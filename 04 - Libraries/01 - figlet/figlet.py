from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()
random_font = choice(figlet.getFonts())

input = input("Input: ")

if len(sys.argv) == 1:
    figlet.setFont(font=random_font)
    print(figlet.renderText(input))
    
elif len(sys.argv) == 3:
    if sys.argv[1].strip() == "-f" or sys.argv[1] == "--font":
        if sys.argv[2].strip() in figlet.getFonts():    
            print(figlet.renderText(input))
            
else:
    print("Invalid")