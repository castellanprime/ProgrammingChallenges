#!/usr/bin/env python
"""
ACM Minesweeper
PC/UVa IDs: 110102/10189

"""

def minesweeper(path_to_file):
    """ Play the minesweeper game

        Args:
            path_to_file:file path
        Returns:
            Nothing
        Raises:
            IOError: if it cannot open file
    """ 

    gameboard = []

    assert(type(path_to_file) is str), "I need a string!"
    assert(path_to_file), "I need a non-empty string!"

    try:
        with open(path_to_file) as f:
            line = f.readline().rstrip()
            while int(line[0]) is not 0:
                field = []
                field.append(list(str((int(line[2]) + 2) * "0" )))
                for i in range(int(line[0])):
                    st = ("0", f.readline().rstrip(), "0")
                    # join takes exactly one argument
                    field.append(list(''.join(st)))
                field.append(list(str((int(line[2]) + 2) * "0" )))                  
                gameboard.append(field)
                line = f.readline().rstrip()
                if line == '':
                    break
    except IOError as e:
        print ("I/O Error({0}) when opening {1}: {2}! I quit!").format(e.errno, path_to_file, e.strerror)
        raise e

    # print gameboard
    for index, item in enumerate(gameboard):
        for i, it in enumerate(item):
            print(item[i])

    # print output
    outputboard = collate_results(gameboard)
    for index, item in enumerate(outputboard):
        print ('{0} {1}{2}'.format('Field','#',index))
        for i in item:
            print(''.join(str(v) for v in i))

def collate_results(gameboard):
    """
        Board algorithm

        Applies rules for the board

        Args:
            gameboard: the input board
        Return:
            outputboard: the output fields
    """
    
    outputboard = []
    for field in gameboard:
        # to copy the entire field, use field[:]
        shape = len(field), len(field[0])
        # the field that would contain the output
        output_field = [[0, ]*(shape[1]) for i in range(shape[0])]
        for row in range(1, shape[0]-1):
            for col in range(1, shape[1]-1):
                if field[row][col] == "*":
                    output_field[row][col]="*"
                    if output_field[row-1][col-1] is not "*":
                        output_field[row-1][col-1] += 1
                    if output_field[row-1][col] is not "*":
                        output_field[row-1][col] += 1
                    if output_field[row-1][col+1] is not "*":
                        output_field[row-1][col+1] += 1
                    if output_field[row][col-1] is not "*":
                        output_field[row][col-1] += 1
                    if output_field[row][col+1] is not "*":
                        output_field[row][col+1] += 1
                    if output_field[row+1][col-1] is not "*":
                        output_field[row+1][col-1] += 1
                    if output_field[row+1][col] is not "*":
                        output_field[row+1][col] += 1
                    if output_field[row+1][col+1] is not "*":
                        output_field[row+1][col+1] += 1         
        # Clean-up
        output_field = output_field[1:-1]
        for index in range(len(output_field)):
            output_field[index] = output_field[index][1:-1]
        outputboard.append(output_field)
    return outputboard  


minesweeper("test")
