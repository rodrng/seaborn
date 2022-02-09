import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips') # 내장데이터셋 팁 데이터

# print(tips)
x = [0,1,2,3]
labels = ['Thur', 'Fri', 'Sat', 'Sun']

tip_sum = tips.groupby('day').tip.sum()
male_tip = tips[tips['sex']=='Male'].groupby('day').tip.sum()
female_tip = tips[tips['sex']=='Female'].groupby('day').tip.sum()

# plt.bar(x, male_tip, width=0.3, color='blue')
# plt.bar(x+0.3, female_tip, width=0.3, color='red')

# plt.xticks(x, labels)

sns.barplot(x=labels, y=tip_sum, color='red')

plt.show()