from tkinter import *
import random

WIDTH = 800
HEIGHT = 600
BG_color = "BLACK"
FPS = 60
SPACE_SIZE = 50
S_PARTS = 4
SNAKE_COLOR = "#FF00FF"
FOOD_COLOR = "#00FF00"

class Snake:

    def __init__(self):
        self.body_size = S_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0,S_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = game_canvas.create_rectangle(x ,y, x+SPACE_SIZE , y+SPACE_SIZE ,fill=SNAKE_COLOR , tag="snake" )
            self.squares.append(square)

class Food:

    def __init__(self):

        x = random.randint(0,(WIDTH // SPACE_SIZE )-1)*SPACE_SIZE
        y = random.randint(0,(HEIGHT // SPACE_SIZE )- 1)*SPACE_SIZE

        self.coordinates = [x,y]

        game_canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE ,fill=FOOD_COLOR, tag="food")

def start_snake(snake,food):
    x,y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x,y))

    square = game_canvas.create_rectangle(x ,y, x+SPACE_SIZE , y+SPACE_SIZE ,fill=SNAKE_COLOR)
    
    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        scorelabel.config(text=("SCORE = {}".format(score)))
        game_canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        game_canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    main_screen.after(FPS, start_snake ,snake , food)


def changedirection(new_direction):
    
    global direction

    if new_direction == 'left':
        direction != 'left'
        direction = new_direction
    elif new_direction == 'right':
        direction != 'right'
        direction = new_direction
    elif new_direction == 'up':
        direction != 'up'
        direction = new_direction
    elif new_direction == 'down':
        direction != 'down'
        direction = new_direction

def collision(snake):
    
    pass

def gameover():
    pass

main_screen = Tk()
main_screen.title("Snake Game")
main_screen.resizable(False,False)

score = 0
direction = "down"

scorelabel = Label(main_screen,text=("SCORE = {}".format(score)),font=("Poppins",35))
scorelabel.pack()

game_canvas = Canvas(main_screen, height=HEIGHT , width=WIDTH ,bg=BG_color)
game_canvas.pack()

main_screen.bind('<Left>', lambda event: changedirection('left'))
main_screen.bind('<Right>', lambda event: changedirection('right'))
main_screen.bind('<Up>', lambda event: changedirection('up'))
main_screen.bind('<Down>', lambda event: changedirection('down'))

food = Food()
snake = Snake()

start_snake(snake,food)

main_screen = mainloop()