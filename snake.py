
       

import tkinter as tk
import random

root = tk.Tk()
root.title("Snake + Chase Block")

SIZE = 20
W = 400
H = 400
canvas = tk.Canvas(root, width=W, height=H, bg="white")
canvas.pack()

# ---------------- SNAKE ----------------
snake = [(10, 10)]
dx, dy = 1, 0

# ---------------- FOOD ----------------
food_list = []
NUM_FOOD = 3

def spawn_food():
    while len(food_list) < NUM_FOOD:
        f = (random.randint(1, W//SIZE - 2),
             random.randint(1, H//SIZE - 2))
        if f not in food_list:
            food_list.append(f)

spawn_food()

# ---------------- WALLS ----------------
num_unbreakable = 10
num_breakable = 6

unbreakable_walls = set()
breakable_walls = set()

# random unbreakables
for _ in range(num_unbreakable):
    unbreakable_walls.add((random.randint(1, W//SIZE - 2),
                           random.randint(1, H//SIZE - 2)))

# random breakables
for _ in range(num_breakable):
    breakable_walls.add((random.randint(1, W//SIZE - 2),
                         random.randint(1, H//SIZE - 2)))

# ---------------- BORDER WALLS ----------------
for x in range(W//SIZE):
    unbreakable_walls.add((x, 0))                     # top
    unbreakable_walls.add((x, H//SIZE - 1))           # bottom

for y in range(H//SIZE):
    unbreakable_walls.add((0, y))                     # left
    unbreakable_walls.add((W//SIZE - 1, y))           # right


# ---------------- CHASE BLOCK ----------------
chaser = (3, 3)
chase_delay = 0


# ---------------- DRAW ----------------
def draw():
    canvas.delete("all")

    # food
    for fx, fy in food_list:
        canvas.create_rectangle(fx*SIZE, fy*SIZE,
                                fx*SIZE+SIZE, fy*SIZE+SIZE,
                                fill="red")

    # unbreakable walls (black)
    for x, y in unbreakable_walls:
        canvas.create_rectangle(x*SIZE, y*SIZE,
                                x*SIZE+SIZE, y*SIZE+SIZE,
                                fill="black")

    # breakable walls (green)
    for x, y in breakable_walls:
        canvas.create_rectangle(x*SIZE, y*SIZE,
                                x*SIZE+SIZE, y*SIZE+SIZE,
                                fill="green")

    # snake
    for x, y in snake:
        canvas.create_rectangle(x*SIZE, y*SIZE,
                                x*SIZE+SIZE, y*SIZE+SIZE,
                                fill="blue")

    # chaser block
    cx, cy = chaser
    canvas.create_rectangle(cx*SIZE, cy*SIZE,
                            cx*SIZE+SIZE, cy*SIZE+SIZE,
                            fill="purple")


# ---------------- CHASER LOGIC ----------------
def move_chaser():
    global chaser, chase_delay

    chase_delay += 1
    if chase_delay % 3 != 0:
        return

    cx, cy = chaser
    px, py = snake[0]

    dx = 1 if px > cx else -1 if px < cx else 0
    dy = 1 if py > cy else -1 if py < cy else 0

    new = (cx + dx, cy + dy)

    if new in unbreakable_walls:
        return

    if new in breakable_walls:
        breakable_walls.remove(new)
        chaser = new
        return

    chaser = new


# ---------------- GAME LOOP ----------------
def game_loop():
    global snake

    head_x, head_y = snake[0]
    new_head = (head_x + dx, head_y + dy)

   
    # hit breakable wall → break it
    if new_head in breakable_walls:
        breakable_walls.remove(new_head)

    snake.insert(0, new_head)

    # check food
    if new_head in food_list:
        food_list.remove(new_head)
        spawn_food()
    else:
        snake.pop()

    move_chaser()

    # death check
    if new_head == chaser:
        canvas.delete("all")
        canvas.create_text(W//2, H//2,
                           text="BRUHHHHHHHH,YOU DIED",
                           fill=("black"),
                           font=("Arial", 15, "bold"))
        return

    draw()
    root.after(150, game_loop)



def up(event):
    global dx, dy
    if dy != 1:
        dx, dy = 0, -1

def down(event):
    global dx, dy
    if dy != -1:
        dx, dy = 0, 1

def left(event):
    global dx, dy
    if dx != 1:
        dx, dy = -1, 0

def right(event):
    global dx, dy
    if dx != -1:
        dx, dy = 1, 0

root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Left>", left)
root.bind("<Right>", right)

draw()
root.after(150, game_loop)
root.mainloop()
