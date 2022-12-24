from random import random
from tkinter import Tk,Canvas
from time import sleep

window=Tk()
canvas=Canvas(window,bg="#FFFFFF",width=1000,height=580)
window.title("gravity")

g=1
totaltime=1000
frequency=25

def start():
    n=1000
    positions=[]
    velocitys=[]
    masses=[]
    for i in range(n):
        # x,y=random()*400+360,random()*300+160
        x,y=random()*1000,random()*580
        positions.append((x,y))
        dx,dy=random()-0.5,random()-0.5
        # v=[[[1,-1],[-1,-1]],
        #     [[1,1],[-1,1]]]
        # dx,dy=v[x<560][y<290]
        velocitys.append((dx*2,dy*2))
        masses.append(1)
    
    for t in range(totaltime*frequency):
        n=len(positions)
        #update all positions
        newpositions=[]
        newvelocitys=[]
        newmasses=[]
        for i in range(n):
            x1,y1=positions[i]
            dx1,dy1=velocitys[i]
            m1=masses[i]
            for j in range(n):
                if i!=j:
                    p2x,p2y=positions[j]
                    d2=(p2x-x1)**2+(p2y-y1)**2
                    d=d2**0.5
                    a=g*masses[j]/d2
                    dx1+=a*(p2x-x1)/d
                    dy1+=a*(p2y-y1)/d
            x1+=dx1
            y1+=dy1
            if 20>x1:
                x1=21
                dx1=0
            elif x1>980:
                x1=979
                dx1=0
            elif 20>y1:
                y1=21
                dy1=0
            elif y1>560:
                y1=559
                dy1=0
            #print(t,i,dx1,dy1)
            newpositions.append((x1,y1))
            newvelocitys.append((dx1,dy1))
            newmasses.append(m1)
        positions=newpositions
        velocitys=newvelocitys
        masses=newmasses
        
        overlap=True
        while overlap:
            n=len(positions)
            overlap=False
            for i in range(n):
                for j in range(n):
                    #print(len(positions),len(masses),i,j,positions)
                    if i<j and (positions[i][0]-positions[j][0])**2+(positions[i][1]-positions[j][1])**2<max(masses[i],masses[j]):#(masses[i]+masses[j])**0.5:
                        overlap=True
                        break
                if overlap:
                    break
            if overlap:
                m2=masses.pop(j)
                m1=masses.pop(i)
                if m1>m2:
                    positions.pop(j)
                    position=positions.pop(i)
                else:
                    position=positions.pop(j)
                    positions.pop(i)
                dx2,dy2=velocitys.pop(j)
                dx1,dy1=velocitys.pop(i)
                dx=(dx1*m1+dx2*m2)/(m1+m2)
                dy=(dy1*m1+dy2*m2)/(m1+m2)
                positions.append(position)
                masses.append(m1+m2)
                velocitys.append((dx,dy))
                
        
        canvas.delete("all")
        for p in range(n):
            x,y=positions[p][0],positions[p][1]
            r=masses[p]**0.5
            canvas.create_oval(x-r,y-r,x+r,y+r)
        canvas.create_text(100,10,text=str(t//frequency)+"/"+str(totaltime))
        canvas.update()
        
        sleep(1/frequency)

def click(coordinate):
    start()
canvas.bind("<Button-1>",click)
canvas.pack()
window.mainloop()

