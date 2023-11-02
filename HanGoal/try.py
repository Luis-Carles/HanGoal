import calcule as c
verbs = [['stand','서다','seoda'],['sell','파다','pada'],['watch','보다','boda'],
        ['wait','기다리다','gidarida'],['learn','배우다','baeuda'],['being pretty','예쁘다','yeppeuda'],
        ['eat','먹다','meokda'],['sit','앉다','anjda'],['count','세다','seda'],['become','되다','dweda'],['go back','뒤다','dwida']]

for x in range (len(verbs)):
    print(c.calculateVerb(verbs[x],0,0,0))
    print(c.calculateVerb(verbs[x],1,0,0))