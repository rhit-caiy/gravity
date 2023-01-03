from random import random
from tkinter import Tk,Canvas
#from time import sleep
import math

window=Tk()
canvas=Canvas(window,bg="#FFFFFF",width=1000,height=1000)
window.title("gravity")

g=0.01
totaltime=10000
frequency=10
num=100
r=400#distance of sun and planet
rpoint=1
xcenter=450
ycenter=400
msun=100000
mplanet=1
vplanet=(g*msun/r)**0.5
print("vplanet",vplanet)

def start():
    xplanet=r
    yplanet=0
    
    vxplanet=0
    vyplanet=-vplanet
    
    positions=[]
    velocitys=[]
    
    alpha=mplanet/(msun+mplanet)
    
    xratio=[1-(alpha/3)**(1/3),1+(alpha/3)**(1/3),-(1+5*alpha/12),((msun-mplanet)/(msun+mplanet))/2,(msun-mplanet)/(msun+mplanet)/2]
    yratio=[0,0,0,-3**0.5/2,3**0.5/2]
    # rratio=[(xratio[i]**2+yratio[i]**2)**0.5 for i in range(5)]
    # for i in range(5):
    #     print(xratio[i],yratio[i],rratio[i])
    for l in range(2,5):#2,5
        x,y=r*xratio[l],r*yratio[l]
        v=vplanet#*rratio[l]
        dx,dy=v*yratio[l],-v*xratio[l]
        #print(dx,dy,dx**2+dy**2)
        for i in range(num):
            positions.append((x+random()-0.5,y+random()-0.5))
            velocitys.append((dx,dy))
    
    for t in range(totaltime*frequency):
        n=len(positions)
        #update all positions
        newpositions=[]
        newvelocitys=[]
        for i in range(n):
            x1,y1=positions[i]
            dx1,dy1=velocitys[i]
            
            d2=x1**2+y1**2
            d=d2**0.5
            a=g*msun/d2
            dx1-=a*x1/d
            dy1-=a*y1/d
            
            d2=(xplanet-x1)**2+(yplanet-y1)**2
            d=d2**0.5
            a=g*mplanet/d2
            dx1+=a*(xplanet-x1)/d
            dy1+=a*(yplanet-y1)/d
            
            x1+=dx1
            y1+=dy1
            
            newpositions.append((x1,y1))
            newvelocitys.append((dx1,dy1))
        positions=newpositions
        velocitys=newvelocitys
        
        d2=xplanet**2+yplanet**2
        d=d2**0.5
        a=msun*g/d2
        vxplanet-=a*xplanet/d
        vyplanet-=a*yplanet/d
        xplanet+=vxplanet
        yplanet+=vyplanet
        
        planetangle=math.atan(yplanet/xplanet)
        if xplanet<0:
            planetangle+=math.pi
        
        canvas.delete("all")
        
        canvas.create_oval(xplanet*0.1-5+xcenter,yplanet*0.1-5+ycenter,xplanet*0.1+5+xcenter,yplanet*0.1+5+ycenter,fill="#0000FF")
        canvas.create_oval((xplanet**2+yplanet**2)**0.5-5+xcenter,-5+ycenter,(xplanet**2+yplanet**2)**0.5+5+xcenter,5+ycenter,fill="#FFFFFF")
        
        canvas.create_oval(-20+xcenter,-20+ycenter,20+xcenter,20+ycenter,outline="#FF0000",fill="#FF0000")
        #canvas.create_text(100,10,text=str(t//frequency)+"/"+str(totaltime)+"  "+str(t))
        canvas.create_text(100,10,text=str(t)+"/"+str(frequency*totaltime))
        #canvas.create_text(200,10,text=str((xplanet**2+yplanet**2)**0.5))
        
        for p in range(n):
            x,y=positions[p][0],positions[p][1]
            
            
            r1=(x**2+y**2)**0.5
            theta=math.atan(y/x)-planetangle
            if x<0:
                theta+=math.pi
            
            x=math.cos(theta)*r1
            y=math.sin(theta)*r1
            
            canvas.create_oval(x-rpoint+xcenter,y-rpoint+ycenter,x+rpoint+xcenter,y+rpoint+ycenter,outline=("#FF0000","#00FF00","#0000FF")[p//num])
        
        
        canvas.update()
        
        #sleep(1/frequency)

def click(coordinate):
    start()
canvas.bind("<Button-1>",click)
canvas.pack()
window.mainloop()

