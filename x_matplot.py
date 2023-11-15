import matplotlib.pyplot as plot
import numpy as np
import pandas as pd

#Line Chart
plot.figure(figsize=(5,3),dpi=200) #figzie spcifies the ratio between length and width; dpi is the size of the image
plot.plot([1,2,3,4],[2,4,6,8],label='2x',color="black",linewidth='2',marker='.',markersize='10',linestyle='-') #plot the graph
plot.title("My First Graph",fontdict={'fontsize':20})
plot.xlabel("X-AXIS")
plot.ylabel("Y-AXIS")
plot.xticks(list(range(1,5))) #range of x-axis
plot.yticks(list(range(2,9,2))) #range of y-axis
plot.legend() #show the label of the plot 2x
plot.show() #show the graph; if we don't this function to show the graph and use plot function multiple times, then multiple graphs will be shown together

plot.figure(figsize=(5,3),dpi=200)
x=np.arange(0,10.5,0.5)
plot.plot(x[:11],x[:11]**2,label='x^2')
plot.plot(x[10:],x[10:]**2,label='x^2',linestyle='--')
plot.legend()
#plot.savefig("my graph",dpi=200) #save the picture to the current directory
plot.show()

#Bar chart
'''
labels=['A','B','C']
values=[3,5,4]
plot.figure(figsize=(5,3),dpi=200)
plot.title("My Second Graph",fontdict={'fontsize':20})
plot.xlabel("Category")
plot.ylabel("Number")
plot.bar(labels,values)
plot.show()
'''
#scatter plot
data1=list(range(10))
data2=list(range(10,20))
plot.scatter(data1,data2,color="black")
plot.show()


