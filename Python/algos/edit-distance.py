
class editDistance:
    def __init__(self, word1, word2):
        self.word1 = word1.lower()
        self.word2 = word2.lower() 
        self.similarityArray = [[0 for j in range(0, len(self.word1) + 1)] for i in range(0, len(self.word2) + 1)]

    # word 1 is horizontal, word 2 is vertical
    
    
        #     method to initialize the base edges of the matrix as follows as well as create each row
        #     _ a s d f
        #     _ 0 1 2 3 4
        #     h 1
        #     j 2
        #     k 3
    def initSimilarities(self):
        for j in range(0, len(self.word2) + 1):
            if j == 0:
                for i in range(0, len(self.word1) + 1):
                    self.similarityArray[j][i] = i
            else:
                self.similarityArray[j][0] = j

    
        #   /**
        #    * method to fill in the cells of similarityArray using dynamic programming, the process of which is explained in
        #    * the pdf along with the assignment
        #    *
        #    * coordinate (i, j) represents the ith column (i - 1th char index of word1) and
        #    * jth row (j - 1th char index of word2) starting from (1, 1)
        #    */
    def fillSimilarities(self):
        for j in range(1, len(self.word2) + 1):
            for i in range(1, len(self.word1) + 1):
                if self.word2[j - 1] == self.word1[i - 1]:
                    # costs nothing to convert suffixes, cost dependent on the value of the suffix without the comparing prefixes
                    self.similarityArray[j][i] = self.similarityArray[j - 1][i - 1]
                else:
                    # min of the costs of the suffix when inserting, replacing, or deleting, respectively
                    self.similarityArray[j][i] = 1 + min(self.similarityArray[j - 1][i], self.similarityArray[j - 1][i - 1], self.similarityArray[j][i - 1])

    def findScore(self):
       return self.similarityArray[len(self.word2)][len(self.word1)]

    

test1 = editDistance("gazed", "hand")
test1.initSimilarities()
test1.fillSimilarities()
print(str(test1.similarityArray))
print(test1.findScore())
