from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np

marks = np.arange(11)
numbers = [1,1,7,4,8,7,6,7,3,2,3]

fig, ax = plt.subplots()

ax.set_title('Hydroinformatik I 2019 - Notenspiegel')
ax.set_ylabel('Anzahl von Noten')

plt.bar(marks, numbers)
plt.xticks(marks, ('1.0','1.3','1.7','2.0','2.3','2.7','3.0','3.3', '3.7', '4.0', '5.0'))
plt.grid(True)
plt.show()
