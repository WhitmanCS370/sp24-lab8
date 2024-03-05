# sp24-lab8
Materials for week 8 lab in CS-370, which includes Ch. 8 "A File Archiver" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_March 5, 2024_

Organization:
* SDX-ch10: The code files for the _SDX Ch. 10_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
Who will start out as
* DRIVER: Shahrom Dehoti
* NAVIGATOR: Gabe Paris-Moe

You will switch halfway through the _SDX Ch. 9_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 10?
* Version control uses hashing to uniquely identify each saved file. Testing is done using mock file system because it is faster and saver. Then, we use base class to specify what a component must be able to do and deerive child classes to implement those operations. 
* What questions did you have about the material in the chapters? What did you find confusing?
* We are a bit confused on what race conditions exactly are and how they affect the files.


### Exercise 1: What familiar design pattern does this chapter employ?

Write your answers to the questions below.

* What design pattern do you think Wilson is using in section 10.4, and why?
* We believe that Wilson is using a Template Method design pattern because the skeleton of the algorithm is defined in the superclass but subclasses are allowed to override specific steps of the algorithm without changing its structure.
* How might you use this pattern to implement other kinds of archive features/properties?
* We will need to be able to deal with different file types which all have specififc methods with which you can deal with them. So we can use the Template Method design pattern to structure our code so we can override on our superclasses to deal with these cases.

### Exercise 2: Applying the ideas in this chapter to your group project

Many of the concepts---and their implementations---in this chapter could be useful for your personal archive project. With your partner, discuss how you might extend the code from this chapter to be useful in your group project. Why and how might you do so?

Shahrom's team needs to refactor their code and Shahrom thinks it will be a good idea to use Template Method design pattern as a structure for the refactored code. It will make it easier to add functionalities in the future.

Gabe's focus will be in tracking backups. He believes that his team would need to add and delete a lot of files that they work with so he wants to have an ability to trace his backups and past versions of the files.

Include a summary of your discussion here.

### Exercise 3: SDX section 10.6

Write a short summary of what you did (which exercises) below.