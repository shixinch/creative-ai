from unigramModel import UnigramModel
from bigramModel import BigramModel
from trigramModel import TrigramModel

from creative_ai.data.dataLoader import loadLyrics, loadMusic

from creative_ai.utils import sentenceTooLong

class LanguageModel:

    def __init__(self):
        """
        Requires: nothing
        Modifies: self
        Effects:  initializes a LanguageModel object with
                    * one UnigramModel
                    * one BigramModel
                    * one TrigramModel
                  This function has been written for you.
        """
        self.uniModel = UnigramModel()
        self.biModel = BigramModel()
        self.triModel = TrigramModel()

    def weightedChoice(self, candidates):
        """
        Requires: candidates is a dictionary of { candidateToken: count } pairs
        Modifies: nothing
        Effects:  returns a candidate token (a key in the candidates dictionary)
                  based on the weight of each candidate's count in the model
        """
        pass

    def getNextCandidate(self, sentence):
        """
        Requires: candidates is a dictionary of { possibleToken: count } pairs
        Modifies: nothing
        Effects:  returns a candidate token (a key in the candidates dictionary)
                  selects a weighted choice from the given model's candidate tokens
        """
        pass

    def getNextToken(self, sentence, possibleTokens):
        """
        Requires: sentence is a list of tokens
                  possibleTokens is a list of tokens
        Modifies: nothing
        Effects:  returns the next token to be added to sentence by calling
                  the getCandidateDictionary and weightedChoice functions.
        """
        pass

    def generateSentence(self, desiredLength, possibleTokens):
        """
        Requires: The ngram models in this language model have been trained
                  desiredLength > 0
        Modifies: nothing
        Effects:  returns a sentence of tokens generated using the ngram models
                  The final sentence should NOT include any of the special symbols.
        """
        sentence = ['^::^', '^:::^']
        pass

    def trainLyricModels(self, lyricDirs):
        """
        Requires: lyricDirs is a list of directories in data/lyrics/
        Modifies: nothing
        Effects:  for every directory in lyricDirs
                call loadLyrics on that directory
                and trains all three ngram models on the returned text
        """
        #for ldir in lyricDirs:
        #    lyrics = loadLyrics(ldir)
        #    for model in models:
        #        model.trainModel(lyrics)
        #return models
        pass

    def trainMusicModels(self, musicDirs):
        """
        Requires: musicDirs is a list of directories in data/midi/
        Modifies: nothing
        Effects:  for every directory in musicDirs
                call loadMusic on that directory
                and trains all three ngram models on the returned text
        """
        # call dataLoader.loadMusic for each directory in musicDirs
        pass

    def output_models(val, output_fn = None):
        """
        Requires: nothing
        Modifies: nothing
        Effects:  outputs the dictionary val to the given filename. Used
                in Test mode. This function has been done for you.
        """
        from pprint import pprint
        if output_fn == None:
            print("No Filename Given")
            return
        with open('TEST_OUTPUT/' + output_fn, 'wt') as out:
            pprint(val, stream=out)

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    # Add your tests here
    pass
