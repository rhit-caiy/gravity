from random import random
from tkinter import Tk,Canvas
#from time import sleep
import math

window=Tk()
canvas=Canvas(window,bg="#FFFFFF",width=1000,height=1000)
window.title("ring")

g=1
totaltime=10000
frequency=1

pointnum=10000
#distance of sun and planet
r=100
#ring
r1=30
r2=300
rpoint=1
xcenter=500
ycenter=500
#masses
msun=1000
mplanet=1
vplanet=(g*msun/r)**0.5
print("vplanet",vplanet)

def start():
    xplanet=(r**2-vplanet**2/4)**0.5
    yplanet=-vplanet/2
    
    vxplanet=0
    vyplanet=-vplanet
    
    positions=[]
    velocitys=[]
    for i in range(pointnum):
        rp=r1+random()*(r2-r1)
        theta=random()*math.pi*2
        x,y=rp*math.sin(theta),rp*math.cos(theta)
        v=(g*msun/rp)**0.5
        dx,dy=v*y/rp,-v*x/rp
        positions.append((x,y))
        velocitys.append((dx,dy))
    
    for t in range(totaltime*frequency):
        n=len(positions)
        #update all positions
        newpositions=[]
        newvelocitys=[]
        for i in range(n):
            x1,y1=positions[i]
            dx1,dy1=velocitys[i]
            
            ds2=x1**2+y1**2
            ds=ds2**0.5
            a=g*msun/ds2
            dx1-=a*x1/ds
            dy1-=a*y1/ds
            
            dp2=(xplanet-x1)**2+(yplanet-y1)**2
            dp=dp2**0.5
            a=g*mplanet/dp2
            dx1+=a*(xplanet-x1)/dp
            dy1+=a*(yplanet-y1)/dp
            
            x1+=dx1
            y1+=dy1
            
            if 25<ds<600 and dp>10:
                newpositions.append((x1,y1))
                newvelocitys.append((dx1,dy1))
        positions=newpositions
        velocitys=newvelocitys
        n=len(positions)
        
        d2=xplanet**2+yplanet**2
        d=d2**0.5
        a=msun*g/d2
        vxplanet-=a*xplanet/d
        vyplanet-=a*yplanet/d
        xplanet+=vxplanet
        yplanet+=vyplanet
        
        canvas.delete("all")
        canvas.create_line(0,ycenter,2*xcenter,ycenter,fill="#FF8080")
        canvas.create_line(xcenter,0,xcenter,2*ycenter,fill="#FF8080")
        for i in range(10):
            canvas.create_line(i*100,ycenter-5,i*100,ycenter+5,fill="#FF8080")
            canvas.create_line(xcenter-5,i*100,xcenter+5,i*100,fill="#FF8080")
        for i in range(100):
            canvas.create_line(i*10,ycenter-2,i*10,ycenter+2,fill="#FF8080")
            canvas.create_line(xcenter-2,i*10,xcenter+2,i*10,fill="#FF8080")
        for i in 0.5,1,2,3:
            canvas.create_oval(xcenter-r*i,ycenter-r*i,xcenter+r*i,ycenter+r*i,outline="#FF0000")
        
        canvas.create_oval(xplanet-5+xcenter,yplanet-5+ycenter,xplanet+5+xcenter,yplanet+5+ycenter,fill="#0000FF")
        
        canvas.create_oval(-20+xcenter,-20+ycenter,20+xcenter,20+ycenter,outline="#FF0000",fill="#FF0000")
        canvas.create_text(100,10,text=str(t)+"/"+str(frequency*totaltime))
        canvas.create_text(300,10,text="radius "+str((xplanet**2+yplanet**2)**0.5))
        canvas.create_text(500,10,text="point: "+str(n))
        canvas.create_text(700,10,text="mass ratio "+str(mplanet)+":"+str(msun))
        
        for p in range(n):
            x,y=positions[p][0],positions[p][1]
            canvas.create_oval(x-rpoint+xcenter,y-rpoint+ycenter,x+rpoint+xcenter,y+rpoint+ycenter,outline="#000000")
        
        
        canvas.update()
        
        #sleep(1/frequency)

def click(coordinate):
    start()
canvas.bind("<Button-1>",click)
canvas.pack()
window.mainloop()

