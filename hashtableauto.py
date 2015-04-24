from collections import defaultdict
import re
import random

letters = 'abcdefghijklmnopqrstuvwxyz'

def closest(word):
    splitset = [(word[:x],word[x:]) for x in range(len(word)+1)]
    deleteset = [x+y[1:] for (x,y) in splitset if y]
    transposeset = [x+y[1]+y[0]+y[2:] for (x,y) in splitset if len(y)>1]
    replaceset = [x+z+y[1:] for (x,y) in splitset for z in letters if y]
    insertset = [x+z+y for (x,y) in splitset for z in letters]
    return set(deleteset+transposeset+replaceset+insertset)

def getwords(filename):
    text = file(filename).read()
    words = re.findall('[a-z]+', text.lower())
    return words

class hashtable(object):

    def __init__(self, words):
        self.hashed = [[] for x in range(50)]
        for word in words:
            random.seed(word)
            (self.hashed[random.randint(0,49)]).append(word)

    def lookup(self, word):
        random.seed(word)
        return (word in self.hashed[random.randint(0,49)])

class dl_algorithm(object):

    def __init__(self, dictname, structtype):
        if structtype == 1:
            try:
                self.dict = hashtable(getwords(dictname))
            except NameError:
                print ("The hashtable methods are not working properly... yet. - Larry Zhang, 2015")
        elif structtype == 2:
            try:
                self.dict = trie(getwords(dictname))
            except NameError:
                print ("The trie methods are not working properly... yet. - Humphrey Obuobi, 2015")
        elif structtype == 3:
            try:
                self.dict = dawg(getwords(dictname))
            except NameError:
                print ("The D.A.W.G. methods are not working properly... yet. - Ben Zheng, 2015")
        else:
            print ("Invalid structtype argument, there are only 3 types of structs currently defined.")
            print ("We currently only have a hashtable, trie, and D.A.W.G. defined.")
            print ("These correspond to arguments 1, 2, and 3. Other arguments are not acceptable.")

        print ("ITS WORKING ITS WORKING - Shing-Shing Cao, 2015")

    def correct(self, word):
        if (self.dict).lookup(word) == True:
            return word
        else:
            dist1 = set(x for x in closest(word) if (self.dict).lookup(x));
            if dist1:
                return dist1.pop();
            else:
                dist2 = set(y for x in closest(word) for y in closest(x) if (self.dict).lookup(y));
                if dist2:
                    return dist2.pop();
                else:
                    return "No similar word found"