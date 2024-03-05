# sp24-lab8
Materials for week 8 lab in CS-370, which includes Ch. 8 "A File Archiver" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_March 5, 2024_

Organization:
* SDX-ch10: The code files for the _SDX Ch. 10_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
Who will start out as
* DRIVER: Sam
* NAVIGATOR: Zurain, Aidan

You will switch halfway through the _SDX Ch. 9_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 10?
Creating a custom version control system using a hashmap and a mock filesystem
* What questions did you have about the material in the chapters? What did you find confusing?
We're a little confused on the implementation, file locking. I didnt know what different functions were suppose to return as far as pre and post conditions go


### Exercise 1: What familiar design pattern does this chapter employ?

Write your answers to the questions below.

* What design pattern do you think Wilson is using in section 10.4, and why?
Extract class and turning the code more object oriented, delegating tasks to methods as part of the archive class
* How might you use this pattern to implement other kinds of archive features/properties?
Having classes that good load distribution -- classes aren't too large. Proper inheritance and distribution of classes

### Exercise 2: Applying the ideas in this chapter to your group project

Many of the concepts---and their implementations---in this chapter could be useful for your personal archive project. With your partner, discuss how you might extend the code from this chapter to be useful in your group project. Why and how might you do so?

Include a summary of your discussion here.
Everyone agrees that our projects need major refactoring, including better naming conventions, documantation. Certain functionalities could be extracted into more classes and methods. Our projects could implement the strategy pattern with different kinds of audio effects and filters. 

### Exercise 3: SDX section 10.6

Write a short summary of what you did (which exercises) below.
We did the JSON manifest exercise and implemented a rudimentary template for a flag condition
