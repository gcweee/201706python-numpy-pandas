
# coding: utf-8

# In[ ]:

import pygame,sys
from pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World!')

while True:
    sysFont=pygame.font.SysFont('None',28)
    rendered=sysFont.render("Hello World!",0,(155,100,100))
    screen.blit(rendered,(100,100))
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()


# In[ ]:

import pygame,sys
from pygame.locals import *

#初始化其他Pygame函数
pygame.init()

#创建pygame surface对象用于绘图
screen=pygame.display.set_mode((400,300))
#窗口标题
pygame.display.set_caption('Hello My Python World!')

#一直有一个主循环一直运行,直到退出事件的发生.
while True:
    #根据英文逗号隔开的系统字体列表字符串(None)和字体大小创建字体对象
    sysFont=pygame.font.SysFont('None',28)
    #render(text,antialias(smooth),colors,background)
    rendered=sysFont.render("Hello My Python World!",0,(155,100,100))
    #draw one image onto surface,with location of (123,223)
    screen.blit(rendered,(123,223))
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()


# In[ ]:

import os
import pygame,sys
import numpy as np
from pygame.locals import *

os.chdir(r'C:\Users\Administrator\Desktop')

img=pygame.image.load('head.jpg')
pygame.init()
clock=pygame.time.Clock()#创建一个游戏中的时钟对象
screen=pygame.display.set_mode((1300,1400))
pygame.display.set_caption('animating objects!')

steps=np.linspace(20,360,40).astype(int)
right=np.zeros((2,len(steps)))
down=np.zeros((2,len(steps)))
left=np.zeros((2,len(steps)))
up=np.zeros((2,len(steps)))

right[0]=steps
right[1]=20
down[0]=360
down[1]=steps
left[0]=steps[::-1]
left[1]=360
up[0]=20
up[1]=steps[::-1]

pos=np.concatenate((right.T,down.T,left.T,up.T))
i=0

while True:
    screen.fill((255,255,255))
    if i>=len(pos):
        i=0
    screen.blit(img,pos[i])
    i+=1
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(30)#30为每秒钟的帧数


# In[ ]:

import os
import pygame,sys
import numpy as np
from pygame.locals import *
import matplotlib as mpl

mpl.use('Agg')
import matplotlib.backends.backend_agg as agg

os.chdir(r'C:\Users\Administrator\Desktop')


fig=plt.figure(figsize=[3,3])
ax=fig.add_subplot(111)
canvas=agg.FigureCanvasAgg(fig)

def plot(data):
    ax.plot(data)
    canvas.draw()
    renderer=canvas.get_renderer()
    
    raw_data=renderer.tostring_rgb()
    size=canvas.get_width_height()
    
    return pygame.image.fromstring(raw_data,size,'RGB')

pygame.init()
img=pygame.image.load('Jellyfish.jpg')

clock=pygame.time.Clock()
screen=pygame.display.set_mode((1300,1400))
pygame.display.set_caption('animating objects!')

steps=np.linspace(20,360,40).astype(int)
right=np.zeros((2,len(steps)))
down=np.zeros((2,len(steps)))
left=np.zeros((2,len(steps)))
up=np.zeros((2,len(steps)))

right[0]=steps
right[1]=20
down[0]=360
down[1]=steps
left[0]=steps[::-1]
left[1]=360
up[0]=20
up[1]=steps[::-1]

pos=np.concatenate((right.T,down.T,left.T,up.T))
i=0
history=np.array([])
surf=plot(history)

while True:
    screen.fill((255,255,255))
    if i>=len(pos):
        i=0
    screen.blit(img,pos[i])
    history=np.append(history,pos[i])
    screen.blit(surf,(100,100))
    i+=1
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(30)


# In[ ]:

import sklearn.cluster
import numpy as np
import matplotlib.pyplot as plt
import pygame,sys
from pygame.locals import *

positions=np.random.randint(0,400,size=(30,2))

#生成欧式距离
positions_norms=np.sum(positions**2,axis=1)
#用欧式距离初始化关联矩阵
S=-positions_norms[:,np.newaxis]-positions_norms[np.newaxis,:]
+2*np.dot(positions,positions.T)

#创建AffinityPropagation对象并根据关联矩阵进行聚类
aff_pro=sklearn.cluster.AffinityPropagation().fit(S)
labels=aff_pro.labels_

polygon_points=[]

for i in range(max(labels)+1):
    polygon_points.append([])
#对数据点进行聚类
for i in range(len(labels)):
    polygon_points[labels[i]].append(positions[i])

pygame.init()
screen=pygame.display.set_mode((400,400))

while True:
    screen.fill((255,255,255))
    for i in range(len(polygon_points)):
        #根据指定的Surface对象,颜色和数据点列表绘制多边形
        pygame.draw.polygon(screen,(255,0,0),polygon_points[i])
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


