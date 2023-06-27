###Dependencies
import numpy as nm


##Deprecated: Local option
#Variables
fileName = 'lib'
file = fileName + '.npy'
words = nm.load(file)
lib = words.tolist()

#Methods

def getWordKey(w,data):
    found = False
    i =0
    pos = -1
    cand= "lol"

    while (not found):
        cand = words[i][data]
        if (cand == w):
            found = True
            pos = i

    return pos

def addNewWord(w,h,t):

    lib.append(([w,h,t]))
    nm.save(file,lib)

def findWord(w,data):

    resul = getWordKey(w,data)

    if(resul==-1):
        return ['','','']
    else:
        return words[resul]





## Option 2: redis

##Option 3: Mong