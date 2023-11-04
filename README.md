# Wordfind

## Background

Given a nested list of lowercased letters to represent the word grid and a list of lowercased words, we want to write a program to find all the lowercased words in the word grid, if possible.

## Approach

For each word we find, we will capitlize the letters of that word on the grid. After searching through the entire grid, the program will print the grid and the number of founded words.

A word may lies vertically, horizontally, or diagonally in the word grid. The order of the letters can be forward or backward. Multiple words may overlap one or more letters. Each word may only found once in the grid and the letters must line up in only one direction.

Given the conditions, we may break down the entire program into small helper functions such as:

    1. A function to get the word from the word list
    2. A function to find the starting coordinates of each word
    3. A function to feed the checking directions
    4. Following the each starting coordinates, a function to check whether all the letters of a given word lined up in the given direction
    5. A function to check if current checking position is within the grid

## Sample run
Given a list of words:
```
['meow', 'wed', 'do', 'justice']
```
and a grid of letters:
```
j m w e
e e p p
q o x u
w w e d
w g j o
```
The program will print:
```
j M w e
e E p p
q O x u
w W E D
w g j O
Found 3 words
```

## How to run

To run the program and play Yahtzee
```
python3 wordfind.py
```

## Author

Truong Pham

