#6a
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,8])
y=np.array([3,7])
plt.plot(x,y)
plt.show()

#6b
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,3,1,5]
plt.plot(x,y,'b-o',label='line with markers')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Linear plot with line formating')
plt.legend()
plt.grid(True)
plt.show()
