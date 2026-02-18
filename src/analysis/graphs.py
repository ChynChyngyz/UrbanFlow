import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("D:/Users/Admin/PycharmProjects/UrbanFlow/data/logs/intersection_244500423.csv")

pivot = df.pivot(index="time", columns="dir", values="queue")

pivot.plot()
plt.ylabel("Queue length")
plt.title("Queues over time")
plt.show()
