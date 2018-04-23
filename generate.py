#!/usr/bin/env python

# Used in Starter Code
import sys

# Model imports
from models.languageModel import LanguageModel

# Used In Music Generation
from musicInfo import KEY_SIGNATURES, NOTE_DURATIONS

# Used in Lyrics Generation
from utils import printSongLyrics

# Test Mode
from utils import runTestMode

# Global constants
TEAM = 'YOUR NAME HERE' # FIXME add your team name here
LYRICSDIRS = ['the_beatles']
TESTLYRICSDIRS = ['the_beatles_test']
MUSICDIRS = ['gamecube']
WAVDIR = 'wav/'

PROMPT = """
(1) Generate song lyrics by The Beatles
(2) Generate a song using data from Nintendo Gamecube
(3) Quit the music generator
> """

def runLyricsGenerator():
    """
    Requires: nothing
    Modifies: nothing
    Effects:  creates a LanguageModel, trains it on lyric data,
              generates a verse one, a verse two, and a chorus, then
              calls printSongLyrics to print the song out.
    """
    verseOne = []
    verseTwo = []
    chorus = []
    pass

def runMusicGenerator(songName):
    """
    Requires: songName is the string name of a file to write wav songs to
    Modifies: nothing
    Effects:  creates a LanguageModel, trains it on music data,
              uses models to generate a song and write it to the file
              named songName.wav
    """
    song = []
    pass

def main():
    """
    Requires: Nothing
    Modifies: Nothing
    Effects:  This is your main function, which is done for you. It runs the
              entire generator program for both the reach and the core.

              It prompts the user to choose to generate either lyrics or music.
    """

    if len(sys.argv) == 2:
        if sys.argv[1] == "--test":
            runTestMode()
            sys.exit()

    lyricsTrained = False
    musicTrained = False

    print('Welcome to the ' + TEAM + ' music generator!')
    while True:
        userInput = raw_input(PROMPT)
        if userInput == '1':
            print("Under construction")
            '''
            FIXME uncomment these lines when ready AND delete "Under construction"
            if not lyricsTrained:
                print('Starting lyrics generator and loading data...')
                lyricsModels = trainLyricModels(LYRICSDIRS)
                print('Data successfully loaded')
                lyricsTrained = True

            runLyricsGenerator(lyricsModels)
            '''
        elif userInput == '2':
            print("Under construction")
            '''
            FIXME uncomment these lines when ready AND delete "Under construction"
            if not musicTrained:
                print('Starting music generator and loading data...')
                musicModels = trainMusicModels(MUSICDIRS)
                print('Data successfully loaded')
                musicTrained = True

            songName = raw_input('What would you like to name your song? ')
            runMusicGenerator(musicModels, WAVDIR + songName + '.wav')
            '''
        elif userInput == '3':
            print('Thank you for using the ' + TEAM + ' music generator!')
            sys.exit()
        elif userInput.isdigit():
            print("Invalid menu option!")
        else:
            print("Please enter a number.")

# This is how python tells if the file is being run as main
if __name__ == '__main__':
    main()
