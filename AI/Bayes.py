import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False
print("-----------主观Bayes方法EH公式分段线性差值-----------")
print("请输入LS：")
LS=float(input())
print("请输入LN：")
LN=float(input())
print("请输入P(H)：")
PH=float(input())
print("请输入P(E)：")
PE=float(input())

P1=(LS*PH)/((LS-1)*PH+1)
P0=(LN*PH)/((LN-1)*PH+1)
plt.title('主观Bayes方法EH公式分段线性差值')
plt.xlabel('P(E/S)')
plt.ylabel('P(H/S)')
xline1=[0,PE]
yline1=[P0,PH]
xline2=[PE,1]
yline2=[PH,P1]
plt.plot(xline1,yline1,'b')
plt.plot(xline2,yline2,'r')
plt.xlim(0,1.1)
plt.legend()
plt.axhline(y=PH,ls="--",lw=1)
plt.axvline(x=PE,ls="--",lw=1)
plt.grid(linestyle=":")
plt.show()