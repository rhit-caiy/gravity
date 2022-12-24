from random import random
from tkinter import Tk,Canvas
from time import sleep

window=Tk()
canvas=Canvas(window,bg="#DDDDDD",width=1000,height=1000)
window.title("gravity")

g=10
totaltime=100
frequency=100
num=100
r=300#distance of sun and planet
rpoint=0.5
xcenter=500
ycenter=500
msun=10000
mplanet=1
vplanet=(g*msun/r)**0.5
xsun=0
ysun=0


def start():
    xplanet=xsun+r
    yplanet=xsun
    vxplanet=0
    vyplanet=-vplanet
    
    positions=[]
    velocitys=[]
    
    alpha=mplanet/(msun+mplanet)
    #draft
    '''
    for i in range(n):
        #x,y=random()*1000,random()*1000
        #x,y=random()*500+500,500
        x,y=xsun-(r*(1+5*alpha/12))+random()*2-1,500+random()*2-1#L3
        positions.append((x,y))
        #dx,dy=random()-0.5,random()-0.5
        #dx,dy=0,-(g*msun/(x-500))**0.5
        dx,dy=random()*2-1,vplanet+random()*2-1#L3
        velocitys.append((dx,dy))
    '''
    
    xratio=[1-(alpha/3)**(1/3),1+(alpha/3)**(1/3),-(1+5*alpha/12),((msun-mplanet)/(msun+mplanet))/2,(msun-mplanet)/(msun+mplanet)/2]
    yratio=[0,0,0,-3**0.5/2,3**0.5/2]
    rratio=[(xratio[i]**2+yratio[i]**2)**0.5 for i in range(5)]
    for l in range(2,5):
        for i in range(num):
            x,y=xsun+r*xratio[l],ysun+r*yratio[l]
            dx,dy=vplanet*yratio[l]/rratio[l],-vplanet*xratio[l]/rratio[l]
            positions.append((x+random()-0.5,y+random()-0.5))
            velocitys.append((dx,dy))
    print(xratio,yratio,rratio)
    
    
    # #L1
    # for i in range(n):
    #     x,y=xsun+r*(1-(alpha/3)**(1/3))+random()-0.5,yplanet+random()-0.5
    #     dx,dy=0+random()-0.5,-(vplanet*(x-xsun)/r)+random()-0.5
    #     positions.append((x,y))
    #     velocitys.append((dx,dy))
    # #L2
    # for i in range(n):
    #     x,y=xsun+r*(1+(alpha/3)**(1/3))+random()-0.5,yplanet+random()-0.5
    #     dx,dy=0+random()-0.5,-(vplanet*(x-xsun)/r)+random()-0.5
    #     positions.append((x,y))
    #     velocitys.append((dx,dy))
        
    #L3
    # for i in range(n):
    #     x,y=xsun-(r*(1+5*alpha/12))+random()-0.5,500+random()-0.5
    #     dx,dy=random()*-0.5,(vplanet*(xsun-x)/r)+random()-0.5
    #     positions.append((x,y))
    #     velocitys.append((dx,dy))
    
    # #L4
    # for i in range(n):
    #     x,y=xsun+(r/2*((msun-mplanet)/(msun+mplanet)))+random()-0.5,ysun-0.5*r*3**0.5+random()-0.5
    #     dx,dy=-0.75**0.5*vplanet+random()-0.5,-0.5*vplanet+random()-0.5
    #     positions.append((x,y))
    #     velocitys.append((dx,dy))
    
    # #L5
    # for i in range(n):
    #     x,y=xsun+(r/2*((msun-mplanet)/(msun+mplanet)))+random()-0.5,ysun+0.5*r*3**0.5+random()-0.5
    #     dx,dy=0.75**0.5*vplanet+random()-0.5,-0.5*vplanet+random()-0.5
    #     positions.append((x,y))
    #     velocitys.append((dx,dy))
    
    
    for t in range(totaltime*frequency):
        n=len(positions)
        #update all positions
        newpositions=[]
        newvelocitys=[]
        for i in range(n):
            x1,y1=positions[i]
            dx1,dy1=velocitys[i]
            
            d2=(xsun-x1)**2+(xsun-y1)**2
            d=d2**0.5
            a=g*msun/d2
            dx1+=a*(xsun-x1)/d
            dy1+=a*(ysun-y1)/d
            
            d2=(xplanet-x1)**2+(yplanet-y1)**2
            d=d2**0.5
            a=g*mplanet/d2
            dx1+=a*(xplanet-x1)/d
            dy1+=a*(yplanet-y1)/d
            
            x1+=dx1
            y1+=dy1
            # if 0>x1:
            #     x1=1
            #     dx1=0
            # elif x1>1000:
            #     x1=999
            #     dx1=0
            # elif 0>y1:
            #     y1=1
            #     dy1=0
            # elif y1>1000:
            #     y1=999
            #     dy1=0
            newpositions.append((x1,y1))
            newvelocitys.append((dx1,dy1))
        positions=newpositions
        velocitys=newvelocitys
        '''
        for i in range(n):
            if 450<positions[i][0]<550 and 450<positions[i][1]<550:#in the sun
                positions[i]=(r+500,500)
                velocitys[i]=(0,-vplanet)
        '''
        d2=(xplanet-xsun)**2+(yplanet-ysun)**2
        d=d2**0.5
        a=msun*g/d2
        vxplanet+=a*(xsun-xplanet)/d
        vyplanet+=a*(ysun-yplanet)/d
        xplanet+=vxplanet
        yplanet+=vyplanet
        
        '''
        canvas.delete("all")
        for p in range(n):
            x,y=positions[p][0],positions[p][1]
            canvas.create_oval(x-r+xcenter,y-r+xcenter,x+r+ycenter,y+r+ycenter,outline=("#FF0000","#00FF00","#0000FF")[p//100])
        canvas.create_oval(xplanet-5+xcenter,yplanet-5+ycenter,xplanet+5+xcenter,yplanet+5+ycenter,fill="#0000FF")
        canvas.create_oval(xsun-20+xcenter,ysun-20+ycenter,xsun+20+xcenter,ysun+20+ycenter,outline="#FF0000",fill="#FF0000")
        canvas.create_text(100,10,text=str(t//frequency)+"/"+str(totaltime)+"  "+str(t))
        '''
        canvas.delete("all")
        for p in range(n):
            x,y=positions[p][0],positions[p][1]
            canvas.create_oval(x-rpoint+xcenter,y-rpoint+xcenter,x+rpoint+ycenter,y+rpoint+ycenter,outline=("#FF0000","#00FF00","#0000FF")[p//100])
        canvas.create_oval(xplanet-5+xcenter,yplanet-5+ycenter,xplanet+5+xcenter,yplanet+5+ycenter,fill="#0000FF")
        canvas.create_oval(xsun-20+xcenter,ysun-20+ycenter,xsun+20+xcenter,ysun+20+ycenter,outline="#FF0000",fill="#FF0000")
        canvas.create_text(100,10,text=str(t//frequency)+"/"+str(totaltime)+"  "+str(t))
        
        
        canvas.update()
        
        sleep(1/frequency)

def click(coordinate):
    start()
canvas.bind("<Button-1>",click)
canvas.pack()
window.mainloop()

