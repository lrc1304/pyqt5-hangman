#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import random

if sys.platform == "linux" or sys.platform == "linux2":
    # TODO remove this OpenGL fix when PyQt
    # doesn't require OpenGL to be loaded first.
    # NOTE This must be placed before any other imports!
    import ctypes
    from ctypes.util import find_library
    libGL = find_library("GL")
    ctypes.CDLL(libGL, ctypes.RTLD_GLOBAL)

from PyQt5 import QtWidgets, uic
from PyQt5.QtQuick import *

from PyQt5.QtCore import pyqtProperty, QCoreApplication, QObject, QUrl, pyqtSignal, pyqtSlot
from PyQt5.QtQml import qmlRegisterType, QQmlComponent, QQmlEngine


class Data(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialise the value of the properties.
        self._word = ''
        self._lettersOwned = ''
        self._wordList = []                

        # Load words
        with open('words.txt') as fp:
            for line in fp:
                self._wordList.append(line[:-1])
        
        

    # Define signals
    wordChanged = pyqtSignal()
    lettersOwnedChanged = pyqtSignal()
    errorCountChanged = pyqtSignal()
    vowelBought = pyqtSignal(['QChar'])

    # Define the getter of the 'word' property.  The C++ type of the
    # property is QString which Python will convert to and from a string.
    @pyqtProperty('QString', notify = wordChanged)
    def word(self):
        return self._word
    
    # Private setter with signal emission
    def setWord(self, word):
        if (self._word != word):
            self._word = word
            self.wordChanged.emit()


    # Define the getter of the 'lettersOwned' property.  The C++ type of the
    # property is QString which Python will convert to and from a string.
    @pyqtProperty('QString', notify = lettersOwnedChanged)
    def lettersOwned(self):
        return self._lettersOwned

    # Private setter with signal emission
    def setLettersOwned(self, lettersOwned):
        if (self._lettersOwned != lettersOwned):
            self._lettersOwned = lettersOwned
            self.lettersOwnedChanged.emit()

    @pyqtProperty('QString')
    def vowels(self):
        return "AEIOU"
    
    @pyqtProperty('QString')
    def consonants(self):
        return "BCDFGHJKLMNPQRSTVWXYZ"


    # Define the getter of the 'errorCount' property.  The C++ type and
    # Python type of the property is int.
    @pyqtProperty(int, notify = errorCountChanged)
    def errorCount(self):
        nbErrors = 0
        for c in self._lettersOwned:
            if ((c in self._word) == False):
                nbErrors = nbErrors +1
        return nbErrors
  

    # Define the setter of the 'shoeSize' property.
    #@shoeSize.setter
    #def shoeSize(self, shoeSize):
    #    self._shoeSize = shoeSize

    @pyqtSlot()
    def reset(self):
        print('reset')
        self._lettersOwned=""
        self.lettersOwnedChanged.emit()
        self.errorCountChanged.emit()
        self.chooseRandomWord()

    @pyqtSlot()
    def reveal(self):
        print('reveal')
        self._lettersOwned = self.vowels + self.consonants
        self.lettersOwnedChanged.emit()
        self.errorCountChanged.emit()

    @pyqtSlot()
    def gameOverReveal(self):
        print('gameOverReveal')
        self._lettersOwned = self.vowels + self.consonants
        self.lettersOwnedChanged.emit()


    @pyqtSlot('QString')
    def requestLetter(self, value):
        print('requestLetter: ' + value)
        if (len(value) == 1):
            c = str(value[0]).upper()
            currentVowels = str(self.vowels)
            if (c in currentVowels):
                self.buyVowel(c)
            else:
                self.registerLetterBought(c)


    @pyqtSlot('QString')
    def guessWord(self, value):
        print('guessWord: ' + value)
        if (value.upper() == self._word.upper()):
            self._lettersOwned = self._lettersOwned + self._word.upper()
        else:
            # Add penalty
            pass
        self.lettersOwnedChanged.emit()

    
    def chooseRandomWord(self):
        if self._wordList.count != 0:
            i = random.randint(0, len(self._wordList) -1)
            self.setWord(self._wordList[i].upper())

    def buyVowel(self, c):
        self.registerLetterBought(c)

    def registerLetterBought(self, c):
        if (c in self._lettersOwned):
            return
        self._lettersOwned = self._lettersOwned + str(c)
        self.lettersOwnedChanged.emit()
        if ((c in self._word) == False):
            self.errorCountChanged.emit()



if __name__ == "__main__":

    # Build Application
    app = QtWidgets.QApplication(sys.argv)

    # Register the Python type.  Its URI is 'HangmanData', it's v1.0 and the type
    # will be called 'Data' in QML.
    qmlRegisterType(Data, 'HangmanData', 1, 0, 'Data')
    
    # Data
    data = Data()

    # Build view
    view = QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    rootContext = view.engine().rootContext()
    rootContext.setContextProperty("applicationData", data)



    # Load QML File
    current_path = os.path.abspath(os.path.dirname(__file__))
    qml_file = os.path.join(current_path, 'qml/hangman/main.qml')
    view.setSource(QUrl.fromLocalFile(qml_file))
    if view.status() == QQuickView.Error:
        sys.exit(-1)

    # Show the view
    view.show()

    data.chooseRandomWord()

    # Enter event loop
    res = app.exec_()

    # Cleanup
    del view
    sys.exit(res)

