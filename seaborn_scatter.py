import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

# sns.regplot(x='petal_length', y='petal_width', data=iris) # 추세선 까지 출력됨
# sns.scatterplot(x='petal_length', y='petal_width', data=iris,
# hue='species', style='species', s=100)

sns.pairplot(iris, diag_kind='kde', hue='species')
plt.show()