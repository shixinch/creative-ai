class UnigramModel:

    def trainModel(self, text):
        """
        Requires: text is a list of lists of tokens
        Modifies: self.nGramCounts
        Effects:  this function populates self.nGramCounts as a dictionary
                  of { token1: count } pairs
        """
        pass

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of tokens
        Modifies: nothing
        Effects:  returns True if this unigram model has trained on tokens
        """
        pass

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of tokens, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next tokens to be added
                  to the current sentence.
        """
        pass

###############################################################################
# Main
###############################################################################

# This is the code python runs when unigramModel.py is run as main
if __name__ == '__main__':

    # An example trainModel test case
    uni = UnigramModel()
    text = [ [ 'brown' ] ]
    uni.trainModel(text)
    # Should print: { 'brown' : 1 }
    print(uni)

    text = [ ['the', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]
    uni.trainModel(text)
    # Should print: { 'brown': 1, 'dog': 1, 'fox': 1, 'lazy': 1, 'the': 2 }
    print(uni)

    # An example trainingDataHasNGram test case
    uni = UnigramModel()
    sentence = "Eagles fly in the sky"
    print(uni.trainingDataHasNGram(sentence)) # should be False
    uni.trainModel(text)
    print(uni.trainingDataHasNGram(sentence)) # should be True
