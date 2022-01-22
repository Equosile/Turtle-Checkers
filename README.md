# Turtle-Checkers  
[ Python 3 Turtle Library ] Pilot-Test: Checkers  
  
  
[ INTRODUCTION ]  
Even thought the original purpose of this project is about "Minimax With Alpha-Beta Pruning Agent",  
the performance test of Python Turtle is still meaningful to demonstrate,  
such that the project is shared throughout this GitHub page.  
  
Turtle can help in drawing objects on its virtual canvas.  
Other than utilising Turtle, there can be much more professional approaches  
such as composing individual graphic engines by exploiting Vulkan, OpenGL, etc.  
Nevertheless, one major advantage of using Turtle is derived from its simplicity.  
Turtle has already prepared its own drawing methods,  
which can be convenient in terms of educational purposes.  
  
[ A Detailed Information For Turtle ]  
https://docs.python.org/3/library/turtle.html  
  
In addition, Turtle is a sort of basic components in Python 3,  
so predominantly additional installations like "pip" are not required.  
  
This project demonstates the performance test of Turtle,  
playing a simple checkers board game.  
  
  
[ INSTRUCTION ]  
  
Python Programme: checkers.py  
  
The programme has been tested within the Anaconda 3 python development environment.  
Other environments especially based on Web Browsers like Google Colap CANNOT execute the local turtle library.  
Since there is no same graphical support on Web Browsers,  
the Turtle formalities on web versions are different to local styles.  
  
In order to launch the programme, type the following command on the Anaconda bash.  
  
python checkers.py  
  
e.g.) In Anaconda bash,  
?> python checkers.py  
  
  
[ POSSIBLE ISSUES ]  
  
Some operating systems like certain linux distributions may not support python tkinter.  
Because tutle has to succeed the tkinter legacies,  
those OSs would have issues in executing the tutle library.  
  
In this case, python tkinter should additionally be installed.  
  
e.g.) In Debian style,  
#> sudo apt-get install python3-tk  
  
e.g.) In Anaconda style,  
#> pip install python-tk  
  
  
