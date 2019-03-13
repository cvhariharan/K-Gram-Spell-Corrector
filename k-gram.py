import json, operator

class Correct:

    def __init__(self, wordsList, k=2):
        self.k = k
        self.wordsList = wordsList

    def getKGrams(self, word):
        kgrams = []
        if len(word) >= 2:
            for i in range(len(word)-self.k):
                kgrams.append(word[i:i+self.k])
        return kgrams

    def jaccard(self, word1, word2):
        kgramWord1 = set(self.getKGrams(word1))
        kgramWord2 = set(self.getKGrams(word2))
        return len(kgramWord1.intersection(kgramWord2))/len(kgramWord1.union(kgramWord2))

    def createIndex(self):
        self.index = {}
        for i in range(len(self.wordsList)):
            #Only store the first k-gram 
            kgram = self.getKGrams(self.wordsList[i])
            if len(kgram) >= 1:
                kgram = kgram[0]
                if kgram not in self.index.keys():
                    self.index[kgram] = [self.wordsList[i]]
                else:
                    self.index[kgram].append(self.wordsList[i])

        with open('index.json', 'w') as indexFile:
            indexFile.write(json.dumps(self.index))
    
    def loadIndex(self, indexFile):
        with open(indexFile) as index:
            self.index = json.loads(index.read())
    
    def suggest(self, word):
        wordScores = {}
        if not hasattr(self, 'index'):
            return ""
        else:
            if len(word) >= 2:
                firstGram = self.getKGrams(word)[0]
                if firstGram in self.index.keys():
                    similarWords = self.index[firstGram]
                    for i in range(len(similarWords)):
                        wordScores[similarWords[i]] = self.jaccard(similarWords[i], word)
                else:
                    return ""

        
        sortedScores = sorted(wordScores.items(), key=operator.itemgetter(1))
        return sortedScores
    

def load_words():
    with open('words.txt') as word_file:
        valid_words = list(word_file.read().split())
    return valid_words

wordsList = load_words()
print(len(wordsList))
c = Correct(wordsList, 2)
# c.createIndex()
c.loadIndex('./index.json')
res = c.suggest("latop")
print(c.jaccard("latop", "laptop"))
# print(res)
print(res[len(res)-2])