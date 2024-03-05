# sp24-lab8
Materials for week 8 lab in CS-370, which includes Ch. 8 "A File Archiver" adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_March 5, 2024_

Organization:
* SDX-ch10: The code files for the _SDX Ch. 10_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Luke, Neel

## Team Roles for Part 1
Who will start out as
* DRIVER: Luke
* NAVIGATOR: Neel

You will switch halfway through the _SDX Ch. 10_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 10?
    Version Control/tracking backups can be achieved by hashing a repository's contents every time they are saved, and then checking which files have changed to minimize storage. If a file's content's hash is the same as it was in a previous version, there is no reason to save backups of both.
* What questions did you have about the material in the chapters? What did you find confusing?
    It seems like SDX dude reverse hashes the contents to get the file contents, but that's not possible, so the old versions must be stored somewhere. Where?


### Exercise 1: What familiar design pattern does this chapter employ?

Write your answers to the questions below.

* What design pattern do you think Wilson is using in section 10.4, and why?
    Wilson uses inheritence when he makes the archivelocal class

* How might you use this pattern to implement other kinds of archive features/properties?
    We could turn this into a strategy pattern when making other kinds of archives.

### Exercise 2: Applying the ideas in this chapter to your group project

Many of the concepts---and their implementations---in this chapter could be useful for your personal archive project. With your partner, discuss how you might extend the code from this chapter to be useful in your group project. Why and how might you do so? Include a summary of your discussion here.

    We could use the principles described here (like hashing) to (semi)efficiently make sure we don't have duplicate files in the archive. Also, if the target audience of your archive was a musician (or someone else who edits sounds often), they would care about version control for their files.

### Exercise 3: SDX section 10.6

Write a short summary of what you did (which exercises) below.

    Sequencing Backups: This wouldn't solve the problem of race conditions because if two different requests were made to pull the current "time"step before it got updated, the files would have the same name and save over each other. To solve this, the timestep field would need to be locked before the operations started.

    JSON manifests: We were successful in making manifest.py correctly turn a directory of CSVs into a directory of JSONs. however, the instructions were very unclear on what to do with saving the user name, and how the old data (no user name saving) should be ported over. Is the user doing the migration now the "owner" of those files? should we leave it blank? We went with the latter but it's ambiguous.