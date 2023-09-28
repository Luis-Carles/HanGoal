###Dependencies
import numpy as nm
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

########################
#PERSISTENCE METHODS
########################

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

def saveExam(exam,results):
    # Saving the exam and the results
    checks.append(results)
    now = str(datetime.now())
    exam.append(now)
    exams.append(exam)

    nm.save(fileExam,exams)
    nm.save(fileResults,checks)

## Option 2: redis

## Option 3: Mongo