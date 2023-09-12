###Dependencies
import numpy as nm
import random
import exam as e
import backup as b
import calcule as cal
from datetime import datetime


##Deprecated: Local option
#Variables

fileName = '.\local\lib'+ '.npy'
words = nm.load(fileName,allow_pickle=True)
lib = words.tolist()
#print(lib)

fileExam = '.\local\exams'+ '.npy'
questions = nm.load(fileExam,allow_pickle=True)
exams = questions.tolist()
#print(exams)

fileResults = '.\local\checks'+ '.npy'
answers = nm.load(fileResults,allow_pickle=True)
checks = answers.tolist()
#print(answers)

#Methods

def getWordKey(f,data):
    found = False
    i =0
    pos = -1
    cand= "lol"
    limit = len(lib)

    while (not found) and (limit>0):
        cand = lib[i][data]
        if (cand == f):
            found = True
            pos = i
        i=i+1
        limit = limit -1

    return pos

def addNewWord(w,h,t):

    lib.append(([w,h,t]))
    nm.save(fileName,lib)

def findWord(w,data):

    resul = getWordKey(w,data)

    if(resul==-1):
        return ['','','']
    else:
        return lib[resul]
    
def modifyWord(w,h,t,data):
    if(data==0):
        pos = getWordKey(w,data)
        lib[pos][1]=h
        lib[pos][2]=t
    if(data==1):
        pos = getWordKey(h,data)
        lib[pos][0]=w
        lib[pos][2]=t
    if(data==2):
        pos = getWordKey(t,data)
        lib[pos][0]=w
        lib[pos][1]=h

    nm.save(fileName,lib)

def prepareExam(l):
    exam = []
    rep = []
    limit = l
    n = 0
    m = 0
    found = False

    results = []

    if limit>len(lib):
        limit = len(lib)
    
    while (limit>0):
        n = random.randint(0,(len(lib)-1))
        m = len(rep)
        i = 0
        found = False

        while (not found) and (m>0):
            if(rep[i]==lib[n]):
                found =True
            else:
                m = m-1
                i = i+1

        if(not found):
            exam.append(lib[n])
            rep.append(lib[n])
            limit = limit -1

    # Saving the exam and the results
    results = e.vExam(exam)
    checks.append(results)
    now = str(datetime.now())
    exam.append(now)
    exams.append(exam)

    nm.save(fileExam,exams)
    nm.save(fileResults,checks)

def prepareNumbersExam(l):
    exam = []
    limit = l
    Q = ['','','']
    n = 0
    dayWeeks = [['monday','월요일','woryoil'],['tuesday','화요일','hwayoil'],['wednesday','수요일','suyoil'],
                ['thursday','목요일','mogyoil'],['friday','금요일','geumyoil'],['saturday','토요일','toyoil'],
                ['sunday','일요일','iryoil']]
    meridium = [['am','오전','ojeon'],['pm','오후','ohu']]
    units = [['kg','킬로그램','killogeuraem'],['cm','센티미터','sentimiteo'],['room','호','ho']]
    nounQ = [['years','살','sal'],['people','명','myeong'],['animals','마리','mari'],
             ['things','개','gae'],['bottles','병','byeong'],['books','권','gwon']]
    prefixes = [['010','Korea'],['34','Spain']]

    if limit>50:
        limit = 50

    while (limit>0):
        n = random.randint(0,4) # 4--->5 when phone number is done

        if(n == 0):
            y = random.randint(1900,2024)
            m = random.randint(1,12)
            d = random.randint(1,31)
            dw = random.randint(1,7)

            answer = cal.calculateDate(y,m,d)

            Q[0]= str(y) + '/' + str(m) + '/' + str(d) + ', ' + dayWeeks[dw-1][0]
            Q[1]= answer[0][0] + ' 년 ' + answer[1][0] + '월 ' + answer[2][0] + ' 일, ' + dayWeeks[dw-1][1]
            Q[2]= answer[0][1] + ' 년 ' + answer[1][1] + '월 ' + answer[2][1] + ' 일, ' + dayWeeks[dw-1][2]
        
        if(n == 1):
            h = random.randint(1,12)
            min = random.randint(0,59)
            sec = random.randint(0,59)
            mr = random.randint(0,1)
            
            answer = cal.calculateTime(h,min,sec)

            Q[0]= str(h) + ':' + str(min) + ':' + str(sec) + ' ' + meridium[mr][0]
            Q[1]= answer[0][0] + ' 시 ' + answer[1][0] + '분 ' + answer[2][0] + ' 초 ' + meridium[mr][1]
            Q[2]= answer[0][1] + ' 시 ' + answer[1][1] + '분 ' + answer[2][1] + ' 초 ' + meridium[mr][2]

        if(n == 2):
            price = random.randint(1000,100000)

            answer = cal.calculateBig(price)

            Q[0]= str(price) + ' 원'
            Q[1]= answer[0] + ' 원' 
            Q[2]= answer[1] + ' 원' 

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
            which = random.randint(0,6)

            answer = cal.calculateBig(quantity)

            Q[0]= str(quantity) + ' ' + nounQ[which][0]
            Q[1]= answer[0] + ' ' + nounQ[which][1]
            Q[2]= answer[1] + ' ' + nounQ[which][2]

        if(n == 5):
            prefix = random.randint(0,1)
            phone1 = random.randint(1,99)
            phone2 = random.randint(1,99)

            answer = cal.calculatePhone(int(prefixes[prefix][0]),phone1,phone2)

            Q[0]= prefixes[prefix][0] + '-' + str(phone1) + '-' + str(phone2) 
            Q[1]= answer[0][0] + '-' + answer[1][0] + '-' + answer[2][0] 
            Q[2]= answer[0][1] + '-' + answer[1][1] + '-' + answer[2][1] 

        exam.append(Q)
        limit = limit -1

    # Saving the exam and the results
    results = e.nExam(exam)
    checks.append(results)
    now = str(datetime.now())
    exam.append(now)
    exams.append(exam)

    nm.save(fileExam,exams)
    nm.save(fileResults,checks)

def reviseExam(d):
    return (exams[d],checks[d])

newones =[[],[]]

def addSeveral():
    for x in range(len(newones)):
        lib.append(([newones[x][0],newones[x][1],newones[x][2]]))

    nm.save(fileName,lib)

def retrieveBackup(ver):
    if(ver == 1):
        lib = b.backup1
        nm.save(fileName,lib)

## Option 2: redis

## Option 3: Mongo