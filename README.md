# sp24-lab8
Materials for week 8 lab in CS-370, which includes Ch. 8 "A File Archiver" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_March 5, 2024_

Organization:
* SDX-ch10: The code files for the _SDX Ch. 10_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Jack A. and Grant D.

## Team Roles for Part 1
Who will start out as
* DRIVER: Grant
* NAVIGATOR: Jack

You will switch halfway through the _SDX Ch. 10_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 10?
File storage and compression and retrieval using hashing. Using manifests to store sets of versions of files. (In our case a more basic one using just csv files and no remote storage)


* What questions did you have about the material in the chapters? What did you find confusing?
How exeactly does glob() work?


### Exercise 1: What familiar design pattern does this chapter employ?

Write your answers to the questions below.

* What design pattern do you think Wilson is using in section 10.4, and why?
We think that Wilson is using a subclass method design pattern. He refactored his work in backup.py to use OOP and defined an Archive base class that other subclasses like ArchiveLocal can inherit from and extend/override methods of. 

* How might you use this pattern to implement other kinds of archive features/properties?

We can create a new specific type of Archive class that inherits from the base Archive class and add new methods that are specific to its use or override the backup method if we need to change it's functionality. We can also add additionall attributes as needed.

### Exercise 2: Applying the ideas in this chapter to your group project

Many of the concepts---and their implementations---in this chapter could be useful for your personal archive project. With your partner, discuss how you might extend the code from this chapter to be useful in your group project. Why and how might you do so?

Include a summary of your discussion here.

1) Using their design patterns and using base classes
2) Version control for audio files (keep track of the state of audio file as we work. could come in handy if a user adds a filter to their file and doesn't like it tec.)
3) Manifests for playlists (keep track of the state of all the files and their metadata)

### Exercise 3: SDX section 10.6

Write a short summary of what you did (which exercises) below.

