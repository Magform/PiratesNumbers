# Pirates Numbers
## _Sea of Thieves gold, doublons and sinked boats counter_

Pirates Numbers is a software written in python which, thanks to an OCR tool for python ([pytesseract]), allows you to identify how much gold and how many doubloons you have and tell you how much you have earned from the previous check, very useful if you are interested in knowing exactly how much gold you have earned in the current game session for example.<br>
Inside the software there is also a function that allows you to count how many boats have been sunk, this data is also saved in a text file, thus allowing it to be saved even if the software is restarted.

## Installation and frist configuration
The frist thing to do to use this software is to download it and extract all the file from the zip, after this you need to execute PiratesNumbers.exe and do the frist configuration. 
### Frist configuration
To configure the software you need to start Sea of Thieves then enter a random session press TAB and do a screenshot, now you can close the game, open the screenshot and place it fullscreen using F11.<br>
Next this you have to return on Pirates Numbers and click on option now a window will open for you, my advice is to click "Test preset" and click "use" on all preset until in the two boxes that appears gold and doubloons appear respectively.<br> <b>It's important that appears only the number of gold and the number of doubloons, nothing else </b><br>
Now you need only to close this windows, click on "Apply preset" and select the preset that give you the right results.<br>
If no preset is good for your amount of gold and doubloons or for your monitor, you need to go and find the coordinates of all four points by yourself, or just one if you have between 10000000 and 99999999 gold and between 10000 and 99999 doubloons.<br>
To do this you need to try to guess the value in the Option windows, generally the value is:
- between 1600 and 2000 for the frist value
- 75 for the second value
- between 1800 and 2200 for the third value
- 110 for the fourth value
- between 1500 and 1900 for the fifth value
- 75 for the sixth value
- between 1600 and 2000 for the seventh value
- 110 for the eighth value
If you have the amount of gold and doubloons mentioned before once you have entered the first two values you can try clicking "Test with standard distance" and if it give you the right results you can click on "Apply with standard distance".<br>
If you don't have that amount of gold and doubloons or the result is not as it should be, you have to go and find all the coordinate using the test button, after which you will have to click on Apply.
Now all the setup is done, you only need to open the game and, when you need to do some check you have to open the software and click on refresh, go on the game and press TAB so that your gold and doubloons appear at the top right.

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

Pirates numbers uses a lot of library to work properly:
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
   
   [discord]: <https://discord.gg/AENAggdyYj>
   [here]: <https://stackoverflow.com/questions/53898526/tkinter-labels-overlapping>
  
