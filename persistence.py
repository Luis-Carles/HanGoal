###Dependencies
import numpy as nm
import random
import exam as e


##Deprecated: Local option
#Variables
fileName = '.\local\lib'
file = fileName + '.npy'
words = nm.load(file)
lib = words.tolist()

fileExam = '.\local\exams'+ '.npy'
questions = nm.load(fileExam)
exams = questions.tolist()

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
    nm.save(file,lib)

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

    nm.save(file,lib)

def prepareExam(l):
    exam = []
    rep = []
    limit = l
    n = 0
    m = 0
    i = 0
    found = False

    results = []

    if limit>len(lib):
        limit = len(lib)
    
    while (limit>0):
        n = random.randint(0,limit)
        m = len(rep)
        found = False

        while (not found) and (m>0):

            if(rep[i]==lib[n]):
                found =True
            else:
                m = m-1
                i = i+1

        if(not found):
            exam.append(lib[n])
            limit = limit -1

    # Saving the exam and the results
    results = e.main(exam)
    final = (exam,results)
    exams.append(final)

    nm.save(fileExam,exams)


## Option 2: redis

## Option 3: Mongo