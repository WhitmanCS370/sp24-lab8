# sp24-lab8
Materials for week 8 lab in CS-370, which includes Ch. 8 "A File Archiver" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_March 5, 2024_

Organization:
* SDX-ch10: The code files for the _SDX Ch. 10_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Jacob, Jas

## Team Roles for Part 1
Who will start out as
* DRIVER: Jacob 
* NAVIGATOR: Jas

You will switch halfway through the _SDX Ch. 9_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 10?
Creating a file archiver and saving files. Making sure there are backups for the files using hash maps. Utilizes mock objects once again for testing. 

* What questions did you have about the material in the chapters? What did you find confusing?
We understand what is happening but the how is confusing. 

### Exercise 1: What familiar design pattern does this chapter employ?

Write your answers to the questions below.

* What design pattern do you think Wilson is using in section 10.4, and why?
We think Wilson uses strategy pattern because he utilizes child classes and resuses function code to create interchangeable objects. 

* How might you use this pattern to implement other kinds of archive features/properties?
We can make more child and parent classes to extend the code. We can also resuse function code to create new objects that interact with files in new ways. 

### Exercise 2: Applying the ideas in this chapter to your group project

Many of the concepts---and their implementations---in this chapter could be useful for your personal archive project. With your partner, discuss how you might extend the code from this chapter to be useful in your group project. Why and how might you do so?

Include a summary of your discussion here.
Saving new files and backing up copies of files is going to be really important during Epoch 2. Especially when it comes to editing sound files. 

### Exercise 3: SDX section 10.6

Write a short summary of what you did (which exercises) below.
We attempted exercise one and created a solution that would use the length of the backup directory to keep track of the number of manifests. We had no idea how to test this and spent the rest of lab attempting so.