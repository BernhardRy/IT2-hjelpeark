import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (4 * x**3) - (x**5)

xverdier = np.linspace(-2, 2, 50)
yverdier = f(xverdier)

# xverdier = [xverdi for xverdi in range(-2, 3)]
# yverdier = [f(xverdi) for xverdi in xverdier]

plt.plot(xverdier, yverdier)
plt.show()