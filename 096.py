"""
 A1 A2 A3| A4 A5 A6| A7 A8 A9    4 . . |. . . |8 . 5     4 1 7 |3 6 9 |8 2 5 
 B1 B2 B3| B4 B5 B6| B7 B8 B9    . 3 . |. . . |. . .     6 3 2 |1 5 8 |9 4 7
 C1 C2 C3| C4 C5 C6| C7 C8 C9    . . . |7 . . |. . .     9 5 8 |7 2 4 |3 1 6 
---------+---------+---------    ------+------+------    ------+------+------
 D1 D2 D3| D4 D5 D6| D7 D8 D9    . 2 . |. . . |. 6 .     8 2 5 |4 3 7 |1 6 9 
 E1 E2 E3| E4 E5 E6| E7 E8 E9    . . . |. 8 . |4 . .     7 9 1 |5 8 6 |4 3 2 
 F1 F2 F3| F4 F5 F6| F7 F8 F9    . . . |. 1 . |. . .     3 4 6 |9 1 2 |7 5 8 
---------+---------+---------    ------+------+------    ------+------+------
 G1 G2 G3| G4 G5 G6| G7 G8 G9    . . . |6 . 3 |. 7 .     2 8 9 |6 4 3 |5 7 1 
 H1 H2 H3| H4 H5 H6| H7 H8 H9    5 . . |2 . . |. . .     5 7 3 |2 9 1 |6 8 4 
 I1 I2 I3| I4 I5 I6| I7 I8 I9    1 . 4 |. . . |. . .     1 6 4 |8 7 5 |2 9 3 

 possible_grid = 003020600..... (len => 81)
 
 81 squares, 
 each square have 3 unit    units['A1'] => [A1,A2..A9],[A1,B1..I1],[A1,A2,A3,B1,B2..C3]
 each sqaure have 20 peers  peers['A1'] => set(unit['A1']) - set(['A1']) 
 unit_list just prepare for units

 peter norvig I Freaking Admire you!
"""

def caculate(): 
    strings = file('sudoku.txt').readlines()
    sudokus = ''.join([s[:9] for s in strings if 'Grid' not in s]) 
    return sum([first_3_digit(sudokus[i:i+81]) for i in range(0,4050,81)])

def cross(A,B):
    return [a+b for a in A for b in B]

digits = '123456789'
cols = digits
rows = 'ABCEDFGHI'
squares = cross(rows,cols)    #[A1,A2..(len 81)....I9]
unit_list = ([cross(rows,c) for c in cols] +      #[A1,B1..I1],[A2,B2..I2]..[A9..I9]
             [cross(r,cols) for r in rows] +                #[A1,A2..A9],[B1,B2..B9]..    
             [cross(rs,cs)  for rs in ('ABC', 'DEF', 'GHI') #[A1,A2,A3],[B1,B2,B3]..
                            for cs in ('123','456','789')])
units = dict((s,[u for u in unit_list if s in u]) 
             for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s]))  for s in squares) 

# peers['A1'] = set(['F1', 'C2', 'A7', 'G1', 'I1', 'H1', 'A9', 'A3', 
#                    'A2', 'A5', 'B1', 'B2', 'B3', 'C3', 'A8', 'C1', 
#                    'D1', 'E1', 'A6', 'A4'])
def first_3_digit(grid):
    values =  solve(grid)
    return eval(values['A1']+values['A2']+values['A3'])
 
def solve(grid): return search(parse_grid(grid))

def search(values):
    if values is False:
        return False 
    if all(len(values[s]) == 1 for s in squares): 
        return values 
    ## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) for d in values[s])

def some(seq):
    "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False



def parse_grid(grid):                       # every square can be any digits at start
    values = dict((s,digits) for s in squares)  # {'A1': '123456789', 'A2': '123456789'..
    for s,d in grid_values(grid).items():       # {'A1': '0','A2':'0','A3':'3'..}
        if d in digits and not assign(values, s, d):   # then we assign proper value to it 
            return False
    return values

def grid_values(grid):
    chars = [i for i in grid if i in digits+'.0']
    assert len(chars) == 81
    " {'A1': '0', 'A2': '0', 'A3': '3'.... "
    return dict(zip(squares,chars))

def assign(values,s,d):                     # value =>       {   'A3':'3'  
    other_values = values[s].replace(d,'')  # other_value => {.. 'A3':'12456789'..
    if all(eliminate(values, s, d1) for d1 in other_values):
        return values
    else:
        return False

def eliminate(values,s,d):   # values['A3'] = '3' 
    if d not in values[s]:   # values['A1'] = '123456789' 
        return values
    remainder = values[s] = values[s].replace(d,'')
    if len(remainder) == 0:
        return False
    if len(remainder) == 1:
        d1 = values[s] # now we sure,this square can only assigned d
        if not all(eliminate(values,s1,d1) for s1 in peers[s]):
            return False
    # if it turns out that none of A1,A2, A4 through A9 has a 3 as a possible value, 
    # then the 3 must belong in A3 
    for u in units[s]:  
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        if len(dplaces) == 1:
            if not assign(values,dplaces[0],d):
                return False
    return values

def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print ''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols)
        if r in 'CF': print line
    print

hardest_sudoku_on_earth ='.....6....59.....82....8....45........3........6..3.54...325..6..................'
print caculate()
