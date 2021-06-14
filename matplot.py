import matplotlib.pyplot as plt
from simulator import Simulator
import numpy as np

simp = Simulator(n_Hawk=500, n_Dove=10000)
results = simp.loop(iter=10)




values = results

labels = [f'gen{i+1}' for i, val in enumerate(results)]
Dove = [result[0] for result in results]
Hawk = [result[1] for result in results]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Dove, width, label='Dove')
rects2 = ax.bar(x + width/2, Hawk, width, label='Hawk')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('survive')
ax.set_title('Scores by generation and type')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()