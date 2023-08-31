###Dependencies
import random
import os

###Showing and resolving the exam

## First option: console
def main (e):
    results = []
    response = ['','']
    sel = False
    opt = 0
    calification = 0

    for x in range (len(e)):
        opt = random.choice([0,0,1,2])

        if(opt == 0):
            while(not sel):
                os.system('cls')
                response[0] = str(input("\n How would you translate:\n\n"
                    + "\n\t"+str(e[x][opt])+"\n\n"
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
                        +"\n\t[examQuestionT "+str(x)+"]")
                else:
                    sel = True

            sel = False
            if (response[0] == e[x][1]):
                if(response[1] == e[x][2]):
                    results.append([e[x][opt],response[0],response[1],int(2)])
                    calification = calification + 2
                else:
                    results.append([e[x][opt],response[0],response[1],int(1)])
                    calification = calification + 1
            else:
                results.append([e[x][opt],response[0],response[1],int(0)])

        if(opt == 1):
            while(not sel):
                os.system('cls')
                response[0] = str(input("\n How would you translate:\n\n"
                    + "\n\t"+str(e[x][opt])+"\n\n"
                    + "\n\tto english."+"\n\n"))

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
                    + "\n\t"+str(e[x][opt])+"\n\n"
                    + "\n\tfrom hangul."+"\n\n"))

                if (response[1]==''):
                    print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[examQuestionT "+str(x)+"]")
                else:
                    sel = True

            sel = False
            if (response[0] == e[x][0]):
                if(response[1] == e[x][2]):
                    results.append([response[0],e[x][opt],response[1],int(2)])
                    calification = calification + 2
                else:
                    results.append([response[0],e[x][opt],response[1],int(1)])
                    calification = calification + 1
            else:
                results.append([response[0],e[x][opt],response[1],int(0)])                    

        if(opt == 2):
            while(not sel):
                os.system('cls')
                response[0] = str(input("\n How would you transliterate:\n\n"
                    + "\n\t"+str(e[x][opt])+"\n\n"
                    + "\n\tto hangul."+"\n\n"))

                if (response[0]==''):
                    print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[examQuestion "+str(x)+"]")
                else:
                    sel = True

            sel = False        
            while(not sel):
                os.system('cls')
                response[1] = str(input("\n How would you translate:\n\n"
                    + "\n\t"+str(e[x][opt])+"\n\n"
                    + "\n\tto english."+"\n\n"))

                if (response[1]==''):
                    print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[examQuestionE "+str(x)+"]")
                else:
                    sel = True

            sel = False
            if (response[0] == e[x][1]):
                if(response[1] == e[x][0]):
                    results.append([response[1],response[0],e[x][opt],int(2)])
                    calification = calification + 2
                else:
                    results.append([response[1],response[0],e[x][opt],int(1)])
                    calification = calification + 1
            else:
                results.append([response[1],response[0],e[x][opt],int(0)])
    
    print("\n you have finished the exam. \n\nYou got:"
     +"\n\t"+str(calification)+" / "+str(2*(len(e)))
     +"\n\tYou are able to revise the exam through the examMenu.")

    return results
                    
## Second option: react