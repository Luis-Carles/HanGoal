###Dependencies
import random
import os
import calcule as cal
import persistence as per

########################
#SHOWING EXAMS FUNCTIONS
########################

## First option: console
def exam (e,c):
    results = []
    response = ['','']
    sel = False
    opt = 0
    choices = c
    calification = 0

    for x in range (len(e)):
        opt = random.choice(choices)

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

def vExam(e):
    return exam(e,[0,0,1,2])

def nExam(e):
    return exam(e,[0,0,1,1])

########################
#PREPARE EXAMS FUNCTIONS
########################

def prepareExam(l):
    exam = []
    rep = []
    limit = l
    n = 0
    m = 0
    found = False

    results = []

    if limit>len(per.lib):
        limit = len(per.lib)
    
    while (limit>0):
        n = random.randint(0,(len(per.lib)-1))
        m = len(rep)
        i = 0
        found = False

        while (not found) and (m>0):
            if(rep[i]==per.lib[n]):
                found =True
            else:
                m = m-1
                i = i+1

        if(not found):
            exam.append(per.lib[n])
            rep.append(per.lib[n])
            limit = limit -1

    # Saving the exam and the results
    results = vExam(exam)
    per.saveExam(exam,results)

def prepareNumbersExam(l):
    exam = []
    limit = l
    n = 0
    dayWeeks = [['monday','월요일','woryoil'],['tuesday','화요일','hwayoil'],['wednesday','수요일','suyoil'],
                ['thursday','목요일','mogyoil'],['friday','금요일','geumyoil'],['saturday','토요일','toyoil'],
                ['sunday','일요일','iryoil']]
    meridium = [['am','오전','ojeon'],['pm','오후','ohu']]
    units = [['kg','킬로그램','killogeuraem'],['cm','센티미터','sentimiteo'],['room','호','ho']]
    nounQ = [['years','살','sal'],['people','명','myeong'],['animals','마리','mari'],
             ['things','개','gae'],['bottles','병','byeong'],['books','권','gwon']]
    prefixes = [['0082','공공팔두','gonggongpaldu'],['0034','공공삼사','gonggongsamsa']]

    if limit>50:
        limit = 50

    while (limit>0):
        n = random.randint(0,5) 
        Q = ['','','']
        answer = []

        if(n == 0):
            y = random.randint(1900,2024)
            m = random.randint(1,12)
            d = random.randint(1,31)
            dw = random.randint(1,7)

            answer = cal.calculateDate(y,m,d)

            Q[0]= str(y) + '/' + str(m) + '/' + str(d) + ' ' + dayWeeks[dw-1][0]
            Q[1]= answer[0][0] + ' 년 ' + answer[1][0] + '월 ' + answer[2][0] + ' 일 ' + dayWeeks[dw-1][1]
            Q[2]= answer[0][1] + ' nyeon ' + answer[1][1] + 'wol ' + answer[2][1] + ' il ' + dayWeeks[dw-1][2]
        
        if(n == 1):
            h = random.randint(1,12)
            min = random.randint(0,59)
            sec = random.randint(0,59)
            mr = random.randint(0,1)
            
            if(sec<10):
                sec = '0' + sec
                
            answer = cal.calculateTime(h,min,sec)

            Q[0]= str(h) + ':' + str(min) + ':' + str(sec) + ' ' + meridium[mr][0]
            Q[1]= answer[0][0] + ' 시 ' + answer[1][0] + '분 ' + answer[2][0] + ' 초 ' + meridium[mr][1]
            Q[2]= answer[0][1] + ' si ' + answer[1][1] + 'bun ' + answer[2][1] + ' cho ' + meridium[mr][2]

        if(n == 2):
            price = random.randint(1000,100000)

            answer = cal.calculateBig(price)

            Q[0]= str(price) + ' won'
            Q[1]= answer[0] + ' 원' 
            Q[2]= answer[1] + ' won' 

        if(n == 3):
            unit = random.randint(1,1000)
            which = 0
            if(unit>=225):
                which = 2
            if(130<unit<225):
                which = 1

            answer = cal.calculateBig(unit)

            Q[0]= str(unit) + ' ' + units[which][0]
            Q[1]= answer[0] + ' ' + units[which][1]
            Q[2]= answer[1] + ' ' + units[which][2]

        if(n == 4):
            quantity = random.randint(1,99)
            which = random.randint(0,5)

            answer = cal.calculateQuantity(quantity)

            Q[0]= str(quantity) + ' ' + nounQ[which][0]
            Q[1]= answer[0] + ' ' + nounQ[which][1]
            Q[2]= answer[1] + ' ' + nounQ[which][2]

        if(n == 5):
            prefix = random.randint(0,1)
            phone1 = random.randint(100,999)
            phone2 = random.randint(100,999)
            phone3 = random.randint(100,999)

            answer = cal.calculatePhone(phone1,phone2,phone3)

            Q[0]= prefixes[prefix][0] + '-' + str(phone1) + '-' + str(phone2) + '-' + str(phone3)
            Q[1]= prefixes[prefix][1] + '-' + answer[0][0] + '-' + answer[1][0] + '-' + answer[2][0] 
            Q[2]= prefixes[prefix][2] + '-' + answer[0][1] + '-' + answer[1][1] + '-' + answer[2][1] 

        exam.append(Q)
        limit = limit -1

    # Saving the exam and the results
    results = nExam(exam)
    per.saveExam(exam,results)

def prepareVerbsExam(l):
    exam = []
    limit = l
    pf = 0
    n = 0
    manners = 0
    v = 0

    if limit>50:
        limit = 50

    while (limit>0):
        manners = random.randint(0,1)
        if(manners == 0):
            pf = 0
        if(manners == 1):
            pf = 1
    
        n = random.randint(0,6)
        negation = random.choice([0,0,0,1,2])

        Q = ['','','']
        answer = []

        if(n == 0):
            v = random.randint(0,len(per.verbs))

            answer = cal.calculateVerb(per.verbs[v],pf,n,negation)

            Q[0]= answer[0]
            Q[1]= answer[1]
            Q[2]= answer[2]
        
        if(n == 1):
            v = random.randint(0,len(per.verbs))

            answer = cal.calculateVerb(per.verbs[v],pf,n,negation)

            Q[0]= ''
            Q[1]= ''
            Q[2]= ''

        if(n == 2):
            v = random.randint(0,len(per.verbs))

            answer = cal.calculateVerb(per.verbs[v],pf,n,negation)

            Q[0]= ''
            Q[1]= ''
            Q[2]= ''

        if(n == 3):
            v = random.randint(0,len(per.verbs))

            answer = cal.calculateVerb(per.verbs[v],pf,n,negation)

            Q[0]= ''
            Q[1]= ''
            Q[2]= ''

        if(n == 4):
            v = random.randint(0,len(per.verbs))

            answer = cal.calculateVerb(per.verbs[v],pf,n,negation)

            Q[0]= ''
            Q[1]= ''
            Q[2]= ''

        if(n == 5):
            v = random.randint(0,len(per.verbs))

            answer = cal.calculateVerb(per.verbs[v],pf,n,negation)

            Q[0]= ''
            Q[1]= ''
            Q[2]= ''

        if(n == 6):
            v = random.randint(0,len(per.verbs))

            answer = cal.calculateVerb(per.verbs[v],pf,n,negation)

            Q[0]= ''
            Q[1]= ''
            Q[2]= ''
  
        exam.append(Q)
        limit = limit -1

    # Saving the exam and the results
    results = vExam(exam)
    per.saveExam(exam,results)

## Second option: react