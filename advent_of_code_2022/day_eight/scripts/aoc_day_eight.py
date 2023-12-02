import numpy as np
import re

def read_data_extract(n_rows=None, n_cols=None):
    with open("advent_of_code_2022/day_eight/data/aoc_day_eight.txt", "r") as aoc_day_eight_file:
        aoc_day_eight_data = aoc_day_eight_file.readlines()
        aoc_day_eight_data = np.array(
            [eval(height) 
            for tree_heights in aoc_day_eight_data 
            for height in re.split("", tree_heights) if re.match("\d", height)])
        aoc_day_eight_data = aoc_day_eight_data.reshape([n_rows, n_cols])
    return aoc_day_eight_data

tree_matrix = read_data_extract(n_rows=5, n_cols=5)

rows, columns = tree_matrix.shape

visible_tree_positions = np.zeros((rows, columns))

def text_max(row):
    test = 
    for i, value in enumerate(row):
        if (i == 0) or (i == len(row)-1):
            

    #return np.greater(row, np.maximum.accumulate(row))

    #test = np.array([], dtype=bool)
    #for i in row:
    #    np.append(
    #        np.any(np.greater(i, np.maximum.accumulate(row)))
    #    )
    #return test
    #[print(i) for i in row if np.any(i > np.maximum.accumulate(row))]
    #row_max = np.maximum.accumulate(row)
    #return np.greater(row, row_max)

np.apply_along_axis(func1d=text_max, axis=0, arr=tree_matrix)

visible_tree_positions = np.zeros((rows, columns))

for i in range(rows):
    if i == 0 or i == rows - 1:  # Top and bottom of matrix
        visible_tree_positions[i,:] = 1
    for j in range(columns):
        if j == 0 or j == columns - 1:  # Left and right side of matriix
            visible_tree_positions[:,j] = 1
        tree = tree_matrix[i,j]
        #tree_row = tree_matrix[i,:]
        #tree_column = tree_matrix[:,j]
        if i == 0:
            print(tree_matrix[i,j])
            print(tree_matrix[i, j-1])
            print(tree_matrix[i, j+1:])
            print(tree_matrix[i-1, j])
            print(tree_matrix[i+1:, j])
        else:
            break
        if np.any(
            (tree > tree_matrix[i, j-1]) or 
            (tree > tree_matrix[i, j+1:])) or np.any(
            (tree > tree_matrix[i-1, j]) or 
            (tree > tree_matrix[i+1:, j])):
            visible_tree_positions[i,j] = 1

        print(tree)
        print(tree_row)
        print(tree_column)



        #if any((tree > np.maximum.accumulate(tree_row))) or any((tree > np.maximum.accumulate(reversed(tree_row)))):
        #    visible_tree_positions[i,j] = 1
        
        #if np.any(np.greater(tree, tree_row)):
        #    visible_tree_positions[i,j] = 1
        
        #(tree > np.max(tree_row[:j], initial=0)) or (tree > np.max(tree_row[j+1:], initial=0)) or (tree > np.max(tree_column, initial=0)) or (tree > np.max(tree_column[i+1:,], initial=0)):
            #visible_tree_positions[i,j] = 1

def get_previous_value(x):
    for i in x:
        try:
            print(x[i-1,])
        except np.AxisError:
            return 0

t = np.array([0,1,2,3])

np.apply_along_axis(get_previous_value, axis=0, arr=t)
 
