# Wordfind
A program that solve word search puzzles

The program takes two parameters: a grid of lower-case single-letter strings, and a list of lower-case words. For each word, find it in the grid, if possible. If found, then for each letter comprising the word in the grid, change the letter to its capitalized version. wordfind returns the number of words that were found. Words can occur in any of the 8 directions. They can also overlap in one or more letters. A word will only occur once in the puzzle. 

For example, if we begin with a grid:

j m w e
e e p p
q o x u
w w e d
w g j o

and a list of words ['meow', 'wed', 'do', 'justice'], the wordfind function modifies the grid:

j M w e
e E p p
q O x u
w W E D
w g j O

and returns 3.
