
import random
import turtle

gameSpeed = 0.15

def setupGameWindow():
    window = turtle.Screen()
    window.title("Yılan Oyunu")
    window.bgcolor("lightgreen")
    window.setup(width=600, height=600)
    window.tracer(0)
    return window

def resetGame():
    global head, food, segments, score, gameOverMessage
    head.goto(0, 100)
    head.direction = "stop"

    for segment in segments:
        segment.hideturtle()
    segments.clear()

    food.goto(0, 0)
    score = 0
    updateScore()

    if 'gameOverMessage' in globals():
        gameOverMessage.clear()

    gameLoop()

def quitGame():
    gameWindow.bye()

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

def goUp():
    if head.direction != 'down':
        head.direction = 'up'

def goDown():
    if head.direction != 'up':
        head.direction = 'down'

def goRight():
    if head.direction != 'left':
        head.direction = 'right'

def goLeft():
    if head.direction != 'right':
        head.direction = 'left'

def updateScore():
    scoreDisplay.clear()
    scoreDisplay.write(f"Skor: {score}", align="center", font=("Arial", 24, "bold"))

def gameOver():
    global gameOverMessage
    if 'gameOverMessage' not in globals():
        gameOverMessage = turtle.Turtle()
        gameOverMessage.hideturtle()
        gameOverMessage.color("red")
    gameOverMessage.clear()
    gameOverMessage.write("Kaybettiniz!\nR: Tekrar Başlat\nQ: Çık", align="center", font=("Arial", 24, "bold"))

    gameWindow.listen()
    gameWindow.onkey(resetGame, 'r')
    gameWindow.onkey(quitGame, 'q')

def gameLoop():
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        gameOver()
        return

    for segment in segments:
        if segment.distance(head) < 20:
            gameOver()
            return

    move()

    if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape("square")
        newSegment.color("gray")
        newSegment.penup()
        segments.append(newSegment)

        global score
        score += 10

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    updateScore()
    gameWindow.update()
    gameWindow.ontimer(gameLoop, int(gameSpeed * 1000))

gameWindow = setupGameWindow()

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 100)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("purple")
food.penup()
food.goto(0, 0)
food.shapesize(0.80, 0.80)

segments = []
score = 0

scoreDisplay = turtle.Turtle()
scoreDisplay.speed(0)
scoreDisplay.color("blue")
scoreDisplay.penup()
scoreDisplay.hideturtle()
scoreDisplay.goto(0, 260)
updateScore()

gameWindow.listen()
gameWindow.onkey(goUp, 'Up')
gameWindow.onkey(goDown, 'Down')
gameWindow.onkey(goRight, 'Right')
gameWindow.onkey(goLeft, 'Left')

gameLoop()
gameWindow.mainloop()
