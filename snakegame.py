from tkinter import *
import random

WIDTH = 800
HEIGHT = 600
BG_color = "BLACK"
FPS = 180
SPACE_SIZE = 40
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
        
    if collision(snake):
         gameover()
    else:
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
    
    x , y = snake.coordinates[0]
    
    if  x < 0  or x >= WIDTH:
        return True
    elif y < 0 or y >= HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]: 
            return True
        
    return False

def changedirection(new_direction):
    
    global direction

    if new_direction == 'left':
        direction = 'left'
    elif new_direction == 'right':
        direction = 'right'
    elif new_direction == 'up':
        direction = 'up'
    elif new_direction == 'down':
        direction = 'down'
    
def gameover():
    game_canvas.delete(ALL)
    game_canvas.create_text(game_canvas.winfo_width()/2, game_canvas.winfo_height()/2, font=('Poppins', 70), text="GAME OVER", fill="red", anchor=CENTER)

main_screen = Tk()
main_screen.title("Snake Game")
main_screen.resizable(False,False)

score = 0
direction = "right"

scorelabel = Label(main_screen,text=("SCORE = {}".format(score)),font=("Poppins",35))
scorelabel.pack()

game_canvas = Canvas(main_screen, height=HEIGHT , width=WIDTH ,bg=BG_color)
game_canvas.pack()

main_screen.update()

window_width = main_screen.winfo_width()
window_height = main_screen.winfo_height()
screen_width = main_screen.winfo_screenwidth()
screen_height = main_screen.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

main_screen.geometry(f"{window_width}x{window_height}+{x}+{y}")

main_screen.bind('a', lambda event: changedirection('left'))
main_screen.bind('d', lambda event: changedirection('right'))
main_screen.bind('w', lambda event: changedirection('up'))
main_screen.bind('s', lambda event: changedirection('down'))

food = Food()
snake = Snake()

start_snake(snake,food)

main_screen = mainloop()