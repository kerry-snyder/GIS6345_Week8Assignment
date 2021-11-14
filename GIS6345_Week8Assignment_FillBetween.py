import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2, 5, 0.01)
y1 = -2*x*x + x + 10
y2 = 7*x*x + x

fig, ax = plt.subplots()
ax.plot(x, y1, x, y2, color='purple')
ax.fill_between(x, y1, y2, where=(y2 > y1), facecolor='green', alpha=0.5)
ax.fill_between(x, y1, y2, where=(y2 <= y1), facecolor='yellow', alpha=0.5)
ax.set_title('Fill Between_KSnyder')
ax.set_ylabel('y')
ax.set_xlabel('x')

plt.show()





