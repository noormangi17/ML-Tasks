import numpy as np
import matplotlib.pyplot as plt
subjects=["English","Math","Science","Urdu"]
averages=[87,92,82,77]
max_index=np.argmax(averages)
colors=['skyblue']*len(subjects)
colors[max_index]='pink'
plt.bar(subjects,averages,color=colors)
plt.title("BarChart")
plt.legend()
plt.xlabel("Subjects")
plt.ylabel("Average")
plt.show()