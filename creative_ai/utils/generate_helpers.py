import random
from creative_ai.models.languageModel import LanguageModel
from creative_ai.data.dataLoader import loadLyrics, loadMusic, prepData


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

def sentenceTooLong(desiredLength, currentLength):
    """
    Requires: nothing
    Modifies: nothing
    Effects:  returns a bool indicating whether or not this sentence should
              be ended based on its length. This function has been done for
              you.
    """
    STDEV = 1
    val = random.gauss(currentLength, STDEV)
    return val > desiredLength

def printSongLyrics(verseOne, verseTwo, chorus):
    """
    Requires: verseOne, verseTwo, and chorus are lists of lists of strings
    Modifies: nothing
    Effects:  prints the song. This function is done for you.
    """
    verses = [verseOne, chorus, verseTwo, chorus]

    print()
    for verse in verses:
        for line in verse:
            print((' '.join(line)).capitalize())
        print()

def trainLyricModels(lyricDirs, test=False):
    """
    Requires: lyricDirs is a list of directories in data/lyrics/
    Modifies: nothing
    Effects:  loads data from the folders in the lyricDirs list,
              using the pre-written DataLoader class, then creates an
              instance of each of the NGramModel child classes and trains
              them using the text loaded from the data loader. The list
              should be in tri-, then bi-, then unigramModel order.
              Returns the list of trained models.
    """
    model = LanguageModel()

    for ldir in lyricDirs:
        lyrics = prepData(loadLyrics(ldir))
        model.updateTrainedData(lyrics)

    return model

def trainMusicModels(musicDirs):
    """
    Requires: lyricDirs is a list of directories in data/midi/
    Modifies: nothing
    Effects:  works exactly as trainLyricsModels, except that
              now the dataLoader calls the DataLoader's loadMusic() function
              and takes a music directory name instead of an artist name.
              Returns a list of trained models in order of tri-, then bi-, then
              unigramModel objects.
    """

    model = LanguageModel()

    for mdir in musicDirs:
        music = prepData(loadMusic(mdir))
        model.updateTrainedData(music)

    return model