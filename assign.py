# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Rename columns for easier reference
df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# Map species indices to their names
species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
df['species'] = df['species'].map(species_map)

# Set the style for the plots
sns.set(style="whitegrid")

# --------------------------
# Visualization 1: Violin Plot
# --------------------------
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='species', y='sepal_length', palette="muted")
plt.title("Violin Plot of Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.show()

# --------------------------
# Visualization 2: Box-and-Whisker Plot
# --------------------------
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='species', y='sepal_length', palette="pastel")
plt.title("Box-and-Whisker Plot of Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.show()

# --------------------------
# Visualization 3: Bar Plot with Error Bars
# --------------------------
species_groups = df.groupby('species')['sepal_length']
means = species_groups.mean()
std_devs = species_groups.std()

plt.figure(figsize=(10, 6))
plt.bar(means.index, means, yerr=std_devs, capsize=5, color=['lightblue', 'lightgreen', 'salmon'])
plt.title("Mean Sepal Length with Error Bars (Std Dev)")
plt.ylabel("Mean Sepal Length (cm)")
plt.xlabel("Species")
plt.show()

# --------------------------
# Visualization 4: Strip Plot
# --------------------------
plt.figure(figsize=(10, 6))
sns.stripplot(data=df, x='species', y='sepal_length', jitter=True, palette="viridis", size=6)
plt.title("Strip Plot of Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.show()

# --------------------------
# Visualization 5: Swarm Plot
# --------------------------
plt.figure(figsize=(10, 6))
sns.swarmplot(data=df, x='species', y='sepal_length', palette="coolwarm", size=6)
plt.title("Swarm Plot of Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
plt.show()

# --------------------------
# Visualization 6: KDE Plot (Density Plot)
# --------------------------
plt.figure(figsize=(10, 6))
for species in df['species'].unique():
    sns.kdeplot(df[df['species'] == species]['sepal_length'], label=species, fill=True)
plt.title("KDE Plot of Sepal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Density")
plt.legend(title="Species")
plt.show()

# --------------------------
# Visualization 7: Pair Plot
# --------------------------
sns.pairplot(df, hue='species', diag_kind='kde', palette="husl")
plt.suptitle("Pair Plot of Iris Dataset", y=1.02)
plt.show()
