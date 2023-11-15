import matplotlib.pyplot as plot
import numpy as np
digital_call_K=float(input())
digital_call_payoff=float(input())
call_option_K=float(input())
plot.figure(figsize=(4,3),dpi=200) #figzie spcifies the ratio between length and width; dpi is the size of the image
x1=np.linspace(digital_call_K,digital_call_K*1.1)
y1=np.power(x1,0)-1+digital_call_payoff
x2=np.linspace(digital_call_K*0.9,digital_call_K)
y2=np.power(x2,0)-1
plot.plot(x1,y1,label='Payoff of digital call option',color="black",linewidth='1',linestyle='-') #plot the graph
plot.plot(x2,y2,color="black",linewidth='1',linestyle='-')
plot.plot([call_option_K,digital_call_K],[0,digital_call_payoff],label="Payoff of bull call spread",color="orange",linewidth='1',linestyle='--')
plot.title("Payoff Chart",fontdict={'fontsize':10})
plot.xlabel("Stock price")
plot.ylabel("Payoff")
plot.legend(loc="upper left",fontsize=4)
plot.show()