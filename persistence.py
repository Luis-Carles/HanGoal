###Dependencies
import numpy as nm
import random
import exam as e
import backup as b


##Deprecated: Local option
#Variables

fileName = '.\local\lib'+ '.npy'
words = nm.load(fileName)
lib = words.tolist()

fileExam = '.\local\exams'+ '.npy'
questions = nm.load(fileExam)
exams = questions.tolist()

fileResults = '.\local\checks'+ '.npy'
answers = nm.load(fileResults)
checks = answers.tolist()

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
    results = e.main(exam)
    checks.append(results)
    exams.append(exam)

    nm.save(fileExam,exams)
    nm.save(fileResults,checks)

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