class TrigramModel:

    def trainModel(self, text):
        """
        Requires: text is a list of lists of tokens
        Modifies: self.nGramCounts
        Effects:  this function populates self.nGramCounts as a 3D
                  dictionary of { token1: { token2: { token3: count }}} pairs
        """
        pass

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of tokens, and len(sentence) >= 2
        Modifies: nothing
        Effects:  returns True if the last two tokens in sentence match
                  some trigram in this model
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

if __name__ == '__main__':
    # Add your test cases here
    pass
