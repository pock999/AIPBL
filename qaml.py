#pip install matplotlib
#pip install numpy
import matplotlib.pyplt as plt
import numpy as np
import random

RowData=[]
#���ո��

N=
#��Ƽƶq

rK=0.5
rI=10
#�ǲ߲v

I=
#��J�h�`�I��

K=
#��X�h�`�I��

J=(I+K)/2
#���üh�`�I��

InputLayer=
#��l�ܿ�J���
OutputLayer=
#��l�ܿ�X���


#��l���v��(�x�})

wH=
#���V�Ǽ�����
wY=
#���V�Ǽ��k��
tH=
#�ϦV�Ǽ����䪺bias
tY=
#�ϦV�Ǽ��k�䪺bias

e=[]#���~�v

for i in range(1:9999):#�V�m����9999��
	n= random.randrange(0, N+1, 1)#��ܸ�Ʋղ�n��
	x=InputLayer()#��n��Ʋ�input����
	t=OutputLayer()#��n��Ʋ�output����
	
	#�e�V�Ǽ����q
	#��J������
	h=sigmoid(wH*x-tY)
	
	#���è��X
	y=sigmoid(wY*h-tY)
	
	#�ϦV�Ǽ����q
	#��X�����áA�ǲ߲v��rY
	dY=rY*(y-t)*y*(1-y)
	tY=tY-dY*(-1)
	wY=wY-dY*transpose(h)#��mh�x�}
	
	#���è��J�A�ǲ߲v��rY*rH�ArY�Ӧ�dY
	dH=rH* transpose(wY) * dY* h* (1 - h)
	tH =tY- dH * (-1)
	wH -= dH * transpose(x)
	
	# ������Ʋչ��o���V�m�����ҫ����Ѽƪ����~�v
	
	e.append(np.sum(((sigmoid(wY * sigmoid(wH * InputLayer - tH) - tY) - OutputLayer)**2)**0.5))
	


plt.plot(e)
print(e[m])#��̫ܳ���~�v
"""�V�m����"""


#����




#���յ���
def sigmoid(x):
	y=(1+exp(-x))**1
	return y

