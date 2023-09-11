###Dependencies
import numpy as nm
import random
import exam as e
import backup as b
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

def calculeDate (y,m,d):

    year = y
    month = m
    day = d
    answer = [['',''],['',''],['','']]

    if (y<2000):
        answer[0][0] = '천구백'
        answer[0][1] = 'cheongubaek'
        year = year - 1900

    if(y>=2000): 
        answer[0][0] = '이천'
        answer[0][1] = 'icheon'
        year = year - 2000 

    if(9 < year < 20):
        answer[0][0] = answer[0][0] + '십'
        answer[0][1] = answer[0][1] + 'sib'
        year = year - 10

    if(19 < year < 30):
        answer[0][0] = answer[0][0] + '이십'
        answer[0][1] = answer[0][1] + 'isib'
        year = year - 20 

    if(29 < year < 40):
        answer[0][0] = answer[0][0] + '삼십'
        answer[0][1] = answer[0][1] + 'samsib'
        year = year - 30 

    if(39 < year < 50):
        answer[0][0] = answer[0][0] + '사십'
        answer[0][1] = answer[0][1] + 'sasib'
        year = year - 40

    if(49 < year < 60):
        answer[0][0] = answer[0][0] + '오십'
        answer[0][1] = answer[0][1] + 'osib'
        year = year - 50

    if(59 < year < 70):
        answer[0][0] = answer[0][0] + '육십'
        answer[0][1] = answer[0][1] + 'yuksib'
        year = year - 60

    if(69 < year < 80):
        answer[0][0] = answer[0][0] + '칠십'
        answer[0][1] = answer[0][1] + 'chilsib'
        year = year - 70

    if(79 < year < 90):
        answer[0][0] = answer[0][0] + '팔십'
        answer[0][1] = answer[0][1] + 'palsib'
        year = year - 80

    if(89 < year < 100):
        answer[0][0] = answer[0][0] + '구십'
        answer[0][1] = answer[0][1] + 'gusib'
        year = year - 90

    if(0 < year < 10):
        if(year == 1):
            answer[0][0] = answer[0][0] + '일'
            answer[0][1] = answer[0][1] + 'il'
            year = year - 1

        if(year == 2):
            answer[0][0] = answer[0][0] + '이'
            answer[0][1] = answer[0][1] + 'i'
            year = year - 2

        if(year == 3):
            answer[0][0] = answer[0][0] + '삼'
            answer[0][1] = answer[0][1] + 'sam'
            year = year - 3

        if(year == 4):
            answer[0][0] = answer[0][0] + '사'
            answer[0][1] = answer[0][1] + 'sa'
            year = year - 4

        if(year == 5):
            answer[0][0] = answer[0][0] + '오'
            answer[0][1] = answer[0][1] + 'o'
            year = year - 5

        if(year == 6):
            answer[0][0] = answer[0][0] + '육'
            answer[0][1] = answer[0][1] + 'yuk'
            year = year - 6

        if(year == 7):
            answer[0][0] = answer[0][0] + '칠'
            answer[0][1] = answer[0][1] + 'chil'
            year = year - 7

        if(year == 8):
            answer[0][0] = answer[0][0] + '팔'
            answer[0][1] = answer[0][1] + 'pal'
            year = year - 8

        if(year == 9):
            answer[0][0] = answer[0][0] + '구'
            answer[0][1] = answer[0][1] + 'gu'
            year = year - 9

    if(0 < month < 13):
        if(month == 1):
            answer[1][0] = answer[1][0] + '일'
            answer[1][1] = answer[1][1] + 'il'

        if(month == 2):
            answer[1][0] = answer[1][0] + '이'
            answer[1][1] = answer[1][1] + 'i'

        if(month == 3):
            answer[1][0] = answer[1][0] + '삼'
            answer[1][1] = answer[1][1] + 'sam'

        if(month == 4):
            answer[1][0] = answer[1][0] + '사'
            answer[1][1] = answer[1][1] + 'sa'

        if(month == 5):
            answer[1][0] = answer[1][0] + '오'
            answer[1][1] = answer[1][1] + 'o'

        if(month == 6):
            answer[1][0] = answer[1][0] + '유'
            answer[1][1] = answer[1][1] + 'yu'

        if(month == 7):
            answer[1][0] = answer[1][0] + '칠'
            answer[1][1] = answer[1][1] + 'chil'

        if(month == 8):
            answer[1][0] = answer[1][0] + '팔'
            answer[1][1] = answer[1][1] + 'pal'

        if(month == 9):
            answer[1][0] = answer[1][0] + '구'
            answer[1][1] = answer[1][1] + 'gu'

        if(month == 10):
            answer[1][0] = answer[1][0] + '시'
            answer[1][1] = answer[1][1] + 'si'

        if(month == 11):
            answer[1][0] = answer[1][0] + '십일'
            answer[1][1] = answer[1][1] + 'sibil'

        if(month == 12):
            answer[1][0] = answer[1][0] + '십이'
            answer[1][1] = answer[1][1] + 'sibi'

    return answer


def prepareNumbersExam(l):
    exam = []
    limit = l
    Q = ['','','']
    n = 0
    dayWeeks = [['monday','월요일','woryoil'],['tuesday','화요일','hwayoil'],['wednesday','수요일','suyoil'],
                ['thursday','목요일','mogyoil'],['friday','금요일','geumyoil'],['saturday','토요일','toyoil'],
                ['sunday','일요일','iryoil']]

    if limit>50:
        limit = 50

    while (limit>0):
        n = random.randint(0,4)

        if(n == 0):
            y = random.randint(1900,2024)
            m = random.randint(1,12)
            d = random.randint(1,31)
            dw = random.randint(1,7)

            answer = calculeDate(y,m,d)

            Q[0]= str(y) + '/' + str(m) + '/' + str(d) + ', ' + dayWeeks[dw-1][0]
            Q[1]= answer[0][0] + ' 년 ' + answer[1][0] + '월 ' + answer[2][0] + ' 일, ' + dayWeeks[dw-1][1]
            Q[2]= answer[0][1] + ' 년 ' + answer[1][1] + '월 ' + answer[2][1] + ' 일, ' + dayWeeks[dw-1][2]
        
        if(n == 1):
            print("Doing")

        if(n == 2):
            print("Doing")

        if(n == 3):
            print("Doing")

        if(n == 4):
            print("Doing")

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