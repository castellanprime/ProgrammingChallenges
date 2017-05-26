"""
    Question:

    Determine if a Sudoku is valid: according to https://sudoku.com/au/TheRules.aspx

    The Sudoku board could be partially filled, where empty cells are filled with the character '.'

    [ 5 ][ 3 ][   ]#[   ][ 7 ][   ]#[   ][   ][   ]
    [ 6 ][   ][   ]#[ 1 ][ 9 ][ 5 ]#[   ][   ][   ]
    [   ][ 9 ][ 8 ]#[   ][   ][   ]#[   ][ 6 ][   ]
    ============================================== 
    [ 8 ][   ][   ]#[   ][ 6 ][   ]#[   ][   ][ 3 ]
    [ 4 ][   ][   ]#[ 8 ][   ][ 3 ]#[   ][   ][ 1 ]
    [ 7 ][   ][   ]#[   ][ 2 ][   ]#[   ][   ][ 6 ]
    ==============================================
    [   ][ 6 ][   ]#[   ][   ][   ]#[ 2 ][ 8 ][   ]
    [   ][   ][   ]#[ 4 ][ 1 ][ 9 ]#[   ][   ][ 5 ]
    [   ][   ][   ]#[   ][ 8 ][   ]#[   ][ 7 ][ 9 ]

    * A partially filled Sudoku which is valid


    First Solution(Solution1)

    Naive solution:

    Wrong:
 
    Because you are scanning the row more than once for every possible element


    Second Solution(Solution2)

    Naive Solution:

    Correct:

    It is somewhat linear

"""


# Wrong solution
class Solution1(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # Solution:
        # We need to search every number in the horizontal and vertical directions at the same time
        # We also need to search for that number in the 3 by 3 grid
        
        # We record the first sightings of each number in a list
        first_sightings = [False for i in range(0, 10)]
        
        col , row = 0, 0
        for num in range(1, 10):
            for column_index in range(0, len(board[0])):
                if board[row][column_index] == '.':
                    continue
                else:
                    if board[row][column_index] == num and first_sightings[num] is False:
                        first_sightings[num] = True
                    if board[row][column_index] == num and first_sightings[num]:
                        return False
            for row_index in range(0, len(board)):
                if board[row_index][col] == '.':
                    continue
                else:
                    if board[row_index][col] == num and first_sightings[num] is False:
                        first_sightings[num] = True
                    if board[row_index][col] == num and first_sightings[num]:
                        return False
            row += 1
            col += 1
            
        # We search for the number in the 3 by 3 grid
        first_sightings[:] = [False for i in range(0, 10)]
        for row_in in range(0, len(board), 3):
            for column in range(0, len(board[0]), 3):
                for num in range(1, 10):
                    for row_index in range(0, 3):
                        for column_index in range(0, 3):
                            if board[row_index][column_index] == '.':
                                continue
                            else:
                                if board[row_index][column_index] == num and first_sightings[num] is False:
                                    first_sightings[num] = True
                                if board[row_index][column_index] == num and first_sightings[num]:
                                    return False


class Solution2(object):
    @staticmethod
    def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # Solution:

        # We record the first sightings of each number in a list
        first_sightings = [False for i in range(0, 10)]

        # We look at rows:
        # We mark off occurences of a number if we have not found it already
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                num = board[row][col]
                if num != '.':
                    if first_sightings[int(num)] is False:
                        first_sightings[int(num)] = True
                    else:
                        return False
            first_sightings[:] = [False for i in range(0, 10)]

        first_sightings = [False for i in range(0, 10)]   

        # We look at columns:
        # We mark off occurences of a number if we have not found it already
        for col in range(0, len(board[0])):
            for row in range(0, len(board)):
                num = board[row][col]
                if num != '.':
                    if first_sightings[int(num)] is False:
                        first_sightings[int(num)] = True
                    else:
                        return False
            first_sightings[:] = [False for i in range(0, 10)]

        first_sightings = [False for i in range(0, 10)]

        # We look at 3 by 3 grids:
        # We mark off occurences of a number if we have not found it already
        for i_row in range(0, len(board), 3):
            row_end = i_row + 3
            for i_col in range(0, len(board[0]), 3):
                col_end = i_col + 3
                for row in range(i_row, row_end):
                    for col in range(i_col, col_end):
                        num = board[row][col]
                        if num != '.':
                            if first_sightings[int(num)] is False:
                                first_sightings[int(num)] = True
                                print(first_sightings)
                            else:
                                return False
                first_sightings[:] = [False for i in range(0, 10)]

        return True


def main():
    import sys, os
    try:
        board = [[".", ".", ".", ".", ".", ".", ".", ".", "."] for i in range(0, 9)]
        num_of_testcases = int(sys.stdin.readline().rstrip())
        for num in range(0, num_of_testcases):
            char_row = sys.stdin.readline().rstrip()
            row, col = 0, 0
            #print("Board length: ", len(board))
            while row < len(board)-1:
                if char_row:
                    for index, char in enumerate(char_row):
                        board[row][col] = char
                        col += 1
                    row += 1
                    #rint("Row: ", row)
                    col = 0
                char_row = sys.stdin.readline().rstrip()
            print(Solution2.isValidSudoku(board))
    except KeyboardInterrupt as e:
        print("Closing")

main()