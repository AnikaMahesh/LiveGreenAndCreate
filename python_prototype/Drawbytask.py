import tkinter as tk
import turtle
dn = 0
baba = 0
fir = 0
frog = 0
y = 1
z = 1
v = 0
cv = 0
print ("Do the tasks to get fun tools and tricks!")
x = 1
cl = 1
t = turtle.Turtle()
s = turtle.Turtle()
b = turtle.Turtle()
f = turtle.Turtle()
c = turtle.Turtle()
l = turtle.Turtle()
d = turtle.Turtle()
r = turtle.Turtle()
screen = turtle.Screen()
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.not_there = tk.Button(self)
        self.not_there["text"] = "take a cloth bag instead of a plastic bag."
        self.not_there["command"] = self.say_yes
        self.not_there.pack(side="right")
        self.not_there["bg"] = "yellow"
        self.no_there = tk.Button(self)
        self.no_there["bg"] = "yellow"
        self.no_there["text"] = "plant a tree."
        self.no_there["command"] = self.say
        self.no_there.pack(side="right")
        self.there = tk.Button(self)
        self.nap = tk.Button(self)
        self.nap["text"] = "Avoid eating meat."
        self.nap["fg"] = "black"
        self.nap["bg"] = "yellow"
        self.nap["command"] = self.say_hi
        self.nap.pack(side="right")
        self.law = tk.Button(self)
        self.law["text"] = "Use less disposable materals."
        self.law["fg"] = "black"
        self.law["bg"] = "yellow"
        self.law["command"] = self.magpie
        self.law.pack(side="right")
        self.blaw = tk.Button(self)
        self.blaw["text"] = "Walk instead of drive."
        self.blaw["fg"] = "black"
        self.blaw["bg"] = "yellow"
        self.blaw["command"] = self.no_way
        self.blaw.pack(side="right")
        self.why = tk.Button(self)
        self.why["text"] = "lights off when not needed."
        self.why["fg"] = "black"
        self.why["bg"] = "orange"
        self.why["command"] = self.cartman
        self.why.pack(side="right")
        self.wh = tk.Button(self)
        self.wh["text"] = "compost something."
        self.wh["fg"] = "black"
        self.wh["bg"] = "yellow"
        self.wh["command"] = self.fire
        self.wh.pack(side="right")
        self.whee = tk.Button(self)
        self.whee["text"] = "clear"
        self.whee["fg"] = "white"
        self.whee["bg"] = "green"
        self.whee["command"] = self.space_
        self.whee.pack(side="right")
    def say_hi(self):
        global v
        print("You are saving resources that are used to feed the livestock, and land that could be used for other things")
        v = v+1
        if v == 1:
            self.n = tk.Button(self)
            self.n["text"] = ("blocks")
            self.n["fg"] = ("red")
            self.n["bg"] = ("white")
            self.n["command"] = self.sam
            self.n.pack(side="bottom")
            v = v+1
        if v == 3:
            self.o = tk.Button(self)
            self.o["text"] = ("blocks")
            self.o["fg"] = ("white")
            self.o["bg"] = ("red")
            self.o["command"] = self.sammy
            self.o.pack(side="bottom")
            v = v+1
        else:
            print("products obtained")
    def fire(self):
        global fir
        fir = fir+1
        if fir == 1:
            print("you have earned the fire banner")
            self.fumigate = tk.Button(self)
            self.fumigate["text"] = "rainbow banner"
            self.fumigate["command"] = self.banner
            self.fumigate["fg"] = "red"
            self.fumigate["bg"] = "black"
            self.fumigate.pack(side="bottom")
        elif fir == 2:
            print("you have earned the circle tool")
            self.fumigater = tk.Button(self)
            self.fumigater["text"] = "circle"
            self.fumigater["command"] = self.circle
            self.fumigater["fg"] = "green"
            self.fumigater["bg"] = "black"
            self.fumigater.pack(side="bottom")
        else:
           print("products obtained")
    def circle(self):
        for p in range(370):
            t.forward(1)
            t.right(1)
    def say_yes(self):
        global cv
        cv = cv+1
        if cv == 1:
            print("You have earned the wooden planks.")
            self.p = tk.Button(self)
            self.p["text"] = "wooden plank"
            self.p["command"] = self.wood
            self.p["fg"] = "brown"
            self.p["bg"] = "black"
            self.p.pack(side="bottom")
        elif cv == 2:
            self.p = tk.Button(self)
            self.p["text"] = "black ink"
            self.p["command"] = self.aldoe
            self.p["fg"] = "green"
            self.p["bg"] = "blue"
            self.p.pack(side="bottom")
    def say(self):
        global frog
        frog = frog+1
        print("You have earned the right to turn.")
        if frog == 1:
            self.n = tk.Button(self)
            self.n["text"] = "turn"
            self.n["fg"] = "blue"
            self.n["bg"] = "green"
            self.n["command"] = self.nvm
            self.n.pack(side="bottom")
        elif frog == 2:
            self.n = tk.Button(self)
            self.n["text"] = "turn left"
            self.n["fg"] = "purple"
            self.n["bg"] = "green"
            self.n["command"] = self.nevermind
            self.n.pack(side="bottom")
        else:
            print("products obtained")
    def nevermind(self):
        t.right(-45)
    def wood(self):
        t.width(4)
        t.color('brown')
        t.forward(15)
        t.width(1)
        t.color('black')
    def cartman(self):
        global dn
        dn = dn+1
        if dn == 1:
            print("Press the button and bring the storm!")
            self.nt = tk.Button(self)
            self.nt["text"] = "Lightning"
            self.nt["fg"] = "yellow"
            self.nt["bg"] = "black"
            self.nt["command"] = self.fbi
            self.nt.pack(side="bottom")
        elif dn == 2:
            print("Press the button and bring the storm!")
            self.nato = tk.Button(self)
            self.nato["text"] = "diamond"
            self.nato["fg"] = "lightblue"
            self.nato["bg"] = "purple"
            self.nato["command"] = self.star
            self.nato.pack(side="bottom")
    def star(self) :
        print("you have switched off the lights when they are not needed.")
        st = turtle.Turtle()
        u = 5
        st.right(135)
        for marvelous in range(20):
            st.hideturtle()
            turtle.bgcolor('purple')
            st.color('lightblue')
            st.right(110)
            st.forward(u)
            st.right(70)
            st.forward(u)
            st.right(110)
            st.forward(u)
            st.right(70)
            st.forward(u)
            st.clear()
            u = u+8
        for marvelous in range(20):
            st.hideturtle()
            turtle.bgcolor('lightblue')
            st.color('purple')
            st.right(110)
            st.forward(u)
            st.right(70)
            st.forward(u)
            st.right(110)
            st.forward(u)
            st.right(70)
            st.forward(u)
            st.clear()
            u = u-8

    def no_way(self) :
        global x
        if x == 1:
            print("Green like the trees, green like a lizard and green like these planks!")
            self.p = tk.Button(self)
            self.p["text"] = "Green planks"
            self.p["fg"] = "green"
            self.p["bg"] = "black"
            self.p["command"] = self.green
            self.p.pack(side="bottom")
            x = x+1
        elif x == 2:
            print("White, seen in the storm!")
            self.npo = tk.Button(self)
            self.npo["text"] = "white planks"
            self.npo["fg"] = "white"
            self.npo["bg"] = "blue"
            self.npo["command"] = self.bean
            self.npo.pack(side="bottom")
            x = x+1
        else:
            print("products obtained")
    def space_(self) :
        global z
        t.goto(0,0)
        t.clear()
        s.clear()
        b.clear()
        f.clear()
        c.clear()
        l.clear()
        r.clear
        d.clear
        z = 1
        turtle.bgcolor('white')
    def bean(self):
        t.color('white')
        t.forward(10)
    def sam(self):
        o = 20
        t.speed(0)
        t.right(90)
        for othre in range(5):
            for forin in range(6):
                t.color('green')
                t.forward(o)
                t.right(60)
            t.right(60)
            t.forward(o)
            t.right(60)
            t.forward(o)
            t.forward(-o)
            t.right(240)
            t.forward(o)
            o = o/2
            for forin in range(6):
                t.color('brown')
                t.forward(o)
                t.right(60)
            t.right(60)
            t.forward(o)
            t.right(60)
            t.forward(o)
            t.forward(-o)
            t.right(240)
            t.forward(o)
            o = o*2
    def sammy(self):
        t = turtle.Turtle()
        o = 20
        t.speed(0)
        t.right(90)
        for othre in range(5):
            for forin in range(6):
                r.color('red')
                r.forward(o)
                r.right(60)
                r.color('blue')
            r.right(60)
            r.forward(o)
            r.color('purple')
            r.right(60)
            r.forward(o)
            r.color('green')
            r.forward(-o)
            r.right(240)
            r.color('orange')
            r.forward(o)
    def nvm(self):
        t.color('black')
        t.right(45)
    def aldoe(self):
        t.forward(20)
        t.color('black')
    def arrow(self):
        global baba
        baba = baba+1
        if baba == 1:
            self.npr = tk.Button(self)
            self.npr["text"] = "Arrow"
            self.npr["fg"] = "white"
            self.npr["bg"] = "black"
            self.npr["command"] = self.arrow_b
            self.npr.pack(side="bottom")
        else:
            print("Good job you are helping the environment!😀")
    def magpie(self):
        global y
        if y == 1:
            self.plaw = tk.Button(self)
            self.plaw["text"] = "water banner"
            self.plaw["fg"] = "white"
            self.plaw["bg"] = "black"
            self.plaw["command"] = self.screamer
            self.plaw.pack(side="bottom")
            y = y+1
        elif y == 2:
            self.evil = tk.Button(self)
            self.evil["text"] = "Snake Banner"
            self.evil["fg"] = "white"
            self.evil["bg"] = "purple"
            self.evil["command"] = self.wilderness
            self.evil.pack(side="bottom")
            y = y+1
        else:
            print("products obtained")
    def green(self):
        global x
        t.color('green')
        t.forward(10)
    def screamer(self):
        t.color('blue')
        for side in range(4) :
            t.speed(0)
            t.forward(10)
            t.right(45)
            t.forward(10)
            t.right(225)
            t.forward(8)
            t.right(90)
            t.forward(10)
            t.right(250)
            t.forward(20)
            t.right(60)
            t.forward(20)
            t.right(140)
            t.forward(15)
            t.right(330)
            t.forward(21)
            t.right(300)
            t.forward(20)
    def fbi(self):
        l = turtle.Turtle()
        b = 100
        l.hideturtle()
        l.speed(0)
        for got in range(15):
            l.penup()
            l.goto(0,340)
            turtle.bgcolor('black')
            l.color('yellow')
            l.right(90)
            l.pendown()
            l.forward(b)
            l.right(90)
            l.forward(b)
            l.right(270)
            l.forward(b)
            l.right(90)
            l.forward(b/2)
            l.right(270)
            l.forward(b+b)
            l.forward(-b+-b)
            l.right(90)
            l.forward(-b/2)
            l.right(270)
            l.forward(3*b)
            l.forward(-3*b)
            l.right(180)
            l.forward(b)
            l.right(270)
            l.forward(-2*b)
            l.right(270)
            l.forward(2*b)
            l.forward(-b)
            l.right(270)
            l.forward(b/2)
            l.right(90)
            l.forward(3*b)
            l.right(270)
            l.forward(b)
            l.right(90)
            l.forward(3*b)
            l.forward(-3*b)
            l.right(90)
            l.forward(b*2)
            l.right(270)
            l.forward(b*3)
            l.forward(-b)
            l.right(90)
            l.forward(b/2)
            l.right(270)
            l.forward(b*2)
            b = b-10
            l.penup()
            l.goto(0,340)
            l.pendown()
            l.clear()
            screen.update()
            l.right(90)
        turtle.bgcolor('white')
    def banner(self):
        t.speed(0)
        for foreign in range(4):
            t.color('red')
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.color('orange')
            t.right(270)
            t.forward(10)
            t.right(270)
            t.forward(10)
            t.right(90)
            t.color('yellow')
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.color('green')
            t.right(270)
            t.forward(10)
            t.right(270)
            t.forward(10)
            t.right(90)
            t.color('blue')
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.color('purple')
            t.right(270)
            t.forward(10)
            t.right(270)
            t.forward(10)
            t.right(90)
    def wilderness(self):
        global z
        t.speed(0)
        def square():
            for g in range(4):
                t.forward(z)
                t.right(90)
        for sequence in range(7):
            t.color('purple')
            square()
            z = z+4
            t.color('blue')
            square()
            z = z+4
root = tk.Tk()
app = Application(master=root)
app.mainloop()
