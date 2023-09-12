import tkinter as tk
import keyboardGui as kb
import os

def main():
    
    kb.show_keyboard_and_input()

    ####### Your program logic here...

    exam = [['2021/7/14 monday','이천이십일 년 칠월 십사 일 월요일','icheonisibil nyeon chilwol sibsa woryoil'],
            ['2021/7/14 monday','이천이십일 년 칠월 십사 일 월요일','icheonisibil nyeon chilwol sibsa woryoil']]

    response = ['','']
    sel = False
    opt = 0

    while(not sel):
        os.system('cls')
        response[0] = str(input("\n How would you translate:\n\n"
            + "\n\t"+str(exam[0][opt])+"\n\n"
            + "\n\tto korean."+"\n\n"))

        if (response[0]==''):
                    print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[examQuestion "+str(x)+"]")
        else:
            sel = True

    sel = False        
    while(not sel):
        os.system('cls')
        response[1] = str(input("\n How would you romanize:\n\n"
            + "\n\t"+str(response[0])+"\n\n"
            + "\n\tfrom hangul."+"\n\n"))

        if (response[1]==''):
            print("\nERROR: Null String, \n\nmust use a"
                +"\n\tnon void String for:"
                +"\n\t[examQuestionT "+str(0)+"]")
        else:
            sel = True

    opt = 1

    while(not sel):
        os.system('cls')
        response[0] = str(input("\n How would you translate:\n\n"
            + "\n\t"+str(exam[1][opt])+"\n\n"
            + "\n\tto korean."+"\n\n"))

        if (response[0]==''):
                    print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[examQuestion "+str(x)+"]")
        else:
            sel = True

    sel = False        
    while(not sel):
        os.system('cls')
        response[1] = str(input("\n How would you romanize:\n\n"
            + "\n\t"+str(response[0])+"\n\n"
            + "\n\tfrom hangul."+"\n\n"))

        if (response[1]==''):
            print("\nERROR: Null String, \n\nmust use a"
                +"\n\tnon void String for:"
                +"\n\t[examQuestionT "+str(1)+"]")
        else:
            sel = True


if __name__ == "__main__":
    main()