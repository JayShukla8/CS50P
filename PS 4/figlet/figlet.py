from pyfiglet import Figlet
figlet = Figlet()
import random
import sys

def main():
    fonts = []
    fonts = figlet.getFonts()

    n = len(sys.argv)

    if((n==1)or(n==3)):
        if(n==1):
            random_font = random.choice(fonts)
            figlet.setFont(font=random_font)
        else:
            if((sys.argv[1]=="-f") or (sys.argv[1]=="--font")):
                if sys.argv[2] in fonts:
                    figlet.setFont(font=sys.argv[2])
                else:
                    sys.exit("Invalid Usage")
            else:
                sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")

    str = input("Input: ")
    print(figlet.renderText(str))

if __name__ == "__main__":
    main()
