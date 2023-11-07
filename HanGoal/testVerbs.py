import calcule as c

verbs = [['eat','먹다','meokda'],['sit','앉다','anjda'],['marry','결혼하다','gyeolhonhada'],
         ['national of','출신이다','chulsinida'],['count','세다','seda'],['wait','기다리다','gidarida'],
         ['stand','서다','seoda'],['learn','배우다','baeuda'],['being pretty','예쁘다','yeppeuda'],
         ['gggg','게다','geda'],['become','되다','dweda'],['go back','뒤다','dwida']]

#Present
print('\nPRESENT\n')
for x in range (len(verbs)):
    print(c.calculateVerb(verbs[x],0,0,0))
    print(c.calculateVerb(verbs[x],1,0,0))

#Past
print('\nPAST\n')
for x in range (len(verbs)):
    print(c.calculateVerb(verbs[x],0,1,0))
    print(c.calculateVerb(verbs[x],1,1,0))

#Past
print('\nPAST PROGRESSIVE\n')
for x in range (len(verbs)):
    print(c.calculateVerb(verbs[x],0,2,0))
    print(c.calculateVerb(verbs[x],1,2,0))