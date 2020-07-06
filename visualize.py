import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/train.csv')
fig = plt.figure(figsize=(18,6))

df.Survived.value_counts().plot(kind='bar',alpha=0.5)

plt.show()