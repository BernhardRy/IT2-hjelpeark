import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6]
y = []

for tall in x:
    y.append(3*tall+2)

plt.plot(x, y) # opretter et plott
plt.show()