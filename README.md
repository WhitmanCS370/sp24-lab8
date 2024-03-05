# sp24-lab8
Materials for week 8 lab in CS-370, which includes Ch. 8 "A File Archiver" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_March 5, 2024_

Organization:
* SDX-ch10: The code files for the _SDX Ch. 10_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
Who will start out as
* DRIVER: Oliver Baltzer
* NAVIGATOR: Clara Bates

You will switch halfway through the _SDX Ch. 9_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 10?

The main idea of the chapter was using mock objects tot test a version control software. 
The version control was implemented using a manifest which contains hash values for files.

* What questions did you have about the material in the chapters? What did you find confusing?

What the hash function does?
How backups are stored in the version control.

### Exercise 1: What familiar design pattern does this chapter employ?

Write your answers to the questions below.

* What design pattern do you think Wilson is using in section 10.4, and why?
  The strategy design pattern, because it can offload the handling of the file to another separate algorithm or class
* How might you use this pattern to implement other kinds of archive features/properties?
  We think that we could use the strategy design pattern to interchange the file analysis for other types of analysis whether that be different types of analysis of types of file.
### Exercise 2: Applying the ideas in this chapter to your group project

Many of the concepts---and their implementations---in this chapter could be useful for your personal archive project. With your partner, discuss how you might extend the code from this chapter to be useful in your group project. Why and how might you do so?
    If the project has any editing features it would be nice to have a version control to rollback changes. It would do this by saving backups of the files. The mock objects tool would be super useful for testing a file manager. 
Include a summary of your discussion here.

### Exercise 3: SDX section 10.6

Write a short summary of what you did (which exercises) below.

We completed the first 2 parts of JSON Manifests and discussed how we would implement the third part.