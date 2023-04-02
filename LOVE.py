# Import turtle package
import turtle
t = turtle.Turtle()
t.screen.bgcolor('black')


# Defining a method to draw curve
def curve():
	for i in range(200):

		# Defining step by step curve motion
		turtle.right(1)
		turtle.forward(1)

# Defining method to draw a full heart
def heart():

	# Set the fill color to red
	turtle.fillcolor('red')

	# Start filling the color
	turtle.begin_fill()

	# Draw the left line
	turtle.left(140)
	turtle.forward(113)

	# Draw the left curve
	curve()
	turtle.left(120)

	# Draw the right curve
	curve()

	# Draw the right line
	turtle.forward(112)

	# Ending the filling of the color
	turtle.end_fill()


# Defining method to write text
def txt():

	# Move turtle to air
	turtle.up()

	# Move turtle to a given position
	turtle.setpos(-90, -115)

	# Move the turtle to the ground
	turtle.down()

	# Set the text color to lightgreen
	turtle.color('white')

	# Write the specified text in
	# specified font style and size
	turtle.write("Chhod Sare in qisson ko," "\n" "In iraado ko," "\n" "In waadon ko," "\n" "Tu Aaina dekh Aur bta" "\n" "Meri pasand kaise hai!! " "\n" "just kidding😂", font=(
	"Verdana", 12, "normal"))


# Draw a heart
heart()

# Write text
txt()

# To hide turtle
turtle.ht()
a=input()
