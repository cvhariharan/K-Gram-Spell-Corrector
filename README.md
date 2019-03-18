## K-Gram Spell Corrector

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/acd14b694f124576976f24f0406e8f49)](https://app.codacy.com/app/cvhariharan/K-Gram-Spell-corrector?utm_source=github.com&utm_medium=referral&utm_content=cvhariharan/K-Gram-Spell-corrector&utm_campaign=Badge_Grade_Dashboard)

This is a simple K-Gram spell corrector with basic indexing. The indexing here is only to retrieve words with the same initial bi-gram. Similarity is calculated using Jaccard coefficient.  

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