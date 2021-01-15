import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[3,5,7,9]
z=[10,8,6,6,4]
plt.xlabel('X valoo')
plt.ylabel('Y 4')
#plt.axis([0,5,2,11])
plt.plot(x,y,'b-*')
plt.plot(x,z,'r:0')
plt.show()
