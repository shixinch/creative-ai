class BigramModel:

    def trainModel(self, text):
        """
        Requires: text is a list of lists of tokens
        Modifies: self.nGramCounts
        Effects:  this function populates self.nGramCounts as a 2D
                  dictionary of { token1: { token2: count}} pairs
        """
        pass

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of tokens, and len(sentence) >= 1
        Modifies: nothing
        Effects:  returns True if the last token in sentence matches
                  some bigram in this model
        """
        pass

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of tokens, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence.
        """
        pass

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    # Add your test cases here
    pass
