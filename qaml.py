#pip install matplotlib
#pip install numpy
import matplotlib.pyplt as plt
import numpy as np
import random

RowData=[]
#測試資料

N=
#資料數量

rK=0.5
rI=10
#學習率

I=
#輸入層節點數

K=
#輸出層節點數

J=(I+K)/2
#隱藏層節點數

InputLayer=
#初始話輸入資料
OutputLayer=
#初始話輸出資料


#初始化權重(矩陣)

wH=
#正向傳播左邊
wY=
#正向傳播右邊
tH=
#反向傳播左邊的bias
tY=
#反向傳播右邊的bias

e=[]#錯誤率

for i in range(1:9999):#訓練次數9999次
	n= random.randrange(0, N+1, 1)#選擇資料組第n個
	x=InputLayer()#第n資料組input部分
	t=OutputLayer()#第n資料組output部分
	
	#前向傳播階段
	#輸入到隱藏
	h=sigmoid(wH*x-tY)
	
	#隱藏到輸出
	y=sigmoid(wY*h-tY)
	
	#反向傳播階段
	#輸出到隱藏，學習率為rY
	dY=rY*(y-t)*y*(1-y)
	tY=tY-dY*(-1)
	wY=wY-dY*transpose(h)#轉置h矩陣
	
	#隱藏到輸入，學習率為rY*rH，rY來自dY
	dH=rH* transpose(wY) * dY* h* (1 - h)
	tH =tY- dH * (-1)
	wH -= dH * transpose(x)
	
	# 全部資料組對於這次訓練完的模型的參數的錯誤率
	
	e.append(np.sum(((sigmoid(wY * sigmoid(wH * InputLayer - tH) - tY) - OutputLayer)**2)**0.5))
	


plt.plot(e)
print(e[m])#顯示最後錯誤率
"""訓練結束"""


#測試




#測試結束
def sigmoid(x):
	y=(1+exp(-x))**1
	return y

