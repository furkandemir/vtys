import turtle 

wn = turtle.Screen() #wn adında bir ekran yarat
wn.title('Bong Game') #ekran başlığı
wn.bgcolor('black') #arkaplan rengi
wn.setup(width=800, height=600) #ekran boyutu
wn.tracer(1) #ekran akıcılığı

score_a = 0
score_b = 0

paddle_a = turtle.Turtle()
paddle_a.speed(0) #tahtanın hızı demek değil animasyonun hızı
paddle_a.shape('square') #a tahtasının şekli
paddle_a.color('white') 
paddle_a.shapesize(stretch_wid=5 , stretch_len=1)
paddle_a.penup() 
paddle_a.goto(-350, 0) #konumu x,y ekseni şeklinde

paddle_b = turtle.Turtle()
paddle_b.speed(0) 
paddle_b.shape('square')
paddle_b.color('white') 
paddle_b.shapesize(stretch_wid=5 , stretch_len=1)
paddle_b.penup() 
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0) #tahtanın hızı demek değil animasyonun hızı
ball.shape('square') #a tahtasının şekli
ball.color('white') 
ball.penup() 
ball.goto(0, 0) #konumu x,y ekseni şeklinde
ball.dx = 2
ball.dy = -2

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.color('white')
pen.goto(0,260)
pen.hideturtle()
pen.write('Player A:0   Player B:0',align='center',font=('Corier',24,'normal'))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')

while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if (ball.ycor() > 290):
        ball.sety(290)
        ball.dy *= -1
    
    if (ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *= -1

    if (ball.xcor() > 390):
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A:{}   Player B:{}'.format(score_a, score_b),align='center',font=('Corier',24,'normal'))


    if (ball.xcor() < -390):
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A:{}   Player B:{}'.format(score_a, score_b),align='center',font=('Corier',24,'normal'))


    if (ball.xcor() > 340 and ball.xcor() < 350) and  (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and  (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1