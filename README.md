# pyqt5-hangman
Hangman game based on python, PyQt5 and QML

Requirements: python5, pyqt5


In Qt there’s an example of a Hangman, the visual part is written in QML, and the core, which is written in C++. We translated the C++ part to Python and changed some things so it worked how we wanted.
 It is written so we can monetize it. We treat the vowels separately from the other letters. So in case we decided to actually monetize it, the user would only be able to use the vowels in case he/ she paid for them, or in function of the wins the user has achieved without the vowels, just guessing the words.

The first thing we need to do is prepare the computer so we can execute afterwards the program and we have all the libraries that we need.

First we need to install Visual Studio Code. https://code.visualstudio.com/docs/?dv=win

Then we have to install the extensions
- The python extension is already installed
- Install the QML extension →QML 1.0.0 : bbenoist.qml
- Install the Visual Studio IntelliCode 1.1.6→visualstudioexptteam.vscodeintellicode
Install Python 3.7
Once it’s installed verify it’s good by opening the command station and executing →python --version
Actualize pip with →python -m pip install --upgrade pip
Install PyQt5 with → pip3 install pyqt5
Select in the VS Code the correct python interpreter (the one we installed pyqt5)
We started from a version of the hangman for Qt in C++.
- Coned →https://github.com/eskilblomfeldt/qthangman.git
- Prepare the files:
   + We created a directory called pyqthangman
   + We copied the QML file into the pyqthangman directory.
 - Create the file hangman.py which will be our main file.
   This file will have three parts:
   + The imports
   + The data class
   + The main
- We changed the C++ part to python 
- Install →pyinstaller--> pip3 install --upgrade pyinstaller



