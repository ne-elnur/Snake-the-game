from tkinter import *
import random

Width = 800
Height = 600
Seg_size = 20

In_game = True

def create_block():
    global BlocK
    posx = Seg_size * random.randint(1, (Width - Seg_size) / Seg_size)
    posy = Seg_size * random.randint(1, (Height - Seg_size) / Seg_size)
    BlocK = c.create_oval(posx, posy,
                          posx + Seg_size, posy + Seg_size,
                          fill="red")
    
class Score(object):

    def __init__(self):
        self.score = 0
        self.x = 65
        self.y = 15
        c.create_text(self.x, self.y, text="SCORE: {}".format(self.score), font="Arial 20",
                      fill="black", tag="score", state='hidden')
        
    def increment(self):
        c.delete("score")
        self.score += 1
        c.create_text(self.x, self.y, text="SCORE: {}".format(self.score), font="Arial 20",
                      fill="white", tag="score")
        
    def reset(self):
        c.delete("score")
        self.score = 0

def main():
    global In_game
    if In_game:
        s.move()

        head_coords = c.coords(s.segments[-1].instance)
        x1, y1, x2, y2 = head_coords

        if x2 > Width or x1 < 0 or y1 < 0 or y2 > Height:
            In_game = False

        elif head_coords == c.coords(BlocK):
            s.add_segment()
            c.delete(BlocK)
            create_block()
             
        else:
            for index in range(len(s.segments) - 1):
                if head_coords == c.coords(s.segments[index].instance):
                    In_game = False

        root.after(100, main)
        
    else:
        set_state(restart_text, 'normal')
        set_state(game_over_text, 'normal')

class Segment(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x + Seg_size, y + Seg_size,
                                           fill="yellow")
                                           
class Snake(object):
    def __init__(self, segments):
        self.segments = segments

        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}

        self.vector = self.mapping["Right"]

    def move(self):
        for index in range(len(self.segments) - 1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,
                 x1 + self.vector[0] * Seg_size, y1 + self.vector[1] * Seg_size,
                 x2 + self.vector[0] * Seg_size, y2 + self.vector[1] * Seg_size)

    def add_segment(self):
        score.increment()
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - Seg_size
        y = last_seg[3] - Seg_size
        self.segments.insert(0, Segment(x, y))

    def change_direction(self, event):
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]

    def reset_snake(self):
        for segment in self.segments:
            c.delete(segment.instance)

def set_state(item, state):
    c.itemconfigure(item, state=state)
    c.itemconfigure(BlocK, state='hidden')

def clicked(event):
    global In_game
    s.reset_snake()
    In_game = True
    c.delete(BlocK)
    score.reset()
    c.itemconfigure(restart_text, state='hidden')
    c.itemconfigure(game_over_text, state='hidden')
    start_game()

def start_game():
    global s
    create_block()
    s = create_snake()

    c.bind("<KeyPress>", s.change_direction)
    main()

def create_snake():
    segments = [Segment(Seg_size, Seg_size),
                Segment(Seg_size * 2, Seg_size),
                Segment(Seg_size * 3, Seg_size)]
    return Snake(segments)

root = Tk()
root.title("Snake-the-game")

c = Canvas(root, width=Width, height=Height, bg="green")
c.grid()

c.create_line(30, 50, 20, 65, fill='black')
c.create_line(30, 50, 30, 65, fill='black')
c.create_line(40, 50, 30, 65, fill='black')
c.create_line(40, 50, 40, 65, fill='black')
c.create_line(50, 50, 40, 65, fill='black')
c.create_line(50, 50, 50, 65, fill='black')
c.create_line(60, 50, 50, 65, fill='black')
c.create_line(60, 50, 60, 65, fill='black')

c.create_line(50, 400, 40, 415, fill='black')
c.create_line(50, 400, 50, 415, fill='black')
c.create_line(60, 400, 50, 415, fill='black')
c.create_line(60, 400, 60, 415, fill='black')
c.create_line(70, 400, 60, 415, fill='black')
c.create_line(70, 400, 70, 415, fill='black')
c.create_line(80, 400, 70, 415, fill='black')
c.create_line(80, 400, 80, 415, fill='black')

c.create_line(300, 85, 290, 100, fill='black')
c.create_line(300, 85, 300, 100, fill='black')
c.create_line(310, 85, 300, 100, fill='black')
c.create_line(310, 85, 310, 100, fill='black')
c.create_line(320, 85, 310, 100, fill='black')
c.create_line(320, 85, 320, 100, fill='black')
c.create_line(330, 85, 320, 100, fill='black')
c.create_line(330, 85, 330, 100, fill='black')

c.create_line(760, 545, 750, 560, fill='black')
c.create_line(760, 545, 760, 560, fill='black')
c.create_line(770, 545, 760, 560, fill='black')
c.create_line(770, 545, 770, 560, fill='black')
c.create_line(780, 545, 770, 560, fill='black')
c.create_line(780, 545, 780, 560, fill='black')
c.create_line(790, 545, 780, 560, fill='black')
c.create_line(790, 545, 790, 560, fill='black')

