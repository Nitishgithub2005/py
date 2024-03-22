#4a
import matplotlib.pyplot as plt
categories=['0-10','10-20','20-30','30-40','40-50',]
values=[55,48,25,68,90]
plt.bar(categories,values,color='skyblue')
plt.xlabel('overs')
plt.ylabel('runs')
plt.title('Overs vs runs')
plt.show()

#4b
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10]
y = [90, 80, 20, 40 , 50, 69, 30, 10, 99, 75]
plt.scatter(x, y, color = "black")
plt.show()
