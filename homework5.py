#1 The Odd Ones Out
import numpy as np

def onlyOdd(arr):
    odd_rows = arr[np.all(arr % 2 == 1, axis=1)]
    return odd_rows

arr = np.array([[1,2,3], [5,7,9,]])
print(onlyOdd(arr))
#2 Let's play Checkers!
import numpy as np

def checkerboard():
    return np.zeros((8,8), dtype=int)

print(checkerboard())

#2.2
def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    board[::2, ::2] = 1  
    board[::2, 1::2] = 1  

print(checkerboard())

#2.3
def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    board[::2, ::2] = 1  
    board[1::2, 1::2] = 1  
    return board

print(checkerboard())

#2.4
def reverse():
    board = np.zeros((8, 8), dtype=int)
    board[1::2, ::2] = 1  
    board[::2, 1::2] = 1  

print(reverse())

#3 The expanding universe

import numpy as np

def expansion(universe, spaces):

    space_string = ' ' * spaces
    expanded = [space_string.join(list(word)) for word in universe]
    return np.array(expanded)

universe = np.array(['galaxy', 'clusters'])
print(expansion(universe, 1))
print(expansion(universe, 2))

#4 Exoplanets

def secondLargest(planets):
    
    second_largest_values = []
    for col in planets.T:  
        unique_values = np.unique(col)  
        if len(unique_values) < 2:
            second_largest_values.append(None) 
            second_largest_values.append(np.sort(unique_values)[-2])  
    return np.array(second_largest_values)

np.random.seed(42)
planets = np.random.randint(100, 1000, (5, 5))
print(planets)
print(secondLargest(planets))