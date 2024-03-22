#5a
import matplotlib.pyplot as plt
import numpy as np
a = np.array([12,23,33,44,45,56,78,89,92,100])
fig, ax = plt.subplots(figsize = (8,5))
ax.hist(a, bins = [10,25,50,75,100],color='skyblue',edgecolor='black')
plt.show()

#5b
import matplotlib.pyplot as plt
import numpy as np
cars = ['AUDI', 'LAND ROVER', 'FORD', 'PORSCHE', 'MERCEDES']
data = [45, 55, 62, 10, 33]
plt.pie(data, labels = cars)
plt.show()
