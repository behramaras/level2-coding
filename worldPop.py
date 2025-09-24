import matplotlib.pyplot as plt
import pandas as pd

# Read CSV file and drop empty columns
df = pd.read_csv("worldPop.csv")
df.dropna(axis=1, inplace=True)

# Country names and population data
countryNames = list(name.capitalize() for name in df.iloc[:, 0])
populationNumbers = list(df.iloc[:, 1])

# Set figure size
plt.figure(figsize=(8, 8))

# Create pie chart
wedges, texts, autotexts = plt.pie(populationNumbers, autopct="%1.1f%%", startangle=90)

# Make percentage labels white
for autotext in autotexts:
    autotext.set_color("white")

# Add legend    
legend = plt.legend(wedges, countryNames, title="Countries", loc="center right", bbox_to_anchor=(0, 0.5))
legend.get_title().set_color("red")
plt.title("Population of Countries", color="blue")

# Show chart
plt.show()
