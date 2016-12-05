# EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.


# Tasks
## 1-5. Complete the tasks seen in the first-fifth.py files! (~120 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently, after each task, with descriptive commit messages [1p]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm seen in `third.py`. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:


### How can you create a graphical user interface and draw a rectangle on it in python? What are the tools needed for it? [2p]
#### Your answer:
First of all we have to import the Tkinter module, it is the standard GUI (graphical user interface) library for python /from tkinter import */. After that we can start using it, within a function, or within OO structure. How does it works? First of all we've to set our root(root = Tk() ). After that we have to set our Canvas, for easier use later we should give it to a variable (canvas = canvas = Canvas(root, width="300", height="300"), now we can set the width and height of our canvas, after that in the next line canvas.pack() our canvas builder. 
Now we can draw our rectangle! If we want to draw more, with different positions, than we should use another variable for this, box = canvas.create_rectangle(50,50, param, param2). So as you can see we called our canvas var which is the Canvas, and inside there are lot of built in drawing methods. After we set our rectangle, we call root.mainloop(), we always end our drawing-part by calling the mainloop method of the root window.

### What does V stand for in MVC? [2p]
#### Your answer:
