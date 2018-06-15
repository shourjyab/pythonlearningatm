grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]
for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end='')
    print()

#not using the end part produces output in a column form
    #se we add end but by adding end all of it comes in one line
    #so after adding end to break the lines up to look like output
    #we call another print function
               
