###Dependencies
import numpy as nm


##Deprecated: Local option
#Variables
fileName = 'lib'
file = fileName + '.npy'
words = nm.load(file)
lib = words.tolist()
#print(lib)

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



## Option 2: redis

##Option 3: Mong