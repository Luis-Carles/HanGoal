#Dependencies
import os
from konlpy import *
import persistence as per

###Initial Menu

#Variables
sel = [False,False,False,False,False,False,False]

##Library

def library ():
 
 while (not sel[2]):
        for x in range(len(sel)-1):
         sel[x+1] = False
         os.system('cls')

        print("\nWelcome to the Library, \n\nChoose an option:"
        +"\n\t0: -Introducing a new word."
        +"\n\t1: -Look for a specific word."
        +"\n\t2: -Modifying a specific word."
        +"\n\t3: -Returning to Initial menu")

        while(not sel[3]):
            try:
                opt = int(input("\nChoose one option \n\n"
                + "\n\tmust be an integer between 0-3\n\n"))
            except ValueError:
                print("option must be an integer")
                exit(-1)

            if (opt<0) or (opt>3):
                print("\nERROR: wrong option, \n\nmust use a"
                +"\n\tinteger between 0-3 for:"
                +"\n\t[libraryMenu option]")
            else:
                sel[3] = True

        if (opt == 3):
            sel[2]= True
            os.system('cls')

        if (opt == 0):
            w =''
            h=''
            t=''
            os.system('cls')
            while(not sel[4]):
                    w = str(input("\nIntroduce the new word \n\n"
                    + "\n\tmust be in English\n\n"))


                    if (w==''):
                        print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[new Word English]")
                    else:
                        sel[4] = True
            
            sel[4]=False
            while(not sel[4]):
                    h = str(input("\nIntroduce the new word in Korean \n\n"
                    + "\n\tmust be in Hangul\n\n"))


                    if (h==''):
                        print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[new Word Hangul]")
                    else:
                        sel[4] = True   

            sel[4]=False
            while(not sel[4]):
                    t = str(input("\nIntroduce the new word transliteration \n\n"
                    + "\n\tmust be in latin alphabet\n\n"))


                    if (t==''):
                        print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[new word transliteration]")
                    else:
                        sel[4] = True 

            per.addNewWord(w,h,t)

        if (opt == 1):
            f= ''
            data = 0
            resul = []
            a = ''

            w =''
            h=''
            t=''
            os.system('cls')
            while(not sel[5]):
                    data = int(input("\nIntroduce how do you want to find the word:\n\n"
                    + "\n\t0: Through English original word\n\n"
                    + "\n\t1: Through Korean traslated word\n\n"
                    + "\n\t2: Through romanized transliteration\n\n"))


                    if (data<0) or (data>2):
                        print("\nERROR: wrong option, \n\nmust use a"
                        +"\n\tinteger between: 0-2"
                        +"\n\t[searching Word Option]")
                    else:
                        sel[5] = True
            
            sel[5]=False
            os.system('cls')
            while(not sel[5]):
                    f = str(input("\nIntroduce word you wish to find:\n\n"
                    + "\n\tmust be a non empty string\n\n"))


                    if (f==''):
                        print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[word to Find]")
                    else:
                        sel[5] = True   

            resul = per.findWord(f,data)

            sel[5]=False     
            if(resul[0]==''):
                os.system('cls')
                while(not sel[5]):
                        a = str(input("\n There was no coincidence in the library for that word."
                        +"\n\t do you wanna introduce it as a new one?"
                        +"\n\t y/n ?"))


                        if (a!='y')or (a!='n'):
                            print("\nERROR: Non valid String, \n\nmust use a"
                            +"\n\t simple y or n for:"
                            +"\n\t[add the non-Found word option]")
                        else:
                            sel[5] = True 
                if(a=='y'):
                    if(data==0):
                            sel[5]=False
                            os.system('cls')
                            while(not sel[5]):
                                    h = str(input("\nIntroduce the new word in Korean \n\n"
                                    + "\n\tmust be in Hangul\n\n"))


                                    if (h==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new Word Hangul]")
                                    else:
                                        sel[5] = True   

                            sel[5]=False
                            while(not sel[5]):
                                    t = str(input("\nIntroduce the new word transliteration \n\n"
                                    + "\n\tmust be in latin alphabet\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new word transliteration]")
                                    else:
                                        sel[5] = True   
                        
                            per.addNewWord(f,h,t)

                    if(data==1):
                            sel[5]=False
                            os.system('cls')
                            while(not sel[5]):
                                    w = str(input("\nIntroduce the new word English \n\n"
                                    + "\n\tmust be in English\n\n"))


                                    if (w==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new Word English]")
                                    else:
                                        sel[5] = True   

                            sel[5]=False
                            while(not sel[5]):
                                    t = str(input("\nIntroduce the new word transliteration \n\n"
                                    + "\n\tmust be in latin alphabet\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new word transliteration]")
                                    else:
                                        sel[5] = True   
                        
                            per.addNewWord(w,f,t)

                    if(data==2):
                            sel[5]=False
                            os.system('cls')
                            while(not sel[5]):
                                    w = str(input("\nIntroduce the new word English \n\n"
                                    + "\n\tmust be in English\n\n"))


                                    if (w==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new Word English]")
                                    else:
                                        sel[5] = True   

                            sel[5]=False
                            while(not sel[5]):
                                    h = str(input("\nIntroduce the new word in Korean \n\n"
                                    + "\n\tmust be in Hangul\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new word Hangul]")
                                    else:
                                        sel[5] = True   
                        
                            per.addNewWord(w,h,f)
            else:
                print("\nSUCCESS: the word was found!"
                +"\n\t")
                print(resul)

        if (opt == 2):
            f= ''
            data = 0
            resul = []
            a = ''

            w =''
            h=''
            t=''

            os.system('cls')
            while(not sel[6]):
                    data = int(input("\nIntroduce how do you want to find the word:\n\n"
                    + "\n\t0: Through English original word\n\n"
                    + "\n\t1: Through Korean traslated word\n\n"
                    + "\n\t2: Through romanized transliteration\n\n"))


                    if (data<0) or (data>2):
                        print("\nERROR: wrong option, \n\nmust use a"
                        +"\n\tinteger between: 0-2"
                        +"\n\t[modifying Word Option]")
                    else:
                        sel[6] = True
            
            sel[6]=False
            os.system('cls')
            while(not sel[6]):
                    f = str(input("\nIntroduce word you wish to modify:\n\n"
                    + "\n\tmust be a non empty string\n\n"))


                    if (f==''):
                        print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[word to modify]")
                    else:
                        sel[6] = True   

            resul = per.findWord(f,data)

            sel[6]=False
            os.system('cls')     
            if(resul[0]==''):
                while(not sel[6]):
                        a = str(input("\n There was no coincidence in the library for that word."
                        +"\n\t do you wanna introduce it as a new one?"
                        +"\n\t y/n ?"))


                        if (a!='y')or (a!='n'):
                            print("\nERROR: Non valid String, \n\nmust use a"
                            +"\n\t simple y or n for:"
                            +"\n\t[add the non-Found word option]")
                        else:
                            sel[6] = True 
                if(a=='y'):
                    if(data==0):
                            sel[6]=False
                            os.system('cls')
                            while(not sel[6]):
                                    h = str(input("\nIntroduce the new word in Korean \n\n"
                                    + "\n\tmust be in Hangul\n\n"))


                                    if (h==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new Word Hangul]")
                                    else:
                                        sel[6] = True   

                            sel[6]=False
                            while(not sel[6]):
                                    t = str(input("\nIntroduce the new word transliteration \n\n"
                                    + "\n\tmust be in latin alphabet\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new word transliteration]")
                                    else:
                                        sel[6] = True   
                        
                            per.addNewWord(f,h,t)

                    if(data==1):
                            sel[6]=False
                            os.system('cls')
                            while(not sel[6]):
                                    w = str(input("\nIntroduce the new word English \n\n"
                                    + "\n\tmust be in English\n\n"))


                                    if (w==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new Word English]")
                                    else:
                                        sel[6] = True   

                            sel[6]=False
                            while(not sel[6]):
                                    t = str(input("\nIntroduce the new word transliteration \n\n"
                                    + "\n\tmust be in latin alphabet\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new word transliteration]")
                                    else:
                                        sel[6] = True   
                        
                            per.addNewWord(w,f,t)

                    if(data==2):
                            sel[6]=False
                            os.system('cls')
                            while(not sel[6]):
                                    w = str(input("\nIntroduce the new word English \n\n"
                                    + "\n\tmust be in English\n\n"))


                                    if (w==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new Word English]")
                                    else:
                                        sel[6] = True   

                            sel[6]=False
                            while(not sel[6]):
                                    h = str(input("\nIntroduce the new word in Korean \n\n"
                                    + "\n\tmust be in Hangul\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new word Hangul]")
                                    else:
                                        sel[6] = True   
                        
                            per.addNewWord(w,h,f)
            else:
                    if(data==0):
                            sel[6]=False
                            os.system('cls')
                            while(not sel[6]):
                                    h = str(input("\nIntroduce the new word in Korean \n\n"
                                    + "\n\tmust be in Hangul\n\n"))


                                    if (h==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new Word Hangul]")
                                    else:
                                        sel[6] = True   

                            sel[6]=False
                            while(not sel[6]):
                                    t = str(input("\nIntroduce the new word transliteration \n\n"
                                    + "\n\tmust be in latin alphabet\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new word transliteration]")
                                    else:
                                        sel[6] = True   
                        
                            per.modifyWord(f,h,t)

                    if(data==1):
                            sel[6]=False
                            os.system('cls')
                            while(not sel[6]):
                                    w = str(input("\nIntroduce the new word English \n\n"
                                    + "\n\tmust be in English\n\n"))


                                    if (w==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new Word English]")
                                    else:
                                        sel[6] = True   

                            sel[6]=False
                            while(not sel[6]):
                                    t = str(input("\nIntroduce the new word transliteration \n\n"
                                    + "\n\tmust be in latin alphabet\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new word transliteration]")
                                    else:
                                        sel[6] = True   
                        
                            per.modifyWord(w,f,t)

                    if(data==2):
                            sel[6]=False
                            os.system('cls')
                            while(not sel[6]):
                                    w = str(input("\nIntroduce the new word English \n\n"
                                    + "\n\tmust be in English\n\n"))


                                    if (w==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new Word English]")
                                    else:
                                        sel[6] = True   

                            sel[6]=False
                            while(not sel[6]):
                                    h = str(input("\nIntroduce the new word in Korean \n\n"
                                    + "\n\tmust be in Hangul\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new word Hangul]")
                                    else:
                                        sel[6] = True   
                        
                            per.modifyWord(w,h,f)
             
      
##Exam


##Loop

def mainMenu ():

 while (not sel[0]):
        for x in range(len(sel)):
                sel[x] = False
                
        print("\n Welcome to HanGoal, \n\nChoose an option:"
        +"\n\t0: -Entering the Library."
        +"\n\t1: -Starting a new exam."
        +"\n\t2: -Exiting HanGoal.")

        while(not sel[1]):
            try:
                opt = int(input("\nChoose one option \n\n"
                + "\n\tmust be an integer between 0-2\n\n"))
            except ValueError:
                print("option must be an integer")
                exit(-1)

            if (opt<0) or (opt>2):
                print("\nERROR: wrong option, \n\nmust use a"
                +"\n\tinteger between 0-2 for:"
                +"\n\t[mainMenu option]")
            else:
                sel[1] = True  

        if (opt==0):
            os.system('cls')
            library()
        
        #if (opt==1):
        #    exam()

        if (opt==2):
            print("\n Hope u will come back!")
            sel[0]= True
            os.system('cls')
           
mainMenu()