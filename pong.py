from tkinter import *
from tkinter import messagebox
import random, time

class Ball:
    def __init__(self,canvas,bat,bat2,color):
        self.canvas = canvas
        self.bat = bat
        self.bat2 = bat2
        self.playerScore = 0
        self.player1Score = 0
        self.drawP1 = None
        self.drawP = None
        self.id = self.canvas.create_oval(10,10,35,35,fill=color)
        self.canvas.move(self.id,327,220)
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.x = random.choice([-2.5,2.5])
        self.y = -2.5
        
    def checkwin(self):
        winner = None
        if self.playerScore == 10:
           winner = 'Player left wins'
           #gameOver = True
        if self.player1Score == 10:
            winner = 'Player Right'
            #gameOver = True
        return winner
    
    def checkForgameOver(self):
        gameOver = False
        if self.playerScore == 10 or self.player1Score == 10:
            gameOver = True
            return gameOver
        return gameOver
            
    def updatep(self,val):
        self.canvas.delete(self.drawP)
        self.drawP = self.canvas.create_text(170,50,font=('freesansbold.ttf', 40),text=str(val),fill='white')

    def updatep1(self,val):
        self.canvas.delete(self.drawP1)
        self.drawP1 = self.canvas.create_text(550,50,font=('freesansbold.ttf', 40),text=str(val),fill='white')

    def hit_bat(self,pos):
        bat_pos = self.canvas.coords(self.bat.id)
        if pos[2] >= bat_pos[0] and pos[0] <= bat_pos[2]:
            if pos[3] >= bat_pos[1] and pos[3] <= bat_pos[3]:
                return True
            return False
        
    def hit_bat2(self,pos):
        bat_pos = self.canvas.coords(self.bat2.id)
        if pos[2] >= bat_pos[0] and pos[0] <= bat_pos[2]:
            if pos[3] >= bat_pos[1] and pos[3] <= bat_pos[3]:
                return True
            return False   

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 4
        if pos[3] >= self.canvas_height:
            self.y = -4
        if pos[0] <= 0:
            self.player1Score += 1
            self.canvas.move(self.id,327,220)
            self.x = 4
            self.updatep1(self.player1Score)
        if pos[2] >= self.canvas_width:
            self.playerScore += 1
            self.canvas.move(self.id,-327,-220)
            self.x = -4
            self.updatep(self.playerScore)
        if self.hit_bat(pos):
            self.x = 4
        if self.hit_bat2(pos):
            self.x = -4

class pongbat():
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(40,200,25,310,fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.y = 0
        
        self.canvas.bind_all('w', self.up)
        self.canvas.bind_all('s', self.down)

    def up(self,evt):
        self.y = -5

    def down(self,evt):
        self.y = 5

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = -0

            
class pongbat2():
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(680,200,660,310,fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.y = 0
        self.canvas.bind_all('<KeyPress-Up>', self.up)
        self.canvas.bind_all('<KeyPress-Down>', self.down)
        

    def up(self,evt):
        self.y = -5

    def down(self,evt):
        self.y = 5

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = -0

def main():
    tk = Tk() #creating a tk object
    tk.title("Pong")
    tk.resizable(0,0) # resizeable makes rhe window a fixedsize
    tk.wm_attributes("-topmost",1) #the wm_attributes tell tkinter to place *this* window infront of all other windows
    canvas = Canvas(tk,bg="black",width=700,height=400,bd=0,highlightthickness=0) #create canvas and create a few additional features
    canvas.pack() #tells the canvas to size it's self according to the width and heigh parameters just given
    tk.update() #update tells tkinter to initialise itself for the animation in the game to come - this last line is very important as otherwise things wouldn't quite work correctly!
    def callback():
        if messagebox.askokcancel("Quit", "Do you really wish to quit?, (Clicking cancel will reload game)"):
            tk.destroy()
    def on_exit():
        """When you click to exit, this function is called"""
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            tk.destroy() 
    canvas.create_line(350,0,350,400,fill='white')
    tk.protocol("WM_DELETE_WINDOW", on_exit) #TODO make a way of exiting that doesn't throw an error in shell
    bat1 = pongbat(canvas, 'white')
    bat2 = pongbat2(canvas, 'white')
    ball1 = Ball(canvas,bat1,bat2, 'green') #here we are creating an object (green ball) from ball class
    while 1:
        ball1.draw()
        bat1.draw()
        bat2.draw()
        tk.update()
        if ball1.checkwin():
            messagebox.showinfo('Game End',ball1.checkwin()+' won!!')
        if ball1.checkForgameOver():
            callback()
            tk.destroy()
            main()
        canvas.after(10)
if __name__ == '__main__':
    main().mainloop




