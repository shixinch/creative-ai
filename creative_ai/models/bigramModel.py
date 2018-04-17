from creative_ai.utils.print_helpers import ppGramJson

class BigramModel():

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the NGramModel object)
        Effects:  This is the NGramModel constructor. It sets up an empty
                  dictionary as a member variable.
        """
        self.nGramCounts = {}

    def __str__(self):
        """
        Requires: nothing
        Modifies: nothing
        Effects:  Returns the string to print when you call print on an
                  NGramModel object. This string will be formatted in JSON
                  and display the currently trained dataset.
                  This function is done for you.
        """

        return ppGramJson(self.nGramCounts)

    def trainModel(self, text):
        """
        Requires: text is a list of lists of strings
        Modifies: self.nGramCounts, a two-dimensional dictionary. For examples
                  and pictures of the BigramModel's version of
                  self.nGramCounts, see the spec.
        Effects:  this function populates the self.nGramCounts dictionary,
                  which has strings as keys and dictionaries of
                  {string: integer} pairs as values.
        """
        data = text

        for line in data:
            for word1, word2 in zip(line, line[1:]):
                try:
                    self.nGramCounts[word1][word2] += 1
                except:
                    try:
                        self.nGramCounts[word1].update({word2: 1})
                    except:
                        self.nGramCounts[word1] = {word2: 1}

    def trainingDataHasNGram(self, sentence):
        """
        Requires: sentence is a list of strings
        Modifies: nothing
        Effects:  returns True if this n-gram model can be used to choose
                  the next token for the sentence. For explanations of how this
                  is determined for the BigramModel, see the spec.
        """

        if len(sentence) < 1:
            return False

        word = sentence[-1]
        return word in self.nGramCounts

    def getCandidateDictionary(self, sentence):
        """
        Requires: sentence is a list of strings, and trainingDataHasNGram
                  has returned True for this particular language model
        Modifies: nothing
        Effects:  returns the dictionary of candidate next words to be added
                  to the current sentence. For details on which words the
                  BigramModel sees as candidates, see the spec.
        """
        word = sentence[-1]

        if word in self.nGramCounts:
            return self.nGramCounts[word]

        return {}

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    # Add your test cases here
    bi = BigramModel()
    text = [ ['the', 'brown', 'fox'], ['the', 'lazy', 'dog'], ['the', 'brown', 'lazy', 'fox'] ]
    bi.trainModel(text)
    print(bi)
