#!/usr/bin/env python3
"""
****************************************************************************************************
    FILE:        wordfind.py

    DESCRIPTION: With a given grid of letters, and a list of words. Find all the words in the grid,
        if possible. Report the number of word found in the grid. Capitalize the letters of the
        found words in the grid.

 ***************************************************************************************************
"""

def printGrid(grid):
    """ Display the grid """

    for row in grid:
        outputStr = ""
        for letter in row:
            outputStr += letter + " "
        print(outputStr)

def confirm_pattern(grid, letters, letter_row, letter_col, dir_row, dir_col):
    """ Given a starting coordinate and a checking direction, check if all the letters all the
        letters of the given word lined up. """

    patterns = []
    for letter in letters:
        if not is_in_bounds(grid, letter_row, letter_col) or \
          letter != grid[letter_row][letter_col]:
            return None
        patterns.append((letter_row, letter_col))
        letter_row += dir_row
        letter_col += dir_col
    return patterns

def find_pattern_with(grid, letters, start_row, start_col):
    """ Given all the directions, check if there exists a direction in which all the letters
        of the given word lined up. """

    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]

    for dir_row, dir_col in directions:
        result = confirm_pattern(grid, letters, start_row, start_col, dir_row, dir_col)
        if result:
            return result
    return None

def find_pattern(grid, letters, starting_coords):
    """ From each coordinate of the starting letter, check if the given word started
        at that coordinate. """

    for start_row, start_col in starting_coords:
        found_pattern = find_pattern_with(grid, letters, start_row, start_col)
        if found_pattern:
            return found_pattern
    return None

def is_in_bounds(grid, row, col):
    """ Return True if loc_tuple is a legal position within grid.
        Return False otherwise. """

    if row < 0 or row >= len(grid):
        return False
    if col < 0 or col >= len(grid[0]):
        return False
    return True

def locate_first_letter(grid, starting_letter):
    """ Return a list of the coordinates (tuples) of the starting letter in the grid. """

    starting_coords = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == starting_letter:
                starting_coords.append((i, j))
    return starting_coords

def dissect_word(word):
    """ Dissect each word into letters and put them into a list"""

    return [letter for letter in word]

def wordfind(grid, words):
    """ For each word in words, find it once in the grid, if possible.
        Capitalize the letters of the found word in the grid."""

    word_locs = []
    total_word = 0
    for word in words:
        # Dissect each word into letters.
        letters = dissect_word(word)
        # Find the coordinates of the first letter.
        starting_coords = locate_first_letter(grid, letters[0])
        # From all the starting location (first letter of the word), look
        # in all directions to check whether all the letters of the word
        # lined up in the same direction.
        found_pattern = find_pattern(grid, letters, starting_coords)
        # If in a direction, all the letters of the word lined up, then
        # a word is found in the grid. Save the coordinates of the letters
        if found_pattern:
            total_word += 1
            word_locs += found_pattern

    # Change the original grid to a grid that had the found words in uppercase.
    for row_loc, col_loc in word_locs:
        grid[row_loc][col_loc] = grid[row_loc][col_loc].upper()

    return total_word

def main():
    """ The main function. """

    myGrid = [['j', 'm', 'w', 'e'],
              ['e', 'e', 'p', 'p'],
              ['q', 'o', 'x', 'u'],
              ['w', 'w', 'e', 'd'],
              ['w', 'g', 'j', 'o']]
    words = ['meow', 'wed', 'do', 'justice']
    count = wordfind(myGrid, words)
    printGrid(myGrid)
    print("Found {} words".format(count))

if __name__ == "__main__":
    main()
