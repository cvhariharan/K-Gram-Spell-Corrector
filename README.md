## K-Gram Spell Checker
This is a simple K-Gram spell checker with basic indexing. The indexing here is only to retrieve words with the same initial bi-gram. Similarity is calculated using Jaccard coefficient.  

### Create Index
```python
# wordsList is a list of words with correct spellings, the second param is the value of k for k-gram
c = Correct(wordsList, 2)
c.createIndex() # creates an index.json file in the working directory and loads it
```

### Load Index
```python
c.loadIndex() # looks for index.json in the working directory and loads it, not needed if createIndex is used
```

### Get Word Suggestions
```python
res = c.suggest("palontolody") # returns a sorted dict of words in ascending order, ordered by Jaccard coefficients
print(res[len(res)-1]) # print the last word which will have the largest Jaccard coefficient
```