c.create_line(740, 225, 730, 240, fill='black')
c.create_line(740, 225, 740, 240, fill='black')
c.create_line(750, 225, 740, 240, fill='black')
c.create_line(750, 225, 750, 240, fill='black')
c.create_line(760, 225, 750, 240, fill='black')
c.create_line(760, 225, 760, 240, fill='black')
c.create_line(770, 225, 760, 240, fill='black')
c.create_line(770, 225, 770, 240, fill='black')

c.create_line(470, 500, 460, 515, fill='black')
c.create_line(470, 500, 470, 515, fill='black')
c.create_line(480, 500, 470, 515, fill='black')
c.create_line(480, 500, 480, 515, fill='black')
c.create_line(490, 500, 480, 515, fill='black')
c.create_line(490, 500, 490, 515, fill='black')
c.create_line(500, 500, 490, 515, fill='black')
c.create_line(500, 500, 500, 515, fill='black')

c.create_line(170, 575, 160, 590, fill='black')
c.create_line(170, 575, 170, 590, fill='black')
c.create_line(180, 575, 170, 590, fill='black')
c.create_line(180, 575, 180, 590, fill='black')
c.create_line(190, 575, 180, 590, fill='black')
c.create_line(190, 575, 190, 590, fill='black')
c.create_line(200, 575, 190, 590, fill='black')
c.create_line(200, 575, 200, 590, fill='black')

c.create_line(570, 20, 560, 35, fill='black')
c.create_line(570, 20, 570, 35, fill='black')
c.create_line(580, 20, 570, 35, fill='black')
c.create_line(580, 20, 580, 35, fill='black')
c.create_line(590, 20, 580, 35, fill='black')
c.create_line(590, 20, 590, 35, fill='black')
c.create_line(600, 20, 590, 35, fill='black')
c.create_line(600, 20, 600, 35, fill='black')

c.create_line(125, 215, 115, 230, fill='black')
c.create_line(125, 215, 125, 230, fill='black')
c.create_line(135, 215, 125, 230, fill='black')
c.create_line(135, 215, 135, 230, fill='black')
c.create_line(145, 215, 135, 230, fill='black')
c.create_line(145, 215, 145, 230, fill='black')
c.create_line(155, 215, 145, 230, fill='black')
c.create_line(155, 215, 155, 230, fill='black')

c.create_line(655, 385, 645, 400, fill='black')
c.create_line(655, 385, 655, 400, fill='black')
c.create_line(665, 385, 655, 400, fill='black')
c.create_line(665, 385, 665, 400, fill='black')
c.create_line(675, 385, 665, 400, fill='black')
c.create_line(675, 385, 675, 400, fill='black')
c.create_line(685, 385, 675, 400, fill='black')
c.create_line(685, 385, 685, 400, fill='black')

c.create_line(250, 415, 240, 430, fill='black')
c.create_line(250, 415, 250, 430, fill='black')
c.create_line(260, 415, 250, 430, fill='black')
c.create_line(260, 415, 260, 430, fill='black')
c.create_line(270, 415, 260, 430, fill='black')
c.create_line(270, 415, 270, 430, fill='black')
c.create_line(280, 415, 270, 430, fill='black')
c.create_line(280, 415, 280, 430, fill='black')

c.create_line(520, 190, 510, 205, fill='black')
c.create_line(520, 190, 520, 205, fill='black')
c.create_line(530, 190, 520, 205, fill='black')
c.create_line(530, 190, 530, 205, fill='black')
c.create_line(540, 190, 530, 205, fill='black')
c.create_line(540, 190, 540, 205, fill='black')
c.create_line(550, 190, 540, 205, fill='black')
c.create_line(550, 190, 550, 205, fill='black')

c.create_line(320, 250, 310, 265, fill='black')
c.create_line(320, 250, 320, 265, fill='black')
c.create_line(330, 250, 320, 265, fill='black')
c.create_line(330, 250, 330, 265, fill='black')
c.create_line(340, 250, 330, 265, fill='black')
c.create_line(340, 250, 340, 265, fill='black')
c.create_line(350, 250, 340, 265, fill='black')
c.create_line(350, 250, 350, 265, fill='black')

c.create_line(450, 350, 440, 365, fill='black')
c.create_line(450, 350, 450, 365, fill='black')
c.create_line(460, 350, 450, 365, fill='black')
c.create_line(460, 350, 460, 365, fill='black')
c.create_line(470, 350, 460, 365, fill='black')
c.create_line(470, 350, 470, 365, fill='black')
c.create_line(480, 350, 470, 365, fill='black')
c.create_line(480, 350, 480, 365, fill='black')

c.focus_set()

game_over_text = c.create_text(Width / 2, Height / 2, text="GAME OVER!",
                               font='Arial 20', fill='red',
                               state='hidden')
                               
restart_text = c.create_text(Width / 2, Height - Height / 3,
                             font='Arial 25',
                             fill='light green',
                             text="RESTART",
                             state='hidden')

c.tag_bind(restart_text, "<Button-1>", clicked)

score = Score()

start_game()

root.mainloop()
