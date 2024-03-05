# sp24-lab8
Materials for week 8 lab in CS-370, which includes Ch. 8 "A File Archiver" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_March 5, 2024_

Organization:
* SDX-ch10: The code files for the _SDX Ch. 10_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Steven Lin
Aiden von Buchwaldt

## Team Roles for Part 1
Who will start out as
* DRIVER: Steven Lin
* NAVIGATOR: Aiden von Buchwaldt

You will switch halfway through the _SDX Ch. 9_ activity.

## Part 1 Documentation
## Already completed with other group before reforming group
Write your answers to the questions below.

* What were the main ideas from SDX chapter 10?
* What questions did you have about the material in the chapters? What did you find confusing?


### Exercise 1: What familiar design pattern does this chapter employ?

Write your answers to the questions below.

* What design pattern do you think Wilson is using in section 10.4, and why?
* How might you use this pattern to implement other kinds of archive features/properties?

### Exercise 2: Applying the ideas in this chapter to your group project

Many of the concepts---and their implementations---in this chapter could be useful for your personal archive project. With your partner, discuss how you might extend the code from this chapter to be useful in your group project. Why and how might you do so?

Include a summary of your discussion here.

### Exercise 3: SDX section 10.6

Write a short summary of what you did (which exercises) below.

Did Sequencing backups; Wrote filename() to check for existing manifest files and return the next number. Modified backup() and write_manifest() to use this instead of current_time()

Did json filename; Modified backup() and write_manifest() to use either csv or json based on input. Modified fileName() to also check for json