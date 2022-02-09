import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris') # seaborn 내장 데이터 iris 불러오기
# print(iris) # iris 라는 데이터셋을 불러옴
# print(iris.describe()) # 전체 데이터셋에 통계값을 보여줌

# #히스토그램 그리기
# fig, ax = plt.subplots(2,2)
#
# plt.subplot(2,2,1)
# plt.hist(iris['sepal_length'], bins=10, color='blue')
# plt.subplot(2,2,2)
# plt.hist(iris['sepal_width'], bins=10, color='red')
# plt.subplot(2,2,3)
# plt.hist(iris['petal_length'], bins=10, color='green')
# plt.subplot(2,2,4)
# plt.hist(iris['petal_width'], bins=10, color='yellow')
# plt.show()

# sns.histplot(iris['sepal_length'])
# sns.distplot(iris['sepal_width'])
# plt.show()

sns.distplot(iris[iris['species'] == 'setosa']['petal_length'], label='setosa', color='red')
sns.distplot(iris[iris['species'] == 'versicolor']['petal_length'], label='versicolor', color='blue')
sns.distplot(iris[iris['species'] == 'virginica']['petal_length'], label='virginica', color='yellow')
plt.legend()
plt.show()