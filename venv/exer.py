# from numpy import *
# import operator
# x=array([[3,3],[4,3],[1,1],[1,2]])
# y=[1,1,-1,-1]
# w=[0,0]
# b=0
# N=15#设置最多迭代次数
# flag=True
# cnt=0
# while(cnt<N):
#     flag=True
#     for i in range(3):
#         if(y[i]*(sum(x[i]*w)+b)<=0):
#             flag=False
#             w=w+x[i]*y[i]
#             b=b+y[i]
#             print("迭代:")#输出中间迭代结果
#             print(w)
#             print(b)
#     cnt+=1
#     if(flag==True):break;
# print("结果")
# print(w)
# print(b)
#

from PIL import Image
im=Image.open("E:\\1.jpg")
r,g,b=im.split()
om=Image.merge("RGB",(b,g,r))
om.save("E:\\2.jpg")
