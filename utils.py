# Used in sentenceTooLong
import random

def printSongLyrics(verseOne, verseTwo, chorus):
    """
    Requires: verseOne, verseTwo, and chorus are lists of lists of strings
    Modifies: nothing
    Effects:  prints the song. This function is done for you.
    """
    verses = [verseOne, chorus, verseTwo, chorus]
    print("RANDOMLY GENERATED SONG by " + TEAM)
    print("*" * 40)
    print
    for verse in verses:
        for line in verse:
            print (' '.join(line)).capitalize()
        print

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

def runTestMode():
    print("-" * 10, "TEST MODE", "-" * 10)
    testLyricsModels = trainLyricModels(TESTLYRICSDIRS)
    trigram = testLyricsModels[0].nGramCounts
    bigram = testLyricsModels[1].nGramCounts
    unigram = testLyricsModels[2].nGramCounts
    output_models(unigram, output_fn = "unigram_student.txt")
    output_models(bigram, output_fn = "bigram_student.txt")
    output_models(trigram, output_fn = "trigram_student.txt")
    print('Student models have been written to the TEST_OUTPUT folder')
