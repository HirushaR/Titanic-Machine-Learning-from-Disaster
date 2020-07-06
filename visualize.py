import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/train.csv')
fig = plt.figure(figsize=(18,6))

plt.subplot2grid((2,3),(0,0))
df.Survived.value_counts(normalize=True).plot(kind='bar',alpha=0.5)
plt.title('Survived')

plt.subplot2grid((2,3),(0,1))
plt.scatter(df.Survived, df.Age, alpha=0.1)
plt.title('Age wrt Survived')
plt.show()