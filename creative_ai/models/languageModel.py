import random
from creative_ai.models.unigramModel import UnigramModel
from creative_ai.models.bigramModel import BigramModel
from creative_ai.models.trigramModel import TrigramModel
from creative_ai.utils.print_helpers import key_value_pairs


class LanguageModel():

    def __init__(self):
        """
        Requires: nothing
        Modifies: self (this instance of the NGramModel object)
        Effects:  This is the NGramModel constructor. It sets up an empty
                  dictionary as a member variable.
        """
        self.models = [TrigramModel(), BigramModel(), UnigramModel()]

    def __str__(self):

        output_list = [
            '{} contains {} trained paths.'.format(
                model.__class__.__name__, key_value_pairs(model.nGramCounts)
                ) for model in self.models
            ]

        output = '\n'.join(output_list)

        return output

    def updateTrainedData(self, text):

        for model in self.models:
            model.trainModel(text)

    def selectNGramModel(self, sentence):
        """
        Requires: models is a list of NGramModel objects sorted by descending
                  priority: tri-, then bi-, then unigrams.
        Modifies: nothing
        Effects:  returns the best possible model that can be used for the
                  current sentence based on the n-grams that the models know.
                  (Remember that you wrote a function that checks if a model can
                  be used to pick a word for a sentence!)
        """
        for model in self.models:
            if model.trainingDataHasNGram(sentence):
                return model

        return self.models[-1]

    def weightedChoice(self, candidates):
        """
        Requires: candidates is a dictionary; the keys of candidates are items
                  you want to choose from and the values are integers
        Modifies: nothing
        Effects:  returns a candidate item (a key in the candidates dictionary)
                  based on the algorithm described in the spec.
        """
        keys = []
        items = []

        for k, v in candidates.items():
            keys.append(k)
            items.append(v)

        for i in range(1, len(items)):
            items[i] = items[i] + items[i - 1]

        num = random.randrange(0, max(items))

        for i, v in enumerate(items):
            if v > num:
                return keys[i]

    def getCandidateToken(self, sentence):
        """
        Requires: sentence is a list of strings, and this model can be used to
                  choose the next candidate token for the current sentence
        Modifies: nothing
        Effects:  returns the next candidate token to be added to sentence by calling
                  the getCandidateDictionary, weightedChoice, and
                  selectNGramModel functions.
                  For more information on how to put all these functions
                  together, see the spec.
        """
        modelToUse = self.selectNGramModel(sentence)
        return self.weightedChoice(modelToUse.getCandidateDictionary(sentence))


    def getNextToken(self, sentence, filter=None):
        """
        Requires: sentence is a list of strings, and this model can be used to
                  choose the next token for the current sentence
        Modifies: nothing
        Effects:  returns the next token to be added to sentence by calling
                  the getCandidateDictionary and weightedChoice functions.
                  For more information on how to put all these functions
                  together, see the spec.
        """

        token = self.getCandidateToken(sentence)

        if filter != None:
            while token not in filter:
                token = self.getCandidateToken(sentence)

        return token


if __name__ == '__main__':
    # test cases here

    model = LanguageModel()

    text = [ ['the', 'brown', 'fox'], ['the', 'lazy', 'dog'] ]

    model.updateTrainedData(text)

    print(model.getNextToken(['the']))

    print(model)