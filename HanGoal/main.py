#Dependencies
import os
from konlpy import *
import exam as e
import persistence as per

###Initial Menu

#Variables
sel = [False,False,False,False,False,False,False,False,False]

##Library

def library ():
 
 while (not sel[2]):
        for x in range(len(sel)-1):
         sel[x+1] = False

        print("\nWelcome to the Library, \n\nChoose an option:"
        +"\n\t0: -Introducing a new word."
        +"\n\t1: -Introducing a new verb."
        +"\n\t2: -Look for a specific word/verb in the Library."
        +"\n\t3: -Modifying a specific word/verb in the Library."
        +"\n\t4: -Returning to Initial menu")

        while(not sel[3]):
            try:
                opt = int(input("\nChoose one option \n\n"
                + "\n\tmust be an integer between 0-4\n\n"))
            except ValueError:
                print("option must be an integer")
                exit(-1)

            if (opt<0) or (opt>4):
                print("\nERROR: wrong option, \n\nmust use a"
                +"\n\tinteger between 0-4 for:"
                +"\n\t[libraryMenu option]")
            else:
                sel[3] = True

        if (opt == 4):
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
            w =''
            h=''
            t=''
            os.system('cls')
            while(not sel[7]):
                    w = str(input("\nIntroduce the new verb \n\n"
                    + "\n\tmust be in English\n\n"))


                    if (w==''):
                        print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[new Verb English]")
                    else:
                        sel[7] = True
            
            sel[7]=False
            while(not sel[7]):
                    h = str(input("\nIntroduce the new verb in Korean \n\n"
                    + "\n\tmust be in Hangul\n\n"))


                    if (h==''):
                        print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[new verb Hangul]")
                    else:
                        sel[7] = True   

            sel[7]=False
            while(not sel[7]):
                    t = str(input("\nIntroduce the new verb transliteration \n\n"
                    + "\n\tmust be in latin alphabet\n\n"))


                    if (t==''):
                        print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t[new verb transliteration]")
                    else:
                        sel[7] = True 

            per.addNewVerb(w,h,t)

        if (opt == 2):
            f= ''
            o = ''
            _o = o
            data = 0
            resul = []
            a = ''

            w =''
            h=''
            t=''
            os.system('cls')

            while(not sel[8]):
                    o = int(input("\nIntroduce which you want to find:\n\n"
                    + "\n\t0: a word in the library\n\n"
                    + "\n\t1: a verb in the library\n\n"))

                    if (o<0) or (o>1):
                        print("\nERROR: wrong option, \n\nmust use a"
                        +"\n\tinteger between: 0-1"
                        +"\n\t[searching Option]")
                    else:
                        sel[8] = True

            if(o==0):
                _o = 'word'
            if(o==1):
                _o = 'verb'
            sel[8]=False

            while(not sel[5]):
                    data = int(input("\nIntroduce how do you want to find the "+ _o +":\n\n"
                    + "\n\t0: Through English original word\n\n"
                    + "\n\t1: Through Korean traslated word\n\n"
                    + "\n\t2: Through romanized transliteration\n\n"))


                    if (data<0) or (data>2):
                        print("\nERROR: wrong option, \n\nmust use a"
                        +"\n\tinteger between: 0-2"
                        +"\n\t[searching "+ _o +" Option]")
                    else:
                        sel[5] = True
            
            sel[5]=False
            os.system('cls')
            while(not sel[5]):
                    f = str(input("\nIntroduce the "+ _o +" you wish to find:\n\n"
                    + "\n\tmust be a non empty string\n\n"))


                    if (f==''):
                        print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t["+ _o +" to Find]")
                    else:
                        sel[5] = True   

            if(o==0):
                resul = per.findWord(f,data)
            if(o==1):
                resul = per.findVerb(f,data)

            sel[5]=False     
            if(resul[0]==''):
                os.system('cls')
                while(not sel[5]):
                        a = str(input("\n There was no coincidence in the library for that "+ _o +"."
                        +"\n\t do you wanna introduce it as a new one?"
                        +"\n\t y/n ?"))


                        if (a!='y')and (a!='n'):
                            print("\nERROR: Non valid String, \n\nmust use a"
                            +"\n\t simple y or n for:"
                            +"\n\t[add the non-Found "+ _o +" option]")
                        else:
                            sel[5] = True 
                if(a=='y'):
                    if(data==0):
                            sel[5]=False
                            os.system('cls')
                            while(not sel[5]):
                                    h = str(input("\nIntroduce the new "+ _o +" in Korean \n\n"
                                    + "\n\tmust be in Hangul\n\n"))


                                    if (h==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" Hangul]")
                                    else:
                                        sel[5] = True   

                            sel[5]=False
                            while(not sel[5]):
                                    t = str(input("\nIntroduce the new "+ _o +" transliteration \n\n"
                                    + "\n\tmust be in latin alphabet\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" transliteration]")
                                    else:
                                        sel[5] = True   

                            if(o==0):
                                per.addNewWord(f,h,t)
                            if(o==1):
                                per.addNewVerb(f,h,t)

                    if(data==1):
                            sel[5]=False
                            os.system('cls')
                            while(not sel[5]):
                                    w = str(input("\nIntroduce the new "+ _o +" English \n\n"
                                    + "\n\tmust be in English\n\n"))


                                    if (w==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" English]")
                                    else:
                                        sel[5] = True   

                            sel[5]=False
                            while(not sel[5]):
                                    t = str(input("\nIntroduce the new "+ _o +" transliteration \n\n"
                                    + "\n\tmust be in latin alphabet\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" transliteration]")
                                    else:
                                        sel[5] = True   
                        
                            if(o==0):
                                per.addNewWord(w,f,t)
                            if(o==1):
                                per.addNewVerb(w,f,t)

                    if(data==2):
                            sel[5]=False
                            os.system('cls')
                            while(not sel[5]):
                                    w = str(input("\nIntroduce the new "+ _o +" English \n\n"
                                    + "\n\tmust be in English\n\n"))


                                    if (w==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" English]")
                                    else:
                                        sel[5] = True   

                            sel[5]=False
                            while(not sel[5]):
                                    h = str(input("\nIntroduce the new "+ _o +" in Korean \n\n"
                                    + "\n\tmust be in Hangul\n\n"))


                                    if (h==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" Hangul]")
                                    else:
                                        sel[5] = True   
                        
                            if(o==0):
                                per.addNewWord(w,h,f)
                            if(o==1):
                                per.addNewVerb(w,h,f)
            else:
                print("\nSUCCESS: the word was found!"
                +"\n\t")
                print(resul)

        if (opt == 3):
            f= ''
            data = 0
            o = ''
            _o = o
            resul = []
            a = ''

            w =''
            h=''
            t=''

            os.system('cls')

            while(not sel[8]):
                    o = int(input("\nIntroduce which you want to modify:\n\n"
                    + "\n\t0: a word in the library\n\n"
                    + "\n\t1: a verb in the library\n\n"))

                    if (o<0) or (o>1):
                        print("\nERROR: wrong option, \n\nmust use a"
                        +"\n\tinteger between: 0-1"
                        +"\n\t[modifying Option]")
                    else:
                        sel[8] = True

            if(o==0):
                _o = 'word'
            if(o==1):
                _o = 'verb'
            sel[8]=False

            while(not sel[6]):
                    data = int(input("\nIntroduce how do you want to find the "+ _o +":\n\n"
                    + "\n\t0: Through English original word\n\n"
                    + "\n\t1: Through Korean traslated word\n\n"
                    + "\n\t2: Through romanized transliteration\n\n"))


                    if (data<0) or (data>2):
                        print("\nERROR: wrong option, \n\nmust use a"
                        +"\n\tinteger between: 0-2"
                        +"\n\t[modifying "+ _o +" Option]")
                    else:
                        sel[6] = True
            
            sel[6]=False
            os.system('cls')
            while(not sel[6]):
                    f = str(input("\nIntroduce "+ _o +" you wish to modify:\n\n"
                    + "\n\tmust be a non empty string\n\n"))


                    if (f==''):
                        print("\nERROR: Null String, \n\nmust use a"
                        +"\n\tnon void String for:"
                        +"\n\t["+ _o +" to modify]")
                    else:
                        sel[6] = True   

            if(o==0):
                resul = per.findWord(f,data)
            if(o==1):
                resul = per.findVerb(f,data)

            sel[6]=False
            os.system('cls')     
            if(resul[0]==''):
                while(not sel[6]):
                        a = str(input("\n There was no coincidence in the library for that "+ _o +"."
                        +"\n\t do you wanna introduce it as a new one?"
                        +"\n\t y/n ?"))


                        if (a!='y')and (a!='n'):
                            print("\nERROR: Non valid String, \n\nmust use a"
                            +"\n\t simple y or n for:"
                            +"\n\t[add the non-Found "+ _o +" option]")
                        else:
                            sel[6] = True 
                if(a=='y'):
                    if(data==0):
                            sel[6]=False
                            os.system('cls')
                            while(not sel[6]):
                                    h = str(input("\nIntroduce the new "+ _o +" in Korean \n\n"
                                    + "\n\tmust be in Hangul\n\n"))


                                    if (h==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" Hangul]")
                                    else:
                                        sel[6] = True   

                            sel[6]=False
                            while(not sel[6]):
                                    t = str(input("\nIntroduce the new "+ _o +" transliteration \n\n"
                                    + "\n\tmust be in latin alphabet\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" transliteration]")
                                    else:
                                        sel[6] = True   

                            if(o==0):
                                per.addNewWord(f,h,t)
                            if(o==1):
                                per.addNewVerb(f,h,t)
                    if(data==1):
                            sel[6]=False
                            os.system('cls')
                            while(not sel[6]):
                                    w = str(input("\nIntroduce the new "+ _o +" English \n\n"
                                    + "\n\tmust be in English\n\n"))


                                    if (w==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" English]")
                                    else:
                                        sel[6] = True   

                            sel[6]=False
                            while(not sel[6]):
                                    t = str(input("\nIntroduce the new "+ _o +" transliteration \n\n"
                                    + "\n\tmust be in latin alphabet\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" transliteration]")
                                    else:
                                        sel[6] = True   

                            if(o==0):
                                per.addNewWord(w,f,t)
                            if(o==1):
                                per.addNewVerb(w,f,t)
                    if(data==2):
                            sel[6]=False
                            os.system('cls')
                            while(not sel[6]):
                                    w = str(input("\nIntroduce the new "+ _o +" English \n\n"
                                    + "\n\tmust be in English\n\n"))


                                    if (w==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" English]")
                                    else:
                                        sel[6] = True   

                            sel[6]=False
                            while(not sel[6]):
                                    h = str(input("\nIntroduce the new "+ _o +" in Korean \n\n"
                                    + "\n\tmust be in Hangul\n\n"))


                                    if (h==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" Hangul]")
                                    else:
                                        sel[6] = True   

                            if(o==0):
                                per.addNewWord(w,h,f)
                            if(o==1):
                                per.addNewVerb(w,h,f)
            else:
                    if(data==0):
                            sel[6]=False
                            os.system('cls')
                            while(not sel[6]):
                                    h = str(input("\nIntroduce the new "+ _o +" in Korean \n\n"
                                    + "\n\tmust be in Hangul\n\n"))


                                    if (h==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" Hangul]")
                                    else:
                                        sel[6] = True   

                            sel[6]=False
                            while(not sel[6]):
                                    t = str(input("\nIntroduce the new "+ _o +" transliteration \n\n"
                                    + "\n\tmust be in latin alphabet\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" transliteration]")
                                    else:
                                        sel[6] = True   
                        
                            if(o==0):
                                per.modifyWord(f,h,t,data)
                            if(o==1):
                                per.modifyVerb(f,h,t,data)

                    if(data==1):
                            sel[6]=False
                            os.system('cls')
                            while(not sel[6]):
                                    w = str(input("\nIntroduce the new "+ _o +" English \n\n"
                                    + "\n\tmust be in English\n\n"))


                                    if (w==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" English]")
                                    else:
                                        sel[6] = True   

                            sel[6]=False
                            while(not sel[6]):
                                    t = str(input("\nIntroduce the new "+ _o +" transliteration \n\n"
                                    + "\n\tmust be in latin alphabet\n\n"))


                                    if (t==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" transliteration]")
                                    else:
                                        sel[6] = True   
                        
                            if(o==0):
                                per.modifyWord(w,f,t,data)
                            if(o==1):
                                per.modifyVerb(w,f,t,data)

                    if(data==2):
                            sel[6]=False
                            os.system('cls')
                            while(not sel[6]):
                                    w = str(input("\nIntroduce the new "+ _o +" English \n\n"
                                    + "\n\tmust be in English\n\n"))


                                    if (w==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" English]")
                                    else:
                                        sel[6] = True   

                            sel[6]=False
                            while(not sel[6]):
                                    h = str(input("\nIntroduce the new "+ _o +" in Korean \n\n"
                                    + "\n\tmust be in Hangul\n\n"))


                                    if (h==''):
                                        print("\nERROR: Null String, \n\nmust use a"
                                        +"\n\tnon void String for:"
                                        +"\n\t[new "+ _o +" Hangul]")
                                    else:
                                        sel[6] = True   
                        
                            if(o==0):
                                per.modifyWord(w,h,f,data)
                            if(o==1):
                                per.modifyVerb(w,h,f,data)
             
      
##Exam

def exam():
 
 while (not sel[2]):
        limit =0
        for x in range(len(sel)-1):
         sel[x+1] = False

        print("\nLets prepare the exam. \n\nChoose an option:"
        +"\n\t0: -Vocabulary exam."
        +"\n\t1: -Grammar exam."
        +"\n\t2: -Numbers exam."
        +"\n\t3: -Verbs exam."
        +"\n\t4: -Revise recent exams."
        +"\n\t5: -Returning to Initial menu")

        while(not sel[3]):
            try:
                opt = int(input("\nChoose one option \n\n"
                + "\n\tmust be an integer between 0-5\n\n"))
            except ValueError:
                print("option must be an integer")
                exit(-1)

            if (opt<0) or (opt>5):
                print("\nERROR: wrong option, \n\nmust use a"
                +"\n\tinteger between 0-5 for:"
                +"\n\t[ExamMenu option]")
            else:
                sel[3] = True

        if (opt == 5):
            sel[2]= True
            os.system('cls')

        if (opt == 0):
            os.system('cls')
            while(not sel[4]):
                try:
                    limit = int(input("\nChoose the number of words:\n\n"
                    + "\n\tmust be an integer\n\n"))
                except ValueError:
                    print("option must be an integer")
                    exit(-1)

                if (limit<1):
                    print("\nERROR: wrong option, \n\nmust use a"
                    +"\n\tpositive non-zero integer for:"
                    +"\n\t[vocabularyExam option]")
                else:
                    sel[4] = True

            e.prepareExam(limit) 

        #if (opt == 1): 

        if (opt == 2):
            os.system('cls')
            while(not sel[7]):
                try:
                    limit = int(input("\nChoose the number of questions:\n\n"
                    + "\n\tmust be an integer\n\n"))
                except ValueError:
                    print("option must be an integer")
                    exit(-1)

                if (limit<1):
                    print("\nERROR: wrong option, \n\nmust use a"
                    +"\n\tpositive non-zero integer for:"
                    +"\n\t[numbersExam option]")
                else:
                    sel[7] = True 

            e.prepareNumbersExam(limit)

        if (opt == 3):
            os.system('cls')
            while(not sel[8]):
                try:
                    limit = int(input("\nChoose the number of questions:\n\n"
                    + "\n\tmust be an integer\n\n"))
                except ValueError:
                    print("option must be an integer")
                    exit(-1)

                if (limit<1):
                    print("\nERROR: wrong option, \n\nmust use a"
                    +"\n\tpositive non-zero integer for:"
                    +"\n\t[numbersExam option]")
                else:
                    sel[8] = True 

            e.prepareVerbsExam(limit)

        if (opt == 4):
            os.system('cls')

            while(not sel[5]):
                os.system('cls')
                try:
                    for x in range(len(per.exams)):
                         print("\n"+str(x)+": "+"Exam taken on "+str(per.exams[x][len(per.exams[x])-1])+".\n"
                               "\t")
                         
                    d = int(input("\nChoose between all the exams available: \n\n"
                    + "\n\tmust be an integer between [0 -"+str((len(per.checks)-1))+")\n\n"))
                except ValueError:
                    print("option must be an integer")
                    exit(-1)

                if (d<0) or (d>(len(per.checks)-1)):
                    print("\nERROR: wrong option, \n\nmust use an"
                    +"\n\tinteger between 0 and"+str((len(per.checks)-1))+ " stored for:"
                    +"\n\t[examRevision option]")
                else:
                    sel[5] = True
            
            rev = per.reviseExam(d)
            print("\n")
            print(rev[0])
            print("\n\t")
            print("\n")
            print(rev[1])

##Loop

def mainMenu ():

 while (not sel[0]):
        for x in range(len(sel)):
                sel[x] = False
                
        print("\n Welcome to HanGoal, \n\nChoose an option:"
        +"\n\t0: -Entering the Library."
        +"\n\t1: -Exam menu."
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
        
        if (opt==1):
            os.system('cls')
            exam()

        if (opt==2):
            print("\n Hope u will come back!")
            sel[0]= True
            os.system('cls')
           
mainMenu()