import tkinter as tk
import keyboardGui as kb
import os

def main():
    ####### Your program logic here...

    exam = [['2021/7/14 monday','이천이십일 년 칠월 십사 일 월요일','icheonisibil nyeon chilwol sibsa woryoil'],
            ['2021/7/14 monday','이천이십일 년 칠월 십사 일 월요일','icheonisibil nyeon chilwol sibsa woryoil']]

    response = ['','']
    sel = False
    opt = 0

    print(exam)
     
    while(not sel):
        os.system('cls')
        print("\n How would you translate:\n\n"
            + "\n\t"+str(exam[0][opt])+"\n\n"
            + "\n\tto korean."+"\n\n")
        
        response[0] = kb.show_keyboard_and_input()

        if (response[0]==''):
                    print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[examQuestion "+"]")
        else:
            sel = True
            print (response[0])

    sel = False        
    while(not sel):
        os.system('cls')
        print("\n How would you translate:\n\n"
            + "\n\t"+str(exam[0][opt])+"\n\n"
            + "\n\tto korean."+"\n\n")
        
        response[1] = kb.show_keyboard_and_input()

        if (response[1]==''):
            print("\nERROR: Null String, \n\nmust use a"
                +"\n\tnon void String for:"
                +"\n\t[examQuestionT "+"]")
        else:
            sel = True
            print (response[1])

    opt = 1

    while(not sel):
        os.system('cls')
        print("\n How would you translate:\n\n"
            + "\n\t"+str(exam[0][opt])+"\n\n"
            + "\n\tto korean."+"\n\n")
        
        response[0] = kb.show_keyboard_and_input()

        if (response[0]==''):
                    print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[examQuestion "+"]")
        else:
            sel = True
            print (response[0])

    sel = False        
    while(not sel):
        os.system('cls')
        print("\n How would you translate:\n\n"
            + "\n\t"+str(exam[0][opt])+"\n\n"
            + "\n\tto korean."+"\n\n")
        
        response[1] = kb.show_keyboard_and_input()

        if (response[1]==''):
            print("\nERROR: Null String, \n\nmust use a"
                +"\n\tnon void String for:"
                +"\n\t[examQuestionT "+"]")
        else:
            sel = True
            print (response[1])


if __name__ == "__main__":
    main()