# sp24-lab8
Materials for week 8 lab in CS-370, which includes Ch. 8 "A File Archiver" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_March 5, 2024_

Organization:
* SDX-ch10: The code files for the _SDX Ch. 10_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Coden + Rhys

## Team Roles for Part 1
Who will start out as
* DRIVER: Coden
* NAVIGATOR: Rhys

You will switch halfway through the _SDX Ch. 9_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 10?
You can save files, hash them, and hash their version histories. Basically, you can make Git using python.
* What questions did you have about the material in the chapters? What did you find confusing?
How is this different from how GitHub is done?


### Exercise 1: What familiar design pattern does this chapter employ?

Write your answers to the questions below.

* What design pattern do you think Wilson is using in section 10.4, and why?
Delegation because it delegates method to the superclass object and doesn't use inheritance. The superclass is
the base class that prescribes the general steps in creating a backup. 
He's using it to refactor and clean up his code :). By splitting things up into multiple classes, it's easier to 
see where things are happening or where things are going wrong (more maintainable).
* How might you use this pattern to implement other kinds of archive features/properties?
Separating metadata and sounds into different (but related) objects, making it so we can keep things static when they
can be and more easily search for features and things. (makes it easier to do stuff).

### Exercise 2: Applying the ideas in this chapter to your group project

Many of the concepts---and their implementations---in this chapter could be useful for your personal archive project. With your partner, discuss how you might extend the code from this chapter to be useful in your group project. Why and how might you do so?

Include a summary of your discussion here.
We will be caching stuff (like metadata and file locations) but not in exactly the same way that Wilson is. The concepts are helpful
but not directly applicable. There's easier ways to deal with cached things than in python directly (sometimes).

### Exercise 3: SDX section 10.6

Write a short summary of what you did (which exercises) below.

exercise 1: we replaced the time variable with a global sequence variable that increments. It doesn't need to be a parameter, and
names the manifest files by their number in the sequences instead of the time they were created.

exercise 2a: We implemented stuff with json and csv saving. We use the manifest (output from backup), which is a dict and easy
to translate to CSV or JSON :).

exercise 2b: make migrate.py. converted by opening the csv, saving everything to a local variable, then opening the json file
and putting everything back.