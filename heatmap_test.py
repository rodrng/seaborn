import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('flights')

# print(data)

data = data.pivot('month','year','passengers')
# print(data)

# plt.pcolor(data)

sns.heatmap(data, cmap="RdYlGn_r", annot=True, fmt='d')
plt.show()
