import tkinter as tk
import random

root = tk.Tk()
root.title("Snake - 1")

SIZE = 20
W = 400
H = 400
canvas = tk.Canvas(root, width=W, height=H, bg="white")
canvas.pack()

snake = [(10, 10)]
dx = 1
dy = 0
food = (random.randint(0, W//SIZE - 1),random.randint(0, H//SIZE - 1))

def draw():
    canvas.delete("all")
    fx, fy = food
    canvas.create_rectangle(fx*SIZE, fy*SIZE,
                            fx*SIZE+SIZE, fy*SIZE+SIZE,
                            fill="red")
    for (x, y) in snake:
        canvas.create_rectangle(x*SIZE, y*SIZE,
                                fx*SIZE+SIZE, y*SIZE+SIZE,
                                fill="green")

def game_loop():
    global snake, food
    head_x,head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)
    snake.insert(0, new_head)
    if new_head == food:
        food = (random.randint(0, W//SIZE - 1))
        random.randint(0, H//SIZE - 1)
    else:
        snake.pop()
    draw()
    root.after(150, game_loop)

def up(event):
    global dx, dy
    dx, dy = 0, -1

def down(event):
    global dx, dy
    dx, dy = 0, 1

def left(event):
    global dx, dy
    dx, dy = -1,0

def right(event):
    global dx, dy  
    dx, dy = 1, 0

root.bind("<Up>", up) 
root.bind("<Down>", down)
root.bind("<Left>", left) 
root.bind("<Right>", right)  

draw()
root.after(150, game_loop)
root.mainloop()

       

