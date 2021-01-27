import turtle
from random import randint

import math

kiirus = 1     	# tulnuka liikumise kiirus
tulnukatearv = 10
kuulikiirus = 50

# RUUT

pliiats = turtle.Turtle()

# paneme algusruudu õigesse kohta
pliiats.penup()
pliiats.setposition(-300, 300)
	
# hakkame pliiatsiga joonistama
pliiats.pendown()

# teeme nelja küljega ruudu
for kylg in range(4):
	pliiats.forward(600)
	pliiats.right(90)
	
pliiats.hideturtle()


# RAKETT

rakett = turtle.Turtle()
rakett.penup()
turtle.register_shape('ship.gif')
rakett.shape('ship.gif')
rakett.penup
rakett.left(90)

# tulnukad

turtle.register_shape('invador.gif')

tulnukad = []
for i in range(tulnukatearv):
	tulnukad.append(turtle.Turtle())

for ykstulnukas in tulnukad:
	ykstulnukas.penup()
	x = randint(-300,300)
	y = randint(200,300)
	ykstulnukas.setx(x)
	ykstulnukas.sety(y)
	ykstulnukas.shape('invador.gif')


# KUUL

kuul = turtle.Turtle()
kuul.color('red')
kuul.penup()
kuul.speed(0)
kuul.setheading(90)
kuul.shapesize(2,2)
kuul.hideturtle()
kuuliolek = 'valmis'




def moveRight():
	x = rakett.xcor()
	x = x+10
	rakett.setx(x)

def moveLeft():
	x = rakett.xcor()
	x = x-10
	rakett.setx(x)

def moveUp():
	y = rakett.ycor()
	y = y+10
	rakett.sety(y)


def moveDown():
	y = rakett.ycor()
	y = y-10
	rakett.sety(y)

def tulistamine():
	global kuuliolek
	print('! Toimus tulistamine...')
	if kuuliolek == 'valmis':
		kuuliolek = 'lennus'
		print('...kuul lennus')
		x = rakett.xcor()
		y = rakett.ycor() + 10
		kuul.setposition(x,y)
		kuul.showturtle()

def kaspihtas(asi1, asi2):
	kaugus =  math.sqrt(math.pow(asi1.xcor() - asi2.xcor(), 2) + math.pow(asi1.ycor() - asi2.ycor(), 2))
	if kaugus < 30:
		print ('...napikas (', kaugus, ')')
	if kaugus < 20:
		print ('! PIHTAS !')
		return True
	else:
		return False
 


aken = turtle.Screen()
aken.listen()
aken.onkey(moveRight,'Right')
aken.onkey(moveLeft,'Left')
aken.onkey(moveUp,'Up')
aken.onkey(moveDown,'Down')
aken.onkey(tulistamine,'space')



#liikumine

while True:
	for ykstulnukas in tulnukad:
		y = ykstulnukas.ycor()
		y = y - kiirus
		ykstulnukas.sety(y)
		
	if kuuliolek == 'lennus':
		y = kuul.ycor()
		y = y + kuulikiirus
		kuul.sety(y)

	if kuul.ycor()>300:
		kuul.hideturtle()
		kuuliolek = 'valmis'
		
	for ykstulnukas in tulnukad:
		if kaspihtas(kuul, ykstulnukas):
			kuul.hideturtle()
			kuuliolek = 'valmis'
			ykstulnukas.hideturtle()
			ykstulnukas.setposition(randint(-300, 300), 300)
			ykstulnukas.showturtle()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
turtle.done()

