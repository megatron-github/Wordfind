"""
 *****************************************************************************
   FILE:        wordfind.py

   DESCRIPTION: With a given grid of letters, and a list of words. Find all
                the words in the grid, if possible. Report how many word in
                are actually found in the grid. Print all found words in the
                grid in uppercase.

 *****************************************************************************
"""


def printGrid(grid):
    """ Display the grid in a nice way """

    for row in grid:
        print(row)

def confirm_pattern(grid, letters_list, letter_row, letter_col,
                    dr_row, dr_col):
    """ From each location of first letter (starting position), find the
        neigbor letter in given direction (if in a given direction, the
        neigbor is out of bounds, immediately quit). for each neigbor letter
        in the given direction, check if that neigbor letter is the second
        letter in word. If yes, continue and compare third neigbor and so on.
        If not, change direction. """

    patterns = []

    # For each location that is followed the starting location (the location
    # of the first letter in each word), check if that location is still in
    # grid. If yes, then check if the letter in that location is the letter
    # that followed the first letter in word. If yes, check the third letter,
    # and so on. If one of the condition above is wrong, change direction.
    for letter in letters_list:
        if is_in_bounds(grid, letter_row, letter_col) is True:
            if letter is grid[letter_row][letter_col]:
                patterns.append((letter, (letter_row, letter_col)))
        letter_row += dr_row
        letter_col += dr_col
    return patterns

def find_pattern_in(grid, letters_list, start_row, start_col):
    """ For each direction from the first letter (starting position),
        examine if there is a pattern. A pattern exists when all letters
        of a word are located in one direction. """

    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]

    # For each direction, if the letters that are followed the first letter
    # are the letters in word. If not, change direction.
    for dr in directions:
        dr_row = dr[0]
        dr_col = dr[1]
        result = confirm_pattern(grid, letters_list,
                                 start_row, start_col,
                                 dr_row, dr_col)
        if len(letters_list) == len(result):
            return result
    return None

def find_pattern(grid, letters_list, start_location):
    """ For each location of the first letter of the word, try to find
        if one of the directions continues to spelling out the word. """

    # From each starting location (first letter of a word), look at all
    # directions and find a pattern (a pattern is found when all letters
    # in a word is found in a single direction)
    for loc in start_location:
        start_row = loc[0]
        start_col = loc[1]
        patterns = find_pattern_in(grid, letters_list,
                                   start_row, start_col)
        if patterns is not None:
            return patterns
    return None

def is_in_bounds(grid, possible_row, possible_col):
    """ Return True if loc_tuple is a legal position within grid.
        Return False otherwise. """

    # Cite: Denzel Capella, Lucas Barusek and Man Nguyen
    # Description: Denzel and Lucas state that if (row_loc, col_loc) are
    # smaller than zero or bigger than grid_size, then (row_loc, col_loc)
    # is outside of grid. Man states len(grid[0]) will find the number of
    # column of the first row, which is also the number of column of the
    # whole grid.
    if possible_row < 0 or possible_row >= len(grid):
        return False
    if possible_col < 0 or possible_col >= len(grid[0]):
        return False
    return True


def locate_first_letter(grid, letter_list):
    """ Return a list of the locations (tuples) of target within grid. """

    # For each word, use the first letter in the list of letters, and return
    # all locations (in the form of list) that the letter of the word
    # is found in grid.
    letter_location = []
    for letter in letter_list:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] is letter:
                    letter_location.append((i, j))
    return letter_location

def dissect_word(word):
    """ Dissect each word into letters and put them into a list"""

    # Make a new list that will break down each into letters, return
    # the list of letters back to wordfind function.
    letters_list = []
    for letter in word:
        letters_list.append(letter)
    return letters_list

def wordfind(grid, words):
    """ For each word in words, if possible, find it once in the grid, case
        insensitive.  Convert those found letters in the grid
        to upper-case."""

    pattern_loc = []
    total_word = 0
    for word in words:

        # Dissect each word into letters.
        letters_list = dissect_word(word)

        # Find all locations of the first letter.
        start_location = locate_first_letter(grid, letters_list[0])

        # From all the starting location (first letter of the word), look
        # in all directions until found the next letters in the word at the
        # in the same direction.
        patterns = find_pattern(grid, letters_list, start_location)

        # If there is a pattern found from a starting location, a word is
        # found. Print that pattern in uppercase in grid.
        if patterns is not None:
            total_word += 1
            for tple in patterns:
                row_loc = tple[1][0]
                col_loc = tple[1][1]
                pattern_loc.append((row_loc, col_loc))

    # Cite: Denzel Cappella
    # Desc: Explain and show how to change the original grid to a grid that
    #       had the need words in uppercase.
    for tple in pattern_loc:
        row_loc = tple[0]
        col_loc = tple[1]
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

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
