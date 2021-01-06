from tkinter import *
from PIL import Image, ImageTk
import random
import os
import sys
#_ballsop = [ImageTk.PhotoImage(i) for i in _balls]

class Game:
    def __init__(self):
        self.used = {}
        self.use = [100]
        self.root = Tk()
        self.HasAccessrow = {}
        self.HasAccesscolumn = {}
        self.root.title('Game lines')
        self.root.geometry('900x640')
        self.root.configure(background='#414141')
        self.col = 0
        self.localgem = []
        self.tileset = Image.open("Lab/Lab3/Python/cell-bgr.png").convert('RGBA')
        self.img_tile = ImageTk.PhotoImage(self.tileset.crop((0,1,67,66)))
        self.colorpic = []
        self.clic = False
        self.selected_circle = 0
        b = (1,1,54,54)
        self.clearedplit = self.
        self.clcked = 0
        self.clckedcolor = 0
        self.balraw = {
            "pink": Image.open("Lab/Lab3/Python/ball-pink.png").convert('RGBA').crop(b).resize((65,65)),
            "red": Image.open("Lab/Lab3/Python/ball-red.png").convert('RGBA').crop(b).resize((65,65)),
            "yellow": Image.open("Lab/Lab3/Python/ball-yellow.png").convert('RGBA').crop(b).resize((65,65)),
            "green": Image.open("Lab/Lab3/Python/ball-green.png").convert('RGBA').crop(b).resize((65,65)),
            "aqua": Image.open("Lab/Lab3/Python/ball-aqua.png").convert('RGBA').crop(b).resize((65,65)),
            "blue": Image.open("Lab/Lab3/Python/ball-blue.png").convert('RGBA').crop(b).resize((65,65)),
            "violet": Image.open("Lab/Lab3/Python/ball-violet.png").convert('RGBA').crop(b).resize((65,65)),
            "bg" : Image.open("Lab/Lab3/Python/cell-bgr.png").convert('RGBA')
        }
        self.balrawselected = {
            "pink": Image.open("Lab/Lab3/Python/ball-pink.png").convert('RGBA').crop(b).resize((65,65)),
            "red": Image.open("Lab/Lab3/Python/ball-red.png").convert('RGBA').crop(b).resize((65,65)),
            "yellow": Image.open("Lab/Lab3/Python/ball-yellow.png").convert('RGBA').crop(b).resize((65,65)),
            "green": Image.open("Lab/Lab3/Python/ball-green.png").convert('RGBA').crop(b).resize((65,65)),
            "aqua": Image.open("Lab/Lab3/Python/ball-aqua.png").convert('RGBA').crop(b).resize((65,65)),
            "blue": Image.open("Lab/Lab3/Python/ball-blue.png").convert('RGBA').crop(b).resize((65,65)),
            "violet": Image.open("Lab/Lab3/Python/ball-violet.png").convert('RGBA').crop(b).resize((65,65)),
            "bg" : Image.open("Lab/Lab3/Python/cell-bgr.png").convert('RGBA')
        }
    
        self._balls = {
            "pink": ImageTk.PhotoImage(self.balraw["pink"]),
            "red": ImageTk.PhotoImage(self.balraw["red"]),
            "yellow": ImageTk.PhotoImage(self.balraw["yellow"]),
            "green": ImageTk.PhotoImage (self.balraw["green"]),
            "aqua": ImageTk.PhotoImage  (self.balraw["aqua"]),
            "blue": ImageTk.PhotoImage  (self.balraw["blue"]),
            "violet": ImageTk.PhotoImage(self.balraw["violet"])
            }
        self._ballsselected = {
        "pink": ImageTk.PhotoImage(  self.balrawselected["pink"]),
        "red": ImageTk.PhotoImage(   self.balrawselected["red"]),
        "yellow": ImageTk.PhotoImage(self.balrawselected["yellow"]),
        "green": ImageTk.PhotoImage (self.balrawselected["green"]),
        "aqua": ImageTk.PhotoImage  (self.balrawselected["aqua"]),
        "blue": ImageTk.PhotoImage  (self.balrawselected["blue"]),
        "violet": ImageTk.PhotoImage(self.balrawselected["violet"])
        }
        self.colors = {0: "pink", 1: "red", 2: "yellow", 3: "green", 4: "aqua", 5: "blue", 6: "violet"}
    def AddScore(self,event):
        self.col = self.col+10
        #self.score = Label(self.root, text = self.col).place(x=770,y = 180)
    def HasAccess(self):
        for i in range(len(self.localgem)):
            print(i)
            

    def click(self,event):
        if event.widget in self.used:
            self.clckedcolor = self.used[event.widget][0]
            self.clcked = event.widget
            self.selected_circle = self.used[event.widget][1]
            self.clic = not self.clic
        elif self.clic == True: 
            self.clic = not self.clic
            event.widget.config(image = self._ballsselected[self.clckedcolor])
            self.used.pop(self.clcked)
            self.clcked.config(image = self.img_tile)
            if (str(event.widget)[7:]) == '':
                self.used.update({event.widget : [self.clckedcolor, 0]})
                self.use.append(0)
            else:
                self.used.update({event.widget : [self.clckedcolor, int(str(event.widget)[7:])-1]})
                self.use.append(int(str(event.widget)[7:])-1)
            self.use.remove(self.selected_circle)
            self.use = list(set(self.use))
            #print(self.used[self.clcked][0])
            #self.use.remove(self.used[self.clcked][1])
            self.RandomPlaceColor()
            print(self.use)
    def restartgame():
        python = sys.executable
        os.execl(python,python, * sys.argv)
    def set_color(self,event):
        for i in self.localgem:
            if str(i)==str(event.widget):
                i.config(image = self._balls['pink'])
    def Place(self):
        for i in range(9):
            for j in range(9):
                lbl = Label(self.root,  image = self.img_tile, borderwidth = 0)
                lbl.bind('<Button-1>', self.click)
                lbl.place(x=7+(j*70),y=(70*i)+7)
                self.localgem.append(lbl)
        #nameenter = Entry(self.root,width=20).place(x = 710, y = 200)
        lbl_name = Label(self.root, text = 'Батя сказал', font=('Arial',26), bg = '#414141', fg='white').place(x=660,y=25)
        lbl_score = Label(self.root, text = 'Счёт: ', font=('Arial',26), bg = '#414141', fg='white').place(x=660,y=100)
        lbl_help = Label(self.root, text = 'Подсказка:', font=('Arial',26), bg = '#414141', fg='white').place(x=660,y=230)
        self.score = Label(self.root, text = self.col,font=('Arial',26), bg = '#414141', fg='white').place(x= 755, y = 100)
    def RandomPlaceColor(self):
        rand1,rand2,rand3 = random.randint(0,6),random.randint(0,6),random.randint(0,6)
        rand11,rand22,rand33 = random.randint(0,80),random.randint(0,80),random.randint(0,80)
        if len(self.use) == 79 :
            lbl = Label(self.root,text ='You lox', font=('Arial',100), bg = '#414141', fg='red')
            lbl.place(x=250,y=250)
            restart = Button(self.root, text = 'Press to restart', bg = '#414141', fg='red', command = Game.restartgame).place(x=410,y=400)
            return 0
            
        while True:
            found = 1
            rand11,rand22,rand33 = random.randint(0,80),random.randint(0,80),random.randint(0,80)
            j = len(self.use)
            for i in self.use:
                if i == rand11 or i == rand22 or i == rand33 or rand11==rand22 or rand11==rand33 or rand22==rand33:
                    found = 2
                    break
                else:
                    j -= 1
                if j == 0:
                    break
            if found == 1:
                break
                
                

        self.use.append(rand11)
        self.use.append(rand22)
        self.use.append(rand33)
        self.use = list(set(self.use))
        self.localgem[rand11].config(image = self._balls[self.colors[rand1]])
        self.localgem[rand22].config(image = self._balls[self.colors[rand2]])
        self.localgem[rand33].config(image = self._balls[self.colors[rand3]])
        self.used.update({self.localgem[rand11] : [self.colors[rand1], rand11]})
        self.used.update({self.localgem[rand22] : [self.colors[rand2], rand22]})
        self.used.update({self.localgem[rand33] : [self.colors[rand3], rand33]})
p = Game()
p.Place()
p.RandomPlaceColor()
p.root.mainloop()


