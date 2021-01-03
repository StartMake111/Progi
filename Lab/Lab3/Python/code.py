from tkinter import *
import numpy
import random
global mass
class Game:
    def __init__(self,rand1,rand2,rand3):
        self.root = Tk()
        self.root.title('Game lines')
        self.can = Canvas(self.root, width=541,height=541,bg='white').place(x=5,y=20)
        self.root.geometry('900x600')
        self.rand1 = rand1
        self.rand2 = rand2
        self.rand3 = rand3
        self.buffer =numpy.zeros((3,),int)
        self.localgem = []
        self.position = [[8+(60*i),22.5+(60*i)] for i in range(9)]
        self.Used = []
        self.Ghosts = []
        for i in range(9):
            for j in range(9):
                self.Ghosts.append([8+(60*j),22.5+(60*i)])
    def RandomGenColor(self):
        self.rand1,self.rand2,self.rand3 = random.randint(0,3),random.randint(0,3),random.randint(0,3)
        self.buffer = [self.rand1,self.rand2,self.rand3]
    def AddMass():
        global mass
        mass+=10
    def Place(self):
        start = 1
        c = Canvas(self.root, width=541,height=541,bg='white')
        c.place(x=5,y=20)
        for i in range(0,10):
            c.create_line(start,0,start,541)
            c.create_line(0,start,541,start)
            start+=60
    def is_in_used(self):
        for i in self.Used:
            if i == self.localgem:
                return False
        self.Used.append(self.localgem)
        return True
    def is_used(aff, good):
        for i in aff:
            if good == i : 
                return False
        return True
    def clear(self):
        lists = self.root.slaves
        for i in lists:
            i.destroy()

    def AddGhost(self):
        for i in self.Ghosts:
            if Game.is_used(self.Used, i):
                blocks = Button(self.can, text = 'gh', fg = 'white',height =3 , width = 4, bg = 'white',command = lambda: Game.clear).place(x=i[0],y=i[1])
    def Replace():
        a = 5
    def RandomDraw(self,a):
        rand1 = random.randint(0,8)
        rand2 = random.randint(0,8)
        self.localgem = [self.position[rand1][0],self.position[rand2][1]]
        while self.is_in_used():        
            rand1 = random.randint(0,8)
            rand2 = random.randint(0,8)
            self.localgem = [self.position[rand1][0],self.position[rand2][1]]
            randcol = random.randint(0,2)
            if randcol == 0 :
                block = Button(self.can, text = 'g', fg = 'green',height=3,width=4,bg='white', command = self.AddGhost).place(x=self.position[rand1][0],y=self.position[rand2][1])
            elif randcol == 1:
                block = Button(self.can, text = 'r', fg = 'green',height=3,width=4,bg='white', command = self.AddGhost).place(x=self.position[rand1][0],y=self.position[rand2][1])
            elif randcol == 2 :
                block = Button(self.can, text = 'b', fg = 'green',height=3,width=4,bg='white', command = self.AddGhost).place(x=self.position[rand1][0],y=self.position[rand2][1])
p = Game(random.randint(0,3),random.randint(0,3),random.randint(0,3))
p.Place()
p.RandomDraw(1)
p.root.mainloop()


