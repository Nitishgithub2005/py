#7
import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
sns.set(style='whitegrid')
sns.scatterplot(x="total_bill",y="tip",data=tips,hue="sex",size="size",palette="Set1",sizes=(20,200))
plt.xlabel("Total bills")
plt.ylabel("Tips")
plt.title("Total bills vs tips")
plt.legend(title='gender')
plt.legend(loc='upper right')
plt.show()
