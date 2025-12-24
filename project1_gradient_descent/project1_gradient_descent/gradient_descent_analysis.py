import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return x**2 - 4*x + 5

x = np.linspace(-1, 5, 100)
y = f(x)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function Visualization")
plt.show()
