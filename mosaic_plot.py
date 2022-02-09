import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

titanic = sns.load_dataset('titanic')

print(titanic.info()) # 타이타닉 데이터의 칼럼명만 출력

titanic = titanic[['survived','pclass','sex']]
titanic['SURVIVE'] = titanic['survived'].map({0:'DEAAD', 1:'ALIVE'})
titanic['CLASS'] = titanic['pclass'].map({1:'1ST', 2:'2ND', 3:'3RD'})
titanic['GENDER'] = titanic['sex'].map({'male':'MAN', 'female':'WOMAN'})
print(titanic)

# mosaic(titanic.sort_values('CLASS'),['SURVIVE','CLASS']) # 객실등급과 생존여부 관계 그래프
mosaic(titanic, ['SURVIVE', 'GENDER'])
plt.show()