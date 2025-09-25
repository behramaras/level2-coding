import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("50_Startups.csv")

states = df.groupby("State").sum()

print(states)

states.plot(kind="bar")
plt.legend(title = "Spend Categories", loc='upper left')
plt.ylabel("Spends Amount")
plt.title("Spends and Profit (Grouped by State)")
plt.show()
