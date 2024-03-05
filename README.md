# sp24-lab8
Materials for week 8 lab in CS-370, which includes Ch. 8 "A File Archiver" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_March 5, 2024_

Organization:
* SDX-ch10: The code files for the _SDX Ch. 10_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
Who will start out as
* DRIVER: Terence 
* NAVIGATOR: Marlyn

You will switch halfway through the _SDX Ch. 9_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 10?
- Implementing version control on a small scale and how to test the implementation 

* What questions did you have about the material in the chapters? What did you find confusing?
- Nothing in particular but more so of jjust trying to understand the whole picture. 


### Exercise 1: What familiar design pattern does this chapter employ?

Write your answers to the questions below.

* What design pattern do you think Wilson is using in section 10.4, and why?
- We think the design pattern is Strategy because it is isolating on algoithm and creating a class that implements it which would allow re-use of code and modification without changing other parts of the system. 

* How might you use this pattern to implement other kinds of archive features/properties?
- We could use this strategy in isolating another algorithm that deals with keeping track of the metadata of files instead of the contents. 

### Exercise 2: Applying the ideas in this chapter to your group project
We could use this strategy in isolating different algorithms for example having a seperate algorithm that archives metadata. 

Many of the concepts---and their implementations---in this chapter could be useful for your personal archive project. With your partner, discuss how you might extend the code from this chapter to be useful in your group project. Why and how might you do so?

* We could extend the code to keep track of how audio files change in terms of edits of the actual audio and its metadata. So if someone edits a specific audio they should be able to see the version history of that audio. 

Include a summary of your discussion here.

### Exercise 3: SDX section 10.6

Write a short summary of what you did (which exercises) below.

We did sequencing backups and mock hashes. 
For mock hashes we edited hash_all.py, we allowed hash_all to read the first line of the file so we could add it to our hash. 
