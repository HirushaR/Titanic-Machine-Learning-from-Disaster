import pandas as pd
import matplotlib.pyplot as plt

female_color = "#FA0000"

df = pd.read_csv('data/train.csv')
fig = plt.figure(figsize=(18,6))

plt.subplot2grid((3,4),(0,0))
df.Survived.value_counts(normalize=True).plot(kind='bar',alpha=0.5)
plt.title('Survived')

plt.subplot2grid((3,4),(0,1))
df.Survived[df.Sex == "male"].value_counts(normalize=True).plot(kind='bar',alpha=0.5)
plt.title('men Survived')

plt.subplot2grid((3,4),(0,2))
df.Survived[df.Sex == "female"].value_counts(normalize=True).plot(kind='bar',alpha=0.5, color=female_color)
plt.title('Women Survived')

plt.subplot2grid((3,4),(0,3))
df.Sex[df.Survived == 1].value_counts(normalize=True).plot(kind='bar',alpha=0.5, color=female_color)
plt.title('Sex of Survived')

plt.show()