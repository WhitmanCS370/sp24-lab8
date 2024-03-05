# sp24-lab8
Materials for week 8 lab in CS-370, which includes Ch. 8 "A File Archiver" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_March 5, 2024_

Organization:
* SDX-ch10: The code files for the _SDX Ch. 10_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Andrew Tate, John Leeds

## Team Roles for Part 1
Who will start out as
* DRIVER: John Leeds
* NAVIGATOR: Andrew Tate

You will switch halfway through the _SDX Ch. 9_ activity.


## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 10?
    * How to use a mock file system to employ testing without touching a real file system
    * Identifying files with a hash
    * Data races :(
    * Version control tries to store patches
* What questions did you have about the material in the chapters? What did you find confusing?
    * Data races :(
    * When would we encounter a data race if operations are handled serially?
    * The diagram at the bottom is confusing


### Exercise 1: What familiar design pattern does this chapter employ?

Write your answers to the questions below.

* What design pattern do you think Wilson is using in section 10.4, and why?
    * This is the **Strategy Pattern**.  Wilson creates an interface for an `Archive`, and then each child class represents an archiving strategy.
* How might you use this pattern to implement other kinds of archive features/properties?
    * You could have a strategy to store deltas between commits 
    * You could use different hashing strategies
    * You could have a general class to access a file but treats hidden and system files differently

### Exercise 2: Applying the ideas in this chapter to your group project

Many of the concepts---and their implementations---in this chapter could be useful for your personal archive project. With your partner, discuss how you might extend the code from this chapter to be useful in your group project. Why and how might you do so?

Include a summary of your discussion here.

* We used a similar pattern to implement our `Storage` because we wanted to allow different ways of interacting with our database and cache.
* We could use a sound modification strategy where each sound modification class implements its respective modify sound function.

### Exercise 3: SDX section 10.6

Write a short summary of what you did (which exercises) below.

* We began by trying to install Python 3.10 on the lab computers but obviously we don't have permission
* Then, we tried to run this on Andrew Tate's Windows computer but some tests required a unix specific command
* We finally got the program to run
* Then, we completed Sequencing Backups and created JSON Manifests.  We also created a migration function which you can call with python3 backup.py migrate_stuff backup_dir
