#1 How many plots
import numpy as np
import matplotlib.pyplot as plt

def sinusoid(x, A, w):
    return A * np.sin(w * x)

x = np.linspace(0, 2 * np.pi, 1000)

A_vals = np.array([1, 2, 3, 4, 5])  
w_vals = np.array([1, 2, 3, 4, 5])  

plt.figure(figsize=(10, 6))

for A in A_vals:
    for w in w_vals:
        y = sinusoid(x, A, w)  
        plt.plot(x, y, label=f'A={A}, w={w}')  

plt.title("Sinusoidal Waves with Different Amplitudes and Frequencies")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()  
plt.grid(True) 
plt.show()

#2 Randomness

import numpy as np
import matplotlib.pyplot as plt

list1 = np.random.randint(0, 101, size=40) 
list2 = np.random.randint(0, 101, size=40)  

plt.figure(figsize=(10, 6))

plt.plot(list1, color='orange', linewidth=10, label="List 1 (Orange Line)")

plt.plot(list2, color='red', linestyle='--', label="List 2 (Red Dashed Line)")

plt.xlabel("Index")  
plt.ylabel("Value")  
plt.title("Plot of Two Random Data Lists")  
plt.legend()  

plt.grid(True)  
plt.show()








