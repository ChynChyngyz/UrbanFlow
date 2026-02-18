import pandas as pd

df = pd.read_csv("D:/Users/Admin/PycharmProjects/UrbanFlow/data/logs/intersection_244500423.csv")

# средняя очередь по направлениям
print(df.groupby("dir")["queue"].mean())

# максимальная очередь
print(df.groupby("dir")["queue"].max())

# общее среднее
print("Overall:", df["queue"].mean())
