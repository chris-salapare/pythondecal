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
