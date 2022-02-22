# Pirates Number
## _Sea of Thieves gold, doublons and sinked boats counter_

Pirates Number is a software written in python which, thanks to an OCR tool for python ([pytesseract]), allows you to identify how much gold and how many doubloons you have and tell you how much you have earned from the previous check, very useful if you are interested in knowing exactly how much gold you have earned in the current game session for example.<br>
Inside the software there is also a function that allows you to count how many boats have been sunk, this data is also saved in a text file, thus allowing it to be saved even if the software is restarted.

## Installation and frist configuration
The frist thing to do to use this software is to download it and extract all the file from the zip in a directory, after this you need to do the frist configuration. 
### Frist configuration
To configure the softer the frist time you use it 

## Known problems
_In order of importance, it is not said, however, that it wavered made in this order_

#### Overlapping numbers
In all the data that change with the various checks, they have the problem that the new data is pasted on top of the previous one instead of replacing it, thus overlapping it if it is smaller in size. <br>
I've found a potential solution [here] but it takes a lot of time to implement it directly in the complete rewrite of the code.

#### Credits button exits the screen
When previous check or last check is present then the part of the GUI to the right of this shifts slightly to the right and part of the credits button exits the screen.<br>
To fix this I just need to remove the milliseconds from the time.

## Future Development
_In order of importance, it is not said, however, that it wavered made in this order_

#### Complete rewrite of the code
I wrote the code a year ago now my programming knowledge has increased and trying to reread it I realize that I have not used many things that instead I should have used to make the code more readable and more compact.<br>
So I intend to rewrite it and comment it so that others can understand it better and can give their contribution to the project.

#### Remove knwon problems
I want to take some time to fix the problems that I and other users discover.

#### Website development
I also wanted to develop a site of the project that would provide the download of the files and all the information about the project

#### Add more presets
If you have different monitor sizes or different amounts of doubloons or gold you will need to use different presets for the software so it is my intention to add as many presets as possible so that everyone can use a preset without having to make it their own.<br>
I also ask those who create their presets to encode them on [discord] or publish them directly on github in order to help those who need the same preset.

## Tech

Pirates number uses a lot of library to work properly:
- [pytesseract] - Recognize and “read” the text embedded in images
- [Pillow] - Image processing
- [keyboard] - register hotkeys
- [tkinter] - GUI toolkit
- [time] - Time-related functions
- [os] - Use operating system dependent functionality
- [datetime] - Manipulate dates
- [glob] - Unix style pathname pattern expansion
- [inspect] - Inspect live objects
- [re] - Regular expression operations
- [functiontools] - Higher-order functions and operations on callable objects
- [tkinter.font] - Tkinter font wrapper
- [webbrowser] - Open link
 
## Collaborate to the project 
 
## License

GPL-3.0 License

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [pytesseract]: <https://pypi.org/project/pytesseract/>
   [Pillow]: <https://pypi.org/project/Pillow/>
   [tkinter]: <https://docs.python.org/3/library/tkinter.html>
   [time]: <https://docs.python.org/3/library/time.html>
   [datetime]: <https://docs.python.org/3/library/datetime.html#module-datetime>
   [keyboard]: <https://pypi.org/project/keyboard/>
   [os]: <https://docs.python.org/3/library/os.html>
   [glob]: <https://docs.python.org/3/library/glob.html>
   [inspect]: <https://docs.python.org/3/library/inspect.html>
   [re]: <https://docs.python.org/3/library/re.html>
   [functiontools]: <https://docs.python.org/3/library/functools.html>
   [tkinter.font]: <https://docs.python.org/3/library/tkinter.font.html>
   [webbrowser]: <https://docs.python.org/3/library/webbrowser.html>
   
   [discord]: <>
   [here]: <https://stackoverflow.com/questions/53898526/tkinter-labels-overlapping>
  
